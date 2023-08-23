#include <gtest/gtest.h>
#include <iostream>
#include "solution.hpp"

namespace {

  TEST(Solution, convertToTitle) {
    // EXPECT_EQ("A", Solution().convertToTitle(1));
    // EXPECT_EQ("AA", Solution().convertToTitle(27));
    // EXPECT_EQ("GDCF", Solution().convertToTitle(125820));
    // EXPECT_EQ("ZY", Solution().convertToTitle(701));
    // EXPECT_EQ("Z", Solution().convertToTitle(26));
    EXPECT_EQ("AZ", Solution().convertToTitle(52));
  }

}

int main(int argc, char** argv) {
    ::testing::InitGoogleTest(&argc, argv);

    return RUN_ALL_TESTS();
}
