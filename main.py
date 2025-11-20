from random import randint

def ask_int() -> None:
  guess = None
  while guess is None:
    try:
      value = int(input("Entrez un nombre entre 1 et 10: "))
      if value >= 1 and value <= 10:
        guess = value
      else:
        print(value, "n'est pas entre 1 et 10")
    except ValueError:
      print("Entier invalide. Réessayez.")
  return guess

if __name__ == "__main__":
  value = randint(1, 11)
  guess = -1
  n = 0
  while guess != value:
    guess = ask_int()
    if guess == value:
      print("Gagné")
    elif guess > value:
      print("Le nombre à trouver est plus petit")
    else:
      print("Le nombre à trouver est plus grand")
    n += 1

  print("Trouvé en", n, "essais")
