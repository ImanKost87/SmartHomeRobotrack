#include <ESP8266WiFi.h>
#include <ESP8266HTTPClient.h>
#include <ESP8266WiFiMulti.h>
#include <WiFiClient.h>

const char *ssid = "HUAWEI Y9 2018";
const char *password = "192837465";

ESP8266WiFiMulti WiFiMulti;

void setup()
{
    Serial.begin(115200);
    WiFi.begin(ssid, password);

    while (WiFi.status() != WL_CONNECTED) {
      delay(1000);  
    }

    String registerMessageFromSensors = "";
    String registerMessageToSensors = "Init1";
    while (registerMessageFromSensors == "") {
      Serial.println(registerMessageToSensors);
      delay(500);
      registerMessageFromSensors = Serial.readString();
    }
    Serial.println(registerMessageFromSensors);
    Serial.println("Allright1");
    Register(registerMessageFromSensors);
    Serial.println("Allright3");
}

void loop()
{
  String data = "";
  if (Serial.available()) {
    data = Serial.readString();
    updateData(data);
  }
  delay(500);
}

void updateData(String data)
{
    if ((WiFiMulti.run() == WL_CONNECTED))
    {
        WiFiClient client;
        HTTPClient http;

        char str[data.length()];
        data.toCharArray(str, data.length()); // todo: Убрать костыль!!!!
        data = String(str);
        data = data.substring(0, data.length() - 1);


        if (http.begin(client, "http://194.58.107.109:8080/W/Ping"))
        {

            http.addHeader("Content-Type", "application/json");
            String postData = "{\"user\": \"Me\",\"password\": \"123\",\"data\": \"" + data + "\"}";

            Serial.println(postData);

            int httpCode = http.POST(postData);
            Serial.println(httpCode);
            if (httpCode > 0)
            {
                if (httpCode == HTTP_CODE_OK || httpCode == HTTP_CODE_MOVED_PERMANENTLY)
                {
                    String payload = http.getString();
                    if(payload != "")
                    {
                      getDataFromServer(payload);
                    }
                }
            }
            http.end();
        }
    }
}

void getDataFromServer(String data) {
  Serial.println(data);
}

void Register(String data)
{
    if ((WiFiMulti.run() == WL_CONNECTED))
    {
        WiFiClient client;
        HTTPClient http;

        char str[data.length()];
        
        data.toCharArray(str, data.length());

        data = String(str);
  
        Serial.println("http://194.58.107.109:8080/W/Register?d=Me|123|" + data);

        String url = "http://194.58.107.109:8080/W/Register?d=Me|123|" + data;
        if (http.begin(client, url))
        {
            Serial.println(http.GET());
            http.end();
        }
    }
}
