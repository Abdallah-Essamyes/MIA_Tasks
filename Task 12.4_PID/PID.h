#include "Arduino.h"
#ifndef PID_H
#define PID_H

class PID{
private:
int u = 0;
int e = 0;
int eDerv = 0;
int ePrev = 0;
int eInt = 0;
long prev_time = 0;
long deltaT = 0;
int ki = 0;
int kp = 0;
int kd = 0;
float target = 0;
float current = 0;

public:
PID(int x, int y,int z);
void set_target(float t);
int pid_control(float current_speed);

};

#endif