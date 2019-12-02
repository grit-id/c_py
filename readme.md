# C to Python Tutorial
### This repository provides how to compile C source code as dynamic library and call it from Python.

The included example provides division and average operation both written in C and Python to compare the execution speed.

## System Requirements

Linux 64 bit

GNU C Compiler (gcc). *(Of course you can use other compiler).*

Git

## How To

Clone the repo
```sh
git clone https://github.com/grit-id/c_py
cd c_py
chmod +x make.sh
./make.sh
python3 work.py
```
## Output Example
```
[aviezab@tufgaming c_py]$ python work.py 
/run/media/aviezab/new_windows/Work/WorkCode/c/c_py/libsample.so
(5, 0)
C Divide Time (ms) 0.021039999865024583
5.0 0
Py Divide Time (ms) 0.004709000222646864
2.0
C Average Time (ms) 0.035897000088880304
2.0
Py Average Time (ms) 0.005119999968883349
```
Specially thanks to [manikachandna97](https://www.geeksforgeeks.org/using-c-codes-in-python-set-1/) for providing groundwork example.

Community chat on telegram: [Indonesian Python Warriors](https://t.me/idpyplc), [Indonesian C/ C++ Warriors](https://t.me/idcplc)


This repo is freely given without any kind of warranty. Use at your own risk.
