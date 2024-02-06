#include <wiringPi.h>
#include <softTone.h>
#include <unistd.h>
#include <stdio.h>

const int buzzer = 1;

void playTune(int note, float duration) {
    softToneWrite(buzzer, note);
    usleep(duration * 1e6);
    softToneWrite(buzzer, 0);  // 부저 끄기
    usleep(100000);  // 소리 간격을 위한 대기 시간
}

int main() {
    if (wiringPiSetup() == -1) {
        return 1;  // wiringPi 초기화 실패
    }

    if (softToneCreate(buzzer) == -1) {
        return 2;  // softTone 초기화 실패
    }

    // 작은별 계이름
    int scale[] = {262, 294, 330, 349, 392, 440, 494};

    // 작은별 악보
    int twinkle[] = {0, 0, 4, 4, 5, 5, 4, 3, 3, 2, 2, 1, 1, 0,
                     4, 4, 3, 3, 2, 2, 1, 4, 4, 3, 3, 2, 2, 1,
                     0, 0, 4, 4, 5, 5, 4, 3, 3, 2, 2, 1, 1, 0};

    // 각 음표의 지속 시간
    float note_duration[] = {0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 1, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 1,
                             0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 1, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 1,
                             0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 1, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 1};

    for (int i = 0; i < sizeof(twinkle) / sizeof(twinkle[0]); ++i) {
        playTune(scale[twinkle[i]], note_duration[i]);

        if (i == 6 || i == 13 || i == 20 || i == 27 || i == 34 || i == 41) {
            usleep(note_duration[i] * 1e6);  // 쉼표일 경우
        }
    }

    softToneWrite(buzzer, 0);  // 부저 끄기
    return 0;
}