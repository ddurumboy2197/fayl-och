def oqish(fayl_ismi):
    try:
        with open(fayl_ismi, 'r') as f:
            ma'lumot = f.read()
            return ma'lumot
    except FileNotFoundError:
        print("Fayl topilmadi.")
        return None

fayl_ismi = "ma'lumot.txt"
print(oqish(fayl_ismi))
