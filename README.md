# PyCompiler
Compile your .py code to .pyc for more speed! :D

Explanation: When you run .py code the Python Interpreter translate your 
code to bytecode as a temporary archive that the Python Virtual Machine can Execute in your actual system 
and that process can be slow if you know how python works. 
The thing that PyCompiler do is it grab the temporary .pyc and make it persistent (as far as i know) and you can
execute the bytcode to run a little bit faster, that boost sometimes the python programmers need :)

So i grabbed the py_compile library and made a (Literally) 4-lines python 
code that can grab the name of the file you want to compile.

The result will be in a directory called "__pycache__".

Remember to put the Code in the same folder as the file you want to compile.

Funfact: i did Compile the PyCompiler code in itself, i did just ran the .py and named the compiler and it just worked.
