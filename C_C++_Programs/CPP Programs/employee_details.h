//#include <iostream>
//using namespace std;
//namespace Details
//{
//	
//	class Employee
//{
//public:
//	int employee_id;
//	char employee_name[10];
//	virtual void getData() = 0;
//	
//	
//};
//
//
//
//class Tester : public Employee
//{
//public:
//	int salary;
//	
//	void getData()
//	{
//		cout<<"Enter the id:";
//		cin>>employee_id;
//		
//		cout<<"Enter the name:";
//		cin>>employee_name;
//		
//		cout<<"Enter the Salary:";
//		cin>>salary;
//	}
//	
//	void print()
//	{
//		cout<<employee_id<<"\t"<<employee_name<<"\t"<<salary<<"\n";
//	}
//	
//	void operator++()
//	{
//		int n;
//		cout<<"Enter the value of bonus:";
//		cin>>n;
//		float bonus;
//		bonus = n*salary/100;
//		cout<<"b:" <<bonus<<"\n";
//		salary = salary + bonus;
//		cout<<"a: " <<salary;
//	}
//};
//
//}
