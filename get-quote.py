import random
def main():
  #print("Keep it logically awesome.")

  a = open("quotes.txt", "a")
  a.write("Now the file has more content!")
  a.close()

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()

  last_1 = 20
  rnd_1 = random.randint(0, last_1)

  last_2 = 20
  rnd_2 = random.randint(0, last_2)

  print(quotes[rnd_1].strip('\n'))
  print(quotes[rnd_2])

if __name__== "__main__":
  main()
