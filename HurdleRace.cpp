#include <iostream>
#include <vector>

using namespace std;

int hurdleFunc(const vector<int>& value, int k) {

    int maxValue = 0;

    for (int i : value) {
        if (i > maxValue) {
            maxValue = i;
        }
    }

    return max(0, maxValue - k);
}

int main() {

    vector<int> height = {1, 6, 3, 5, 2};
    int k = 4;

    cout << hurdleFunc(height, k) << endl;

    return 0;
}
