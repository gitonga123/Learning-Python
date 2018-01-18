
import zipfile,os

print("The Current Working Directory is" + os.getcwd())

folderzip = zipfile.ZipFile('theme_darkly-9.0.0.3.zip')

print(folderzip.namelist())

spamInfo = folderzip.getinfo('theme_darkly')
print(spamInfo.file_size)

print(spamInfo.compress_size)

folderzip.extractall(os.path.join(os.getcwd(),'files','dark'))

folderzip.close()