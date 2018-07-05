import os
import re

def main():
	list = []
	with open('taglist', 'r') as taglistfile:
		all_content=taglistfile.read()
		print all_content
		list = all_content.split('item\n')
		print list
s		for item in list:
			if item == '':
				print item
				continue
			sublist = item.split('\n')
			print sublist
			for line in sublist:
				if not line:
					break
				key, value = line.split(':')
				if key=='basedir':
					basedir = value
				if key=='directory':
					directory = value
				elif key=='branchname':
					branch = value
				elif key=='commitname':
					codecommit = value
				elif key=='tagname':
					tagname = value
				elif key=='comment':
					comment = value
			print directory, branch, codecommit, tagname, comment
			path = basedir + directory
			print path
			os.chdir(path)
			os.system('git checkout ' + branch)
			##os.system('pwd')
			##print('git tag -a ' + tagname + ' -m ' + comment + codecommit)
			os.system('git tag -a ' + tagname + ' -m ' + comment + codecommit)

			var = os.popen('git remote -v').read()
			##print var
			pushline = re.search(r'.*push.*', var).group()
			##print pushline
			match = re.split(r'[\s]', pushline)
			##print match[0]
			os.system('git push ' + match[0] + ' ' + tagname)
	taglistfile.close()


if __name__ == '__main__':
	main()