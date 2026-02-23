#!/usr/bin/env python
# -*- coding: utf-8 -*-

def take_turn():
	while True:
		yield 'X'
		yield 'Y'

def parse_input(input):
	row = int(input[0])
	col = int(input[1])
	return row, col

class Cell():
	# Yes, can also be done with pydantic or simple dataclasses, which would save us an init.
	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.value = None

	def set_value(self, value):
		# Not gonna bother sanitising input
		self.value = value

	def __repr__(self):
		return f"[{self.x}, {self.y}: {self.value}]"

class Board:
	dimension = 3
	cells = {}
	rows = []
	cols = []
	diagonals = []

	def __init__(self):
		for i in range(self.dimension):
			for j in range(self.dimension):
				self.cells[(i, j)] = Cell(i, j)
		for r in range(self.dimension):
			self.rows.append([self.cells[(r, y)] for y in range(self.dimension)])
		for c in range(self.dimension):
			self.cols.append([self.cells[(x, c)] for x in range(self.dimension)])
		self.diagonals.append([self.cells[(x, x)] for x in range(self.dimension)])
		self.diagonals.append([self.cells[(x, self.dimension - x - 1)] for x in range(self.dimension)])

	def place_cell(self, x, y, player):
		if not self.cells[(x, y)].value:
			self.cells[(x, y)].set_value(player)
			return self.cells[(x, y)]
		else:
			return False
		print(f"{x}, {y}: {player}")

	def winner(self, player):
		for row in self.rows:
			if all([cell.value == player for cell in row]):
				return True
		for col in self.cols:
			if all([cell.value == player for cell in col]):
				return True
		for diagonal in self.diagonals:
			if all([cell.value == player for cell in diagonal]):
				return True
		return False



if __name__ == "__main__":
	board = Board()
	winner = False
	turn = take_turn()
	while not winner:
		player = next(turn)
		my_input = input("XY:")
		x, y = parse_input(my_input)

		cell = board.place_cell(x, y, player)
		while not cell:
			print("Cell already occupied; try again.")
			my_input = input("XY:")
			x, y = parse_input(my_input)
			cell = board.place_cell(x, y, player)
		winner = board.winner(player)
	print(f"Winner: {player}")
