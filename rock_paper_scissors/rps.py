#!/usr/bin/python

import sys

def rock_paper_scissors(n):
  plays = ['rock', 'paper', 'scissors']
  all_combos = []
  find_combos(n, plays, all_combos)
  return all_combos

def find_combos(n, plays, all_combos, combo=[]):
  # Base case
  if n == 0:
    all_combos.append(combo)
    return
  
  # Recursion: add each option and call again
  for play in plays:
    c = combo.copy()
    c.append(play)
    find_combos(n-1, plays, all_combos, c)


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')