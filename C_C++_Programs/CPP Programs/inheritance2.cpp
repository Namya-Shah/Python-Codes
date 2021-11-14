//#include <iostream>
//#include <string.h>
//using namespace std;
//
//class Student
//{
//	public:
//	char Name[10];
//	int m1;
//	int m2;
//	
//	void displayData()
//	{
//	cout<<"Enter Name of Student:";
//	cin>>Name;
//	
//	cout<<"Enter Marks1 of Student:";
//	cin>>m1;
//	
//	cout<<"Enter Marks2 of Student:";
//	cin>>m2;
//	}
//	
//	
//};
//
//class Sports
//{
//	public:
//	int sportsmarks;
//	
//	void disp()
//	{
//		cout<<"Enter Sports Marks of Student:";
//		cin>>sportsmarks;
//	}
//	
//};
//
//class Result : public Student, public Sports
//{
//public:
//	int Total;
//	int Avg;
//		
//	void print()
//	{
//	Total = m1 + m2 + sportsmarks;
//	
//	Avg = Total/3;
//	
//	cout<<"\n"<<Total<<"\n";
//	
//	cout<<Avg<<"\n";
//	
//	}
//	
//	
//};
//
//int main()
//{
//	Result objr;
//	objr.displayData();
//	objr.disp();
//	objr.print();
//	
//	return 0;
//}