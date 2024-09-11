#include "PID.h"

PID::PID(int x, int y,int z){
  kp = x;
  ki = y;
  kd = z;
};

void PID::set_target(float t){
  target = t;
}

int PID::pid_control (float current){
  deltaT = (millis() - prev_time)/1e3;
  e = target - current;
  eDerv = (e - ePrev)/deltaT;
  ePrev = e;
  eInt += e * deltaT;
  prev_time = millis();
  u = kp*e + kd*eDerv + ki*eInt;
  return u; 
}