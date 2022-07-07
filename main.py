import pandas as pd

csv = pd.read_csv("üyeler.csv")

uyeler = []

for uye in csv.values:
    uyeler.append(uye[0])

final = ", ".join(uyeler)

with open('üyeler.txt', 'w', encoding='utf8') as f:
    f.write("Destekleriniz için Teşekkürler; " + final)

print("basarili")