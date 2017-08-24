/* https://www.codewars.com/kata/john-and-ann-sign-up-for-codewars/c */

/*
 * On day n the number of katas done by Ann should be n minus the number of
 * katas done by John at day t, t being equal to the number of katas done by Ann
 * herself at day n - 1.
 * a[n] = n - j[a[n - 1]]
 *
 * On day n the number of katas done by John should be n
 * minus the number of katas done by Ann at day t, t being equal to the number
 * of katas done by John himself at day n - 1.
 * j[n] = n - a[j[n - 1]]
 */


/*
 * Using Recursion actually slows down the process
 */

// long long compute_ann(long long n);
// long long compute_john(long long n);
//
// long long compute_ann(long long n) {
// 	if (n == 0) {
// 		return 1;
// 	} else {
// 		return n - compute_john(compute_ann(n - 1));
// 	}
// }
//
// long long compute_john(long long n) {
// 	if (n == 0) {
// 		return 0;
// 	} else {
// 		return n - compute_ann(compute_john(n - 1));
// 	}
// }

#include <stdio.h>
#include <stdlib.h>

long long *john(long long n);
long long *ann(long long n);

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

long long *john(long long n) {
	long long j[n];
	j[0] = 0;
	long long a[n];
	a[0] = 1;
	for (int i = 0; i < n - 1; i++) {
		j[i + 1] = i + 1 - a[j[i]];
		a[i + 1] = i + 1 - j[a[i]];
	}
	long long *dest = (long long *)malloc(sizeof(long long) * n);
	memcpy(dest, j, n * sizeof(long long));
	return dest;
}
long long sumJohn(long long n) {
	long long j[n];
	j[0] = 0;
	long long a[n];
	a[0] = 1;
	long long sumJ = 0;
	for (int i = 0; i < n - 1; i++) {
		j[i + 1] = i + 1 - a[j[i]];
		sumJ += j[i + 1];
		a[i + 1] = i + 1 - j[a[i]];
	}
	return sumJ;
}
long long *ann(long long n) {
	long long j[n];
	j[0] = 0;
	long long a[n];
	a[0] = 1;
	for (int i = 0; i < n - 1; i++) {
		j[i + 1] = i + 1 - a[j[i]];
		a[i + 1] = i + 1 - j[a[i]];
	}
	long long *dest = (long long *)malloc(sizeof(long long) * n);
	memcpy(dest, a, n * sizeof(long long));
	return dest;
}
long long sumAnn(long long n) {
	long long j[n];
	j[0] = 0;
	long long a[n];
	a[0] = 1;
	long long sumA = 1;
	for (int i = 0; i < n - 1; i++) {
		j[i + 1] = i + 1 - a[j[i]];
		a[i + 1] = i + 1 - j[a[i]];
		sumA += a[i + 1];
	}
	return sumA;
}
