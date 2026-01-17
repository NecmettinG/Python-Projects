import matplotlib.pyplot as plt
import numpy as np

#Ağ gecikmelerinin hangi aralıklarda yoğunlaştığını gösterir. Ortalama 50 ms civarında normal dağılımı doğrulamak için kullanılır.

#Soruda normal distribution istendiği için np.random.normal() kullanmamız lazım!!! 50 mean, 10 standart deviation, 1000 number of samples.
#Hoca burada 10 yerine 100 yazmış ama 12. slayttaki ilk sorudaki mantığı kullanırsak 10 olması lazım. bu kadın beni delirtecek yemin ediyorum.
#Hoca hatalı olabilir cidden, 10 olacak standart deviation parametresi.
delays = np.random.normal(50, 10, 1000)

plt.figure()

#Hoca bunu ilk defa gösteriyor amk hem de soruda veriyor bu ne olm. 1D hist de varmış.
plt.hist(delays, bins=40)

plt.xlabel("Delay (ms)")
plt.ylabel("Packet Count")

plt.title("Network packet delay distribution")

plt.grid(True)
plt.show()