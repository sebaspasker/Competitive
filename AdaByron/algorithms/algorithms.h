#ifndef _ALGORITHMS_
#define _ALGORITHMS_

#include <iostream>
#include<stdlib.h> 
#include<stdio.h> 
#include<vector>
#include<algorithm>

using namespace std;

class Algorithms {
	public:
		void heapSort(int arr[], int n);
		void quickSort(int arr[], int low, int high);
		void insertionSort(int arr[], int n);
		void insertionSortRecursive(int arr[], int n);
		void mergeSort(int arr[], int l, int r);
		void selectionSort(int arr[], int n);
		void countSort(vector<int>& arr);
		void countSort(int arr[], int n, int exp); // This one is for radix Sort
		void bubbleSort(int arr[], int n);
		void radixSort(int arr[], int n);
		void bucketSort(float arr[], int n);
		void shellSort(int arr[], int n);
		void treeSort(int arr[], int n);
		void combSort(int a[], int n);
};

#endif
