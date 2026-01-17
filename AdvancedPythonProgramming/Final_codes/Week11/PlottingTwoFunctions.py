import matplotlib.pyplot as plt
import numpy as np

t = np.linspace(0,20, 1000)

#We have 2 functions now.
y1 = np.exp(-0.1*t) * np.sin(5*t)
y2 = 0.5 * np.cos(3*t)

#Grafiğin daha net ve okunaklı olması için:
#Grafik alanı genişletilir. (figsize=(10,5)).
#DPI artırılarak daha yüksek çözünürlük elde edilir.
plt.figure(figsize=(10,5), dpi=150)

#İki fonksiyonun karışmaması için farklı çizim stilleri kullanılır:

#Birinci çizgi (y1): Mor renk, Düz çizgi, Kalınlık: 2.5
plt.plot(t, y1, label="Damped Oscillation", linewidth=2.5, color="purple")

#İkinci çizgi (y2): Turuncu renk, linestyle="--" ile kesikli çizgi, Kalınlık: 2.5
plt.plot(t, y2, label="Forced Vibration", linewidth=2.5, color="orange", linestyle="--")

plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.title("Damped vs Forced Oscillation")

#Izgara çizgileri kesikli hale getirilir. alpha değeri düşürülerek çizgiler daha şeffaf yapılır.
plt.grid(True, linestyle="--", alpha=0.5)

#Çizim komutlarına eklenen label="Damped Oscillation" gibi etiketler,
# plt.legend() komutu ile grafiğin köşesinde bir açıklama kutusu (legend) oluşturur.
#Bu sayede her rengin hangi fonksiyona ait olduğu kolayca anlaşılır.
plt.legend()

plt.show()
