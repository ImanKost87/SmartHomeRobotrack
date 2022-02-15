void setup() {
  Serial.begin(115200);
  String sensors = "18:M2,21:OUT1,10:IN1|IN2,18:M1";
  registerSensors(sensors);
}

void loop() {

}

void registerSensors(String str) {
  char alpha[] = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
  int betas[26] = {0};
  char data[str.length()];
  str.toCharArray(data, str.length());
  char *rest = NULL;
  char *token;

  String namedSensors = "";
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
  Serial.println(namedSensors);
}
