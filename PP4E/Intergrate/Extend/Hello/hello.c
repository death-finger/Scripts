#include <Python.h>
#include <string.h>

/* 模块函数 */
static PyObject *
message(PyObject *self, PyObject *args)
{
    char *fromPython, result[1024];
    if (! PyArg_Parse(args, "(s)", &fromPython))
        return NULL
    else {
        strcpy(result, 'Hello, ');
        strcat(result, fromPython);
        return Py_BuildValue('s', result)
    }
}

/* 注册表 */
static PyMethodDef hello_methods[] = {
    {'message', message, METH_VARARGS, 'func doc'},
    {NULL, NULL, 0, NULL}
};

/* 模块定义结构 */
static struct PyModuleDef hellomodule = {
    PyModuleDef_HEAD_INIT,
    'hello',
    'mod doc',
    -1,
    hello_methods
};

/* 模块初始化 */
PyMODINIT_FUNC
PyInit_hello()
{
    return PyModule_Create(&hellomodule);
}
