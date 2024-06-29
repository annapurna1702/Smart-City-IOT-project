#define trigPin 8
#define echoPin 9
long duration;
int distance;

void setup()
{
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
  Serial.begin(9600);
  Serial3.begin(115200);
  Serial3.println("AT+RST\r\n");
  delay(500);
  Serial3.println("AT+CWMODE=3\r\n");
  delay(500);
  Serial3.println("AT+CWJAP=\"Redmi\",\"123456789\"\r\n");
  delay(500);
  Serial3.println("AT+CIPMUX=1\r\n");
  delay(500);

}

void loop()
{
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);

  duration = pulseIn(echoPin, HIGH);
  distance = duration * 0.034 / 2;

  int value = map(distance, 0, 25, 100, 0);

  if (value<0)
  {
    value=0;
  }
  
  Serial.print("Level of waste=");
  Serial.println(value);

  Serial3.print("AT+CIPSTART=\"TCP\",\"192.168.18.187\",80\r\n");
  delay(100);
  if (Serial3.find("Error1"))
  {
    Serial.println("AT+CIPSTART error");
    return;
  }
  Serial3.println("AT+CIPSEND=200\r\n");
  delay(100);
  if (Serial3.find(">"))
  {
    Serial3.print("GET http://192.168.18.187/bin/data.php?id=");
    Serial3.print(value);
    Serial3.print("&gi=34");
    Serial.println("success");
    delay(1000);


    Serial3.println("AT+CIPCLOSE");
    Serial3.print("AT+CIPSTART=\"TCP\",\"192.168.18.187\",80\r\n");
    delay(100);
    Serial3.println("AT+CIPSEND=200\r\n");
    delay(100);
    Serial3.println("AT+CIPCLOSE");
        Serial3.println("AT+CIPCLOSE");
    Serial3.print("AT+CIPSTART=\"TCP\",\"192.168.18.187\",80\r\n");
    delay(100);
    Serial3.println("AT+CIPSEND=200\r\n");
    delay(100);
    Serial3.println("AT+CIPCLOSE");
        Serial3.println("AT+CIPCLOSE");
    Serial3.print("AT+CIPSTART=\"TCP\",\"192.168.18.187\",80\r\n");
    delay(100);
    Serial3.println("AT+CIPSEND=200\r\n");
    delay(100);
    Serial3.println("AT+CIPCLOSE");
  }
  else
  {
    Serial.print("jadf");
    Serial3.println("AT+CIPCLOSE");
  }
  Serial3.println("AT+CIPCLOSE");
  delay(100);

}
