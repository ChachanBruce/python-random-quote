import random
def main():
  #print("Keep it logically awesome.")

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()

  last_1 = 19
  rnd_1 = random.randint(0, last_1)

  last_2 = 19
  rnd_2 = random.randint(0, last_2)

  print(quotes[rnd_1].strip('\n'))
  print(quotes[rnd_2])

if __name__== "__main__":
  main()
