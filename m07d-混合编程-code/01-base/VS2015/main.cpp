/*
author: juzicode
address: www.juzicode.com
���ں�: ����code/juzicode
date: 2020.8.15
*/

 
#include <python.h>//����python.h

 
//C�������壬������C++��ʽ
int add(int a,int b)
{
	return a + b;
}
 
PyObject* wrap_add_i(PyObject* self, PyObject* args)
{
	//������Ρ�����ֵ����
	int a,b, result;

	//���������������Ľ����ֵ������a��b
	if (!PyArg_ParseTuple(args, "ii", &a,&b))//��2���ַ�����������C���Ժ�����������ͣ���1��i��ʾ����װ������1�����Ϊint�ͣ���������
		return NULL;

	//���ñ���װ����
	result = add(a,b);

	//���ؽ��
	return Py_BuildValue("i", result);//��1���ַ��������������ر��������ͣ�i��ʾint��
} 

static PyMethodDef  MethodsDef[] =
{
	//������������, ��װ����������ģʽ������˵��
	{ "add_i",  wrap_add_i,  METH_VARARGS, "Caculate two int"},
 
	{ NULL, NULL, NULL, NULL }
};

static PyModuleDef ModuleDef = {
	PyModuleDef_HEAD_INIT,
	"c2pyd",   //������ģ������
	NULL,      //ģ���ĵ�������ΪNULL
	-1,       //һ��Ϊ-1
	MethodsDef //PyMethodDef���ͣ���������
};
 
// define PyMODINIT_FUNC extern "C" __declspec(dllexport) PyObject*
PyMODINIT_FUNC
PyInit_c2pyd(void)
{
	return PyModule_Create(&ModuleDef);
}




 