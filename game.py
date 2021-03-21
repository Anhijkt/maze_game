import maze_gen
import pygame as p
import role_game
from time import sleep
from random import choice

maze_x = 20
maze_y = 18
maze = [[0 for i in range(maze_x)] for j in range(maze_y)]
maze_gen.generate_maze(maze)

root = p.display.set_mode((1000,800))

solver = maze_gen.maze_solver()
hero = role_game.player()
p.font.init()
f1 = p.font.Font(None, 30)

while True :
	n = solver.solve(maze)
	if n :
		if n[0] == "end" :
			maze = [[0 for i in range(maze_x)] for j in range(maze_y)]
			maze_gen.generate_maze(maze)
		if n[0] == "fight":
			res = hero.fight(n[1]-3, root)
			if res == "win" :
				hero_pos = maze_gen.find_player(maze)
				if n[2] == "left" :
					maze[hero_pos[0]][hero_pos[1]-1] = 1
				if n[2] == "right" :
					maze[hero_pos[0]][hero_pos[1]+1] = 1
				if n[2] == "up" :
					maze[hero_pos[0]-1][hero_pos[1]] = 1
				if n[2] == "down" :
					maze[hero_pos[0]+1][hero_pos[1]] = 1	
			if res == "dead" :
				print("you dead")
				break
		if n[0] == "heal" :
			hero.heal()
			hero_pos = maze_gen.find_player(maze)
			if n[1] == "left" :
				maze[hero_pos[0]][hero_pos[1]-1] = 1
			if n[1] == "right" :
				maze[hero_pos[0]][hero_pos[1]+1] = 1
			if n[1] == "up" :
				maze[hero_pos[0]-1][hero_pos[1]] = 1
			if n[1] == "down" :
				maze[hero_pos[0]+1][hero_pos[1]] = 1
		if n[0] == "poison" :
			res = hero.poison()
			hero_pos = maze_gen.find_player(maze)
			if res == "dead" :
				print("you dead")
				break
			else :
				if n[1] == "left" :
					maze[hero_pos[0]][hero_pos[1]-1] = 1
				if n[1] == "right" :
					maze[hero_pos[0]][hero_pos[1]+1] = 1
				if n[1] == "up" :
					maze[hero_pos[0]-1][hero_pos[1]] = 1
				if n[1] == "down" :
					maze[hero_pos[0]+1][hero_pos[1]] = 1
	root.fill((0,0,0))
	player_hp_text = f1.render("Player hp:  {}".format(str(hero.hp)), True, (255, 255, 255))
	player_max_hp_text = f1.render("Player max-hp:  {}".format(str(hero.max_hp)), True, (255, 255, 255))
	player_attack_text = f1.render("Player attack:  {}".format(str(hero.attack)), True, (255, 255, 255))
	player_deffense_text = f1.render("Player deffense:  {}".format(str(hero.deffense)), True, (255, 255, 255))
	root.blit(player_hp_text, (800, 40))
	root.blit(player_max_hp_text, (800, 80))
	root.blit(player_attack_text, (800, 120))
	root.blit(player_deffense_text, (800, 160))
	y_pos = 0
	for line in maze :
		x_pos = 0
		for cell in line :
			if cell == 1 :
				img = p.image.load('res/dungeon/floor.png')
				img = p.transform.scale(img, (35,35))
				root.blit(img, (x_pos, y_pos))
			elif cell == 2 :
				img = p.image.load('res/dungeon/player.png')
				img = p.transform.scale(img, (35,35))
				root.blit(img, (x_pos, y_pos))
			elif cell == 3 :
				img = p.image.load('res/dungeon/end.png')
				img = p.transform.scale(img, (35,35))
				root.blit(img, (x_pos, y_pos))
			elif cell == 4 :
				img = p.image.load('res/monsters/devil.png')
				img = p.transform.scale(img, (35,35))
				root.blit(img, (x_pos, y_pos))
			elif cell == 5 :
				img = p.image.load('res/monsters/eye.png')
				img = p.transform.scale(img, (35,35))
				root.blit(img, (x_pos, y_pos))
			elif cell == 6 :
				img = p.image.load('res/monsters/ghost.png')
				img = p.transform.scale(img, (35,35))
				root.blit(img, (x_pos, y_pos))
			elif cell == 7 :
				img = p.image.load('res/monsters/plague_doctor.png')
				img = p.transform.scale(img, (35,35))
				root.blit(img, (x_pos, y_pos))
			elif cell == 8 :
				img = p.image.load('res/monsters/skeleton.png')
				img = p.transform.scale(img, (35,35))
				root.blit(img, (x_pos, y_pos))
			elif cell == 9 :
				img = p.image.load('res/monsters/water_ghoul.png')
				img = p.transform.scale(img, (35,35))
				root.blit(img, (x_pos, y_pos))
			elif cell == 10 :
				img = p.image.load('res/potions/heal_potion.png')
				img = p.transform.scale(img, (35,35))
				root.blit(img, (x_pos, y_pos))
			elif cell == 11 :
				img = p.image.load('res/potions/poison.png')
				img = p.transform.scale(img, (35,35))
				root.blit(img, (x_pos, y_pos))
			else :
				img = p.image.load('res/dungeon/wall.png')
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