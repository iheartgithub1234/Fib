#include <iostream>
#include "math_util.hpp"

int main(int argc, char *argv[]) {
     try {
          int num = std::stoi(argv[1]);
          num = fibonacci(num);

          std::cout << num << std::endl;
     } catch(...) {
          std::cout << "Error" << std::endl;
     }

     return 0;
}