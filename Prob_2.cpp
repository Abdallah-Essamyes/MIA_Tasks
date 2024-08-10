#include <iostream>
using namespace std;

int main(){
    int n,target;
    //cout << "Enter number of elements of array: ";
    cin >> n;
    int* arr = new int[n];;
    //cout << "Enter array elements: ";
    for (int i = 0 ; i < n; i++){
        cin >> arr[i];
    }
    //cout << "Enter target element: ";
    cin >> target;
    int index = -1;
    for (int i = 0 ; i < n; i++) {
        if ( target == arr[i])
         {
            index = i;
            break;
          }
    }
    cout << index;
}