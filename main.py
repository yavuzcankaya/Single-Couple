print("\033[93m Welcome to Couple&Single.")
Sayı = input('\033[93m Number : ')
try:
    if (int(Sayı) % 2 == 0):
      print("\033[93m Number is couple")
    else:
        print("\033[93m Number is single")
except ValueError:
    print("\033[91m Only numbers are acceptable!")
