#include <stdlib.h>
#include <iostream>
#include <string>

int main() {
	std::string s;
	while(std::getline(std::cin, s)) {
		long l = stol(s);
		if(l%9==0 && l != 0) {
			std::cout << l << std::endl;
		}
	}
}

