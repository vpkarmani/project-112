from distutils import extension
import os
import shutil

from_dir="C:/Users/vpkarmani/Downloads"
to_dir="C:/Users/vpkarmani/Dekstop/Document_files"

list_of_files =os.listdir(from_dir)
print(list_of_files)

for file_name in list_of_files:

    name,extension=os.path.splitext(file_name)


    if extension == " ":
        continue
    if extension in ['.txt','.pdf','.doc','docx']:

        path1=from_dir+ '/' + file_name
        path2=to_dir+ '/' + "Document_files"
        path3=to_dir+ '/' + "Document_files"
        +'/' + file_name
        
         
