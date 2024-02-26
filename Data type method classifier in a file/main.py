list_methods = ["list",]
string_methods = ["string",]
tuple_methods = ["tuple",]
set_methods = ["set",]
dict_methods = ["dict",]
all_list = []

#Burada bütün method depolayan listeleri all_list listesinde append() ile depoladık:

for i in dir(list): #dir(data type) ile o datanın classına ait methodları liste şeklinde listeliyor.

    list_methods.append(i)

all_list.append(list_methods)

for i in dir(str):

    string_methods.append(i)

all_list.append(string_methods)

for i in dir(tuple):

    tuple_methods.append(i)

all_list.append(tuple_methods)

for i in dir(set):

    set_methods.append(i)

all_list.append(set_methods)

for i in dir(dict):

    dict_methods.append(i)

all_list.append(dict_methods)

max=0
for i in all_list: #max indexli listin index sayısını bulduk
    temp = len(i) #geçici değer

    if temp>max: #eğer geçici değer max'tan daha büyükse geçici değer, yeni max olucak.
        max = temp


with open("method file.txt","w") as f: #aşağıda her sütunu 30'ar olarak ayırdım.


    for number in range(max): #max elemanlı listin eleman sayısını range'e koyduk.
        f.write("\n") # her satır bitiminden sonra dosyada satır başı yapıcak. MAL, 2 SAAT BUNA UĞRAŞTIN MAL! SÜTUNLARI DA BELLİ BİR DEĞERE SABİTLE VE KARAKTER SAYILARINI DA SAY MAL!
        for x in all_list:

            if number < len(x): #index error yememek için if ve else bloğu açtık. Eğer listin eleman sayısı, number'dan büyük ise bloğa giricek.

                f.write(x[number]) #nested list içindeki değeri dosyaya yazıcak.

                f.write(" "*(30-len(x[number]))) #sütunu 30'a tamamlamak için 30'dan nested listteki değerin karakter sayısını çıkardık.

            else: #eğer for looptaki list tutan değişkenin eleman sayısı, number'dan küçükse ----- 5 tane çizgi basıcak ve 25 boşluk atlicak (30' a tamamlıyoruz sütunu)

                f.write("-----")
                f.write(" "*25)

