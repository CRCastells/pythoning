import requests, sys, os, re, pprint

folderName = sys.argv[2]
url = sys.argv[1] + '/'
#arg1 is website arg2 is folder name to write
os.mkdir(folderName)
os.chdir(folderName)
print(os.getcwd())

index = requests.get(url)
file = open('index.html', 'w')
file.write(index.text)
file.close()


linkregex = re.compile(r'(((link)|(script)|(img)).*((href)|(src))=")(.*\.((css)|(js)|(png)|(jpg)))')
links = linkregex.findall(index.text)
files = []
for link in links:
	files.append(link[8].split('/'))

for file in files:
	while file[0] == '':
		del file[0]
	print('attempting to open file: ' +  '/'.join(file))
	sublist = file[:len(file)-1]
	path = ''
	for folder in sublist:
		path += folder + '/'
		try:
			os.mkdir(path)
		except: 
			print('folder: ' + folder + ' exists')
	try: 
		temp = open('/'.join(file) , 'wb')
		content = requests.get(url+ '/'.join(file))
		temp.write(content.content)
		temp.close()
	except: 
		print('file cannot be found. No such file or dir: ' + str(file))
	
	

pprint.pprint(files)
