import matplotlib.pyplot as plt

#Pasta grafikleri, bir bütünün parçalarını yüzdesel olarak göstermek için kullanılır.
#Bir kompozit malzemenin bileşenleri: Fiber: %60,  Matris: %30,  Dolgu: %10

labels = ["Fiber", "Matrix", "Filler"]
sizes = [60, 30, 10]

plt.figure(figsize=(6, 6))

#autopct="%1.1f%%" → Dilimlerin üzerine yüzde değerlerini otomatik yazar.
#startangle=90 → Grafiğin saat 12 yönünden başlamasını sağlar.
#colors → Her dilime özel renk atanmasını sağlar.
plt.pie(sizes, labels=labels, autopct="%1.1f%%", startangle=90, colors=["royalblue", "lightgreen", "gold"])

plt.title("Composite Material Composition")

plt.show()