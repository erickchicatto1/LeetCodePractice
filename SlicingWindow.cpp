#include <iostream>
#include <climits>

using namespace std;

int maxSumSubarray(int arr[],int n , int k){

    int max_sum = INT_MIN;
    int window_sum = 0;

    //Find the sum of the firts k elements
    for(int i = 0;i<k;i++){
        window_sum += arr[i];
    }


    //Now slide the window across the array
    for(int i=k;i<n;i++){
        window_sum += arr[i] - arr[i - k];  // Slide the window
        max_sum = max(max_sum,window_sum);
    }

    return max_sum;
}


int main(){

    int arr[] = {2,1,5,3,2};
    int k = 3;
    int n = sizeof(arr)/sizeof(arr[0]);

    cout << "Maximum sum of subarray of size " << k << " is " << maxSumSubarray(arr, n, k) << endl;



    return 0;
}

