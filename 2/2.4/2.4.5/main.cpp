#include <iostream>
using namespace std;

int N, S;
long long Answer = 0;

int main() {
    cin >> N >> S;

    int cnt = 0;
    for (int i = 1; i <= N; i++) {
        for (int j = 1; j <= N; j++) {
            if (i + j <= S) {
                Answer += 1;
            }
        }
    }
    cout << Answer << endl;
    return 0;
}
