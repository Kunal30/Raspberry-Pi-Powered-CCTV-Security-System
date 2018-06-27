

import os
path="/home/pi/"
print"blabla"
def upload_files():
	if not os.path.exists(path):
		return
	dir_list=os.listdir(path)
	for file_name in dir_list:
        	if ".jpg" in file_name:
			print"uploaded"
			cmd ="./dropbox_uploader.sh upload "+file_name+" Apps/BerryPiBerry/"+file_name #"./dropbox_uploader.sh upload " + file_name + "Apps/BerryPiBerry/" + file_name
			os.system(cmd)

if __name__ == "__main__":
	upload_files()
