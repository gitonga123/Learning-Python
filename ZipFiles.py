
import zipfile,os

print("The Current Working Directory is" + os.getcwd())

folderzip = zipfile.ZipFile('theme_darkly-9.0.0.3.zip')

print(folderzip.namelist())

spamInfo = folderzip.getinfo('theme_darkly/README.md')
print(spamInfo.file_size)

print(spamInfo.compress_size)

folderzip.close()