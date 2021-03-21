import random
from time import sleep

monsters = {1: {"name": "devil",
				"file": "/res/monsters/devil.png",
				"hp": 100,
				"attack": 15,
				"deffense": 30},
			2: {"name": "eye",
				"file": "/res/monsters/eye.png",
				"hp": 50,
				"attack": 10,
				"deffense": 25},
			3: {"name": "ghost",
				"file": "/res/monsters/ghost.png",
				"hp": 25,
				"attack": 10,
				"deffense": 10},
			4: {"name": "plague doctor",
				"file": "/res/monsters/plague_doctor.png",
				"hp": 50,
				"attack": 10,
				"deffense": 15},
			5: {"name": "skeleton",
				"file": "/res/monsters/skeleton.png",
				"hp": 25,
				"attack": 10,
				"deffense": 10},
			6: {"name": "water ghoul",
				"file": "/res/monsters/water_ghoul.png",
				"hp": 50,
				"attack": 10,
				"deffense": 25}}

class player():
	def __init__(self) :
		self.hp = 100
		self.max_hp = 100
		self.attack = 25
		self.deffense = 10
	def fight(self, monster_id, root) :
		monster_hp = monsters[monster_id]["hp"]
		turn = random.choice(["player","monster"])
		print("fight with: {}".format(monsters[monster_id]["name"]))
		while True :
			print("{} turn".format(turn))
			sleep(0.5)
			if self.hp <= 0 :
				return "dead"
			if monster_hp <= 0 :
				return "win"
			if turn == "player" :
				hit = round(self.attack*(monsters[monster_id]["deffense"]/100))
				monster_hp -= hit
				print("player hit with: {} points".format(hit))
				turn = "monster"
				continue
			if turn == "monster" :
				hit = round(monsters[monster_id]["attack"]*(self.deffense/100))
				self.hp -= hit
				print("monster hit with: {} points".format(hit))
				turn = "player"
				continue
	def heal(self) :
		if self.hp + 25 > self.max_hp :
			self.hp = self.max_hp
		else :
			self.hp += 25
	def poison(self) :
		if self.hp - 25 <= 0 :
			return "dead"
		else :
			self.hp -= 25
			return ""