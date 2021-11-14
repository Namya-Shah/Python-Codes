//#include<iostream>
//#include<string.h>
//using namespace std;
//int sem_count;
//
//class Semester
//{
//	public:
//		int sem_id;
//		char sem_name[25];
//		
//		void getData()
//	{
//		cout<<"Enter Semester ID";
//		cin>>sem_id;
//		
//		cout<<"Enter Semester Name";
//		cin>>sem_name;
//		
//	}
//	void print()
//	{
//		cout<<sem_id<<"\t"<<sem_name<<"\n";
//	}
//	
//	
//};
//
//class Student
//{
//	public:
//		int s_id;
//		char s_name[10];
//		Semester objSem;
//	void getData(Semester objs[5])
//	{
//		
//		cout<<"Enter Student ID:";
//		cin>>s_id;
//		cout<<"Enter Student Name";
//		cin>>s_name;
//		
//		for(int i=0;i< sem_count;i++)
//		{
//			objs[i].print();
//		}
//		cout<<"chose semester id from above id";
//		int sem_selected_id;
//		cin>>sem_selected_id;
//		for(int i=0;i< sem_count;i++)
//		{
//			if(objs[i].sem_id == sem_selected_id)
//			{
//				objSem = objs[i];
//			}
//		}
//		
//	}
//		
//	void printData()
//	{
//		cout<<s_id<<"\t"<<s_name;
//		objSem.print();
//	}
//	
//};
//
//int main()
//{
//	Semester objs[5];
//	cout<<"Enter  no of semester";
//	cin>>sem_count;
//	for(int i=0;i< sem_count;i++)
//	{
//		objs[i].getData();
//	}
//	
//	Student objSS;
//	objSS.getData(objs);
//	objSS.printData();
//}
//	