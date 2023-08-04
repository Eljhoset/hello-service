#include <iostream>
#include <string>
#include <hello-lib/greet.h>


int main(int argc, char* argv[]) {
    if (argc < 2) {
        std::cout << "Usage: " << argv[0] << " <name>" << std::endl;
        return 1;
    }

    std::string name = argv[1];
    std::string greeting = greet(name);
    std::cout << greeting << std::endl;

    return 0;
}