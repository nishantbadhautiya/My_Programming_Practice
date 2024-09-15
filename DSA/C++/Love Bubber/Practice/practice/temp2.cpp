#include<iostream>
using namespace std;
int factorial(int num){
    // base case 
    if(num == 0 || num == 1){
        return num;
    }
    num  = num * factorial(num - 1);
    return num;
}

int power(int num){
    // base case
    if(num == 0){
        return 1;
    }
    int num = 2 * power(num - 1);
    return num;
}


int main()
{
    int num;
    num = 5;
    int ans = factorial(num);
    cout << ans << endl;
    return 0;
}


