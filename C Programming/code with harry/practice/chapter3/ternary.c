#include<stdio.h>

int main()
{
     int age;
     printf("enter your age: ");
     scanf("%d",&age);
     (age>18)? printf("you can vote") :printf("you cannot vote");
     return 0;
}