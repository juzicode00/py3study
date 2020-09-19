/*
author: juzicode
address: www.juzicode.com
公众号: 桔子code/juzicode
date: 2020.8.15
*/

 
#include <python.h>//包含python.h

 
#if 1
//C函数定义，可以是C++格式
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
	//定义入参、返回值变量
	int a,b, result;

	//解析参数，解析的结果赋值到变量a和b
	if (!PyArg_ParseTuple(args, "ii", &a,&b))//第2个字符串参数声明C语言函数的入参类型，第1个i表示被封装函数第1个入参为int型，依次类推
		return NULL;

	//调用被封装函数
	result = add(a,b);

	//返回结果
	return Py_BuildValue("i", result);//第1个字符串参数声明返回变量的类型，i表示int型
} 

PyObject* wrap_add_f(PyObject* self, PyObject* args)
{
	float a, b, result;
	if (!PyArg_ParseTuple(args, "ff", &a, &b))//解析为2个float类型
		return NULL;
	result = add(a, b);
	return Py_BuildValue("f", result);//返回float型结果
}

PyObject* wrap_add_sub_f(PyObject* self, PyObject* args)
{
	float a, b, result, result2;
	if (!PyArg_ParseTuple(args, "ff", &a, &b))//解析为2个float类型
		return NULL;
	result = add(a, b);
	result2 = sub(a, b);
	return Py_BuildValue("ff", result, result2);//返回float型结果的和以及差值
}

PyObject* wrap_ret_nothing(PyObject* self, PyObject* args)
{
	float a, b;
	if (!PyArg_ParseTuple(args, "ff", &a, &b))//解析为2个float类型
		return NULL;
	//do some thing
	//TO DO
	return Py_BuildValue("");//返回float型结果的和以及差值
}




PyObject* wrap_trans_noargs(PyObject* self, PyObject* args)
{
	printf("%s","wrap_trans_noargs: nothing\n");
	
	return Py_BuildValue("");//返回float型结果的和以及差值
}


PyObject* wrap_trans_noargs2(PyObject* self, PyObject* args)
{
	printf("%s", "wrap_trans_noargs2: nothing\n");

	return Py_BuildValue("");//返回float型结果的和以及差值
}

PyObject* wrap_trans_kwargs(PyObject* self, PyObject* args,PyObject *kw)
{
	char* kwlist[] = { "a","b","c","d", NULL };//最后一个元素必须为NULL，NULL前面的元素名称就是python调用传入的参数名称
	float a, b, c,d;
	if (!PyArg_ParseTupleAndKeywords( args, kw, "ffff", kwlist,  &a, &b, &c, &d))
		return NULL;
	printf("wrap_trans_kwargs: a=%f, b=%f, c=%f, d=%f\n", a,b,c,d);
	float result = add(a, b)+ add(c, d);

	return Py_BuildValue("f",result);//返回float型结果的和以及差值
}

static PyMethodDef  MethodsDef[] =
{
	//导出函数名称, 封装函数，参数模式，函数说明
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
	"c2pyd",   //导出的模块名称
	NULL,      //模块文档，可以为NULL
	-1,       //一般为-1
	MethodsDef //PyMethodDef类型，导出方法
};
 
// define PyMODINIT_FUNC extern "C" __declspec(dllexport) PyObject*
PyMODINIT_FUNC
PyInit_c2pyd(void)
{
	return PyModule_Create(&ModuleDef);
}

#endif


 