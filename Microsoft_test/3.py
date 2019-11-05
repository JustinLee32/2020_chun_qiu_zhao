
# Read only region start
class UserMainCode(object):
	@classmethod
	def findPosition(cls, input1, input2, input3):
		'''
		input1 : int
		input2 : int
		input3 : int[-]
		
		Expected return type : int
		'''
		# Read only region end
		# Write code here
		pass
		res=0;nums=list(range(input1+1));flag1=0
		def mycase(e,x,nums,flag1):
			flag=0;ans=0
			if e==1:
				nums[flag1]=-1
				flag1+=1
			elif e==2:
				nums[x-1]=-1
			elif e==3:
				for i in range(x):
					if nums[i]==-1:
						flag+=1
				ans=(x-flag)
			return ans,flag1
		for i in range(input2):
			myres=mycase(input3[i][0],input3[i][1],nums,flag1)
			res+=myres[0]
			flag1=myres[1]
		return res