'''
    This program prints the histogram for the list provided
    We will solve this using list comprehension
    List Comprehension => [expr(item) for item in iterable]
'''
def histogram ( items) : 
    [print(item,' : ', '* ' * item) for item in items]


#histogram ([3, 5, 2, 6, 9])

import socket

print([ip for ip in socket.gethostbyname_ex(socket.gethostname())[2]])

print([l for l in ([ip for ip in socket.gethostbyname_ex(socket.gethostname())[2] 
if not ip.startswith("127.")][:1], [[(s.connect(('8.8.8.8', 53)), 
s.getsockname()[0], s.close()) for s in [socket.socket(socket.AF_INET, 
socket.SOCK_DGRAM)]][0][1]]) if l][0][0])