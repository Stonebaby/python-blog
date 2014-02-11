
'''import title'''
import _config
SITE_TITLE = '<title>'+ _config.title + '</title>'
print SITE_TITLE

'''put all source files into one list, open and merge them together'''
file_list = ["_templates/header.html", "_templates/body.html"]

def merge_file(file_list):
	content = ''
	for file_name in file_list:
		with open(file_name, 'r') as fil:
			for line in fil:
				content += line
	return content
	
f_merge = merge_file(file_list)

'''insert title in f_merge, between the <head> '''
def insert(str):
	f_merge_spl = f_merge.split()
	for index, item in enumerate(f_merge_spl):
		if item == '<head>':
			f_merge_spl.insert( index + 1, SITE_TITLE )
	return ''.join(f_merge_spl)
	
f_merge_title = insert(f_merge)	

'''write into _site/index.html'''
output = open('_site/index.html','w')
output.write("<!DOCTYPE html>\n<html>\n%s</html>" % f_merge_title)



