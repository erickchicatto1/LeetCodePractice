#include <iostream>
#include <vector>
#include <algorithm>

void miniMaxSum(const std::vector<int>& arr){

    long long total_sum = 0;
    long long min_val = arr[0];
    long long max_val = arr[0];

    for(int x:arr){
        total_sum += x;
        
        if(x<min_val){
            min_val = x;
        }

        if (x>max_val){
            max_val = x;
        }


    }

    long long resultado_min = total_sum - max_val;
    long long resultado_max = total_sum - min_val;

    std::cout << resultado_min << " " << resultado_max << std::endl;

}

int main(){
    std::vector<int> arr = {1,2,3,4,5};
    miniMaxSum(arr);
    return 0;
}