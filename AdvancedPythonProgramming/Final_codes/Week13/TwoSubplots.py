import matplotlib.pyplot as plt
import numpy as np

#Hoca soruda linspacelik bir bilgi vermemiş.
t = np.linspace(0, 10, 200)

#Position and Velocity.
P = t**2

V = 2 * t

#plt.subplots(2, 1) komutu ile 2 satır ve 1 sütundan oluşan bir yapı kurmalıyız.
#Create figure with 2 rows and 1 column of subplots.
fig, axes = plt.subplots(2, 1, figsize=(8,6))

#Top subplot: Position vs Time
axes[0].plot(t, P, linestyle="--", color="red")
axes[0].set_title("Position over time") #label methodları subplotlarda bir tık daha değişik ama işlevleri aynı. Başlarına "set_" getir.
axes[0].set_xlabel("Time [s]")
axes[0].set_ylabel("Position [m]")

#Bottom subplot: Velocity vs Time
axes[1].plot(t, V, color="blue")
axes[1].set_title("Velocity over time")
axes[1].set_xlabel("Time [s]")
axes[1].set_ylabel("Velocity [m/s]")

#axes[0] ve axes[1] kullanarak her grafiğe ayrı başlıklar (set_title) ve eksen etiketleri (set_ylabel) atadık.


#plt.tight_layout() kullanarak başlıkların ve eksen yazılarının birbirine girmesini (overlapping) önledik
#Adjust layout the prevent overlaps.
plt.tight_layout()

plt.show()