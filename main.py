#!/usr/bin/env python
# -*- coding: utf-8 -*-

def take_turn():
	while True:
		yield 'X'
		yield 'Y'

def parse_input(input):
	row = input[0]
	col = input[1]
	return row, col

class Board:
	dimension = 3
	cells = {}

	def _init__(self):
		for i in range(self.dimension):
			for j in range(self.dimension):
				self.cells[i][j] = None

	def place_cell(self, x, y, player):
		self.cells[(x, y)] = player
		print(f"{x}, {y}: {player}")

	def winner(self, player):
		for row in range(self.dimension):
			for col in range(self.dimension):
				if all([row[x][y] == player for x in row for y in col]):
					return True
		for col in range(self.dimension):
			for row in range(self.dimension):
				if all([row[x][y] == player for x in row for y in col]):
					return True
		if all([self.cells[x][x] == player for x in range(self.dimension)]):
			return True
		if all([self.cells[x][self.dimension - x] == player for x in range(self.dimension)]):
			return True
		return False



if __name__ == "__main__":
	board = Board()
	winner = False
	while not winner:
		player = next(take_turn())
		my_input = input("XY:")
		x, y = parse_input(my_input)

		board.place_cell(x, y, player)
		winner = board.winner(player)
	print(f"Winner: {player}")
