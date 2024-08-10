#include <iostream>
using namespace std;
//it says it cant find getline but code works just fine, maybe a g++ and vscode inconsistency
int main(){
    string name;
    getline(cin,name);
    cout << "Hello, " << name << "!"<< endl;
}