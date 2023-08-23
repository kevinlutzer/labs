#include <stdlib.h>
#include <stdio.h>
#include <string>
#include <cmath>
#include <iostream>

using namespace std;

class Solution {
public:
    string convertToTitle(int columnNumber) {
        // A starts at 65
        // Z ends at 90
        // 26*26^2 + 26*26  + 26 = ZZZ

        int base = 26;
        int val = 2;
    
        string str = "";

        while(columnNumber >= 0) {

            val = columnNumber % base;
            cout << "Column Number: " << columnNumber << ", Val: " << val << ", divide 26: " << columnNumber / base <<  endl;
            columnNumber = columnNumber / base;

            str.push_back(char(val + 64));

            if (columnNumber == 0) {
                columnNumber = -1;
            }
        }

        cout << "String before reversal: " << str << endl;

        reverse(str.begin(), str.end()); 

        return str;
    }
};