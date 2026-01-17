import matplotlib.pyplot as plt
import numpy as np

#Yapay zekâ eğitimi sırasında loss değerinin her epoch sonunda nasıl azaldığını gösterir.

#.linspace() yerine .arange() kullanılmış!! Soruda sadece değer aralığı verilmiş, point sayısı verilmemiş o yüzden .arange() kullanıldı.
e = np.arange(1,81)

Lo = 1.2

k = 0.08

loss = Lo * np.exp(-k * e)

plt.figure()

#Red color (transparency(alpha)=0.6)
#alpha=0.6 ile noktaların şeffaflığı ayarlanır.
plt.scatter(e, loss, color="red", alpha=0.6)

plt.title("Training loss")
plt.xlabel("epoch")
plt.ylabel("Training Loss over Epochs")

#Grid frame (transparency=0.5, linestyle = --)
#plt.grid(True, linestyle='--', alpha=0.5) → Izgarayı yumuşatır.
plt.grid(True, linestyle="--", alpha=0.5)

plt.show()