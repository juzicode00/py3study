/*
author: juzicode
address: www.juzicode.com
���ں�: ����code/juzicode
date: 2020.8.15
*/

 
#include <python.h>//����python.h

 
#if 1
//C�������壬������C++��ʽ
int add(int a,int b)
{
	return a + b;
}

float add(float a, float b)
{
	return a + b;
}
float sub(float a, float b)
{
	return a - b;
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

PyObject* wrap_add_f(PyObject* self, PyObject* args)
{
	float a, b, result;
	if (!PyArg_ParseTuple(args, "ff", &a, &b))//����Ϊ2��float����
		return NULL;
	result = add(a, b);
	return Py_BuildValue("f", result);//����float�ͽ��
}

PyObject* wrap_add_sub_f(PyObject* self, PyObject* args)
{
	float a, b, result, result2;
	if (!PyArg_ParseTuple(args, "ff", &a, &b))//����Ϊ2��float����
		return NULL;
	result = add(a, b);
	result2 = sub(a, b);
	return Py_BuildValue("ff", result, result2);//����float�ͽ���ĺ��Լ���ֵ
}

PyObject* wrap_ret_nothing(PyObject* self, PyObject* args)
{
	float a, b;
	if (!PyArg_ParseTuple(args, "ff", &a, &b))//����Ϊ2��float����
		return NULL;
	//do some thing
	//TO DO
	return Py_BuildValue("");//����float�ͽ���ĺ��Լ���ֵ
}




PyObject* wrap_trans_noargs(PyObject* self, PyObject* args)
{
	printf("%s","wrap_trans_noargs: nothing\n");
	
	return Py_BuildValue("");//����float�ͽ���ĺ��Լ���ֵ
}


PyObject* wrap_trans_noargs2(PyObject* self, PyObject* args)
{
	printf("%s", "wrap_trans_noargs2: nothing\n");

	return Py_BuildValue("");//����float�ͽ���ĺ��Լ���ֵ
}

PyObject* wrap_trans_kwargs(PyObject* self, PyObject* args,PyObject *kw)
{
	char* kwlist[] = { "a","b","c","d", NULL };//���һ��Ԫ�ر���ΪNULL��NULLǰ���Ԫ�����ƾ���python���ô���Ĳ�������
	float a, b, c,d;
	if (!PyArg_ParseTupleAndKeywords( args, kw, "ffff", kwlist,  &a, &b, &c, &d))
		return NULL;
	printf("wrap_trans_kwargs: a=%f, b=%f, c=%f, d=%f\n", a,b,c,d);
	float result = add(a, b)+ add(c, d);

	return Py_BuildValue("f",result);//����float�ͽ���ĺ��Լ���ֵ
}

static PyMethodDef  MethodsDef[] =
{
	//������������, ��װ����������ģʽ������˵��
	{ "add_i",  wrap_add_i,  METH_VARARGS, "Caculate two int"},
	{ "add_f",  wrap_add_f,  METH_VARARGS, "Caculate two float" },
	{ "add_sub_f",  wrap_add_sub_f,  METH_VARARGS, "Caculate two float" },
	{ "ret_nothing",  wrap_ret_nothing,  METH_VARARGS, "ret nothing" },
	{ "trans_noargs",  wrap_trans_noargs,  METH_NOARGS, "transfer  noargs" },
	{ "trans_kwargs",  (PyCFunction)wrap_trans_kwargs, METH_VARARGS| METH_KEYWORDS, "transfer kwargs" },

	{ NULL, NULL, NULL, NULL }
};

//{ "trans_noargs2", wrap_trans_noargs2, METH_O, "transfer  noargs" },

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

#endif


 