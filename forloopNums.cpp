#include <iostream>

static const std::string names[] = {
    "one","two","three","four","five","six","seven","eight","nine"
};


int main(){

    int a,b;
    std::cin >> a >> b;

    for(int i = a ; i <b+1;i++){
        
        if(i<=9){
           std::cout << names[i-1] << std::endl;
           continue;
        }

    std::cout << (i%2 == 0 ? "even":"odd")<<std::endl;
    
    }

}