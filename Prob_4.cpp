#include <iostream>
using namespace std;

void fill_array( int **arr, int r,int c){
    for (int i = 0 ; i < r; i++){
         for (int j = 0; j < c; j++) cin >> arr[i][j];
    }
}

int main(){
    int r,c,justice_score = 0,villains_score = 0;
    //cout << "Enter number of elements of rows and columns: ";
    cin >> r >> c;
    int **justice_arr = new int*[r];
    for (int i = 0; i < r; ++i) justice_arr[i] = new int[c]; 
    int **villains_arr = new int*[r];
    for (int i = 0; i < r; ++i) villains_arr[i] = new int[c]; 
    //cout << "Enter justice league row elements: " << endl ;
    fill_array(justice_arr,r,c);
   // cout << "Enter villains row elements: " << endl ;
    fill_array(villains_arr,r,c);
    for (int i = 0 ; i < r; i++){
         for (int j = 0; j < c; j++) {
            if ( justice_arr[i][j] > villains_arr[i][j]) justice_score +=1;
            else if ( justice_arr[i][j] < villains_arr[i][j]) villains_score += 1;
    }
    }
    if ( justice_score > villains_score) cout << "Justice League" << endl;
    else if ( justice_score < villains_score) cout << "Villains" << endl;
    else cout << "Tie" << endl;
    
}