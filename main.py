from environment import Environment
from settings import *
import settings
from player import Player
from menu import Menu

class Game:
    def __init__(self):
        # Initialize and setup main game window
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.DOUBLEBUF | pygame.HWSURFACE)
        pygame.display.set_caption("B-rex")
        self.clock = pygame.time.Clock()
        self.running = True

        # Call and store objects
        self.menu = Menu(self.screen)
        self.environment = Environment()
        self.player = Player()
        # storing objects will make iterating over them in the following methods quicker
        self.entities = [self.player, self.environment]


    def update(self):
        # Iterate through, and run, each object's methods
        for entity in self.entities:
            entity.update(objects=self.environment.objects)

    def handle_events(self):
        # Handle pygame events (Singular event)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                settings.game_state = "stop"

            for entity in self.entities:
                entity.handle_events(event=event)


    def draw(self):
        # Display/draw window, screen and entities
        self.screen.fill((GREY))

        for entity in self.entities:
            entity.draw(self.screen)

        # Update each frame from each iteration of main game loop
        pygame.display.flip()
        # Set FPS to 60 / restrict main game loop to have 60 iterations p/s
        self.clock.tick(60)

    def reset(self):
        self.environment = Environment()
        self.player = Player()
        self.entities = [self.player, self.environment]


    def run(self):
        # Always run the game window unless exited
        while self.running:
            # Switching between two game states
            while settings.game_state == "menu":
                self.menu.draw()
                self.menu.handle_events()
                if settings.restart:
                    self.reset()
                    settings.restart = False

            while settings.game_state == "running":
                self.handle_events()
                self.update()
                self.draw()


if __name__ == "__main__":
    game = Game()
    game.run()