class Solution {
public:
    string addBinary(string a, string b) {
        string res = "";
        int i = a.size() - 1;
        int j = b.size() - 1;
        int carry = 0;

        // Mientras haya bits por procesar o un acarreo pendiente
        while (i >= 0 || j >= 0 || carry) {
            // Sumamos el acarreo actual
            int sum = carry;
            
            // Sumamos el bit de 'a' si existe
            if (i >= 0) sum += a[i--] - '0';
            
            // Sumamos el bit de 'b' si existe
            if (j >= 0) sum += b[j--] - '0';
            
            // El nuevo bit es el resto de dividir por 2 (0 o 1)
            res.push_back((sum % 2) + '0');
            
            // El nuevo acarreo es el cociente de dividir por 2
            carry = sum / 2;
        }

        // Como agregamos al final, el resultado está al revés
        reverse(res.begin(), res.end());
        return res;
    }
};