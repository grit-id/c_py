# make.sh for c_py example, written by aviezab
# for compiling shared library
# first we have to make it as static lib with -c flags
cc work.c -fpic -lm -c -Wall -Werror
# second, we make it as dynamic
cc -shared -o libsample.so work.o