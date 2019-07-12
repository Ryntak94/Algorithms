#!/usr/bin/python

import sys

def making_change(amount, denominations):
  if amount == 0:
      return 1
  elif amount < 0:
      return 0
  else:
      res = 0
      for i in range(0, len(denominations)):
          change = making_change(amount-denominations[len(denominations)-1-i], denominations[0:len(denominations)-i])
          if change != 0:
              res += change
  return res

if __name__ == "__main__":
  # Test our your implementation from the command line
  # with `python making_change.py [amount]` with different amounts
  if len(sys.argv) > 1:
    denominations = [1, 5, 10, 25, 50]
    amount = int(sys.argv[1])
    print("There are {ways} ways to make {amount} cents.".format(ways=making_change(amount, denominations), amount=amount))
  else:
    print("Usage: making_change.py [amount]")
