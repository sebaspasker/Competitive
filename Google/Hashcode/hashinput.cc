
#include <iostream>
#include <string>
#include <iostream>
#include <algorithm>
#include <stdlib.h>
#include <string.h>
#include <vector>

using namespace std;

// estructuras to gauapas
struct Book
{
    long scr;
    long id;
};

struct Library
{
    int id;
    double totalD;
    double total_avg;
    double total_score;
    int nb;
    int signup;
    int books_PD;
    vector<Book> books;
};

// peaso split
vector<int> split(string s){
    vector<int> vi;
    string num;
    for (unsigned int i = 0; i < s.size(); i++){
        if (s[i] == ' '){
            vi.push_back(stoi(num));
            num.clear();
        }
        else{
            num += s[i];
        }
    }
    vi.push_back(stoi(num));
    return vi;
}

// debug cout
void coutvector(vector<int> stringV){
    for (int i = 0; i < stringV.size(); i++){
        cout << stringV[i] << " ";
    }
    cout << endl;
}



// main to wapo
int main(){
    string input;
    vector<Library> librerias;

    int numLibros = 0, numLibrerias = 0, diasTotales = 0;

    // leemos primera linea
    getline(cin, input);
    vector<int> stringV = split(input);
    numLibros = stringV[0];
    numLibrerias = stringV[1];
    diasTotales = stringV[2];

    // leemos segunda linea
    getline(cin, input);
    vector<int> scores = split(input);

    // LEEMOS LAS DEMÁS LINEAS DE DOS EN DOS
    while (getline(cin, input)) {
        Library lib;
        // libreria
        stringV = split(input);
        lib.nb = stringV[0];
        lib.signup = stringV[1];
        lib.books_PD = stringV[2];
        //libros
        getline(cin, input);
        stringV = split(input);
				int total_score = 0;
        // metemos cada libro en su libreria
        for (int i = 0; i < stringV.size(); i++){
            Book b;
            b.id = stringV[i];
            b.scr = scores[stringV[i]];
            lib.books.push_back(b);
            total_score += b.scr;
        }
				lib.totalD = (lib.books.size()/lib.books_PD) + lib.signup;
				lib.total_avg = total_score/lib.totalD;
				lib.total_score = lib.total_avg/diasTotales;
        librerias.push_back(lib);
    }

    for (int i = 0; i < librerias.size(); i++){
        vector<Book> newVectorBooks;
        int size = librerias[i].books.size();
        for (int j = 0; j < size; j++){
            int bB = 0;
            for (int k = 0; k < librerias[i].books.size(); k++){
                if (librerias[i].books[bB].scr < librerias[i].books[k].scr){
                    bB = k;
                }
                newVectorBooks.push_back(librerias[i].books[bB]);
                librerias[i].books.erase(librerias[i].books.begin(), librerias[i].books.begin() + bB);
            }
        }
        librerias[i].books = newVectorBooks;
    }
		
		vector<int> repetitionId;
		vector<Library> sortedL;


		
}
}
