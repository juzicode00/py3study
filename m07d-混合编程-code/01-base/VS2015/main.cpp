/*
author: juzicode
address: www.juzicode.com
公众号: 桔子code/juzicode
date: 2020.8.15
*/

 
#include <python.h>//包含python.h

 
//C函数定义，可以是C++格式
int add(int a,int b)
{
	return a + b;
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

static PyMethodDef  MethodsDef[] =
{
	//导出函数名称, 封装函数，参数模式，函数说明
	{ "add_i",  wrap_add_i,  METH_VARARGS, "Caculate two int"},
 
	{ NULL, NULL, NULL, NULL }
};

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




 