def f1(a):
  if a < 0:
    return -a
  return a 

def f2(n):
  total = 0
  while n > 0:
    num = int(input("Enter an integer: "))
    total = total + f1(num)
    n = n - 1
  return total

def run():
  n = int(input("Enter an integer: "))
  print(f"answer is {f2(n)}")

if __name__ == "__main__":
  run()
