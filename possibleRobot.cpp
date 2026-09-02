// Definición de pines para sensores y motores
const int trigPin = 9;
const int echoPin = 10;
const int motorIzqForward = 4;
const int motorIzqBackward = 5;
const int motorDerForward = 6;
const int motorDerBackward = 7;

void setup() {
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
  pinMode(motorIzqForward, OUTPUT);
  pinMode(motorIzqBackward, OUTPUT);
  pinMode(motorDerForward, OUTPUT);
  pinMode(motorDerBackward, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  long distancia = medirDistancia();
  
  // Si hay un obstáculo a menos de 20 cm, toma acción
  if (distancia > 0 && distancia < 20) { 
    detener();
    delay(200);
    retroceder();
    delay(500);
    girarDerecha();
    delay(400);
  } else {
    avanzar();
  }
}

long medirDistancia() {
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);
  long duracion = pulseIn(echoPin, HIGH);
  return duracion * 0.034 / 2; // Conversión a centímetros
}

void avanzar() {
  digitalWrite(motorIzqForward, HIGH);
  digitalWrite(motorIzqBackward, LOW);
  digitalWrite(motorDerForward, HIGH);
  digitalWrite(motorDerBackward, LOW);
}

void retroceder() {
  digitalWrite(motorIzqForward, LOW);
  digitalWrite(motorIzqBackward, HIGH);
  digitalWrite(motorDerForward, LOW);
  digitalWrite(motorDerBackward, HIGH);
}

void girarDerecha() {
  digitalWrite(motorIzqForward, HIGH);
  digitalWrite(motorIzqBackward, LOW);
  digitalWrite(motorDerForward, LOW);
  digitalWrite(motorDerBackward, HIGH);
}

void detener() {
  digitalWrite(motorIzqForward, LOW);
  digitalWrite(motorIzqBackward, LOW);
  digitalWrite(motorDerForward, LOW);
  digitalWrite(motorDerBackward, LOW);
}
