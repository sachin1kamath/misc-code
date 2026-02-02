#include <iostream>
#include <string>
#include <vector>
using namespace std;

void findMoos(string contest, int length, int frequency) {
    //vector<string> moos;

    for (int i = 0; i < length - 3; i++) {
        char currentLetter = contest[i];
        char nextLetter = contest[i + 1];
        char letterAfter = contest[i + 2];
        cout << currentLetter;
        cout << nextLetter;
        cout << letterAfter + ' ';

    }

    //return moos;
}

int main() {
    findMoos("zzmoozzmoo", 10, 2);
    return 0;
}