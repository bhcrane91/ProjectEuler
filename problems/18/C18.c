#include <stdio.h>
#define L 15

int* roll(int* arr, int step) {
	int sign = step > 0 ? 1 : -1;
	step %= (L*sign);
	if (step == 0) return arr;
	int rolled[L];
	int start = (L-step)%L;
	for (int i = 0; i < L; i++) rolled[i] = arr[(i+start)%L];
	return rolled;
}

int* arrmax(int* a, int* b) {
	int* mx[L];
	for (int i = 0; i < L; i++) mx[i] = a[i] > b[i] ? a[i] : b[i];
	return mx;
}

int* idxsum(int* a, int* b) {
	int* mx[L];
	for (int i = 0; i < L; i++) mx[i] = a[i] + b[i];
	return mx;
}

int main() {
	int triangle[L][L] = {
		{ 4,62,98,27,23, 9,70,98,73,93,38,53,60, 4,23},
		{63,66, 4,68,89,53,67,30,73,16,69,87,40,31, 0},
		{91,71,52,38,17,14,91,43,58,50,27,29,48, 0, 0},
		{70,11,33,28,77,73,17,78,39,68,17,57, 0, 0, 0},
		{53,71,44,65,25,43,91,52,97,51,14, 0, 0, 0, 0},
		{41,48,72,33,47,32,37,16,94,29, 0, 0, 0, 0, 0},
		{41,41,26,56,83,40,80,70,33, 0, 0, 0, 0, 0, 0},
		{99,65, 4,28, 6,16,70,92, 0, 0, 0, 0, 0, 0, 0},
		{88, 2,77,73, 7,63,67, 0, 0, 0, 0, 0, 0, 0, 0},
		{19, 1,23,75, 3,34, 0, 0, 0, 0, 0, 0, 0, 0, 0},
		{20, 4,82,47,65, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0},
		{18,35,87,10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0},
		{17,47,82, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0},
		{95,64, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0},
		{75, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0}
	};


	for (int row = 0; row < L-1; row++) {
		int* right = idxsum(roll(triangle[row],-1), triangle[row+1]);
		int* left = idxsum(triangle[row], triangle[row+1]);
		for (int i = L-row-1; i < L; i++) {
			right[i] = 0;
			left[i] = 0;
		}
		triangle[row+1] = &arrmax(left,right);
	}

	printf("%d\n",triangle[L-1][0]);
}