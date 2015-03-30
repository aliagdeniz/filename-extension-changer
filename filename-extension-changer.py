# -*- coding: utf-8 -*-
#!/usr/bin/python

import os, re
from sys import argv

def usage():
	print "\nUsage: python %s <option> <argument1> <argument2> ...\n"%(argv[0])
	print " --add\t\t<directory> <which file type> <to which type>"
	print " --replace\t<directory> <which file type> <to which type>"
	print " --show\t\t<directory>"
	print " --search\t<directory> <which file type>"

	print "\n\tOptions"
	print " --add\t\tadds new filename extension to the and of filename."
	print " --replace\tdeletes current filename extension and adds new extension."
	print " --show\t\tshows all files under the given directory."
	print " --search\tsearches based on given type.\n\n\n"
	print """ Hint: to change all filetype, please use "*" (with double quotes) as <which file type> argument.\n"""
	exit(0)

def find(path,dir):
	for i in os.listdir(path)[::-1]:
		if os.path.isfile(path+"/%s"%i):
			file1.append(path+"/%s"%i)
		if os.path.isdir(path+"/%s"%i):
			dir.append(path+"/%s"%i)

def loop(directory,directory2):
	for i in directory:
		find(i,directory2)

def main_loop():
	i=0
	while True:
		directory2.append([])
		loop(directory2[i],directory2[i+1])
		if len(directory2[i+1]) == 0:
			break
		i+=1

def show_list(list1):
	for i in list1:
		print i

def choose1(type1,list1):
	for i in list1:
		b = re.search("\.%s$"%type1,i)
		if b:
			choosed.append(i)

def choose2(type1,list1):
	for i in list1:
		b = re.search("(.+)\.%s$"%type1,i)
		if b:
			choosed.append(i)
			choosed2.append(b.groups(1)[0])

def choose3(list1):
	for i in list1:
		b = re.search("(.+)\..+$",i)
		if b:
			choosed.append(i)
			choosed2.append(b.groups(1)[0])
		else:
			choosed.append(i)
			choosed2.append(i)

def extension_control(list1):
	if len(list1) == 0:
		print "There is no such file with %s extension in %s directory" %(argv[3],argv[2])
		exit(0)

def add1(list1,type1,type2):
	for i in list1:
		os.rename(i,"%s.%s"%(i,type1))
	if type2=="all":
		print """%s extension added to end of all files in the "%s" directory."""%(type1,argv[2])
	else:
		print """%s extension added to end of all %s files in the "%s" directory."""%(type1,type2,argv[2])

def add_():
	if argv[3]=="*":
		add1(file1,argv[4],"all")
	if not argv[3]=="*":
		choose1(argv[3],file1)
		extension_control(choosed)		
		add1(choosed,argv[4],argv[3])

def replace():
	if argv[3] == "*":
		choose3(file1)
		extension_control(choosed)
		for i in range(0,len(choosed)):
			os.rename(choosed[i],"%s.%s"%(choosed2[i],argv[4]))
		print """All filename extensions in "%s" directory are replaced with %s."""%(argv[2],argv[4])
	else:
		choose2(argv[3],file1)
		extension_control(choosed)
		for i in range(0,len(choosed)):
			os.rename(choosed[i],"%s.%s"%(choosed2[i],argv[4]))
		print """Files with %s extension in "%s" directory are replaced with %s."""%(argv[3],argv[2],argv[4])

def type_control(type1):
	if re.match("^\.",type1):
		print """Wrong <type> argument. Please delete "." if argument contains and write exact directory."""
		exit(0)

def argument_control(type1):
	if not len(argv) == type1:
		usage()

def ingredients(list1):
	for i in list1:
		a = re.search("%s/+(.+)$"%argv[2],i)
		if a:
			subdirectory.append(a.groups(1)[0])

def main():
	global file1
	file1 = []

	global directory
	directory = []

	global directory2
	directory2 = []
	directory2.append([])

	global choosed
	choosed = []

	global choosed2
	choosed2 = []

	global subdirectory
	subdirectory = []
	
	global pdf_content
	pdf_content = []

	global a

	if not len(argv) < 3:
		a = argv[1]
		if  a == "--add" or a == "--replace" or a == "--search" or a == "--show":
			pass
		else:
			print "Invalid option."
			exit(1)

		try:
			find(argv[2],directory)
			loop(directory,directory2[0])
			main_loop()
			if len(file1) == 0:
				print "There is no file in %s directory" %(argv[2])
				exit(0)
		except OSError:
			print "You may be forget <directory> argument. Please check it."
			exit(1)

		if a == "--add":
			argument_control(5)
			type_control(argv[3])
			type_control(argv[4])

			add_()
		elif a == "--replace":
			argument_control(5)
			type_control(argv[3])
			type_control(argv[4])

			replace()

		elif a == "--search":
			argument_control(4)
			type_control(argv[3])

			choose1(argv[3],file1)
			extension_control(choosed)
			show_list(choosed)

		elif a == "--show":
			argument_control(3)
			type_control(argv[2])
			show_list(file1)

		elif a == "--help":
			usage()

		else:
			print "Wrong option. Please use --help option to see usage menu."
	else:
		usage()

if __name__ == '__main__':
	main()
