
'''import title'''
import _config
SITE_TITLE = _config.title
print SITE_TITLE

"""open and read header and body html file"""

f1 = open('_templates/header.html', 'r')
f2 = open('_templates/body.html', 'r')

'''merge the content of two html files together'''
def get_content(fil):
	content = ''
	for line in fil:
		content += line 
	return content + '\n'

content_f1 = get_content(f1) 
content_f2 = get_content(f2)

'''insert title in content_f1, between the <head> '''
def insert(str):
	content_f1_spl = content_f1.split()
	for index, item in enumerate(content_f1_spl):
		if item == '<head>':
			content_f1_spl.insert( index + 1, SITE_TITLE )
	return ''.join(content_f1_spl)
	
content_f1_tit = insert(content_f1)	

f_merge = content_f1_tit + content_f2

'''write into _site/index.html'''
f3 = open('_site/index.html','w')
f3.write("<!DOCTYPE html>\n<html>\n%s</html>" % f_merge)

f3.close()
f2.close()
f1.close()


