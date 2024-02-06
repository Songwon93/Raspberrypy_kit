#include <stdio.h>
#include <wiringPi.h>
#include <softPwm.h>
#include <unistd.h>

#define STEP_OUTA 27
#define STEP_OUTB 0
#define STEP_OUT2A 1
#define STEP_OUT2B 24
#define SW1 3
#define SW2 4
#define SW3 5
#define SW4 6

void setStepperRotation(int stepA, int stepB, int step2A, int step2B) {
    digitalWrite(STEP_OUTA, stepA);
    digitalWrite(STEP_OUTB, stepB);
    digitalWrite(STEP_OUT2A, step2A);
    digitalWrite(STEP_OUT2B, step2B);

    delayMicroseconds(500); // Adjust delay as needed
}

int main() {

    wiringPiSetup();

    pinMode(STEP_OUTA, OUTPUT);
    pinMode(STEP_OUTB, OUTPUT);
    pinMode(STEP_OUT2A, OUTPUT);
    pinMode(STEP_OUT2B, OUTPUT);

    pinMode(SW1, INPUT);
    pinMode(SW2, INPUT);
    pinMode(SW3, INPUT);
    pinMode(SW4, INPUT);

    while (1) {
        if (digitalRead(SW1) == LOW) {
            // Set stepper motor rotation for button 1 (45 degrees)
            setStepperRotation(1, 0, 0, 1);
            printf("45->\n");
            delay(1000); // Rotate for 1 second
        } else if (digitalRead(SW2) == LOW) {
            // Set stepper motor rotation for button 2 (90 degrees)
            setStepperRotation(1, 1, 0, 0);
            printf("90 ->\n");
            delay(1000); // Rotate for 1 second
        } else if (digitalRead(SW3) == LOW) {
            // Set stepper motor rotation for button 3 (180 degrees)
            setStepperRotation(0, 1, 1, 0);
            printf("180 ->\n");
            delay(1000); // Rotate for 1 second
        } else if (digitalRead(SW4) == LOW) {
            // Set stepper motor rotation for button 4 (100 degrees)
            setStepperRotation(0, 0, 1, 1);
            printf("100 ->\n");
            delay(1000); // Rotate for 1 second
        }
    }

    return 0;
}
