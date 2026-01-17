import matplotlib.pyplot as plt
import numpy as np

#İşletim sistemindeki dört işlem (P1 – P4) arasındaki kaynak kullanım yüzdelerini karşılaştırır.

processes = ["P1", "P2", "P3", "P4"]
usage = [35, 25, 20, 20]

plt.figure()

#renk koymayı unutma!
bars = plt.bar(processes, usage, color=["blue", "pink", "yellow", "purple"])

plt.title("Cpu time Distribution (Bar Chart)")
plt.ylabel("Cpu Usage (%)")

for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, height+2, f"{height}", ha="center", fontsize=10)

#Barlar altındaki yazılara herhangi bir rotation vermedik. Düz yazıcaz!
plt.xticks(rotation=0)

#axis="y" ile sadece y düzleminde çizgiler olacak!!!
plt.grid(True, axis="y")

plt.show()