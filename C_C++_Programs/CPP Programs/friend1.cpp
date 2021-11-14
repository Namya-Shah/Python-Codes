//#include<iostream>
//using namespace std;
//
//class Teacher
//{
//private:
//	
//	int t_id;
//	char t_name[10];
//	int t_mobile;
//	
//public:
//	
//	void getData()
//	{
//		cout<<"Enter Teacher ID:";
//		cin>>t_id;
//		cout<<"Enter Teacher Name:";
//		cin>>t_name;
//		cout<<"Enter Teacher Mobile:";
//		cin>>t_mobile;
//	}
//	
//	
//	friend class Student;
//};
//
//class Student
//{
//private:
//	
//	int s_id;
//	char s_name[10];
//	int s_mobile;
//	
//public:
//	
//	void getData()
//	{
//		cout<<"Enter Student ID:";
//		cin>>s_id;
//		
//		cout<<"Enter Student Name:";
//		cin>>s_name;
//		
//		cout<<"Enter Student Mobile:";
//		cin>>s_mobile;
//	}
//	
//	void show(Teacher objT);
//};
//void Student :: show(Teacher objT)
//{
//	cout<<objT.t_id<<"\t"<<objT.t_name<<"\t"<<objT.t_mobile<<"\n";
//	cout<<s_id<<"\t"<<s_name<<"\t"<<s_mobile<<"\n";
//}
//
//int main()
//{
//	Teacher objT;
//	objT.getData();
//	
//	Student objS;
//	objS.getData();
//	objS.show(objT);
//}