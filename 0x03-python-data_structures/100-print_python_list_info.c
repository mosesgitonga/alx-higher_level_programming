#include <stdio.h>
#include <Python.h>

void print_python_list_info(PyObject *p)
{
  pysssize_t size, i;
  pyObject *item;

  size = pyList_Size(p);
    printf("[*] Size of the Python List = %ld\n", size);
    printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

    for (i = 0; i < size; i++) {
        item = PyList_GetItem(p, i);
        printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
    }
}
}
