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

maze = [[0 for i in range(25)] for j in range(25)]
maze_gen.generate_maze(maze)
print(find_direction(maze))

root = p.display.set_mode((650,650))
root.fill((0,0,0))

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
			maze = [[0 for i in range(25)] for j in range(25)]
			maze_gen.generate_maze(maze)
			visited_cells = []
			root.fill((0,0,0))
			p.display.update()
			#continue
			#quit()
		else :
			maze[player_pos[0]][player_pos[1]-1] = 2
			maze[player_pos[0]][player_pos[1]] = 1
	if direction == "right" :
		if maze[player_pos[0]][player_pos[1]+1] == 3 :
			print("ended with : "+str(len(visited_cells))+" steps")
			del maze
			del player_pos
			del visited_cells
			maze = [[0 for i in range(25)] for j in range(25)]
			maze_gen.generate_maze(maze)
			visited_cells = []
			root.fill((0,0,0))
			p.display.update()
			#continue
		else :
			maze[player_pos[0]][player_pos[1]+1] = 2
			maze[player_pos[0]][player_pos[1]] = 1
	if direction == "up" :
		if maze[player_pos[0]-1][player_pos[1]] == 3 :
			print("ended with : "+str(len(visited_cells))+" steps")
			del maze
			del player_pos
			del visited_cells
			maze = [[0 for i in range(25)] for j in range(25)]
			maze_gen.generate_maze(maze)
			visited_cells = []
			root.fill((0,0,0))
			p.display.update()
			#continue
		else :
			maze[player_pos[0]-1][player_pos[1]] = 2
			maze[player_pos[0]][player_pos[1]] = 1
	if direction == "down" :
		if maze[player_pos[0]+1][player_pos[1]] == 3 :
			print("ended with : "+str(len(visited_cells))+" steps")
			del maze
			del player_pos
			del visited_cells
			maze = [[0 for i in range(25)] for j in range(25)]
			maze_gen.generate_maze(maze)
			visited_cells = []
			root.fill((0,0,0))
			p.display.update()
			#continue
		else :
			maze[player_pos[0]+1][player_pos[1]] = 2
			maze[player_pos[0]][player_pos[1]] = 1

	#if find_player(maze) not in visited_cells :
	visited_cells.append(find_player(maze))
	y_pos = 0
	for line in maze :
		x_pos = 0
		for cell in line :
			if cell == 1 :
				p.draw.rect(root, (255,255,255), (x_pos,y_pos,25,25))
			if cell == 2 :
				p.draw.rect(root, (0,150,0), (x_pos,y_pos,25,25))
			if cell == 3 :
				p.draw.rect(root, (150,0,0), (x_pos,y_pos,25,25))
			x_pos += 25
		y_pos += 25
	for i in p.event.get():
		if i.type==	p.QUIT:
			quit()
	p.display.update()
	sleep(0.5)
	#root.fill((0,0,0))