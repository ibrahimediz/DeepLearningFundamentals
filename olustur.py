import os

# os.mkdir("Egzersiz")
fileName = "ilk.ipynb"
liste = ["Cevaplar"]
for item in liste:
    folderPath = ["Egzersiz",item]
    if  folderPath:
        os.mkdir(folderPath)
    open(os.path.join(folderPath,fileName),"a+")