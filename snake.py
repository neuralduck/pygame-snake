import pygame as pg 
from enum import Enum
import random
import math
class Direction(Enum):
	#to get the direction to draw the snake's body
	up = (0, -1)
	down = (0, 1)
	left = (-1, 0)
	right = (1, 0)

class Snake:
	def __init__(self):
		self.width = 800
		self.height = 600
		self.running = True

		pg.init()
		pg.display.set_caption('Snake')
		self.screen = pg.display.set_mode((self.width, self.height))
		self.fps = 30
		self.timer = pg.time.Clock()

		self.x = 100
		self.y = 100
		self.food = [random.choice(list(range(self.width))), random.choice(list(range(self.height)))]
		self.direction = Direction.right
		#self.snake_body = [[50, 50], [49, 50], [48, 50], [47, 50]]
		#self.snake_body = [[i, self.y] for i in list(range(self.x+1))[::-1]]
		self.snake_body = [[self.x-i, self.y] for i in list(range(10))[::-1]]
	def play(self):
		while self.running:
			self.timer.tick(self.fps)
			self.screen.fill((66, 187, 250, 0.8))
			if(math.sqrt((self.food[0] - self.x)**2 + (self.food[1] - self.y)**2) < 20):
				self.snake_body.append(self.snake_body[-1])
				self.food = [random.choice(list(range(self.width))), random.choice(list(range(self.height)))]
			pg.draw.circle(self.screen, 'red', self.food, 10)
			pg.draw.circle(self.screen, (185, 143, 9, 0.8), (self.x, self.y), 10)
			for i, segment in enumerate(self.snake_body):
				pg.draw.circle(self.screen, (216, 206, 80, 0.8), segment, 10)
			self.snake_body.pop()
			self.snake_body.insert(0, [self.x, self.y])
			self.x += self.direction.value[0]*10
			self.y += self.direction.value[1]*10
			self.x = self.x%self.width
			self.y = self.y%self.height
			for event in pg.event.get():
				if event.type == pg.QUIT:
					self.running = False
				if event.type == pg.KEYDOWN:
					if event.key == pg.K_UP:
						if self.direction != Direction.down:
							self.direction = Direction.up
					if event.key == pg.K_DOWN:
						if self.direction != Direction.up:
							self.direction = Direction.down
					if event.key == pg.K_LEFT:
						if self.direction != Direction.right:
							self.direction = Direction.left
					if event.key == pg.K_RIGHT:
						if self.direction != Direction.left:
							self.direction = Direction.right
					if event.key == pg.K_w:
						if self.direction != Direction.down:
							self.direction = Direction.up
					if event.key == pg.K_s:
						if self.direction != Direction.up:
							self.direction = Direction.down
					if event.key == pg.K_a:
						if self.direction != Direction.right:
							self.direction = Direction.left
					if event.key == pg.K_d:
						if self.direction != Direction.left:
							self.direction = Direction.right

			pg.display.update()
		pg.quit()
if __name__ == '__main__':
	s = Snake()
	s.play()


