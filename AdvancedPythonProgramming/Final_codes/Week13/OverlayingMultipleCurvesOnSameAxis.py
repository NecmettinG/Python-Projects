import matplotlib.pyplot as plt
import numpy as np

#Farklı modellerin, deneylerin veya senaryoların sonuçlarını doğrudan karşılaştırmak için,
# tek bir grafik ekseni üzerinde birden fazla eğri çizilebilir.

#Technically, we simply call plt.plot() multiple times on the same axes!

t = np.linspace(0, 10, 200)

Ta = 20 + 5 * np.exp(-0.5 * t)
Tb = 20 + 3 * np.exp(-0.3 * t)
Tc = 20 + 7 * np.exp(-0.8 * t)

plt.figure(figsize=(8, 5))

#Aynı eksen üzerinde art arda plt.plot() komutları yazmalıyız. Her çizgi için ayırt edici bir label tanımlamalıyız.
plt.plot(t, Ta, label="Scenario A" ,color="red")
plt.plot(t, Tb, label="Scenario B" ,color="blue")
plt.plot(t, Tc, label="Scenario C" ,color="purple")

plt.xlabel("Time t [minutes]")
plt.ylabel("Temperature Tn(t) [Celcius]")
plt.title("Temperature response for three scenarios:")

#plt.legend() komutu ile hangi rengin hangi senaryoya ait olduğunu açıkça göstermek için yazdık
plt.legend()
plt.grid(True)

plt.show()
