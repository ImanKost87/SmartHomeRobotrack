int lum = 0 ;
String namedSensors = "";

void setup()
{
  Serial.begin(115200);
  Serial1.begin(115200);
  
  String sensors = "4:IN1,21:OUT1";
  String messageFromWemos = "";
  int i = 0;
  while (messageFromWemos == "") {
    messageFromWemos = Serial1.readString();
    Serial.println(messageFromWemos + String(i++));
    delay(500);
  }
  
  registerSensors(sensors);
  delay(5000);

  pinMode(OUT1, OUTPUT);
}

void loop()
{
  delay(500);
  
  lum = cdsAnalog(IN1) ;
  if (Serial1.available()) {
    Serial1.println("E1:" + String(lum));
    Serial.println("E1:" + String(lum));
  }
  if (lum > 500) {
    led(OUT1, HIGH);
  } else {
    led(OUT1, LOW);
  } 
}

void registerSensors(String str) {
  char alpha[] = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
  int betas[26] = {0};
  char data[str.length()];
  str.toCharArray(data, str.length());
  char *rest = NULL;
  char *token;

  for (token = strtok_r(data, ",", &rest);
       token != NULL;
       token = strtok_r(NULL, ",", &rest)) {
    char *subrest = NULL;
    char *subtoken; int i;
    for (subtoken = strtok_r(token, ":", &subrest), i = 0;
         subtoken != NULL;
         subtoken = strtok_r(NULL, ":", &subrest), i++) {
      if (i == 0) {
        namedSensors = namedSensors + String(subtoken) + ":";
        namedSensors = namedSensors + String(alpha[atoi(subtoken)]);
        betas[atoi(subtoken)] = betas[atoi(subtoken)] + 1;
        namedSensors = namedSensors + String(betas[atoi(subtoken)]) + ",";
      } else if (i == 1) {
        continue;
      }
    }
  }
  namedSensors[namedSensors.length() - 1] = '\0';
  Serial1.print(namedSensors);
  Serial.println(namedSensors);
}

