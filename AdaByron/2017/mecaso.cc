#include <iostream>
#include <stdlib.h>
#include <vector>
#include <string>

using namespace std;

std::vector<int> split(string s) {
	std::vector<int> vi;
	std::string num;
	for(unsigned int i=0; i<s.size(); i++) {
		if(s[i] == ' ')	{
			vi.push_back(stoi(num));
			num.clear();
		} else {
			num += s[i];
		}
	}

	vi.push_back(stoi(num));

	return vi;
}

int main() {
	std::string s;
	while(true) {
		int n;
		scanf("%d", &n);
		if(n==0) break;
		std::string s;
		cin.ignore();
		std::getline(std::cin, s);
		std::vector<int> vi = split(s);
		int total = 0;
		for(int v : vi) {
			total +=v;
		}
		cout << total << endl;
	}
}
