#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

class Solution {
public:
    string addBinary(string a, string b) {
        string res = "";
        int i = a.size() - 1;
        int j = b.size() - 1;
        int carry = 0;

        while (i >= 0 || j >= 0 || carry) {
            int sum = carry;
            
            if (i >= 0) {
                sum += a[i] - '0';
                i--;
            }
            
            if (j >= 0) {
                sum += b[j] - '0';
                j--;
            }
            
          // 1. Decidir qué bit escribir
          if (sum == 0 || sum == 2) {
              res.push_back('0');
          } else { // sum es 1 o 3
              res.push_back('1');
          }
          
          // 2. Decidir si nos llevamos acarreo
          if (sum >= 2) {
              carry = 1;
          } else {
              carry = 0;
          }
        
        }

        reverse(res.begin(), res.end());
        return res;
    }
};

int main() {
    Solution sol;

    // Casos de prueba
    string s1 = "11", s2 = "1";
    string s3 = "1010", s4 = "1011";

    cout << "--- Prueba de Suma Binaria ---" << endl;
    
    // Ejemplo 1: 11 + 1 = 100
    cout << "Suma 1: " << s1 << " + " << s2 << " = " << sol.addBinary(s1, s2) << endl;
    
    // Ejemplo 2: 1010 + 1011 = 10101
    cout << "Suma 2: " << s3 << " + " << s4 << " = " << sol.addBinary(s3, s4) << endl;

    return 0;
}