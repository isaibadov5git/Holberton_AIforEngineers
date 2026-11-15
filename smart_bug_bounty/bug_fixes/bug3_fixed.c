#include <stdio.h>

double compute_sensor_average(const int *readings, int count) {
    int buffer[5];
    int sum = 0;

    if (readings == NULL || count <= 0 || count > 5) {
        return 0.0;
    }

    for (int i = 0; i < count; i++) {
        buffer[i] = readings[i];
        sum += buffer[i];
    }

    return (double)sum / count;
}

int main(void) {
    int temps[5] = {24, 25, 26, 25, 27};
    printf("Average Temp: %.2f\n", compute_sensor_average(temps, 5));
    return 0;
}
