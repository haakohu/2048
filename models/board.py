import sys
sys.path.append('utils')
from tile import Tile
from random import choice
from BoardUtils import get_new_tiles, randomize_tiles

class Board:

  def __init__(self, board_size):
    self.board_size = board_size
    self.score = 0
    self.tiles = get_new_tiles(board_size)
    randomize_tiles(self.tiles,2)
    self.moves = 0

  def __str__(self):
    res = ""
    for tiles in self.tiles:
      for tile in tiles:
        res += str(tile) + " "
      res += "\n"
    return res



  def update_left(self):
    self.moves += 1
    any_changed = False
    for row_i in range(len(self.tiles)):
      row = self.tiles[row_i]
      new_row, changed = self.match(row)
      any_changed = changed or any_changed
      self.tiles[row_i] = new_row

    if any_changed:
      self.spawn_random()


  def update_right(self):
    self.moves += 1
    any_changed = False
    for row_i in range(len(self.tiles)):
      row = list(reversed(self.tiles[row_i]))
      new_row, changed = self.match(row)
      any_changed = changed or any_changed
      new_row.reverse()
      self.tiles[row_i] = new_row
    if any_changed:
      self.spawn_random()

  def update_down(self):
    self.moves += 1
    any_changed = False
    for column_i in range(self.board_size):
      column = list(reversed([row[column_i] for row in self.tiles]))
      new_column, changed = self.match(column)
      any_changed = changed or any_changed
      new_column.reverse()

      for row_i in range(self.board_size):
        self.tiles[row_i][column_i] = new_column[row_i]
    if any_changed:
      self.spawn_random()

  def update_up(self):
    self.moves += 1
    any_changed = False
    for column_i in range(self.board_size):
      column = [row[column_i] for row in self.tiles]
      new_column, changed = self.match(column)
      any_changed = changed or any_changed
      for row_i in range(self.board_size):
        self.tiles[row_i][column_i] = new_column[row_i]
    if any_changed:
      self.spawn_random()


  def spawn_random(self):
    # Get tiles coord that are not taken ( row, column)
    tiles_cords = [(row_i, column_i) for row_i in range(self.board_size) for column_i in range(self.board_size) if self.tiles[row_i][column_i].value == 0]
    print(tiles_cords)
    tile_cord = choice(tiles_cords)
    self.tiles[tile_cord[0]][tile_cord[1]].value = 1

  def match(self, tiles):
    changed = False
    # Remove all 0 tiles
    original_size = len(tiles)
    for i in range(len(tiles)-1):
      tile1 = tiles[i]
      tile2 = tiles[i+1]
      if tile1.value == 0 and tile2.value != 0:
        changed = True

    tiles = [tile for tile in tiles if tile.value != 0]

    #print("tiles to change: \n" + str(tiles))
    for i in range(len(tiles)-1):
      tile1 = tiles[i]
      tile2 = tiles[i+1]
      if tile1 == tile2: # can match
        changed = True
        new_value = tile1.value * 2
        tile1.value = new_value
        self.score += new_value
        del tiles[i+1]
        tiles.append(Tile(0))
    missing_tiles = original_size - len(tiles)
    #print("tiles result: + \n"  + str(tiles))
    return tiles + [Tile(0) for i in range(missing_tiles)], changed








if __name__ == "__main__":
  board = Board(4)
  print(board)
