#include <iostream>
#include <vector>

using namespace std;


//--------------------------------------------------------------
// Middle QuickSort
void 
middle_QuickSort(int v[][2], long left, long right){

    long i,j;
    int pivot,aux, aux2; 
    if (left<right)
    {
        i=left; j=right;
        pivot=v[(i+j)/2][0];
        do
        {
            while (v[i][0]<pivot) i++;
            while (v[j][0]>pivot) j--;
            if (i<=j)
            {
                aux=v[i][0]; aux2=v[i][1];v[i][0]=v[j][0];v[i][1]=v[j][1]; v[j][0]=aux; v[j][1]=aux2;
                i++; j--;
            }
       } while (i<=j);
       if (left<j)  middle_QuickSort(v,left,j);
       if (i<right) middle_QuickSort(v,i,right);
    }
}


vector<int> split(string s) {
	vector<int> vi;
	string num;
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
vector<int> rangeCalculator(int position, int range) {
	vector<int> v;
	if (position - range <= 0) {
		v.push_back(0);
	}	else {
		v.push_back(position-range);
	}
	v.push_back(position+range);
	return v;
}


int main() {
	int n;
	scanf("%d", &n);
	for(unsigned int x=0; x<n; x++) {
		int size, nAnt;
		scanf("%d %d", &size, &nAnt);
		string s;
		cin.ignore();
		getline(cin, s);
		vector<int> vi = split(s);
		int arrayRange[vi.size()/2][2];
		int j=0;
		for(unsigned int i=0; i<vi.size(); i+=2) {
			vector<int> InitAndEnd = rangeCalculator(vi[i], vi[i+1]);
			arrayRange[j][0] = InitAndEnd[0];
			arrayRange[j][1] = InitAndEnd[1];
			j++;
		}
		int max = j;
		int maxRecorrido = 0;
		
		sort(arrayRange, arrayRange);
		for(unsigned int i=0; i<max; i++)	{
			cout << arrayRange[i][0] << " " << arrayRange[i][1] << endl;
		}	 
		cout << endl;
	}
}
