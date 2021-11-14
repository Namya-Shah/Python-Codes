//#include <iostream>
//#include <string.h>
//using namespace std;
//int area_count;
//class Area
//{
//	public:
//		int a_id;
//		char a_name[10];
//		int a_pincode;
//		
//		void getData()
//		{
//			cout<<"Enter Area ID:";
//			cin>>a_id;
//			
//			cout<<"Enter Area Name:";
//			cin>>a_name;
//			
//			cout<<"Enter Area Pincode:";
//			cin>>a_pincode;
//		};
//		
//		void printData()
//		{
//			cout<<a_id<<"\t"<<a_name<<"\t"<<a_pincode<<"\n";
//		}
//};
//
//class Student
//{
//	public:
//		int s_id;
//		char s_name[10];
//		char s_email[20];
//		Area objA;
//		
//		void getData(Area obja[10])
//		{
//			cout<<"Enter Student ID:";
//			cin>>s_id;
//			
//			cout<<"Enter Student Name:";
//			cin>>s_name;
//			
//			cout<<"Enter Student Email:";
//			cin>>s_email;
//			
//			int i;
//			for(i=0; i<area_count; i++)
//			{
//				obja[i].printData();
//			}
//			cout<<"Enter Area Id:";
//			int area_selected_id;
//			cin>>area_selected_id;
//			
//			for(i=0; i<area_count; i++)
//			{
//				if(obja[i].a_id == area_selected_id)
//				{
//					objA = obja[i];
//				}
//			}
//		}
//		
//		void print()
//		{
//			cout<<"\n"<<s_id<<"\t"<<s_name<<"\t"<<s_email;
//			objA.printData();
//		}
//};
//
//int main()
//{
//	
//	
//	cout<<"Enter No. of Areas:";
//	cin>>area_count;
//	Area objAreas[area_count];
//	for(int i=0; i<area_count; i++)
//	{
//		objAreas[i].getData();
//	}
//	
//	int n;
//	int j;
//	cout<<"Enter no. of Students:";
//	cin>>n;
//	Student objs[n];
//	for(j=0; j<n; j++)
//	{
//	objs[j].getData(objAreas);
//	
//	}
//	
//	for(j=0; j<n; j++)
//	{
//		objs[j].print();
//	
//	}
//	
//	
//	
//	return 0;
//}	