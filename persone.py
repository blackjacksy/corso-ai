persone = [
    {
        "nome": "giulia",
        "eta": 18,
        "citta": "rho"
    },
    {
        "nome": "filippo",
        "eta": 49,
        "citta": "ancona"
    },
    {
        "nome": "luigi",
        "eta": 45,
        "citta": "roma"
    }
]

print(persone[1]["nome"])
print("La seconda persona ha", persone[1]["eta"], "anni")

for persona in persone:
    print(persona["nome"])

for persona in persone:
    print(persona["nome"], "ha", persona["eta"], "anni")

for persona in persone:
    eta_futura = persona["eta"] + 10
    print(persona["nome"], "tra 10 anni avrà", eta_futura, "anni")

for persona in persone:
    if persona["eta"] >= 18:
        print(persona["nome"], "è maggiorenne")

for persona in persone:
    if persona["eta"] <= 40:
        print(persona["nome"], "ha", persona["eta"], "ed è di", persona["citta"] )