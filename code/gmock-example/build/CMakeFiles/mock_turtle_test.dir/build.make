# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.27

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:

#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:

# Disable VCS-based implicit rules.
% : %,v

# Disable VCS-based implicit rules.
% : RCS/%

# Disable VCS-based implicit rules.
% : RCS/%,v

# Disable VCS-based implicit rules.
% : SCCS/s.%

# Disable VCS-based implicit rules.
% : s.%

.SUFFIXES: .hpux_make_needs_suffix_list

# Command-line flag to silence nested $(MAKE).
$(VERBOSE)MAKESILENT = -s

#Suppress display of executed commands.
$(VERBOSE).SILENT:

# A target that is always out of date.
cmake_force:
.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /opt/homebrew/Cellar/cmake/3.27.1/bin/cmake

# The command to remove a file.
RM = /opt/homebrew/Cellar/cmake/3.27.1/bin/cmake -E rm -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /Users/kevinlutzer/Projects/labs/code/gmock-example

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /Users/kevinlutzer/Projects/labs/code/gmock-example/build

# Include any dependencies generated for this target.
include CMakeFiles/mock_turtle_test.dir/depend.make
# Include any dependencies generated by the compiler for this target.
include CMakeFiles/mock_turtle_test.dir/compiler_depend.make

# Include the progress variables for this target.
include CMakeFiles/mock_turtle_test.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/mock_turtle_test.dir/flags.make

CMakeFiles/mock_turtle_test.dir/mock_turtle_test.cc.o: CMakeFiles/mock_turtle_test.dir/flags.make
CMakeFiles/mock_turtle_test.dir/mock_turtle_test.cc.o: /Users/kevinlutzer/Projects/labs/code/gmock-example/mock_turtle_test.cc
CMakeFiles/mock_turtle_test.dir/mock_turtle_test.cc.o: CMakeFiles/mock_turtle_test.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green --progress-dir=/Users/kevinlutzer/Projects/labs/code/gmock-example/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object CMakeFiles/mock_turtle_test.dir/mock_turtle_test.cc.o"
	/Library/Developer/CommandLineTools/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -MD -MT CMakeFiles/mock_turtle_test.dir/mock_turtle_test.cc.o -MF CMakeFiles/mock_turtle_test.dir/mock_turtle_test.cc.o.d -o CMakeFiles/mock_turtle_test.dir/mock_turtle_test.cc.o -c /Users/kevinlutzer/Projects/labs/code/gmock-example/mock_turtle_test.cc

CMakeFiles/mock_turtle_test.dir/mock_turtle_test.cc.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green "Preprocessing CXX source to CMakeFiles/mock_turtle_test.dir/mock_turtle_test.cc.i"
	/Library/Developer/CommandLineTools/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /Users/kevinlutzer/Projects/labs/code/gmock-example/mock_turtle_test.cc > CMakeFiles/mock_turtle_test.dir/mock_turtle_test.cc.i

CMakeFiles/mock_turtle_test.dir/mock_turtle_test.cc.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green "Compiling CXX source to assembly CMakeFiles/mock_turtle_test.dir/mock_turtle_test.cc.s"
	/Library/Developer/CommandLineTools/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /Users/kevinlutzer/Projects/labs/code/gmock-example/mock_turtle_test.cc -o CMakeFiles/mock_turtle_test.dir/mock_turtle_test.cc.s

# Object files for target mock_turtle_test
mock_turtle_test_OBJECTS = \
"CMakeFiles/mock_turtle_test.dir/mock_turtle_test.cc.o"

# External object files for target mock_turtle_test
mock_turtle_test_EXTERNAL_OBJECTS =

mock_turtle_test: CMakeFiles/mock_turtle_test.dir/mock_turtle_test.cc.o
mock_turtle_test: CMakeFiles/mock_turtle_test.dir/build.make
mock_turtle_test: lib/libgtest_main.a
mock_turtle_test: lib/libgtest.a
mock_turtle_test: CMakeFiles/mock_turtle_test.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green --bold --progress-dir=/Users/kevinlutzer/Projects/labs/code/gmock-example/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX executable mock_turtle_test"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/mock_turtle_test.dir/link.txt --verbose=$(VERBOSE)
	/opt/homebrew/Cellar/cmake/3.27.1/bin/cmake -D TEST_TARGET=mock_turtle_test -D TEST_EXECUTABLE=/Users/kevinlutzer/Projects/labs/code/gmock-example/build/mock_turtle_test -D TEST_EXECUTOR= -D TEST_WORKING_DIR=/Users/kevinlutzer/Projects/labs/code/gmock-example/build -D TEST_EXTRA_ARGS= -D TEST_PROPERTIES= -D TEST_PREFIX= -D TEST_SUFFIX= -D TEST_FILTER= -D NO_PRETTY_TYPES=FALSE -D NO_PRETTY_VALUES=FALSE -D TEST_LIST=mock_turtle_test_TESTS -D CTEST_FILE=/Users/kevinlutzer/Projects/labs/code/gmock-example/build/mock_turtle_test[1]_tests.cmake -D TEST_DISCOVERY_TIMEOUT=5 -D TEST_XML_OUTPUT_DIR= -P /opt/homebrew/Cellar/cmake/3.27.1/share/cmake/Modules/GoogleTestAddTests.cmake

# Rule to build all files generated by this target.
CMakeFiles/mock_turtle_test.dir/build: mock_turtle_test
.PHONY : CMakeFiles/mock_turtle_test.dir/build

CMakeFiles/mock_turtle_test.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/mock_turtle_test.dir/cmake_clean.cmake
.PHONY : CMakeFiles/mock_turtle_test.dir/clean

CMakeFiles/mock_turtle_test.dir/depend:
	cd /Users/kevinlutzer/Projects/labs/code/gmock-example/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /Users/kevinlutzer/Projects/labs/code/gmock-example /Users/kevinlutzer/Projects/labs/code/gmock-example /Users/kevinlutzer/Projects/labs/code/gmock-example/build /Users/kevinlutzer/Projects/labs/code/gmock-example/build /Users/kevinlutzer/Projects/labs/code/gmock-example/build/CMakeFiles/mock_turtle_test.dir/DependInfo.cmake "--color=$(COLOR)"
.PHONY : CMakeFiles/mock_turtle_test.dir/depend

