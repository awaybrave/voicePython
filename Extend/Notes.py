#Compiling C into Python library
#here is a c function that detects whether a string is a palindrome 

#C program - checkPalindrome.c:
#include<string.h> 
int is_palindrome(char *text){
	int i, n = strlen(text);
	for(i = 0; i <= n/2; i++){
		if(text[i] != text[n-i-1])	return 0; 
	}
	return 1;
}

#Here we define a function called is_palindrome, then we should define the
#corresponding interface file checkPalindrome.i
%module palindrome #define module name
%{
    #include <string.h> #list the included headers
%}
extern int is_palindrome(char *text); #export the function

#Use swig to add python features into C program.
swig -python checkPalindrome.i (use -c++ to deal with c++ library.)
#And it produces checkPalindrome_wrap.c

#Compile checkPalindrome_wrap.c
$ gcc -dynamic -I$PYTHON_HOME/include/python2.7 -c checkPalindrome.c
$ gcc -dynamic -I$PYTHON_HOME/include/python2.7 -c checkPalindrome_wrap.c
$ gcc -dynamiclib palindrome_wrap.o palindrome.o -o _palindrome.so -Wl, -undefined dynamic_lookup

# in mac $PYTHON_HOME is /System/Library/Frameworks/Python.framework/Versions
#/2.7/
#Python.h is under the include/python2.7

#turn to the python interpreter
>>import _palindrome as pl
>>pl.is_palindrome('baccab')

#Notes: 
#1.remember to export the module name in the .i interface file.
#2.export the function you need(no need to export all the functions)
#3.set the correct python home path so that the library is compiled 
#successfully
#4.use dir built-in method to have a deep look into the python module.
#5.installing swig library is so easy and it could be completed in two
#step: ./configure according to the current operating system and 
#make to compile the files.

#Testing:
#testPalindrome.txt contains a large string. TestPython.py waits for the 
#system stdin read and it check whether the input is a palindrome. So does
#testCExtension.py except that it uses the C extension.

# time cat testPalindrome.txt | python testPython.py
# time cat testPalindrome.txt | python testCExtension.py 

# It shows that the larger the input is, the better testCExtension does!
# Remember to ingnores the last character of stdin because it is EFO.

#Besides using swig, we can do it by pure C program.
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
#compiling it by:
gcc -I$PYTHON_HOME -I$PYTHON_HOME/include/python2.7 -shared palindrome2.c -o palindrome2.so -L /System/Library/Frameworks/Python.framework/Versions/2.7/lib/ -l python2.7
#add shared option to tell the complier not to find main function
