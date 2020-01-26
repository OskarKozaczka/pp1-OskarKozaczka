osoba = { "imie": "Marek",
          "nazwisko": "Banach",
          "wiek": 25,
          "hobby": ["programowanie","wycieczki"],
          "student": True,
          "telefon":{"stacjonarny":"2233","komorkowy":"7788"}
          }

print(osoba)

print(osoba["imie"])
print(osoba["hobby"])

osoba["nazwisko"]="Nowak"

print(osoba)

osoba["plec"]="mezczyzna"
print(osoba)

osoba["hobby"].append("rower")
print(osoba)

osoba["telefon"]["sluzbowy"]=3131
print(osoba)