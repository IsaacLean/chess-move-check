import sys

### Constants ###
BOARD_SIZE = 8
# Used for converting from chess to index format
CHARMAP = {
	'A': 0,
	'B': 1,
	'C': 2,
	'D': 3,
	'E': 4,
	'F': 5,
	'G': 6,
	'H': 7
}
COLORSET = set(['Black', 'White']) # Used for checking if input color is valid
INDEXARR = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'] # Used for converting from index to chess format
NAMEARR = ['Bishop', 'King', 'Knight', 'Pawn', 'Queen', 'Rook'] # Used for checking the appropriate piece name

### Utility Functions ###
# Validates attribute with set. Returns normalized attribute on success.
def validAttr(attr, checkSet):
	normalAttr = attr.lower().capitalize()

	if normalAttr in checkSet:
		return normalAttr

	raise Exception('You input an invalid color or piece name!')

# Converts input position from chess format (ex. B:3) to list index format (ex. 1,2)
def formatIndex(position):
	splitPos = position.split(':')
	charCoord = splitPos[0].capitalize()

	if charCoord not in CHARMAP:
		raise Exception('You input a piece with an invalid X coordinate!')

	if int(splitPos[1]) < 1 or int(splitPos[1]) > BOARD_SIZE:
		raise Exception('You input a piece with an invalid Y coordinate!')

	return {'x': CHARMAP[charCoord], 'y': int(splitPos[1]) - 1}

# Converts input position from list index format (ex. 1,2) to chess format (ex. B:3)
def formatChess(position):
	return '<' + INDEXARR[position['x']] + ':' + str(position['y'] + 1) + '>'


### Parent class for all piece types ###
class Piece:
	# Constructor
	def __init__(self, color, name, position):
		self.color = validAttr(color, COLORSET)
		self.name = validAttr(name, NAMEARR)
		self.position = formatIndex(position)

	# Checks if input position (must be in index format) is within the bounds of the board
	def checkBounds(self, position):
		if position['x'] < 0 or position['x'] >= BOARD_SIZE or position['y'] < 0 or position['y'] >= BOARD_SIZE:
			return False
		return True

	# Implementation for move validation. Changes depending on piece type.
	def calcMoves(self, board):
		raise NotImplementedError

	# Prints out piece info (Color, Name, Position)
	def printPiece(self):
		position = formatChess(self.position)
		print self.color + ', ' + self.name + ', ' + position


### King Class which inherits from Piece ###
class King(Piece):
	# Checks for possible moves for piece. Returns list of possible moves.
	def calcMoves(self, chessboard):
		possibleMoves = [] # List of possible moves to return

		# Makes code below easier to read
		x = self.position['x']
		y = self.position['y']

		# King movement options
		moveOptions = [
			{'x': x, 'y': y + 1}, # Up
			{'x': x + 1, 'y': y + 1}, # Up-right
			{'x': x + 1, 'y': y}, # Right
			{'x': x + 1, 'y': y - 1}, # Bottom-right
			{'x': x, 'y': y - 1}, # Bottom
			{'x': x - 1, 'y': y - 1}, # Bottom-left
			{'x': x - 1, 'y': y}, # Left
			{'x': x - 1, 'y': y + 1}, # Up-left
		]

		# Calculate valid moves
		for option in moveOptions:
			if self.checkBounds(option):
				if chessboard.getPos(option) is None:
					possibleMoves.append(option)
				elif chessboard.getPos(option).color != chessboard.playerColor:
					possibleMoves.append(option)

		return possibleMoves


### Pawn Class which inherits from Piece ###
class Pawn(Piece):
	# Checks for possible moves for piece. Returns list of possible moves.
	def calcMoves(self, playerColor, board):
		print 'hurray'
		print playerColor
		self.printPiece()
		print board


### Rook Class which inherits from Piece ###
class Rook(Piece):
	# Checks for possible moves for piece. Returns list of possible moves.
	def calcMoves(self, playerColor, board):
		print 'hurray'
		print playerColor
		self.printPiece()
		print board


### Bishop Class which inherits from Piece ###
class Bishop(Piece):
	# Checks for possible moves for piece. Returns list of possible moves.
	def calcMoves(self, playerColor, board):
		print 'hurray'
		print playerColor
		self.printPiece()
		print board


### Queen Class which inherits from Piece ###
class Queen(Piece):
	# Checks for possible moves for piece. Returns list of possible moves.
	def calcMoves(self, playerColor, board):
		print 'hurray'
		print playerColor
		self.printPiece()
		print board


### Knight Class which inherits from Piece ###
class Knight(Piece):
	# Checks for possible moves for piece. Returns list of possible moves.
	def calcMoves(self, playerColor, board):
		print 'hurray'
		print playerColor
		self.printPiece()
		print board


### Chessboard Class ###
class Chessboard:
	def __init__(self, playerColor, pieces):
		self.playerColor = playerColor # Current player color to determine who's turn it is
		self.pieces = [] # List of all pieces
		self.board = [] # 2D array representation of board

		# Initialize empty board
		for x in range(BOARD_SIZE):
			self.board.append([])
			for y in range(BOARD_SIZE):
				self.board[x].append(None)

		# Populate pieces list
		for i in range(len(pieces)):
			splitData = pieces[i].split(',')

			if len(splitData) < 3:
				raise Exception('You input an invalid piece!')

			# Create the appropriate piece
			if validAttr(splitData[1], NAMEARR) == NAMEARR[0]:
				newPiece = Bishop(splitData[0], splitData[1], splitData[2])
			elif validAttr(splitData[1], NAMEARR) == NAMEARR[1]:
				newPiece = King(splitData[0], splitData[1], splitData[2])
			elif validAttr(splitData[1], NAMEARR) == NAMEARR[2]:
				newPiece = Knight(splitData[0], splitData[1], splitData[2])
			elif validAttr(splitData[1], NAMEARR) == NAMEARR[3]:
				newPiece = Pawn(splitData[0], splitData[1], splitData[2])
			elif validAttr(splitData[1], NAMEARR) == NAMEARR[4]:
				newPiece = Queen(splitData[0], splitData[1], splitData[2])
			elif validAttr(splitData[1], NAMEARR) == NAMEARR[5]:
				newPiece = Rook(splitData[0], splitData[1], splitData[2])
			
			self.board[newPiece.position['x']][newPiece.position['y']] = newPiece
			self.pieces.append(newPiece)

	def printLegalMoves(self):
		moveCount = 0

		if self.pieces[0].color == self.playerColor:
			#iterate through each piece and do the following
			
			currName = self.pieces[0].name
			currPos = self.pieces[0].position
			possibleMoves = self.pieces[0].calcMoves(self)
			
			for possibleMove in possibleMoves:
				print currName + ' at ' + formatChess(currPos) + ' can move to ' + formatChess(possibleMove)
				moveCount += 1

		print str(moveCount) + ' legal moves (' + str(len(self.pieces)) + ' unique pieces) for ' + self.playerColor.lower() + ' player'

	# Show what is at position (x,y) on the board
	def getPos(self, position):
		if self.board[position['x']][position['y']] is None:
			return None
		return self.board[position['x']][position['y']]

	# Print chessboard data
	def printData(self):
		print 'Current Player Turn: ' + self.playerColor.capitalize()
		print 'Pieces: ' + str(self.pieces)
		print 'Board: ' + str(self.board)


### main() ###
# File I/O
#print sys.argv
inputFile = open(sys.argv[1])
fileBreakdown = inputFile.read().splitlines()
inputFile.close()

chessboard = Chessboard(validAttr(fileBreakdown[0], COLORSET), fileBreakdown[1:])
chessboard.printLegalMoves()
