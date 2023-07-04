import os

# os.mkdir("Egzersiz")
fileName = "01_03_MissingData.ipynb"
liste = ["Cevaplar","Arzu","Ersel","Ozkan","Atıf","Omer","Yusuf",\
    "Beytullah","Mehmet","İhsan","OmerReal","Beste","Şafak","Kubra","Hatice","YunusEmre","Berkay","Muhammed","Harun"]
for item in liste:
    folderPath = os.path.join("Egzersiz",item)
    if not os.path.exists(folderPath):
        os.mkdir(folderPath)
    open(os.path.join(folderPath,fileName),"a+")

"""
/workspace/DeepLearningFundamentals/Datasets/50_Startups.csv

yukarıdaki adreste bulunan verisetini pandas kütüphanesini kullanarak
isminize açılan klasördeki 01_01_Pandas.ipynb dosyasına yükleyiniz ve
sırasıyla aşağıdaki işlemleri gerçekleştiriniz.
1. ilk beş satıra bakmak
2. son beş satıra bakmak
3. veri seti ile ilgili bilgiyi ekrana dökmek
4. tanımlayıcı istatistik verisini ekrana yansıtmak
5. ilk 20 satır ve 4. sütunda yer alan bilgileri görüntülemek

"""