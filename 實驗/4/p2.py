words_count={}

file=open('letter.txt')
read_line=file.read()
file.close()
read_line=read_line.lower()
for ch in "~!@#$%^&*()_+`{}|\[\]\:\";\-\\\=<>?,./":
	read_line=read_line.replace(ch,' ')
read_line=read_line.split()  #以空格、'\n'、'\t'等分割字串，此方法返回的是列表[list]
for word in read_line:
	words_count[word]=words_count.get(word,0)+1  
# get方法返回指定鍵的值，如果鍵不在字典中返回默認值 None 或者設置的默認值。這裏設置默認值是0，所以當一個詞第一次出現時返回0，這時語句是words_count[word]=0+1，新建了一個鍵，它的值是1
# 若該詞不是第一次出現，get方法直接返回該鍵目前的值，直接加1計數

order_list=sorted(words_count.items(),key=lambda tup:tup[1],reverse=True)  # 根據鍵值排序，返回列表[list]，列表中的元素類型是元組[tuple]
# items()返回元組，排序的依據是鍵值（元組的第二個元素），True是倒序排列

for i in range(0,len(order_list)):
	print(order_list[i][0],':',order_list[i][1])  #order_list[i]確定元組，order_list[i][0]確定元組中的元素