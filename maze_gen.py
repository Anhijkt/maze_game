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

	for i in range(1,random.randint(10,20)) : #enemy generation
		cell = [random.randint(2,len(maze)-1),random.randint(2,len(maze)-1)]
		while maze[cell[0]][cell[1]] == 0 :
			cell = [random.randint(2,len(maze)-1),random.randint(2,len(maze)-1)]
		maze[cell[0]][cell[1]] = random.randint(4,9)
	
	for i in range(1,random.randint(5,15)) : #generating potions
		cell = [random.randint(2,len(maze)-1),random.randint(2,len(maze)-1)]
		while maze[cell[0]][cell[1]] == 0 :
			cell = [random.randint(2,len(maze)-1),random.randint(2,len(maze)-1)]
		maze[cell[0]][cell[1]] = random.randint(10,11)

	in_cell = [random.randint(2,len(maze)-1),random.randint(2,len(maze)-1)] #in and out of the dungeon
	out_cell = [random.randint(2,len(maze)-1),random.randint(2,len(maze)-1)]
	while maze[in_cell[0]][in_cell[1]] == 0 :
		in_cell = [random.randint(2,len(maze)-1),random.randint(2,len(maze)-1)]
	while maze[out_cell[0]][out_cell[1]] == 0 :
		out_cell = [random.randint(2,len(maze)-1),random.randint(2,len(maze)-1)]
	maze[in_cell[0]][in_cell[1]] = 2
	maze[out_cell[0]][out_cell[1]] = 3

def find_player(maze) :
	for line in maze :
		for cell in line :
			if cell == 2 :
					return [maze.index(line), line.index(cell)]

def find_direction(maze) :
	player_pos = find_player(maze)
	directions = []
	if player_pos[0] > 0 :
		if maze[player_pos[0]-1][player_pos[1]] :
			directions.append("up")
	if player_pos[0] < len(maze)-1 :
		if maze[player_pos[0]+1][player_pos[1]] :
			directions.append("down")
	if player_pos[1] > 0 :
		if maze[player_pos[0]][player_pos[1]-1] :
			directions.append("left")
	if player_pos[1] < len(maze[0])-1 :
		if maze[player_pos[0]][player_pos[1]+1] :
			directions.append("right")
	return directions

class maze_solver :
	def __init__(self) :
		self.visited_cells = []
		self.n = 0
	def solve(self, maze) :
		player_pos = find_player(maze)
		possible_directions = find_direction(maze)
		if "left" in possible_directions :
			if [player_pos[0], player_pos[1]-1] in self.visited_cells :
				possible_directions.remove("left")
		if "right" in possible_directions :
			if [player_pos[0], player_pos[1]+1] in self.visited_cells :
				possible_directions.remove("right")
		if "up" in possible_directions :
			if [player_pos[0]-1, player_pos[1]] in self.visited_cells :
				possible_directions.remove("up")
		if "down" in possible_directions :
			if [player_pos[0]+1, player_pos[1]] in self.visited_cells :
				possible_directions.remove("down")

		if possible_directions : 
			direction = random.choice(possible_directions)
			self.n = len(self.visited_cells)-1
		else :
			#print("dead end")
			maze[player_pos[0]][player_pos[1]] = 1
			player_pos = self.visited_cells[self.n].copy()
			maze[player_pos[0]][player_pos[1]] = 2
			direction = ""
			self.n -= 1
			#player_pos = forks.pop().copy()
			#visited_cells.remove(player_pos)
		if direction == "left" :
			if maze[player_pos[0]][player_pos[1]-1] == 3 :
				print("ended with : "+str(len(self.visited_cells))+" steps")
				del maze
				del player_pos
				del self.visited_cells
				self.visited_cells = []
				return ["end"]
			elif maze[player_pos[0]][player_pos[1]-1] >= 4 and maze[player_pos[0]][player_pos[1]-1] <= 9:
				return ["fight", maze[player_pos[0]][player_pos[1]-1], "left"]
			elif maze[player_pos[0]][player_pos[1]-1] == 10 :
				return ["heal", "left"]
			elif maze[player_pos[0]][player_pos[1]-1] == 11 :
				return ["poison", "left"]
			else :
				maze[player_pos[0]][player_pos[1]-1] = 2
				maze[player_pos[0]][player_pos[1]] = 1
		if direction == "right" :
			if maze[player_pos[0]][player_pos[1]+1] == 3 :
				print("ended with : "+str(len(self.visited_cells))+" steps")
				del maze
				del player_pos
				del self.visited_cells
				self.visited_cells = []
				return ["end"]
			elif maze[player_pos[0]][player_pos[1]+1] >= 4 and maze[player_pos[0]][player_pos[1]+1] <= 9:
				return ["fight", maze[player_pos[0]][player_pos[1]+1], "right"]
			elif maze[player_pos[0]][player_pos[1]+1] == 10 :
				return ["heal", "right"]
			elif maze[player_pos[0]][player_pos[1]+1] == 11 :
				return ["poison", "right"]
			else :
				maze[player_pos[0]][player_pos[1]+1] = 2
				maze[player_pos[0]][player_pos[1]] = 1
		if direction == "up" :
			if maze[player_pos[0]-1][player_pos[1]] == 3 :
				print("ended with : "+str(len(self.visited_cells))+" steps")
				del maze
				del player_pos
				del self.visited_cells
				self.visited_cells = []
				return ["end"]
			elif maze[player_pos[0]-1][player_pos[1]] >= 4 and maze[player_pos[0]-1][player_pos[1]] <= 9:
				return ["fight", maze[player_pos[0]-1][player_pos[1]], "up"]
			elif maze[player_pos[0]-1][player_pos[1]] == 10 :
				return ["heal", "up"]
			elif maze[player_pos[0]-1][player_pos[1]] == 11 :
				return ["poison", "up"]
			else :
				maze[player_pos[0]-1][player_pos[1]] = 2
				maze[player_pos[0]][player_pos[1]] = 1
		if direction == "down" :
			if maze[player_pos[0]+1][player_pos[1]] == 3 :
				print("ended with : "+str(len(self.visited_cells))+" steps")
				del maze
				del player_pos
				del self.visited_cells
				self.visited_cells = []
				return ["end"]
			elif maze[player_pos[0]+1][player_pos[1]] >= 4 and maze[player_pos[0]+1][player_pos[1]] <= 9 :
				return ["fight", maze[player_pos[0]+1][player_pos[1]], "down"]
			elif maze[player_pos[0]+1][player_pos[1]] == 10 :
				return ["heal", "down"]
			elif maze[player_pos[0]+1][player_pos[1]] == 11 :
				return ["poison", "down"]
			else :
				maze[player_pos[0]+1][player_pos[1]] = 2
				maze[player_pos[0]][player_pos[1]] = 1

		#if find_player(maze) not in visited_cells :
		self.visited_cells.append(find_player(maze))
