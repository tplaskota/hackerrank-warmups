#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main(){
    int n;
    cin >> n;
    vector< vector<int> > a(n,vector<int>(n));
    for(int a_i = 0;a_i < n;a_i++){
       for(int a_j = 0;a_j < n;a_j++){
          cin >> a[a_i][a_j];
       }
    }
    int main=0, sec=0;
    for(int i=0;i<n;++i)
        {
        main+=a[i][i];
        sec+=a[i][n-i-1];
    }
    int diff = main - sec > 0 ? main-sec : sec-main;
    cout<<diff;
    return 0;
}

