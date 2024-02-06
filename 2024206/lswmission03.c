#include <stdio.h>
#include <stdlib.h>
#include <wiringPi.h>
#include <softTone.h>
#include <unistd.h>
#include <time.h>

#define SW1 3
#define SW2 4
#define SW3 5
#define SW4 6
#define BUZZER_PIN 1

void playNote(int frequency, int duration) {
    softToneWrite(BUZZER_PIN, frequency);
    usleep(duration * 1000); // Sleep in microseconds
    softToneWrite(BUZZER_PIN, 0); // Stop the buzzer
}

int main(void) {
    const int buzzer_pin = BUZZER_PIN;

    wiringPiSetup();

    pinMode(buzzer_pin, PWM_OUTPUT);

    pwmSetClock(19);
    pwmSetMode(PWM_MODE_MS);

    const int melody[] = { 262, 294, 330, 349, 392, 440, 494, 523 };

    pinMode(SW1, INPUT);
    pinMode(SW2, INPUT);
    pinMode(SW3, INPUT);
    pinMode(SW4, INPUT);

    int ret;

    while (1) {
        ret = digitalRead(SW1);
        if (ret == 0) {
            int scale[] = {932, 1125, 1318, 1396, 1568, 1760, 1975};
            int twinkle[] = {1, 3, 5, 1, 3, 5, 6, 6, 6, 5, 4, 4, 4, 3, 3, 3, 2, 2, 2, 1};
            softToneCreate(BUZZER_PIN);
            for (int i = 0; i < 20; ++i) {  // Adjust the loop size to match the size of your 'twinkle' array
                playNote(scale[twinkle[i]], (i == 6 || i == 13 || i == 20) ? 1000 : 500);
            }
        }

        ret = digitalRead(SW2);
        if (ret == 0) {
            int scale[] = {932, 1125, 1318, 1396, 1568, 1760, 1975};
            int twinkle[] = {5, 5, 6, 6, 5, 5, 3, 5, 5, 3, 3, 2, 5, 5, 6, 6, 5, 5, 3, 5, 3, 2, 3, 1};
            softToneCreate(BUZZER_PIN);
            for (int i = 0; i < 24; ++i) {  // Adjust the loop size to match the size of your 'twinkle' array
                playNote(scale[twinkle[i]], (i == 6 || i == 13 || i == 20 || i == 27) ? 1000 : 500);
            }
        }

        ret = digitalRead(SW3);
        if (ret == 0) {
            int scale[] = {262, 294, 330, 349, 392, 440, 494};
            int twinkle[] = {1, 1, 5, 5, 6, 6, 5, 4, 4, 3, 3, 2, 2, 1,
                            5, 5, 4, 4, 3, 3, 2, 5, 5, 4, 4, 3, 3, 2,
                            1, 1, 5, 5, 6, 6, 5, 4, 4, 3, 3, 2, 2, 1};
            softToneCreate(BUZZER_PIN);
            for (int i = 0; i < 42; ++i) {
                playNote(scale[twinkle[i]], (i == 6 || i == 13 || i == 20 || i == 27 || i == 34 || i == 41) ? 1000 : 500);
            }
        }

        ret = digitalRead(SW4);
        if (ret == 0) {
            printf("SW4 Button push !!\n");
        }

        sleep(1);
    }
        return 0;
}
