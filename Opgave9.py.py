naam = input("Dienst naam:")
tickets = int(input("Hoeveel tickets wilt u kopen?"))
prijs_per_ticket = int(input("Prijs per ticket?"))
print(f"""
Beste {naam} je hebt zojuist {tickets} gekocht voor {prijs_per_ticket} euro per ticket,
met een totale waarde van {tickets*prijs_per_ticket} euro
""")