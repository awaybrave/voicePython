#include <Python.h>
static PyObject *is_palindrome(PyObject *self, PyObject *args){
    int i, n;
    const char *text;
    int result;
    /* "s" means a single string: */
    if(!PyArg_ParseTuple(args, "s",  &text)){
        return NULL;
    }
    /* The old code, more or less: */
    n = strlen(text);
    result = 1;
    for(i = 0; i <= n/2; i++){
        if(text[i] != text[n-i-1]){
            result = 0;
            break;
        }
    }
    /*"i" means a single integer:*/
    return Py_BuildValue("i", result);
}

static PyObject *printStr(PyObject *self, PyObject *args){ 
    const char *text;
    if(!PyArg_ParseTuple(args, "s",  &text)){
        return NULL;
    }
    return Py_BuildValue("s", text);
}

/*A listing of our methods/functions: */
static PyMethodDef PalindromeMethods[] = {
    /*name, function ,argument type, docstring*/
    {"is_palindrome", is_palindrome, METH_VARARGS, "Detect palindrome"},
    {"printStr", printStr, METH_VARARGS, "print string"},
    /*An end-of-listing sentinel:*/ 
    {NULL, NULL, 0, NULL}
};

/*An initialization function for the module(the name is
significant)*/
PyMODINIT_FUNC initpalindrome2(void){ //init<module_name>
    //first argument: module name
    (void)Py_InitModule("palindrome2", PalindromeMethods); 
}
