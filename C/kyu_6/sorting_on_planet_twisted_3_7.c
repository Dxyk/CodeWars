/* https://www.codewars.com/kata/sorting-on-planet-twisted-3-7/c */
#include <stdlib.h>
#include <stdio.h>
#include <string.h>


/**
 * comparison function. defines how sorting is done
 * @param  elem1 the pointer that points to the element 1
 * @param  elem2 the pointer that points to the element 2
 * @return       1 if f_cpy > s_cpy; -1 if f_cpy < s_cpy; 0 if f_cpy == s_cpy
 */
int comp(const void *elem1, const void *elem2) {
	int f = *((int *)elem1);
	int s = *((int *)elem2);
	int f_cpy = f;
	int s_cpy = s;
	char temp1[12], temp2[12];
	sprintf(temp1, "%d", f_cpy);
	for (int i = 0; i < 11; i++) {
		if (temp1[i] == '3') {
			temp1[i] = '7';
		} else if (temp1[i] == '7') {
			temp1[i] = '3';
		}
	}
	sprintf(temp2, "%d", s_cpy);
	for (int i = 0; i < 11; i++) {
		if (temp2[i] == '3') {
			temp2[i] = '7';
		} else if (temp2[i] == '7') {
			temp2[i] = '3';
		}
	}
	f_cpy = (int) strtol(temp1, NULL, 10);
	s_cpy = (int) strtol(temp2, NULL, 10);
	if (f_cpy > s_cpy)
		return 1;
	if (f_cpy < s_cpy)
		return -1;
	return 0;
}

int *sortTwisted37(int *array, int arrayLength) {
	int *result = malloc(sizeof(int) * arrayLength);
	for (size_t i = 0; i < arrayLength; i++) {
		result[i] = array[i];
	}
	qsort(result, arrayLength, sizeof(int), comp);
	return result;
}


int main(int argc, char const *argv[]) {
	int arr[9] = {1, 2, 4, 3, 5, 6, 7, 8, 9};
	int *arr_new = sortTwisted37(arr, 9);
	for (int i = 0; i < 9; i ++) {
		printf("%d ", arr_new[i]);
	}
	return 0;
}
