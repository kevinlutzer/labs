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
        int carry = 0;

        while(columnNumber >= 0) {

            val = columnNumber % base - carry;
            carry = 0; 

            cout << "Carry: " << carry << ", Modulo: " << columnNumber % base << ", Column Number: " << columnNumber << ", Val: " << val << ", divide 26: " << columnNumber / base <<  endl;
            columnNumber = columnNumber / base;

            if (val == 0) {
                str.push_back('Z');
                carry = 1;
            } else {
                str.push_back(char(val + 64));
            }

            if (columnNumber == 0 || (columnNumber == 1 && val == 0)) {
                columnNumber = -1;
            }
        }

        cout << "String before reversal: " << str << endl;

        reverse(str.begin(), str.end()); 

        return str;
    }
};