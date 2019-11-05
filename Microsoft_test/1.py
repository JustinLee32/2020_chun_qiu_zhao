
# Read only region start
class UserMainCode(object):
	@classmethod
	def maxCircles(cls, input1, input2, input3):
		'''
		input1 : int
		input2 : int
		input3 : int
		
		Expected return type : int
		'''
		# Read only region end
		# Write code here
		pass
		res=0
		def isdivided(i,j):
			if i%j==0 or j%i==0:
				return True
			return False
		A=[];b=[]
		i=0;j=0
		while i<input1:
			j=0;b=[];
			while j<input1:
				b.append(0)
				j+=1
			A.append(b)
			i+=1
		for i in range(input1):
			for j in range(input1):
				if isdivided(i,j):
					A[i][j]=1
		
#		def getnext(A,i):
#			for j in range(input1):
#				if A[i][j]==1:
#					return j
		i=input2;res=1
		def finalsolve(A,i,step):
			if step==0 and i!=input2:
				return 0
			if step==0 and i==input2:
				return 1
			if step==1:
				return res
			else:
				res+=res*finalsolve(A,i,step-1)
				

		
input1=input();input2=input();input3=input();
a=UserMainCode()
print(a.maxCircles(input1, input2, input3))
			
		
	
