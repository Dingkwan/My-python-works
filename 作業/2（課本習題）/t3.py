price=input('输入价格：')
if int(price)>=5000:
	print('最终价格为：',int(price)*0.8)
elif int(price)>=3000:
	print('最终价格为：',int(price)*0.85)
elif int(price)>=2000:
	print('最终价格为：',int(price)*0.9)
elif int(price)>=1000:
	print('最终价格为：',int(price)*0.95)
else:print('最终价格为：',int(price))