#include <iostream>
#include <math.h>
#include <algorithm>
#include <vector>
#include <stdlib.h>

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

int gcd(int a, int b) {
	if(a<1 || b<1) {
		exit(1);
	
	}
	int remainder = 0;
	do {
		remainder = a%b;
		a = b;
		b = remainder;
	
	}while (b != 0);
	return a;

}

int lcm(int a, int b) {
	if(a==0 || b==0) {
		return 0;
	
	} else {
		return (a*b)/gcd(a,b);
	
	}

}

int main() {
	while(true ) {
		int n;
		scanf("%d", &n);
		if(n==0) break;
		string s;
		cin.ignore();
		getline(cin , s);
		vector<int> vi = split(s);
		sort(vi.begin(), vi.end());
		int m = 0;
		bool firstEntrance = false;
		for(unsigned int i=0; i<vi.size()-1; i++) {
			if(!firstEntrance) {
				m = vi[0];
				firstEntrance = !firstEntrance;				
			
			}
			m = lcm(m, vi[i+1]);
		
		}
		cout << m << endl;
	
	}

}
