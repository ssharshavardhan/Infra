import os
import shutil
import sys
import platform
import hashlib 
from ntpath import split
from ntpath import basename
from subprocess import call
import socket

filePath = ''
separator = ''
if platform.system() != 'Windows':
	OS = 'Not Windows'
	separator = '/'
	filePath = '/home/'
else:
	OS = 'Windows'
	separator = '\\'
	filePath = 'C:\\User\\'
	
def check_cluster(fd):
	while(1):
		cluster = fd.read(1024)
		if not cluster:
			return
		yield cluster

def Duplicates():
	hashed = {}
	#recursive search in folders and checking their file sizes
	for path, subdirs, files in os.walk(filePath):
		#to exclude shortcuts
		files = [file for file in files if not file[0] == '.']
		subdirs[:] = [directory for directory in subdirs if not directory[0] == '.']
		i = 1
		for file in files:
			try:
				hash_obj = hashlib.sha1()
				path_of_file = os.path.join(path, file)
				fd = open(path_of_file,'rb')
				for cluster in check_cluster(fd):
					hash_obj.update(cluster)
				key = (hash_obj.digest(), os.path.getsize(path_of_file))
				duplicate = hashed.get(key, None)
				if duplicate:
					print i,
					print " "+path_of_file +" and "+ duplicate
					i = i+1
					print 
				else:
					hashed[key] = path_of_file
			except OSError:
				pass

#sort helper
def Sortfileshelper(path,file,extension):
	path_of_folder = path+extension[1:].upper()
	if not os.path.exists(path_of_folder):
		os.makedirs(path_of_folder)
	shutil.move(os.path.join(path,file), os.path.join(path_of_folder,file))

#Displays files on Desktop
def files_on_desktop(path):
	all_files = os.listdir(path)
	all_files[:] = [directory for directory in all_files if not directory[0] == '.']
	print "\nThe following files and folders on desktop\n"
	for l in all_files:
		print l

def Sort_by_data_type(path):
	DATATYPE = ['INTERNET','SYS','SPREADSHEET','PRESENTATION','COMPRESSED','EXECUTABLES','IMAGES','VIDEOS','DATA','PROG','TEXT']
	SYS = ['BAK','CAB','CFG','CPL','CUR','DLL','DMP','DRV','ICNS','ICO','INI','MSI','SYS','TMP']
	EXECUTABLES = ['APK','BIN','CGI','PL','COM','GADGET','JAR','WSF' ]
	COMPRESSED = ['7Z','ARJ','DEB','PKG','RAR','RPM','TAR','GZ','Z','ZIP']
	DATA = ['CSV','MDB','DB','DBF','LOG','JSON','SAV','SQL','XML','DAT']
	SPREADSHEET = ['ODS','XLSX''XLR','XLS',]
	PROG = ['PY','C','CLASS','CPP','CS','H','PHP','JAVA','SH','SWIFT','VB']
	PRESENTATION = ['KEY','ODP','PPS','PPT','PPTX']
	IMAGES = ['ANI','IMG','JPG','MAC','PBM','BMP','CAL','FAX','GIF','PCD','PCX','PCT','PGM','PNG','PPM','PSD','RAS','JBG','JPE','JPEG','TGA'',TIFF','WMF']
	TEXT = ['PDF','RTF','DOC','WKS','DOCX','WPS','TEX','TXT','ODT','WPD']
	INTERNET = ['ASP','ASPX','CER','CFM','CGI','PL','CSS','HTM','HTML','JS','JSP','PART','RSS','XHTML']
	VIDEOS = ['SWF','3GP','AVI','MKV','MOV','RM','WMV','MP4','MPG','3G2','FLV','H264','M4V','VOB','MPEG' ]
	all_files = os.listdir(path)
	all_files[:] = [d for d in all_files if not d[0] == '.']
	for l in all_files:
		for d in DATATYPE:
			for extension in eval(d):
				if l == extension:
					if not os.path.exists(path+d):
						os.makedirs(path+d)
					shutil.move(os.path.join(path,l), os.path.join(path+d,l))
	print "Files have been sorted according to their data!"

def Largefiles():
	while True:
		n = input('No of large files you want to view ')
		if n==0:
			return
		print "\nThe largest "+`n`+" files on your PC are:"
		N_Largest_Files = {}
		for i in range(1,n+1):
			N_Largest_Files['a'+`i`] = 0
		for path, subdirs, files in os.walk(filePath):
			files = [file for file in files if not file[0] == '.']
			subdirs[:] = [directory for directory in subdirs if not directory[0] == '.']
			for file in files:
				try:
					file_size = os.path.getsize(path+separator+file)
					key_minima = min(N_Largest_Files.keys(), key=(lambda k: N_Largest_Files[k]))
					if file_size > N_Largest_Files[key_minima]:
						del N_Largest_Files[key_minima]
						N_Largest_Files[path+separator+file] = file_size
				except OSError:
					pass

		N_Largest_Files = sorted(N_Largest_Files.items(), key=lambda x:x[1] , reverse = True)
		print "Size\t\tFile Name:\n"
		for x in N_Largest_Files:
			var = x[1]/1048576
			print "%.2f" %var,
			print "MB\t"+ x[0]

		N_largest_file_names = []
		for x in N_Largest_Files:
			N_largest_file_names.append(x[0])
		
		while True:
			try:
				x = input("\nOptions : \n1) Sort files by least recently used\n2) Go to main menu\n")
				if x == 1:
					Least_recently_used = sorted(N_largest_file_names, key=os.path.getctime)
					print "\nLargest N files by least recently used\n"
					i = 1
					for file in Least_recently_used:
						print i,
						print " "+file
						i = i+1
					break
				elif x == 2:
					return
				else:
					print "Choose valid Option"
			except:
				print "Choose valid Option"
		try:
			u = raw_input("Input Y to stay in this mode else type N to go back to main menu ")
			u = u[0].lower()
			if u =='y':
				pass
			elif u == 'n':
				return
			else:
				print "Choose valid Option"
		except:
			print "Choose valid option"

def Sortfiles():
	extensions = ['ANI','MDB','SAV','SQL','XML','BMP','CAL','FAX','GIF','IMG','JBG','JPE','PPM','PSD','RAS','PY','C','CLASS','JPEG','JPG','MAC','PBM','PCD','PCX','PCT','PGM','PNG',
	'CPP','CS','CAB','CFG','CPL','CUR','DLL','DMP','DRV','ICNS','ODS','H','PHP','TGA'',TIFF','ICO','INI','MSI','SYS','TMP','PPS','PPT','PPTX','WMF','3G2','3GP','AVI','FLV','H264','M4V','MKV','MOV','MP4','MPG','MPEG','RM','SWF','VOB',
	'WMV','DOC','DOCX','ODT','PDF','RTF','TEX','TXT','WKS','WPS','WPD','BAK','XLR','XLS','XLSX','JAVA','SH','SWIFT','VB','DBF','LOG','JSON','KEY','RAR','RPM','TAR','GZ','Z','ZIP','ODP','ASP','ASPX','CER','CFM','CGI','PL','CSS','HTM','HTML','JS','JSP','PART','RSS','XHTML','APK','BIN','CGI','PL','COM','GADGET','JAR','WSF','7Z','ARJ','DEB','PKG'
	,'CSV','DAT','DB']
	home_path = os.path.expanduser('~')
	path = home_path + '/Desktop/'
	files_in_dir = os.listdir(path)
	files = [ file for file in files_in_dir if os.path.isfile(os.path.join(path,file)) and not os.path.islink(path+file)]	
	while True:
		print "\nChoose your option"
		try:
			sort_option = raw_input("a. Sort based on valid extensions?\nb. Sort based on kinds of extensions?\nc. List files and folders on your Desktop?\nd. Sort folders based on data they hold like images etc.\ne. Exit\n")
			sort_option = sort_option[0]
			if sort_option == 'a' or sort_option == 'b':
				for file in files:
					extension = os.path.splitext(file)[1]
					if extension == '':
						#Files with No extension are taken as txt by default
						extension = '.txt'
					if sort_option == 'a':
						if extension.upper()[1:] in extensions:
							Sortfileshelper(path,file,extension)
					else:
						Sortfileshelper(path,file,extension)
				print "FILES SORTED"
				return
			elif sort_option == 'c':
				files_on_desktop(path)
				return
			elif sort_option == 'd':
				Sort_by_data_type(path)
				return
			elif sort_option == 'e':
				break
			else:
				print "Choose valid Option"
		except:
			print "Choose valid Option"

def main():
	while True:
		try:
			case = input('\nMenu: \nChoose your option\n1. Gets N largest files of system\n2. Sort the files on Desktop\n3. List duplicate files on your system\n4. Exit \n')
			if case == 1:
				#this function prints top n files
				Largefiles()
			elif case == 2:
				#this function sorts files based on extension excluding shortcuts
				Sortfiles()
			elif case == 3:
				#prints duplicate files 
				Duplicates()
			elif case == 4:
				break
			else:
				print "Choose valid option"
		except:
			print "Choose valid option"

if __name__ == "__main__":
    main()
