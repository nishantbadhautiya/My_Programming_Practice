#include<iostream>
using namespace std;

int main()
{
    int num;
    cout<<"Enter the Number ";
    cin>>num;
    int i = 1;
    while (i <= num)
    {
        int j = 1;
        while (j <= num )
        {
            cout<<i<<" ";
            j++;
        }
        cout<<endl;
        i++;
    }
    return 0;
}