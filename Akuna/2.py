def  melon_count(boxes, melons):
	temp=0;i=0;j=0;k=0
	for l in range(len(melons)):
		i=0;
		while i<=len(boxes):
			temp1=0;j=i;k=l
			while k<len(melons) and j<len(boxes):
				if melons[k]<=boxes[j]:
					j+=1;k+=1;temp1+=1
				else:
					j+=1
			temp=max(temp,temp1);i+=1
	return temp
#boxes=[4,3,2,3,1,3,2,4,2];melons=[8,1,2,1,3,4,3,2,4]
boxes=[1,2,1,2];melons=[3,3,2,1]
print(melon_count(boxes, melons))