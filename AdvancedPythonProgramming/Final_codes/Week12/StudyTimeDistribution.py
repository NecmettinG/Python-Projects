import matplotlib.pyplot as plt

activities = ["Coding/Programming", "Debugging&Testing", "Reading Documentation", "Meetings(team/project)", "Code Review"]

percentage = [40, 25, 15, 10, 10]

plt.figure()

#autopct="%1.1f%%" → Dilimlerin üzerine yüzde değerlerini otomatik yazar.
#startangle=90 → Grafiğin saat 12 yönünden başlamasını sağlar.
#colors → Her dilime özel renk atanmasını sağlar. COLORS KOYMAZSAN KENDİSİ COLOR KOYUYORMUŞ HABERİN OLSUN!
plt.pie(percentage, labels=activities, autopct="%1.1f%%", startangle=90, colors=["blue", "yellow", "pink", "red", "purple"])

plt.title("Study Time Distribution (PieChart)")

plt.show()