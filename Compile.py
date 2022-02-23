import py_compile
print("Just a reminder, put this file code in the same directory as the .py code you want to compile.")
File = input("Put the exact name of the file in this input: ")
py_compile.compile(str(File))
