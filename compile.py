
"""open and read header and body html file"""

f1 = open('_templates/header.html', 'r')
f2 = open('_templates/body.html', 'r')

'''merge the content of two html files together'''
def get_content(fil):
	f_merge = ''
	for line in fil:
		f_merge += line 
	return f_merge + '\n'
	
f_merge = get_content(f1) + get_content(f2)	

'''write into _site/index.html'''
f3 = open('_site/index.html','w')
f3.write(f_merge)

f3.close()
f2.close()
f1.close()

