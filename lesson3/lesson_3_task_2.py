from smartphone import Smartphone

catalog = [
    Smartphone("Sumsung", "N2000", "89998887766"),
    Smartphone("Nokia", "G3000", "89918817161"),
    Smartphone("Apple", "S11", "89928827262"),
    Smartphone("Apple", "S16", "89938837363"),
    Smartphone("Sumsung", "N2003", "89948847464")
]

for smartphone in catalog:
    print(f"{smartphone.mark} - {smartphone.model} . {smartphone.number}")