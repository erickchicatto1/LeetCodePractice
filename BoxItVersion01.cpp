#include <iostream>

using namespace std;

class Box {
private:
    int l, b, h;

public:
    // 1. Constructor por defecto usando lista de inicialización
    Box() : l(0), b(0), h(0) {}

    // 2. Constructor parametrizado con validación simple
    Box(int length, int breadth, int height) {
        l = (length > 0) ? length : 0;
        b = (breadth > 0) ? breadth : 0;
        h = (height > 0) ? height : 0;
    }

    // 3. Constructor de copia
    Box(const Box& B) : l(B.l), b(B.b), h(B.h) {}

    // Getters
    int getLength() const { return l; }
    int getBreadth() const { return b; }
    int getHeight() const { return h; }

    // --- NUEVAS CARACTERÍSTICAS ---

    // 4. Cálculo de Área Superficial: 2(lb + lh + bh)
    long long CalculateSurfaceArea() const {
        return 2LL * ( (1LL*l*b) + (1LL*l*h) + (1LL*b*h) );
    }

    // 5. Operador de igualdad (para saber si dos cajas son idénticas)
    bool operator==(const Box& B) const {
        return (l == B.l && b == B.b && h == B.h);
    }

    // 6. Operador de desigualdad
    bool operator!=(const Box& B) const {
        return !(*this == B);
    }

    // --- MÉTODOS EXISTENTES OPTIMIZADOS ---

    long long CalculateVolume() const {
        return (long long)l * b * h;
    }

    // Operador < (Ordenamiento léxico)
    bool operator<(const Box& B) const {
        if (l != B.l) return l < B.l;
        if (b != B.b) return b < B.b;
        return h < B.h;
    }

    // Sobrecarga de salida
    friend ostream& operator<<(ostream& out, const Box& B) {
        out << "Box(L:" << B.l << ", B:" << B.b << ", H:" << B.h << ")";
        return out;
    }
};