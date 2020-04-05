#include <iostream>
#include <stdlib.h>
#include <bits/stdc++.h>

using namespace std;

void bubbleSort(int hours[][2], int N) {
 	int i, j;
	for(i=0; i<N-1; i++) {
		for(j=0; j<N-i-1;j++) {
			if(hours[j][0] > hours[j+1][0]) {
				swap(hours[j][0], hours[j+1][0]);
				swap(hours[j][1], hours[j+1][1]);
			}
		}
	}
}

struct {
	vector<int> hours;
} Friend;

int schedulingAlgorithm(int hours[][2], N) {
	vector<Friend> friends;	
	for(unsigned int i=0; i<N; i++) {
	}
}

int main() {
	while(true) {
		int N;
		scanf("%d", &N);
		int hours[N][2];
		for(int i=0; i<N; i++) {
			scanf("%d %d", &hours[i][0], &hours[i][1]);
		}
		bubbleSort(hours, N);
		int friends = schedulingAlgorithm(hours, N);
	}
}
