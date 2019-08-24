'''
collections:
    -   str
    -   list
    -   dict
    -   tuple
    -   range
    -   set

1. str
    -   Immutable sequence of homogeneous unicode codepoints (characters)
    -   Single quote and double quote
    -   "first" "second" => "firstsecond"
    -   help(str) => to get a list of functions on str
    -   name = " ".join(["Prem", "Anshu", "Mukherji"])  >>> 'Prem Anshu Mukherji'
    -   join is faster and efficient than other concatenation mechanism
    -   partition method divides a string into three around a separator: prefix, separator, suffix
    -   Use underscore as a dummy name for the separator; Underscore is understood by many tools;
    -   "Unforgetable".partition("forget") >> ('Un', 'forget', 'able')
    -   departure, _, arrival = "London:Edinburgh".partition(":") >> departure = London
    -   Use format to insert values into string; replacement fields delimited by { and }
    -   "The age of {0} is {1}.format("Jim", 32) >> The age of Jim is 32
    -   "The age of {name} is {age}".format(name="Jim", age=32)     => named parameter
    -   pos = ("Jim", 32)   => a Tuple declaration
    -   "The age of {pos[0]} is {pos[1]}".format(pos=pos)   => Use of tuple in place of parameter
    -   


2. byte
    -   immutable sequence of bytes
    -   d = b'some bytes'
    -   d.split() => [b'some', b'bytes']


3. list
    -   mutable sequence of heterogeneous objects
    -   s = ["apple", "oranges", 7, 9.0, ] => last character can be comma, list can be heterogeneous
    -   b = []  => empty list
    -   Can be indexed from the end, using negative indexes
    -   "This is a string".split()[-1]  >>  'string'
    -   "This is a string".split()[-2]  >>  'a'
    -   Negative indexes are better than forward indexing
    -   Avoid seq[len(seq) - 1)]; 
    -   Slicing extracts part of a list; slice = seq[start:stop]; stop is not included;
    -   "This is a string".split()[1:-1]    >> ['is', 'a']
    -   "This is a string".split()[1:]      >> ['is', 'a', 'string']
    -   del aSeq[3]     => removes the item at index 3
    -   aSeq.remove('This') => removes 'This' from the list
    -   aSeq.reverse    => reverse sort
    -   aSeq.sort(key)  => sorts on the basis of the key



4. dictionary
    -   mutable mappings of key to values
    -   unordered mapping from unique, immutable keys to mutable values
    -   {k1: v1, k2: v2}
    -   d = {'alice': '42', 'bob': '37', 'eve': '39'}   => dictionary with name as key, age as value
    -   d['alice']  >>> 42 => Retrieval is by key
    -   d['charles'] = '41'     => a new entry is made with key as 'charles' and value as 41
    -   d = dict (g='green', r='red', y='yellow')   >> {'g':'green', 'r':'red', 'y':'yellow'}
    -   d.update(dict(b='blue'))    >> {'g':'green', 'r':'red', 'y':'yellow', 'b':'blue'}
    -   



5. tuple
    -   heterogeneous immutable sequence of arbitrary object
    -   once created, objects can NOT be replaced, added or removed from tuple.
    -   t = ("Norway", 4.953, 3)    => new tuple with a string, float and int
    -   t[1] >>> 4.953   => tuples can be accessed using 'zero' based index
    -   t + (33.43, 256e9) >> ("Norway", 4.953, 3, 33.43, 256e9)   => Tuples can be concatenated
    -   nestedTuple = ((220, 17), (1187, 110), (329, 9))
    -   wrongTuple = (391)   => can NOT make a single element tuple; evaluates as integer;
    -   rightTuple = (391,)  => an extra comma at the end makes it a signle element tuple;
    -   emptyTuple = () 
    -   p = 1, 1, 3, 6, 8   => no parantheses still makes it a tuple
    -   Tuple can be used to return multiple values from a function
    -   min, max = min_max([3, 7, 1, 8])    => min = 1, max = 8
    -   Tuple unpacking allows us to destructure directly into name reference
    -   fname, mname, lname = "prem anshu mukherji".split() => fname = "prem", mname = "anshu" etc.
    -   a, b = b, a     => swapping of two variables
    -   tupleFromList = tuple([32, 12, 76])
    -   tupleFromString = tuple ("premanshu")   => ('p', 'r', 'e', 'm', 'a', 'n', 's', 'h', 'u')
    -   m in tuple('premanshu') >> true     => membership testing ('in', 'not in')


6. range
    -   sequence of arithmatic progression of integers
    -   r = range(5)    => range (0, 5)
    -   r = range (5, 10)   => range from 5 to 9
    -   r = range (5, 10, 2) >> 5, 7, 9   => start, stop, step
    -   Instead of using range, prefer enumerate, to do the enumeration job
    -   enumerate () yields (index, value) tuples
    -   for p in enumerate([33, 44, 55])
            print (p)
        >> (0, 33), (1, 44), (2, 55)
    -   for i, v in enumerate([33, 44, 55])
            print ("index = {}, value = {}".format(i, v))
        >> index = 0, value = 33
        >> index = 1, value = 44
        >> index = 2, value = 55
    -   

7. Set
    -   mutable unordered collection of unique, immutable objects
    -   p = {6, 8, 65, 234, 1233}
    -   e = set() => empty set
    -   add and update methods modify the set
    -   set allows for set algebra
    -   subsets, difference, symmetric-difference, intersection and union etc are support
    -   isSubset and disjoint also supported


'''