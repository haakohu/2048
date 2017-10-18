import sys
sys.path.append('models')
from tile import Tile
from random import randint

def get_new_tiles(board_size):
  tiles = []
  for i in range(board_size):
    tiles += [[]]
    for j in range(board_size):
      tiles[i].append(Tile(0))
  return tiles

def randomize_tiles(tiles, amount):
  taken = []
  size = len(tiles) -1
  while len(taken) != amount:
    coordinate = (randint(0,size), randint(0,size))
    if coordinate in taken:
      continue
    tiles[coordinate[0]][coordinate[1]].value = 1
    taken.append(coordinate)

