#include <gtest/gtest.h>
#include <iostream>
#include "solution.hpp"

namespace {

  TEST(Solution, searchInsert) {
    vector<int> nums{ 1, 3, 5, 6 };
    // int target = 5;
    // EXPECT_EQ(2, Solution().searchInsert(nums, target));
    int target = 2;
    EXPECT_EQ(1, Solution().searchInsert(nums, target));
    // target = 7;
    // EXPECT_EQ(4, Solution().searchInsert(nums, target));
  }
}

int main(int argc, char** argv) {
    ::testing::InitGoogleTest(&argc, argv);

    return RUN_ALL_TESTS();
}
