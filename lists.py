spam = ['bat', 'cat', 'rat', 'elephant']
""">>>spam[1]
'cat'
>>> spam[-1]
'elephant'
>>> spam[-4]
'bat'
>>> spam[4]
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    spam[4]
IndexError: list index out of range
>>> spam['cat']
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    spam['cat']
TypeError: list indices must be integers or slices, not str
>>> spam[1:3]
['cat', 'rat']
>>> spam[3:3]
[]
>>> spam[3:4]
['elephant']
>>> spam[3,-1]
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    spam[3,-1]
TypeError: list indices must be integers or slices, not tuple
>>> spam[3:-1]
[]"""
spam = [10, 20, 30, 40, 50, 60, 70, 80]
spam[1:4] = ['cat', 'dog', 'mouse']
""">>>spam
[10, 'cat', 'dog', 'mouse', 50, 60, 70, 80]
>>> spam = [10, 'cat', 'dog', 'mouse', 50, 60, 70, 80]
>>> spam[8] = ['90']
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    spam[8] = ['90']
IndexError: list assignment index out of range"""
spam[7:8] = [80, 90]
spam
"""[10, 'cat', 'dog', 'mouse', 50, 60, 70, 80, 90]
>>> spam[8]
90"""
for i in [0,2,3,4,6,9]:
	print(i)
"""
	
0
2
3
4
6
9"""
range(4)
#range(0, 4)
list(range(4))
#[0, 1, 2, 3]
list(range(1, 100, 2))
#[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97, 99]
supplies = ['pens', 'pens', 'pens', 'pens', 'pens', 'pens', 'pens', 'pens', 'pens', 'pens', 'pens', 'pens', 'pens', 'pens', 'pens', 'pens', 'pens', 'pens', 'pens', 'pens']
for i in range(len(supplies)):
	print('Index' + str(i) + ' in supplies is: ' + supplies[i])
"""	
Index0 in supplies is: pens
Index1 in supplies is: pens
Index2 in supplies is: pens
Index3 in supplies is: pens
Index4 in supplies is: pens
Index5 in supplies is: pens
Index6 in supplies is: pens
Index7 in supplies is: pens
Index8 in supplies is: pens
Index9 in supplies is: pens
Index10 in supplies is: pens
Index11 in supplies is: pens
Index12 in supplies is: pens
Index13 in supplies is: pens
Index14 in supplies is: pens
Index15 in supplies is: pens
Index16 in supplies is: pens
Index17 in supplies is: pens
Index18 in supplies is: pens
Index19 in supplies is: pens

""" 
cat = ['fat', 'orange', 'loud']
size, color, dispositio = cat
size
#'fat'
size, color, disposition = 'skinny', 'black', 'quiet'
size
"""'skinny'
>>> 
>>> 
>>>""" 
a='AAA'
b='BBB'
a,b=b,a
a
#'BBB'
 
spam = 42
spam=spam +1
spam+=1
spam
#44