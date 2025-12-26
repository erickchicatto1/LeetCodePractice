#include <iostream>

using namespace std;

int max_of_four(int a, int b , int c , int d){

    int result = 0 ;
    int values[4] = {a,b,c,d};

    for(int i = 0 ; i<4;i++){
       if(values[i]>result){
        result = values[i];
       } 
    }

    return result;
}


int main(){

    int a = 2,b=3,c=4,d=5;
    max_of_four(a,b,c,d);


    return 0;
}