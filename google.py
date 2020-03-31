from googlesearch import search 
file = open('search.txt','r')
count=0
while True:
	count+=1
	line=file.readline()
	if not line:
		break
	linee=line.strip()
	print(linee)
	for url in search(linee,tld="co.in",num=10,pause=10): #you can change The Domain You Want By Change The Tld Vaule In This Case co.in
		print(url)
		pass
	pass



