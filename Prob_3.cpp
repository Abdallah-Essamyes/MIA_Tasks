#include <iostream>
using namespace std;


int main(){
    int n,highest;
    //cout << "Enter number of elements of array: ";
    cin >> n;
    int* arr = new int[n];;
    //cout << "Enter array elements: ";
    for (int i = 0 ; i < n; i++){
        cin >> arr[i];
    }

    highest = arr[0];
    for (int i = 1 ; i < n; i++) highest = max(highest, arr[i]);
    
    cout << highest;
}