#include <Python.h>

/**
 * print_python_string - Prints information about a Python string object
 * @p: Pointer to a Python object (assumed to be a string)
 */
void print_python_string(PyObject *p) {
    if (PyUnicode_Check(p)) {
        Py_UCS1 *value;
        Py_ssize_t length;
        Py_ssize_t i;

        printf("[.] string object info\n");
        printf("  type: %s\n", PyUnicode_IS_COMPACT_ASCII(p) ? "compact ascii" : "compact unicode object");
        length = PyUnicode_GET_LENGTH(p);
        printf("  length: %ld\n", length);

        if (PyUnicode_IS_COMPACT_ASCII(p)) {
            value = PyUnicode_1BYTE_DATA(p);
            printf("  value: ");
            for (i = 0; i < length; i++) {
                printf("%c", value[i]);
            }
        } else {
            value = PyUnicode_DATA(p);
            printf("  value: ");
            for (i = 0; i < length; i++) {
                printf("\\u%04x", value[i]);
            }
        }

        printf("\n");
    } else {
        printf("[.] string object info\n");
        printf("  [ERROR] Invalid String Object\n");
    }
}

