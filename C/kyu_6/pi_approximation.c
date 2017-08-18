/*
 * https://www.codewars.com/kata/pi-approximation/c
 */

// learnt: 	- printf type specifiers
// 			- fabs in math.h

#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#define MY_PI 3.14159265358979323846

char *iterPi(double epsilon) {
	double my_pi = 4;
	double my_temp_pi = 0;
	int sign_flag = 1;
	int denom = 1;
	int num_iter = 0;
	// while (MY_PI - my_pi > epsilon || my_pi - MY_PI > epsilon) {
	while (fabs(my_pi - MY_PI) > epsilon){
		my_temp_pi = my_temp_pi + (double)sign_flag / (double)denom;
		my_pi = 4 * my_temp_pi;
		denom += 2;
		num_iter++;
		sign_flag = -sign_flag;
	}
	char *output = malloc(128);
	snprintf(output, 128, "[%d, %.10f]", num_iter, my_pi);
	return output;
}

int main(int argc, char const *argv[]) {
	char *out = iterPi(0.1);
	printf("%s\n", out);
	free(out);
	return 0;
}
