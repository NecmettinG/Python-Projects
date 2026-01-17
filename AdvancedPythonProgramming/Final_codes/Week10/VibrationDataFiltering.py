# "*" işareti, threshold değerinin mutlaka isimle belirtilmesini zorunlu kılar (threshold=1.0).
def classify_vibrations(data, *, threshold = 1.0):

    isAnomaly = lambda x : x > threshold

    anomalyList = list(filter(isAnomaly, data))

    normalList = list(filter(lambda x : not isAnomaly(x), data))

    return normalList, anomalyList

data = [0.12, 0.18, 0.30, 1.2, 5.8, 0.25, 0.40, 7.5, 0.10]

#Threshold mutlaka isimle belirtilecek parametre yollarken!
print(classify_vibrations(data, threshold=1.0))