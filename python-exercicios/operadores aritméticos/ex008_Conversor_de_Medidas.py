metros = int(input("Uma distância em metros: "))
print(f"A medida de {metros:.1f}m corresponde a")

km = metros / 1000
hm = metros / 100
dam = metros / 10
dm = metros * 10
cm = metros * 100
mm = metros * 1000

print(F"{km}km")
print(F"{hm}hm")
print(F"{dam}dam")
print(F"{dm}dm")
print(F"{cm}cm")
print(F"{mm}mm")
