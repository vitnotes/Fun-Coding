#include<iostream>
#include<string.h>
#include<algorithm>
using namespace std;
int main()
{
	int n;
	cout<<"Enter the Number of names you want: ";
	cin>>n;
	string name[n];
	string dummy;
	cout<<"****Don't Leave Space****";
	for(int i=0;i<n;i++)
	{
	cout<<"\nEnter the Name "<<i+1<<':';
	cin>>name[i];
	}
	for(int x=0;x<n;x++)
	{
	dummy = name[x];
	cout<<dummy.substr(0,3);
	reverse(dummy.begin(),dummy.end());/*<alogrithm>*/
	cout<<"\n\nThe Name "<<x+1<<':'<<name[x]<<":::"<<dummy;
	}
	return 0;
}
