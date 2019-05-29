#!/usr/bin/python

import sys

def rock_paper_scissors(n):
  results = []
  possibilities = ["rock", "paper", "scissors"]

  def play(playedSoFar, rounds):
      if rounds == 0:
          return results.append(playedSoFar)
      for i in range(0, 3):
          play(playedSoFar+[possibilities[i]], rounds - 1)
  play([], n)
  return results
if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')
