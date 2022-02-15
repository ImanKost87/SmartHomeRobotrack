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
    Register();
}

void loop()
{
    updateData();
    delay(500);
}

void updateData()
{
    if ((WiFiMulti.run() == WL_CONNECTED))
    {
        WiFiClient client;
        HTTPClient http;

        if (http.begin(client, "http://194.58.107.109:8080/W/Ping"))
        {

            http.addHeader("Content-Type", "application/json");
            String data = "";
            if (Serial.available()) {
              data = Serial.readString();
            }
            String postData = "{\"user\": \"Me\",\"password\": \"123\",\"data\": \"" + data + "\"}";

            int httpCode = http.POST(postData);
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

void Register()
{
    if ((WiFiMulti.run() == WL_CONNECTED))
    {
        WiFiClient client;
        HTTPClient http;

        String data = "0:B1";
        if (Serial.available()) {
          data = Serial.readString();
        }

        String url = "http://194.58.107.109:8080/W/Register?d=Me|123|" + data;
        if (http.begin(client, url))
        {
            http.GET();
            http.end();
        }
    }
}
