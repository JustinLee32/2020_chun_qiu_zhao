Input = input().strip()
Liebiao = list(Input.split())
number = int(Input[0])
del Liebiao[0]
result = ''
for i in range(number):
	length = len(Liebiao[i])
	zeros  = int(8 - (length%8))
	temp = list(Liebiao[i])
	temp.sort()
	temp.extend(['0']*zeros)
	d = ''.join(temp)
	for j in range(int(len(d)/8)):
		result = result + d[8*j:8*j+8] + ' '
result = list(result)
del result[-1]
result = ''.join(result)
print(result)