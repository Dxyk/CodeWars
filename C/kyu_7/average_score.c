#include <stddef.h>
#include <stdio.h>

int average(const int *values, size_t count);

/*
 * Create a function that returns the average of an array of numbers ("scores"),
 * rounded to the nearest whole number. You are not allowed to use any loops
 * (including for, for/in, while, and do/while loops).
 */

int sum(const int *values, unsigned int count) {
	if (count == 0)
		return 0;
	else
		return values[0] + sum(values + 1, count - 1);
}

int average(const int *values, size_t count) {
	double avg = sum(values, count) / (double)count;
	return avg + 0.5;
}

int main(int argc, char const *argv[]) {
	int count = 2;
	int arr[2] = {1, 2};

	printf("%d\n", average(arr, count));
	return 0;
}
