screen_width = 50 # The amount of characters accross the screen
screen_height = 25
background_char = "." # Character to use when printing the background
vertex_char = "V" # Character to use when printing a vertex
canvas_char = "#" # Character to use for the edges of the canvas

def clearCanvas():
    for i in range(0, screen_width):
        print(canvas_char, end="")

    print() # Print a new line

    for i in range(0, screen_height):
        for i in range(0, screen_width):
            print(".", end="")

        print() # Print a new line

    for i in range(0, screen_width):
        print(canvas_char, end="")

    print() # Print a new line

class vertex:
    def __init__(self, xCoord, yCoord, zCoord):
        self.xCoord = xCoord;
        self.yCoord = yCoord;
        self.zCoord = zCoord;

    def displayVertices(self):
        for i in range(0, screen_height):
            if i != self.yCoord:
                for c in range(0, screen_width):
                    print(background_char, end="")

            else:
                for x in range(0, screen_width):
                    if x != self.xCoord:
                        print(background_char, end="")

                    else:
                        print(vertex_char, end="")

            print() # Print a new line

class edge:
    def __init__(self, vertex1, vertex2):
        self.vertex1 = vertex1;
        self.vertex2 = vertex2;

clearCanvas()

vert1 = vertex(20, 3, 15)
vert1.displayVertices()