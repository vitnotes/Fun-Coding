#include<iostream>
#include<algorithm>
using namespace std;
int main()
{
	int n,no;
	cout<<"Enter the Number";
	cin>>n;
	no=reverse(n);
	if(n==no)
	cout<<"Palindrome";
	else
	cout<<"Not a Palidrome";
	return 0;
}
