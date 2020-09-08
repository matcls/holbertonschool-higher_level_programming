#include "Python.h"

/**
 * print_python_list_info -  prints some basic info about Python lists.
 * @p: A PyObject list.
 * Return nothing
 */
void print_python_list_info(PyObject *p)
{
	Py_ssize_t elem = 0;
	PyObject *obj;
	const char *obj_type;
	PyListObject *list = NULL;

	list = (PyListObject *)p;

	printf("[*] Size of the Python List = %zu\n", PyList_Size(p));
	printf("[*] Allocated = %zu\n", list->allocated);
	while (elem < PyList_Size(p))
	{
		obj = PyList_GetItem(p, elem);
		obj_type = Py_TYPE(obj)->tp_name;
		printf("Element %zu: %s\n", elem, obj_type);
		elem++;
	}
}
