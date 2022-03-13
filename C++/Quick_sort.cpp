#include<iostream>
using namespace std;

void swap(int *a, int *b){
	int temp = *a;
	*a = *b;
	*b = temp;
}


int partition(int arr[],int start, int end){

	int mid,pivot,i,j;
	mid = (start + end) / 2;
	pivot = arr[mid];
	i = start;
	j = end;
	swap(&arr[start],&arr[mid]);
	while(i < j){
		while(arr[i] <= pivot)
			i++;
		while(arr[j] > pivot)
			j--;
		if(i < j)
			swap(&arr[i], &arr[j]);
	}
	swap(&arr[j], &arr[start]);
	return j;
}

void quick_sort(int arr[],int start,int end){
	int mid;
	if(start < end){
		mid = partition(arr, start, end);
		quick_sort(arr, start, mid-1);
		quick_sort(arr, mid+1, end);
	}
}
void print(int arr[], int n){
	int i;
	for(i = 0;i < n;i++)
		cout<<arr[i]<<" ";
	cout<<endl;
}
int main(){

	int n ;
	cout<<"Enter array size : ";
	cin>>n;
	int *arr = (int*)malloc(n * sizeof(int));
	for(int i=0;i<n;i++){
		cout<<"Enter element :";
		cin>>arr[i];
	}
	cout<<"\nBefore sort :\n";
	print(arr,n);
	cout<<"\nAfter sort :\n";
	quick_sort(arr,0,n-1);
	print(arr,n);
}
