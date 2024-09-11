#include "PID.h";
PID controller = PID(1, 1, 0);
float vFilt = 0;
float vPrev = 0;
float target_speed = 0;
float current_speed = 0;
float exponential_smoothing(float a);
//pin 5 supports pwm
int motor_pwm_pin = 5;
int dir_0_pin = 2;
int dir_1_pin = 3;

//i had no way to physically test the code so there might be some logical errors but all the syntax is correct
void setup() {

  pinMode(motor_pwm_pin,OUTPUT);
  pinMode(dir_0_pin,OUTPUT);
  pinMode(dir_1_pin,OUTPUT);
  //set motor direction
  digitalWrite(dir_0_pin, LOW);
  digitalWrite(dir_1_pin, HIGH);
  //turn motor off at startup
  digitalWrite(motor_pwm_pin, LOW);
  //define the kp,ki,kd
  target_speed = 30;
  //raise speed using exponential smoothing
  while ( vFilt != target_speed){
    analogWrite(motor_pwm_pin,exponential_smoothing(0.9));
  }
  
  controller.set_target(target_speed);
}

void loop() {
  //continously handle the error
  analogWrite(motor_pwm_pin, controller.pid_control(current_speed));
}

//ISR or function to interuppt code to set current_speed to an encoder reading

float exponential_smoothing(float a) {
  vFilt = a * vPrev + (1 - a) * target_speed;
  vPrev = vFilt;
  return vFilt;
}
