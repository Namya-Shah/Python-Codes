//#include <iostream>
//using namespace std;
//class B;
//class A
//{
//private:
//	int num1;
//public:
//	
//	A(int x)
//	{
//		num1 = x;
//	}
//	
//	friend int sub(A objA, B objB);
//};
//
//class B
//{
//private:
//	int num2;
//public:
//
//	B(int x)
//	{
//		num2 = x;
//	}
//	friend int sub(A objA, B objB);
//};
//
//int sub(A objA, B objB)
//{
//	
//	return objA.num1 - objB.num2;
//}
//
//int main()
//{
//	int ans;
//	A objA(5);
//	B objB(6);
//	ans = sub(objA, objB);
//	cout<<ans;
//}