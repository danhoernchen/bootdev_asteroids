import pygame
from player import Player
from asteroidfield import AsteroidField
from asteroid import Asteroid
from constants import *

pygame_clock = pygame.time.Clock()
dt = 0

def main():
	pygame.init()
	print("Starting asteroids!")
	print(f"Screen width: {SCREEN_WIDTH}")
	print(f"Screen height: {SCREEN_HEIGHT}")
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	asteroids = pygame.sprite.Group()
	Player.containers = (updatable, drawable)
	Asteroid.containers = (updatable, drawable, asteroids)
	AsteroidField.containers = (updatable)
	player = Player((SCREEN_WIDTH/2),(SCREEN_HEIGHT/2))
	asteroid_field = AsteroidField()
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
		dt = (pygame_clock.tick(60)/1000)
		for current_updatable in updatable:
			current_updatable.update(dt)
		screen.fill((0,0,0))
		for current_drawable in drawable:
			current_drawable.draw(screen)
		pygame.display.flip()


if __name__ == "__main__":
	main()