import os
import shutil


class FileManeger:
    def __init__(self):
        self.start = str(self.pwd())

    def mkdir(self,name):
        print('done')
        os.mkdir(name)
    def rmdir(self,name):
        os.rmdir(name)

    def chdir(self,name):
        if (name == '..'):
            os.chdir(self.start)
            return
        os.chdir(name)

    def pwd(self):
        return os.getcwd()
    def touch(self,name):
        text_file = open(name, "w")
    def rename(self,name1,name2):
        os.rename(name1, name2)
    def replace(self,name1,name2):
        os.replace(name1, name2)
    def remove(self,name):
        os.remove(name)
    def write(self,name,text):
        filepath = str(self.pwd()) + '\\' + name
        if os.path.exists(filepath):
            file = open(name, "w")
            file.write(text)
            file.close()
        else:
            print("Файл не существует")
    def cat(self,name):
        filepath = str(self.pwd()) + '\\' + name
        if os.path.exists(filepath):
            file = open(name)
            print(file.read())
            file.close()
        else:
            print("Файл не существует")
    def copyFiles(self,dir1,dir2):
        source_dir = str(self.pwd()) + '\\' + dir1
        target_dir = str(self.pwd()) + '\\' + dir2

        file_names = os.listdir(source_dir)

        for file_name in file_names:
            shutil.move(os.path.join(source_dir, file_name), target_dir)



file = FileManeger()

# file.pwd()
# file.touch('test.txt')
# file.write('test.txt','kek')
# file.cat('test.txt')
# file.chdir('kek')
# print(file.pwd())
# file.chdir('..')
# print(file.pwd())

# print(file.start)
