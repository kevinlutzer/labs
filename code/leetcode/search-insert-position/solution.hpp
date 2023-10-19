#include <stdlib.h>
#include <stdio.h>
#include <string>
#include <cmath>
#include <iostream>

using namespace std;

class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        /*
        Example 1:

        vector<int> vect{ 10, 20, 30 };
        Input: nums = [1,3,5,6], target = 5
        Output: 2

        Example 2:

        Input: nums = [1,3,5,6], target = 2
        Output: 1

        Example 3:

        Input: nums = [1,3,5,6], target = 7
        Output: 4
        */

        int nums_size = nums.size();
        for(int i=0; i < nums_size; i++){

            // base case if target is equal to num
            if (nums[i] == target) {
                return i;
            }

            // handle top bound
            if (nums[i] < target && i + 1 >= nums_size) {
                return i + 1;
            }

            // handle bottom bound
            if (nums[i] > target && i - 1 <= 0) {
                return i - 1;
            }

            // handle for targets in array
            if ((i > 0 && nums[i - 1] < target) || (i == 0 && nums[i] < target)) {
                return i + 1;
            }
        }
        return -1;
    }
};