import os
 
def changeName(path, cName):
    for filename in os.listdir(path):
        if not filename.startswith('BOJ_') and ord('0') <= ord(filename[0]) <= ord('9'):
            print(path+filename, '=>', path+str(cName)+filename)
            os.rename(path+filename, path+str(cName)+filename)
 
changeName('studygroup/','BOJ_')