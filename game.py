import maze_gen
import pygame as p
from time import sleep
from random import choice

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

maze_x = 18
maze_y = 18
maze = [[0 for i in range(maze_x)] for j in range(maze_y)]
maze_gen.generate_maze(maze)
print(find_direction(maze))

root = p.display.set_mode((800,800))

visited_cells = []

while True :
	player_pos = find_player(maze)
	possible_directions = find_direction(maze)
	if "left" in possible_directions :
		if [player_pos[0], player_pos[1]-1] in visited_cells :
			possible_directions.remove("left")
	if "right" in possible_directions :
		if [player_pos[0], player_pos[1]+1] in visited_cells :
			possible_directions.remove("right")
	if "up" in possible_directions :
		if [player_pos[0]-1, player_pos[1]] in visited_cells :
			possible_directions.remove("up")
	if "down" in possible_directions :
		if [player_pos[0]+1, player_pos[1]] in visited_cells :
			possible_directions.remove("down")

	if possible_directions : 
		direction = choice(possible_directions)
		n = len(visited_cells)-1
	else :
		#print("dead end")
		maze[player_pos[0]][player_pos[1]] = 1
		player_pos = visited_cells[n].copy()
		maze[player_pos[0]][player_pos[1]] = 2
		direction = ""
		n -= 1
		#player_pos = forks.pop().copy()
		#visited_cells.remove(player_pos)
	if direction == "left" :
		if maze[player_pos[0]][player_pos[1]-1] == 3 :
			print("ended with : "+str(len(visited_cells))+" steps")
			del maze
			del player_pos
			del visited_cells
			maze = [[0 for i in range(maze_x)] for j in range(maze_y)]
			maze_gen.generate_maze(maze)
			visited_cells = []
		else :
			maze[player_pos[0]][player_pos[1]-1] = 2
			maze[player_pos[0]][player_pos[1]] = 1
	if direction == "right" :
		if maze[player_pos[0]][player_pos[1]+1] == 3 :
			print("ended with : "+str(len(visited_cells))+" steps")
			del maze
			del player_pos
			del visited_cells
			maze = [[0 for i in range(maze_x)] for j in range(maze_y)]
			maze_gen.generate_maze(maze)
			visited_cells = []
		else :
			maze[player_pos[0]][player_pos[1]+1] = 2
			maze[player_pos[0]][player_pos[1]] = 1
	if direction == "up" :
		if maze[player_pos[0]-1][player_pos[1]] == 3 :
			print("ended with : "+str(len(visited_cells))+" steps")
			del maze
			del player_pos
			del visited_cells
			maze = [[0 for i in range(maze_x)] for j in range(maze_y)]
			maze_gen.generate_maze(maze)
			visited_cells = []
		else :
			maze[player_pos[0]-1][player_pos[1]] = 2
			maze[player_pos[0]][player_pos[1]] = 1
	if direction == "down" :
		if maze[player_pos[0]+1][player_pos[1]] == 3 :
			print("ended with : "+str(len(visited_cells))+" steps")
			del maze
			del player_pos
			del visited_cells
			maze = [[0 for i in range(maze_x)] for j in range(maze_y)]
			maze_gen.generate_maze(maze)
			visited_cells = []
		else :
			maze[player_pos[0]+1][player_pos[1]] = 2
			maze[player_pos[0]][player_pos[1]] = 1

	#if find_player(maze) not in visited_cells :
	visited_cells.append(find_player(maze))

	root.fill((0,0,0))
	y_pos = 0
	for line in maze :
		x_pos = 0
		for cell in line :
			if cell == 1 :
				img = p.image.load('res/floor.png')
				img = p.transform.scale(img, (35,35))
				root.blit(img, (x_pos, y_pos))
			elif cell == 2 :
				img = p.image.load('res/player.png')
				img = p.transform.scale(img, (35,35))
				root.blit(img, (x_pos, y_pos))
			elif cell == 3 :
				img = p.image.load('res/end.png')
				img = p.transform.scale(img, (35,35))
				root.blit(img, (x_pos, y_pos))
			else :
				img = p.image.load('res/wall.png')
				img = p.transform.scale(img, (35,35))
				root.blit(img, (x_pos, y_pos))
			x_pos += 40
		y_pos += 40
	for i in p.event.get():
		if i.type==	p.QUIT:
			quit()
	p.display.update()
	sleep(0.5)
	#root.fill((0,0,0))