besmettingen_per_land = [
    1556730, # Spanje
    1408868, # Italie
    932111, # Duitsland
    861331, # Polen
    558779, # Belgie
    484648, # Nederland
    290601, # Zwitserland
    249099, # Oostenrijk
    208295, # Zweden,
    91619, # Griekenland
    70461, # Ierland
    70485, # Denemarken
    32761, # Albanie
    32352, # Noorwegen
    30333, # Luxemburg
    21216, # Finland
]
som = 0
for besmettingen in besmettingen_per_land:
    som = som + besmettingen
print("Het gemiddeld aantal besmettingen", som / len(besmettingen_per_land)) 
