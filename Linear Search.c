#include <stdio.h>

int linearSearch(int arr[], int size, int target) {
    for (int i = 0; i < size; ++i) {
        if (arr[i] == target) {
            return i; // Target found
        }
    }
    return -1; // Target not found
}

int main() {
    int data[] = {3, 8, 12, 5, 19, 21, 25, 30};
    int size = sizeof(data) / sizeof(data[0]);
    int target = 19;

    int index = linearSearch(data, size, target);

    if (index != -1) {
        printf("Target %d found at index %d\n", target, index);
    } else {
        printf("Target %d not found in the array\n", target);
    }

    return 0;
}
