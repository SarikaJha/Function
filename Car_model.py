def checkKey():
    car ={"brand":  "ford",
        "model":  "mustang",
        "year":  1964}
    if "model" in car:
        print("Yes, 'model' is one of the keys in this dictionary.")
    else:
        print("No, 'model' key is not in this dictionary.")

checkKey()