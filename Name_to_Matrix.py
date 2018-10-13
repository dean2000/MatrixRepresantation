import math

'''
solution for Name to Matrix in codewars:
 https://www.codewars.com/kata/name-to-matrix/train/python

'''

# def matrixfy(st):
# 	if not st: return "name must be at least one letter"
# 	divider = 1
# 	while (len(st) / divider) > divider:
# 		divider += 1
# 	splited = list(list(st[i:i+divider])for i in range(0,len(st),divider))
# 	while len(splited[-1]) < divider:
# 		splited[-1] = splited[-1] + ['.']
# 	while len(splited) < divider:
# 		splited.append(['.']*divider)
# 	return splited
		
#refactored

def matrixfy(st):
	if not st: return "name must be at least one letter"
	divider = 1
	if st.count('\n'): 	#for running on a multi line file
		st = st.replace('\n',"")
	while (len(st) / divider) > divider:
		divider += 1
	splited = list(list(st[i:i+divider].ljust(divider,'.'))for i in range(0,len(st),divider))
	if len(splited) < divider:
		splited.append(['.']*divider)
	return splited

if __name__ == '__main__':
	matrixfy(st)

