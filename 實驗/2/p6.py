count=0
for i in range(100,1000):
	a=str(i)[0]
	b=str(i)[1]
	c=str(i)[2]
	if int(a)**3+int(b)**3+int(c)**3==i:
		print(i)
		count=count+1
		if count==1:
			break