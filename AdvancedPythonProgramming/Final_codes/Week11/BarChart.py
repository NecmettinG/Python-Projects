import matplotlib.pyplot as plt
import numpy as np

#Sütun grafikleri(Bar Chart), farklı kategoriler arasındaki sayısal değerleri karşılaştırmak için kullanılır.

materials = ["Carbon/Epoxy", "Glass/Epoxy", "Kevlar/Epoxy"]
E = [135, 45, 70]

plt.figure(figsize=(8,5), dpi=150)

#plt.bar() → Dikey sütunlar oluşturur.
bars = plt.bar(materials, E, color=["black", "skyblue", "gold"])

plt.title("Comparison of Young's Modulus")
plt.ylabel("E (GPa)")
plt.grid(axis="y", linestyle="--", alpha=0.5)

#Bar Chartta bu şekil loop kullanman gerekecek! Bunun methodlarını kesin ezberle!!!
for bar in bars:
    height = bar.get_height()
    #plt.text() → Döngü kullanılarak her sütunun üzerine tam sayısal değerler yazdırılır.
    plt.text(bar.get_x() + bar.get_width()/2, height+2, f"{height}", ha="center", fontsize=10)

#plt.xticks(rotation=20) → Kategori isimleri okunabilirlik için 20° eğik yazılır.
plt.xticks(rotation=20)
plt.show()