# http://stackoverflow.com/questions/7420937/run-program-in-python-shell
# suppose this(function omer) is your 'test.py' file
def omer():
	"""This function runs the core of your program"""
	print("running main")

if __name__ == "__main__":
 # if you call this script from the command line (the shell) it will
 # run the 'main' function
	omer()