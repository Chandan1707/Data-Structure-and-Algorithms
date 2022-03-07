#include<iostream>
using namespace std;

void merge(int arr[], int start, int mid, int end){
    int i,j,k = start;
    int n1,n2;

    n1 = mid - start + 1;
    n2 = end - mid;

    int m1[n1],m2[n2];

    for(i = 0;i<n1;i++)
        m1[i] = arr[start+i];
    
    for(i = 0;i<n2;i++)
        m2[i] = arr[i+mid+1]; 
    
    for(i=0,j=0; i < n1 && j < n2;){
        if(m1[i] < m2[j])
            arr[k++] = m1[i++];
        else
            arr[k++] = m2[j++];
    }
    while(i < n1)
        arr[k++] = m1[i++];
    while(j < n2)
        arr[k++] = m2[j++];
}

void merge_sort(int arr[],int start,int end){
    if(start < end){
        int mid = (start + end)/2;
        merge_sort(arr, start, mid);
        merge_sort(arr, mid+1, end);

        merge(arr,start,mid,end);
    }
}
void print(int arr[],int n){
    for(int i=0;i < n;i++){
        cout<<arr[i]<<" ";
    }
}

int main(){
    int n= 8,i;
    int *arr = (int*)malloc(n * sizeof(int));
    for(i = 0;i < n; i++){
        cout<<"enter element :";
        cin>>arr[i];
    }
    merge_sort(arr,0,8-1);
    print(arr,n);
    return 1;
}