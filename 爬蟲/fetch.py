from bs4 import BeautifulSoup
from urllib import request
import re

url='https://github.com/github/roadmap'
user_agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.1 Safari/605.1.15" #反爬技术
req=request.Request(url,headers={'User-Agent': user_agent} )
srcCode=request.urlopen(req).read().decode('utf-8')
soup=BeautifulSoup(srcCode,'html.parser')

text=soup.article.text

# 将网站源码存入文件
def writeSrccode():
	with open('web_src_code.txt','w') as f:
		f.write(soup.prettify())
	return

# 将要爬取文字存入文件
def writeWebtext():
	with open('webText.txt','w') as t:
		t.write(text)
	return

# 获取图片URL
def getPicUrl():
	return re.findall(r'https:.*?png',soup.decode('utf-8')) + re.findall(r'https:.*?jpg',soup.decode('utf-8'))

# 将图片下载到本地
def fetchPic(piclist):
	m=0
	for pic in piclist:
		request.urlretrieve(pic,'Pics/'+str(m)+'.jpg')
		m+=1
	return

# 词频统计
def countword(fileText):
	words_count={}
	with open(fileText) as file:
		read_line=file.read()
	read_line=read_line.lower()
	for ch in "~!@#$%^&*()_+`{}|\[\]\:\";\-\\\=<>?,./":
		read_line=read_line.replace(ch,' ')
	read_line=read_line.split()  #以空格、'\n'、'\t'等分割字串，此方法返回的是列表[list]
	for word in read_line:
		words_count[word]=words_count.get(word,0)+1
	# get方法返回指定键的值，如果键不在字典中返回默认值 None 或者设置的默认值。这里设置默认值是0，所以当一个词第一次出现时返回0，这时语句是words_count[word]=0+1，新建了一个键，它的值是1
	# 该词不是第一次出现，get方法直接返回该键目前的值，直接加1计数

	return sorted(words_count.items(),key=lambda tup:tup[1],reverse=True)  # 根据键值排序，返回列表[list]，列表中的元素类型是元组[tuple]
	# items()返回元组，排序的依据是键值（元组的第二个元素），True是倒序排列

# 查找以s开头以e结尾的单词
def findSandE():
	found=[]
	for i in range(0,len(sortedList)):
		if re.match(r'\bs\S*?e\b',sortedList[i][0]):
			found.append(sortedList[i][0])
	return found


sortedList=countword('webText.txt')
writeSrccode()
writeWebtext()
fetchPic(getPicUrl())
print('词频统计（前15位）：')
count=0
for i in range(0,len(sortedList)):
		print(sortedList[i][0],':',sortedList[i][1])
		count+=1
		if count==15:
			break

print('-----------------------------')
print('文章中以s开头以e结尾的单词有：')
for word in findSandE():
	print(word)