#include <stdio.h>
#include <stdlib.h>
#include <wiringPi.h>
#include <unistd.h>
#include <time.h>

#define pin_RED 7
#define pin_GREEN 21
#define pin_BLUE 22

int main() {
    wiringPiSetup();
    
    pinMode(pin_RED, OUTPUT);
    pinMode(pin_GREEN, OUTPUT);
    pinMode(pin_BLUE, OUTPUT);

    for (int i = 0; i < 10; ++i) {
        digitalWrite(pin_RED, HIGH);
        usleep(500000);
        digitalWrite(pin_RED, LOW);
        usleep(500000);

        digitalWrite(pin_GREEN, HIGH);
        usleep(500000);
        digitalWrite(pin_GREEN, LOW);
        usleep(500000);

        digitalWrite(pin_BLUE, HIGH);
        usleep(500000);
        digitalWrite(pin_BLUE, LOW);
        usleep(500000);
    }

    return 0;
}