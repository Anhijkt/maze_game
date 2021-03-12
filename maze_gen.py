import random

def find_free_neighbours(maze, cell) :
	free_neighbours = ["left","right","up","down"]
	if cell[0] > 1 :
		if maze[cell[0]-2][cell[1]] :
			free_neighbours.remove("up")
	else :
		free_neighbours.remove("up")
	if cell[0] < len(maze)-3 :
		if maze[cell[0]+2][cell[1]] :
			free_neighbours.remove("down")
	else :
		free_neighbours.remove("down")
	if cell[1] > 1 :
		if maze[cell[0]][cell[1]-2] :
			free_neighbours.remove("left")
	else :
		free_neighbours.remove("left")
	if cell[1] < len(maze[0])-3 :
		if maze[cell[0]][cell[1]+2] :
			free_neighbours.remove("right")
	else :
		free_neighbours.remove("right")
	return free_neighbours

#print(find_free_neighbours(maze, [2,29]))
def generate_maze(maze) :
	cell = [random.randint(2, len(maze)-1), random.randint(2, len(maze[0])-1)]
	#started_cell = cell.copy()
	visited_cells = []
	gen = True

	while gen :
		while find_free_neighbours(maze, cell) :
			direction = random.choice(find_free_neighbours(maze, cell))
			if direction == "up" :
				for i in range(2) :
					cell[0] -= 1
					maze[cell[0]][cell[1]] = 1
			if direction == "down" :
				for i in range(2) :
					cell[0] += 1
					maze[cell[0]][cell[1]] = 1
			if direction == "right" :
				for i in range(2) :
					cell[1] += 1
					maze[cell[0]][cell[1]] = 1
			if direction == "left" :
				for i in range(2) :
					cell[1] -= 1
					maze[cell[0]][cell[1]] = 1
			visited_cells.append(cell.copy())
			i = len(visited_cells)-1
		while len(find_free_neighbours(maze, cell)) < 1 :
			i -= 1
			if i < 0 :
				gen = False
				break
			cell = visited_cells[i].copy()			
	in_cell = [random.randint(2,len(maze)-1),random.randint(2,len(maze)-1)]
	out_cell = [random.randint(2,len(maze)-1),random.randint(2,len(maze)-1)]
	while maze[in_cell[0]][in_cell[1]] == 0 :
		in_cell = [random.randint(2,len(maze)-1),random.randint(2,len(maze)-1)]
	while maze[out_cell[0]][out_cell[1]] == 0 :
		out_cell = [random.randint(2,len(maze)-1),random.randint(2,len(maze)-1)]
	maze[in_cell[0]][in_cell[1]] = 2
	maze[out_cell[0]][out_cell[1]] = 3