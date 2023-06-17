import sys

def getFileInfoStructures (bpfOrig, iFile):

	# Creating a python list from the iFile
	# Each element of the list is itself a list l
	# 1st element of l: line #
	# other elements of l: instructions 

	iFileLines = iFile.readlines()

	insertions = []
	for line in iFileLines:
		line = line.strip()
		insertions.append(line.split("|"))

	"""
	print ("insertions: ")
	print (insertions)
	print("\n\n")
	"""

	# Code to ensure that line numbers are in ascending order

	lineNumbers = [(int)(x[0]) for x in insertions]

	"""
	print ("lineNumbers: ")
	print (lineNumbers)
	print("\n\n")
	"""

	if(lineNumbers != sorted(lineNumbers)):
		print ("Error: Make sure that the line numbers are in ascending order.")
		exit()

	# Make a list of all original bpf instructions
	bpfOrigLines = bpfOrig.readlines()
	bpfOrigInsns = []
	for line in bpfOrigLines:
		bpfOrigInsns.append(line.strip())

	"""
	print ("Orig bpf instructions: ")
	print (bpfOrigInsns)
	print("\n\n")
	"""

	if (any(e > len(bpfOrigInsns) for e in lineNumbers)):
		print ("Error: one of your line numbers is greater than the length of your program.")
		exit()


	return bpfOrigInsns, insertions


def addInstructions (bpfOrigInsns, addFileInsertions, outFile):
	
	# recording current line of the original program to insert 
	currLine = 0

	# Perform each insertion in sequence
	for insertion in addFileInsertions:
		lineNum = (int)(insertion[0]) - 1

		for i in range(currLine, lineNum):
			outFile.write(bpfOrigInsns[i] + "\n")

		currLine = lineNum

		for i in range(1, len(insertion)):
			outFile.write(insertion[i] + ",\n")

	for i in range(currLine, len(bpfOrigInsns) ):
		outFile.write(bpfOrigInsns[i] + "\n")



def modifyInstructions (bpfOrigInsns, modifyFileInsertions, outFile):

	# recording current line of the original program to insert 
	currLine = 0

	# Perform each insertion in sequence
	for insertion in modifyFileInsertions:
		lineNum = (int)(insertion[0]) - 1

		for i in range(currLine, lineNum):
			outFile.write(bpfOrigInsns[i] + "\n")

		currLine = lineNum + 1
		
		outFile.write(insertion[1] + ",\n")

	for i in range(currLine, len(bpfOrigInsns)):
		outFile.write(bpfOrigInsns[i] + "\n")
	

"""
MAIN FUNCTION

"""

# getting all inputs
bpfOrigInput = sys.argv[1]
outFileInput = sys.argv[2]
operation = sys.argv[3]
fileInput = sys.argv[4]

bpfOrig = open(bpfOrigInput, 'r')
outFile = open(outFileInput, 'w')
iFile = open(fileInput, 'r')

bpfOrigInsns, insertions = getFileInfoStructures (bpfOrig, iFile)


# based on operation do separate tasks
if (operation == "ADD"):
	addInstructions (bpfOrigInsns, insertions, outFile)
elif (operation == "MODIFY"):
	modifyInstructions (bpfOrigInsns, insertions, outFile)
else:
	print ("Invalid operation: " + operation)

outFile.close()