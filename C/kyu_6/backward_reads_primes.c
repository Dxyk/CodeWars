#include <stdio.h>
#include <stdlib.h>
/**
 * Backwards Read Primes are primes that when read backwards in base 10 (from
right to left) are a different prime. (This rules out primes which are
palindromes.)

Examples:
13 17 31 37 71 73 are Backwards Read Primes
13 is such because it's prime and read from right to left writes 31 which is
prime too. Same for the others.

Task

Find all Backwards Read Primes between two positive given numbers (both
inclusive), the second one being greater than the first one. The resulting array
or the resulting string will be ordered following the natural order of the prime
numbers.

Example

backwardsPrime(2, 100) => [13, 17, 31, 37, 71, 73, 79, 97] backwardsPrime(9900,
10000) => [9923, 9931, 9941, 9967]

C returns a structure. See "Solution" and "Examples" tabs
 */


// C returns a structure. Results are compared by way of strings. See "Examples"
// tab.
typedef long long ll;
// sz is array size.
typedef struct Data Data;
struct Data {
	ll *array;
	int sz;
};

int backwards(int num) {
	int backward = 0;
	while (num != 0) {
		backward *= 10;
		backward += num % 10;
		num /= 10;
	}
	return backward;
}

int is_prime(int num) {
	for (int i = 2; i * i < num; i++) {
		if (num % i == 0) {
			return 0;
		}
	}
	return 1;
}

Data *backwardsPrime(ll start, ll end) {
	Data *data = malloc(sizeof(Data));
	int sz = 0;
	int i = start;
	while (i < end) {
		if (is_prime(i) && is_prime(backwards(i)) && i != backwards(i)) {
			sz ++;
		}
		i++;
	}
	i = 0;
	data->sz = sz;
	data->array = malloc(sizeof(int) * sz);
	while (start < end) {
		if (is_prime(start) && is_prime(backwards(start)) && start != backwards(start)) {
			data->array[i] = start;
			i ++;
		}
		start++;
	}
	return data;
}

int main(int argc, char const *argv[]) {
	Data *d = backwardsPrime(2, 100);
	for (int i = 0; i < d->sz; i++) {
		printf("%llu ", d->array[i]);
	}
	return 0;
}
