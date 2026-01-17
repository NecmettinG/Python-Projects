import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

#Create a 10 x 10 matrix of random values drawn from a standard normal distribution.
#Oluşturulan bu matris, ısı haritasının (heatmap) temel veri kaynağını oluşturur.
data = np.random.randn(10, 10)

#visualize this matrix as a 2D heatmap with seaborn.
#cmap="viridis" verilerin hangi renk paleti ile gösterileceğini belirler. Renk skalası koyu mor → parlak sarı şeklindedir.
#annot=True or annot=False controls whether numerical values inside the heatmap cells are displayed or not. We won't display currently.
#annot=False → Sadece renkler görünür.
sns.heatmap(data, cmap="viridis", annot=False)

plt.title("2D Heatmap")

plt.show()