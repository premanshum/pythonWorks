'''
A collection of functions which might be handy
'''
# 1. Profiling of python program
#    A profile is a set of statistics that describes how often and
#    for how long various parts of the program executed
import cProfile
def sum():
    print(1+2)
cProfile.run('sum()')

# ======================================================================
# ======================================================================

# 2. List all files in a directory in Python
from os import listdir
from os.path import isfile, join
def printFile() : 

    try:        
        files_list = [f for f in listdir('/home/students') if isfile(join('/home/students', f))]
        print(files_list)
    except :
        print ('directory does not exists!')

printFile()
print("\n")

# ======================================================================
# ======================================================================

# 3. program to check whether a file exists
import os.path
open('abc.txt', 'w')
print(os.path.isfile('abc.txt'))

# ======================================================================
# ======================================================================

# 4. program to access environment variables

import os
# Access all environment variables 
print('*----------------------------------*')
print(os.environ)
print('*----------------------------------*')
# Access a particular environment variable 
print(os.environ['ALLUSERSPROFILE'])
print('*----------------------------------*')
print(os.environ['PATH'])
print('*----------------------------------*')

# ======================================================================
# ======================================================================

# 5. program to get the current username.
import getpass
print(getpass.getuser())

# ======================================================================
# ======================================================================

# 6. find local IP addresses using Python's stdlib
import socket
print([l for l in ([ip for ip in socket.gethostbyname_ex(socket.gethostname())[2] 
if not ip.startswith("127.")][:1], [[(s.connect(('8.8.8.8', 53)), 
s.getsockname()[0], s.close()) for s in [socket.socket(socket.AF_INET, 
socket.SOCK_DGRAM)]][0][1]]) if l][0][0])
