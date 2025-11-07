# 1. Adatok beolvasása listába
adatok=[]
with open ("data.txt", "r", encoding="utf-8") as fin:
    for sor in fin:
        adatok.append(int(sor))

print (adatok)
# 2. Adatok átlaga
atlag = sum(adatok)/len(adatok)
print(f"A beolvasott adatok átlaga: {atlag:.2f}")
# 3. Döntsük el hogy volt-e 4-es
van = False
for szam in adatok:
    if szam == 4:
        van = True
        break
if van:
    print("Van 4-es")
else:
    print("Nincs 4-es")
# 4. Keressük meg hogy volt-e 5-ös
for i in range(len(adatok)):
    if adatok[i] == 5:
        van5 = True
        break

if van5:
    print(f"Van ötös, és a(z) {i}. elem.")
else:
    print("Nincs ötös")
# 5. Hány darab 9-es volt
kilencdb=0
for szam in adatok:
    if szam==9:
        kilencdb+=1 

print(f"A beolvasott számok között {kilencdb} db 9-es van.")
# 6. Mennyi a legnagyobb beírt szám
legnagyobbszam=adatok[0]
for szam in adatok:
    if szam > legnagyobbszam:
        legnagyobbszam=szam

print(f"A legnagyobb szám {legnagyobbszam}")
# 7. Hanyadik indexen van a legkisebb elem
# 8. Páros számok kiírása paros.txt-be