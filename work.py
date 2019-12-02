# work.py from https://www.geeksforgeeks.org/using-c-codes-in-python-set-1/
# Modified by aviezab
# github.com/aviezab

import ctypes 
import os 
import time
from timeit import default_timer as timer

# locating the 'libsample.so' file in the 
# same directory as this file 
_file = 'libsample.so'
_path = os.path.dirname(os.path.realpath(__file__)) + "/" + _file
#_path = os.path.join(*(os.path.split(__file__)[:-1] + (_file, )))
print(_path)
_mod = ctypes.cdll.LoadLibrary(_path) 

# int gcd(int, int) 
gcd = _mod.gcd 
gcd.argtypes = (ctypes.c_int, ctypes.c_int) 
gcd.restype = ctypes.c_int 

# int divide(int, int, int *) 
_divide = _mod.divide 
_divide.argtypes = (ctypes.c_int, ctypes.c_int, 
					ctypes.POINTER(ctypes.c_int)) 

_divide.restype = ctypes.c_int 

def divide(x, y): 
	rem = ctypes.c_int() 
	quot = _divide(x, y, rem) 
	return quot, rem.value 

# void avg(double *, int n) 
# Define a special type for the 'double *' argument 
class DoubleArrayType: 
	def from_param(self, param): 
		
		typename = type(param).__name__ 
		
		if hasattr(self, 'from_' + typename): 
			return getattr(self, 'from_' + typename)(param) 
		
		elif isinstance(param, ctypes.Array): 
			return param 
		
		else: 
			raise TypeError("Can't convert % s" % typename) 

	# Cast from array.array objects 
	def from_array(self, param): 
		if param.typecode != 'd': 
			raise TypeError('must be an array of doubles') 
		
		ptr, _ = param.buffer_info() 
		return ctypes.cast(ptr, ctypes.POINTER(ctypes.c_double)) 
		
	# Cast from lists / tuples 
	def from_list(self, param): 
		val = ((ctypes.c_double)*len(param))(*param) 
		return val 
	
	from_tuple = from_list 
	
	# Cast from a numpy array 
	def from_ndarray(self, param): 
		return param.ctypes.data_as(ctypes.POINTER(ctypes.c_double)) 

DoubleArray = DoubleArrayType() 
_avg = _mod.avg 
_avg.argtypes = (DoubleArray, ctypes.c_int) 
_avg.restype = ctypes.c_double 

def avg(values): 
	return _avg(values, len(values)) 

# struct Point { } 
class Point(ctypes.Structure): 
	_fields_ = [('x', ctypes.c_double), ('y', ctypes.c_double)] 
	
# double distance(Point *, Point *) 
distance = _mod.distance 
distance.argtypes = (ctypes.POINTER(Point), ctypes.POINTER(Point)) 
distance.restype = ctypes.c_double

boottime1 = 0
boottime2 = 0
bench = 0

# Benchmark with C
boottime1 = timer()
print(divide(10, 2))
boottime2 = timer()
bench = (boottime2 - boottime1) * 1000
print("C Divide Time (ms)", bench)

# Benchmark With Python
boottime1 = timer()
h = 10/2
r = 10%2
print(h, r)
boottime2 = timer()
bench = (boottime2 - boottime1) * 1000
print("Py Divide Time (ms)", bench)


# Benchmark with C
boottime1 = timer()
print(avg([1,2,3]))
boottime2 = timer()
bench = (boottime2 - boottime1) * 1000
print("C Average Time (ms)", bench)

# Benchmark with Py
boottime1 = timer()
lx = [1,2,3]
sumlx = 0
for isi in lx:
    sumlx = sumlx + isi
avgx = sumlx/len(lx)
print(avgx)
boottime2 = timer()
bench = (boottime2 - boottime1) * 1000
print("Py Average Time (ms)", bench)


