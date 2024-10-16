
products = {
    "hleb": {
        "cena": 100,
        "kolicina": 220
    },
    "pivo": {
        "cena": 150,
        "kolicina": 220
    },
    "jagode": {
        "cena": 120,
        "kolicina": 22
    }

}


allowed_options = [
   "dodaj", "obrisi", "izlistaj", "stop",
   "istorijat", "obrisati sve",
   "prikazi najskuplji proizvod", "pnp" ]

option = None
history = []


while option not in allowed_options:
    option = input(f"Sta zelite odraditi: {",".join(allowed_options)} \n").lower()

    if option == "obrisi":
        product = None

        while product not in products:
            product = input("Koji proizvod zelite da obrisete? \n ").lower()

        del products[product]

        msg = f"Uspesno ste izbrisali proizvod {product} \n"
        print(msg)
        history.append(msg)
        option = None

    elif option == "dodaj":
        product = None
        while product in products or product is None:
            product = input("Koji proizvod zelite da unesete? \n").lower()

        product_price = None
        while product_price is None or product_price <= 0:
            product_price = int(input("Unesite cenu proizvoda: \n "))

        print(product, product_price)

        product_amount = None
        while product_amount is None or product_amount <= 0:
            product_amount = int(input("Unesite kolicinu: \n "))

        products[product] = {
            "cena": product_price,
            "kolicina": product_amount
        }
        option = None

        msg = f"Dodali ste proizvod {product} \n"
        print(msg)
        history.append(msg)

    elif option == "izlistaj":
        print(products)
        option = None

    elif option == "istorijat":
        print(history)
        option = None

    elif option == "obrisati sve":
        products = {}
        print("Obrisali ste sve proizvode!")
        option = None

    elif option == "prikazi najskuplji proizvod" or "pnp":
        most_expensive_product = None
        highest_price = 0
        for product in products:
            if highest_price < products[product]["cena"]:
                highest_price = products[product]["cena"]
                most_expensive_product = product
        print(f"Najskuplji proizvod je: {most_expensive_product}, sa cenom od: {highest_price}")

print(products)
