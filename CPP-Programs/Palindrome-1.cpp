#include<iostream>
#include<cstring>
using namespace std;
int main()
{
	char c[20];
	int i,j,flag=1;
	cout<<"Enter the word to be checked for palindrome:-";
	cin>>c;
	for(i=0,j=strlen(c)-1;i<strlen(c)/2;i++,j--)
	{
		if(c[j]!=c[i])
		flag=0;
	}
	if(flag==1)
		cout<<"\nIt is Palindrome";
	else
		cout<<"\nIt is not Palindrome";
	
	return 0;
}
