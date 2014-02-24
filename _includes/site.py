#import _config
#SITE_TITLE = '<title>'+ _config.title + '</title>'

file_list = ["_templates/header.html", "_templates/body.html"]
class Site(object):

	def merge_file(self):
		content = ''
		for file_name in file_list:
			with open(file_name, 'r') as fil:
				for line in fil:
					content += line
		return content

	
	def insert(self):
		f_merge_spl = self.merge_file().split()
		for index, item in enumerate(f_merge_spl):
			if item == '<head>':
				f_merge_spl.insert( index + 1, SITE_TITLE )
		return ''.join(f_merge_spl)

	def compile(self):
		output = open('_site/index.html','w')
		output.write("<!DOCTYPE html>\n<html>\n%s</html>" % self.insert())

	def __init__(self):
		self.context = {}
		self._read_config()
		print self.context
		
	def _read_config(self):
		content = ''
		with open('../_settings.json', 'r') as fil:
			for line in fil:
					content += line	
			self.context = content

my_text = Site()
print my_text._read_config()



			



