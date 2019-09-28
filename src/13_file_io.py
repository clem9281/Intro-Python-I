"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here: 

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file

# YOUR CODE HERE
try:
	f = open('foo.txt', 'r')
	print(f.read())
	#for i in f:
		#print(i)
finally:
	f.close()
# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make 
# sure that it contains what you expect it to contain

# YOUR CODE HERE
try:
	g = open('bar.txt', 'w')
	g.write('This is the first line\n')
	g.write('This should be on a newline ')
	g.write('This should be on the same line')
finally:
	g.close()