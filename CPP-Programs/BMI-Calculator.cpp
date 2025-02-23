#include<iostream>
#include<math.h>
using namespace std;
int main()
{
	int c; float height, weight, bmi;
	cout<<"\t\t\nMENU\n1.Height and Weight in Metric System.\n2.Height and Weight in British System."<<endl;
	cin>>c;
	cout<<"Enter Your Height and Weight: ";
	cin>>height>>weight;
	switch(c)
	{
	case 1:
		bmi=(weight)/pow(height,2);
		break;
	case 2:
		bmi=(weight)*703/pow(height,2);
	default:
		cout<<"Invalid Choice";
	}
	cout<<"Your BMI Value is :"<<bmi<<endl;
	if(bmi<18.5)
	cout<<"You're Underweight";
	else if(bmi>=18.5 && bmi<24.9)
	cout<<"You're Normal Weight";
	else if(bmi>=25 && bmi<29.9)
	cout<<"You're Overweight";
	else if(bmi>=30)
	cout<<"You're Obese.";
return 0;
	
}
