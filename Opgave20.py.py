gebruikersnaam = input("Geef je gebruikersnaam")
passwoord = input("Je wacht woord ")
bestand = open("inlog-gebruiker.txt","wt")
bestand.write(f"{gebruikersnaam}\n")
bestand.write(f"{passwoord}\n")
bestand.close()

