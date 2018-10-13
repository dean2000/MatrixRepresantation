from Name_to_Matrix import matrixfy

with open('DbOfNames.csv','r') as file:
	for name in (file.readlines()):
		print(matrixfy(name))

file.close()