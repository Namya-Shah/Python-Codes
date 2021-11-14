#include <iostream>
#include <string.h>
using namespace std;

class HumanBeing
{
public:
	int nose = 1;
	int legs = 2;
	int hands = 2;
	
};

class Male : public HumanBeing
{
public:
	char hair[5];
	void display()
	{
		cout<<nose;
		cout<<hands;
		cout<<legs;
		strcpy(hair,"short");
		cout<<hair;
	}
	
};

class Female : public HumanBeing
{
public:
	char hair[5];
	void display()
	{
		cout<<nose;
		cout<<hands;
		cout<<legs;
		strcpy(hair, "long");
		cout<<hair;
	}
	
	
};

int main()
{
	Male m;
	m.display();
	
	Female m2;
	m2.display();
	return 0;
}