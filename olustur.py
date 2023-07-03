import os

# os.mkdir("Egzersiz")
fileName = "ilk.ipynb"
liste = ["Cevaplar","Arzu","Ersel","Ozkan","Atıf","Omer","Yusuf",\
    "Beytullah","Mehmet","İhsan","OmerReal","Beste","Şafak","Kubra","Hatice","YunusEmre","Berkay","Muhammed","Harun"]
for item in liste:
    folderPath = os.path.join("Egzersiz",item)
    if not os.path.exists(folderPath):
        os.mkdir(folderPath)
    open(os.path.join(folderPath,fileName),"a+")