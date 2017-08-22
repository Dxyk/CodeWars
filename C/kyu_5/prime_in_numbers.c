/* https://www.codewars.com/kata/primes-in-numbers/c */

#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/*
 * Algo:
 * since num's largest prime factor is num
 * create an array of num nums
 * each slot in the arr represents the potential factor.
 * the values in the slot is the max times of the factor
 */
char *factors(int num) {
	int count = 0;
	char *result = malloc(sizeof(char) * 258);
	strcpy(result, "\0");

	int i = 2;
	while (i <= num) {


		count = 0;
		while (num % i == 0) {
			count++;
			num /= i;
		}

		if (count > 0) {
			// printf("%d %d %d\n", i, count, num);
			strcat(result, "(");
			if (count == 1) {
				char factor[12];
				sprintf(factor, "%d", i);
				strcat(result, factor);
			} else {
				char factor[12];
				char times[12];
				sprintf(factor, "%d", i);
				sprintf(times, "%d", count);
				strcat(result, factor);
				strcat(result, "**");
				strcat(result, times);
			}
			strcat(result, ")");
		}

		i += 1;
	}
	return result;
}

int main(int argc, char const *argv[]) {
	// int num = strtol(argv[1], NULL, 10);
	printf("%s\n", factors(7775460));
	return 0;
}
