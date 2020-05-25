# Main classes:
class scene:
	def __init__(self, canvWidth, canvHeight):
		self.canvWidth = canvWidth
		self.canvHeight = canvHeight
		self.canvas = []

	# Create the array for the canvas
	def resetCanvas(self):
		self.canvas = []
		for y in range(0, self.canvHeight):
			currentLine = []
			for x in range(0, self.canvWidth):
				currentLine.append("`") # "`" is the background character

			self.canvas.append(currentLine)

	def printCanvas(self):
		# Actually display (print) the canvas
		for i in range(0, len(self.canvas)):
			for y in range(0, len(self.canvas[i])):
				print(self.canvas[i][y], end="")
					
			print()

	def addVertex(self, vertX, vertY):
		self.canvas[vertY][vertX] = "#" # "/" is the character representing a vertex

# The rest if the code just makes use of the classes
mainScene = scene(30, 15)
mainScene.resetCanvas()
mainScene.addVertex(3, 2)
mainScene.addVertex(5, 9)
mainScene.printCanvas()
