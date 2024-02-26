"""
*Bu program, projenin bulunduğu klasörde bulunan student.txt dosyasını okuyor. Bu dosyada öğrenci isim-soyismi, bölümü ve sınav notları bulunuyor.
*Isim ve soyisim arasında - olduğu için onları ayrı olarak ayırdık. Birden fazla ismi olan öğrencilere extra olarak dikkat ettik. Soyisimlerini isimlerinden ayırdık.
*Bazı bölümler iki ayrı kelime içerdiğinden, mesela "Bilgisayar Muh", Onları da birleştirmeye dikkat ettik.
*Notlarda ise vizeler, ortalamayı %30, final ise %40 etkiliyor. Eğer ortalama 50'nin altında ise veya ortalama 50 üstünde olmasına rağmen final notu 70'in altındaysa kalıyorsun.
*Program, geçen ve kalan öğrenciler için ayrı 2 tane dosya yaratıp kalanları failed.txt dosyasına, geçenleri passed.txt dosyasına write edicek. Dosyalar program çalışırken oluştu.
*Bütün özellikler tıpkı excel dosyası gibi key columnlar altına düzgün bir şekilde yazılacak. her column arasında 30 karakter boşluk olacak.
*Koddaki printler, kodun durumunu kontrol etmek amaçlı yazıldı.
"""
students_list = [] #.readlines() ile elde edeceğimiz listedeki string elemanlarını (yani dosyadaki satırlar) depolamak için boş bir liste oluşturduk
keys = ["Name","Surname","Department","Average","Status"] #Key column kısmı için bu key listesini oluşturduk. Keylere ait değerler, o keyin column'nunun altına sıralanacak.

with open("students.txt","r") as f: #students.txt dosyasını okuduk.

    get_rid_of_first_line = f.readline() #Dosyaya bakarsan ilk satırda keyleri vermiş ve bunu depolamak istemiyoruz. o yüzden ilk satırı şimdiden atladık.
    lines = f.readlines() #geri kalan satırları .readlines() ile liste şeklinde elde ettik. Her satır string şeklinde depolandı ve sonlarında \n var. Bu önemli! Bundan kurtulucaz.
    print(lines)

    for x in lines: #satırları içeren listeyi loopa soktuk.

        students_list.append(x)#Satır stringlerini üstte yarattığımız student_list listesine depoladık. Hala sonlarında \n var!

the_final_list = [] #listeyi revize ettikten sonra en sonki değişkenleri bu listeye depolayacaz. (mesela isimler arasında hala - var. Onlardan kurtulmamız lazım)

for i in students_list: #satırları string olarak depolamış listi loopa soktuk.
    temp_list = i.split(" ")#Dosyaya bakarsan satırlarda her özellik arasıda boşluk var. Mesela Eleanor-Taylor Fizik 78/90/70\n şeklinde özellikleri space ile ayırmış.
                            #string tutan i'yi boşluklardan ayırıp, Boşluklardan önceki ve sonraki karakterleri liste şeklinde getirdik ve temp_list geçici listesine eşitledik.
                            #['Eleanor-Taylor', 'Fizik', '78/90/70\n'] şeklinde

    name_list = temp_list[0].split("-")#isimleri ayrıca ayırmak için temp_list'in 0. indexindeki isim-soyisim stringini -'den böldük. ['Eleanor', 'Taylor'] listi elde ettik.
                                        #name_list listesindeki en son eleman daima soyadını temsil ediyor. Buna dikkat edicez.
    print(temp_list)
    print(name_list)

    if len(name_list)>2: #Eğer bir kişinin birden fazla ismi varsa bu bloğa girecek.
        for_list = []#isimleri depolamak için geçici bir liste oluşturduk. ana loop her en başa döndüğünde sıfırlanacak.
        for index in range(1,len(name_list)):#1'den başlatmamızın sebebi index error yememek için. index-1 sayesinde yine 0. indexten başladık. En son indexe (soyadı) uğramadık.
                                                #Soyadı için ayrı bir işlem yapıcaz. Sadece isimleri depolayacaz.
            for_list.append(name_list[index-1])#for_list geçici listesine soyadı hariç, Bütün isimleri depoladık. index-1 ile 0'dan en son indexin bir öncesine kadar gidicez.

        print(for_list)
        name = " ".join(for_list)#for_list geçici listesindeki isim elemanlarını stringe çevirdik ve name'ye eşitledik. isimler arasında boşluk olacak. örneğin Charles Booth.
        print(name)
        surname = name_list[len(name_list) - 1]#soyadını ise name_list listesinin en son indexindeki elemandan direkt elde ettik ve surname'ye eşitledik.

    else: #eğer kişi tek isimli ise:
        name = name_list[0]#direkt 0. index isim, 1. index soyisim olduğundan name ve surname'yi eşitledik.
        surname = name_list[1]

    department = "" #bölüm için boş bir string oluşturduk
    for x in range(1,len(temp_list)-1):#temp_listte 1. indexten son indexin bir öncesine kadar bölüm elemanları içeriyor ve bazı bölümler birden fazla kelime içeriyor.
        department += f"{temp_list[x]} " #Bu şekilde bölümün ismini eksiksiz bir stringe çeviriyoruz ve kelimeler arasında boşluk da var.


    grades = temp_list[len(temp_list)-1].split("/") #notlar 67/87/79\n şeklinde bir string ve en sonda \n var. öncelikle /'dan önceki ve sonraki karakterleri ayırıp listelettik.
    print(grades) #['67', '87', '79\n'] şeklinde list elde ettik. temp_list'in en son indexindeki tek string şeklindeki notları elemanlara bölüp listeledik. son indexte hala \n var.

    average = (int(grades[0]))*0.3 + (int(grades[1]))*0.3 + (int(grades[2].replace("\n","")))*0.4 #average hesapladık. final notundaki \n'dan .replace("\n","") ile kurtulduk.
    print(average)                                                                                #notları stringten inte çevirdik. .replace() sadece stringlerde çalışıyor!
    if average < 50 or int(grades[2].replace("\n","")) < 70: #geçti mi kaldı mı onu kontrol ettik.
        status = "failed"

    else:
        status = "passed"

    the_final_list.append([name,surname,department,average,status])#revize ettiğimiz değerleri the_final_list'e nested list olarak depoladık.

print(the_final_list)

with open("failed.txt","w") as failed: #kalan öğrenciler için. Dosyayı otomatikmen oluşturacak ve kalan öğrencileri yazıcak.

    for index in keys: #key columnları dosyaya yazdık. keyler ["Name","Surname","Department","Average","Status"] şeklinde. aralarında 30 boşluk olucak şekilde dosyaya yazıcaz.
        failed.write(index)#key listi içindeki column elemanları teker teker aynı satırda yazdık.
        failed.write(" "*(30-len(index))) #30 karakter boşluk attık. Her column arasında 30 boşluk var. düzenli olması için stringin uzunluğunu hesaba katman lazım.

    failed.write("\n")#satır başı yaptık.

    for x in the_final_list:

        if x[4] == "failed": #eğer x'in tuttuğu listenin 4. indexi failed'a eşit ise: (yani status'un değeri)

            for var in x:
                failed.write(str(var)) #var'ın tuttuğu listede average kısmı float tipinde olduğundan hata yememek için stringe çevirdik. zaten string olanlar aynı kalıcak!
                failed.write(" "*(30-len(str(var))))#30 boşluk atıcaz. düzenli olması için stringin uzunluğunu hesaba katman lazım. mesela 5 karakterli stringten sonra 25 boşluk
            failed.write("\n")#satırla işimiz bitince looptan çıkar çıkmaz dosyada satır başı yapıcak.


with open("passed.txt", "w") as passed: #aynı schedule ama bu sefer geçenler için bir dosya oluşturup geçenleri yazıcaz.
    for index in keys:
        passed.write(index)
        passed.write(" " * (30 - len(index)))

    passed.write("\n")

    for x in the_final_list:

        if x[4] == "passed":

            for var in x:
                passed.write(str(var))
                passed.write(" " * (30 - len(str(var))))
            passed.write("\n")

