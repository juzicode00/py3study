/*
author: juzicode
address : www.juzicode.com
���ں� : ����code / juzicode
date : 2020.8.1
*/
#include "stdio.h"
#include <iostream>

#ifdef __cplusplus
extern "C" {
#endif 

//��������int
__declspec(dllexport) int addi(int x, int y) 
{
	return x + y;
}

//��������double
__declspec(dllexport) double addd(double x, double y)
{
	return x + y;
}

//��������float
__declspec(dllexport) float addf(float x, float y)
{
	return x + y;
}

//��������long long
__declspec(dllexport) long long addll(long long x, long long y)
{
	return x + y;
}

//��������char
__declspec(dllexport) char trans_c(char y)
{
	return y ;
}

//��������wchar_t
__declspec(dllexport) wchar_t trans_wc(wchar_t y)
{
	return y;
}

//�������� charָ��
__declspec(dllexport) char* trans_cp(char* y)
{
	return y;
}

//�������� wchar_tָ��
__declspec(dllexport) wchar_t* trans_wcp(wchar_t* y)
{
	return y;
}


//  int����
__declspec(dllexport) long long trans_array_i(int x[10])
{
	long long sum = 0;
	printf("in c:");
	for (int i = 0; i < 10; i++)
	{
		printf("%d ", x[i]);
		sum += x[i];
	}
	printf("\n");
	return sum;
}


//char����
__declspec(dllexport) char trans_array_c(char x[20])
{
	for (int i = 0; i < 20; i++)
	{
		printf("%c ", x[i]);
	}
	printf("\n");
	return x[0];
}


//�ṹ��
typedef struct __ts_fruit {
	int id;
	char name[10];
	float weight;
}TS_FRUIT, *PTS_FRUIT;

__declspec(dllexport) int trans_struct(TS_FRUIT fruit)
{
	printf("id=%d \n", fruit.id);
	printf("name=%s \n", fruit.name);
	printf("weight=%f \n", fruit.weight);
	printf("\n");
	return 0;
}

//�ṹ��ָ��
__declspec(dllexport) int modify_struct_p(PTS_FRUIT fruit)
{
	fruit->id = 202008;
	memset(fruit->name, 0, 10);
	strcpy(fruit->name, "juzicode");
	fruit->weight = 11.5;
	return 0;
}



//intָ��
__declspec(dllexport) int modify_i(int* x)
{
	printf("modify_i: before modify, x=%d \n", *x);
	*x = *x + 10;
	printf("modify_i: after  modify, x=%d \n", *x);
	return 0;
}

//int���飬ָ������
__declspec(dllexport) int modify_i_array(int  x[],int len)
{
	printf("modify_i: before modify, x[0]=%d \n", *x);
	for (int i=0; i < len; i++) {
		*(x + i) = 1000+ *(x + i);
	}
	printf("modify_i: after  modify, x[0]=%d \n", *x);
	return 0;
}

//charָ��
__declspec(dllexport) int modify_c(char* x)
{
	printf("modify_c: before modify, x=%c \n", *x);
	*x = *x + 10;
	printf("modify_c: after  modify, x=%c \n", *x);
	return 0;
}

//charָ��
__declspec(dllexport) int modify_c2(char* x)
{
	printf("modify_c2: before modify, x=%s\n", x);
	strcpy(x, "juzicode.com");
	printf("modify_c2: after  modify, x=%s \n", x);
	return 0;
}

//char���飬ָ������
__declspec(dllexport) int modify_c_array(char x[],int length)
{
	printf("modify_c_array: before modify, x=%s\n", x);
	char *temp = new char[length];
	memcpy(temp,x, length);
	memset(x, 0, length);
	if (length < 50) {
		return -1;
	}
	strcpy(x, "juzicode.com ");
	strcat(x, temp);
	delete temp;
	printf("modify_c_array: after  modify, x=%s \n", x);
	return 0;
}



//void* ָ��
__declspec(dllexport) int void_pointer(void* x)
{
	char* cp = (char*)(x);
	printf("void_pointer: thransfer to char, x=%c \n", *cp);

	int* ip = (int*)(x);
	printf("void_pointer: thransfer to int, x=%d \n", *ip);

	return 0;
}




#ifdef __cplusplus
}
#endif            









