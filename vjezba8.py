products = {
    "audi": {
        "color": "crna",
        "amount": 20,
        "preis": 2000
    },
    "bmw": {
        "color": "plava",
        "amount": 59,
        "preis": 10000
    },
    "mercedes": {
        "color": "crvena",
        "amount": 40,
        "preis": 20000
    }
}

option = None
history = []
allowed_options = ["dodaj", "obrisi", "izlistaj","stop","istorijat","obrisi sve","najskuplji proizvod"]
while option not in allowed_options:
    option = input(f"Odaberite radnju koju zelite izvrsiti? {", ".join(allowed_options)}").lower()
    if option == "dodaj":
        product = None
        color = None
        amount1 = None

        while product not in products or product is None:
            product = input("Koji auto zelite unijeti: \n")

            color = input("Koje je boje auto: \n")

            preis = int(input("Kolika je cjena auta: \n"))

            print(f"Dodali ste {product} {color} {preis}")
            products[product] = {color, preis}
            history.append(f"Dodali ste {product} {color} {preis}")
            option = None
    elif option == "obrisi":
        product = None
        while product in products or product is None:
            product = input("Koji auto zelite obrisati: \n").lower()
            del products[product]
            history.append(f"Obrisali ste {product}")
            option = None
    elif option == "izlistaj":
        print(products)
        option = None
    elif option == "istorijat":
        print(history)
        option = None
    elif option == "obrisi sve":
        products=[]
        print(products)
    elif option == "najskuplji proizvod":
        n_c = 0
        n_p = None
        for product in products:
            if n_c < products[product]["preis"]:
                n_c = products[product]["preis"]
                n_p = product
        print(products[n_p]["preis"])


