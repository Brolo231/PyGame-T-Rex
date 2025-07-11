import random
from random import randint
from utils import draw_text
from settings import *
import settings

class Environment:
    def __init__(self):
        self.floor = pygame.Rect(0, FLOOR + PLAYER_SIZE, SCREEN_WIDTH, 1)
        self.object_speed = 5
        self.objects = []


    def update(self, **kwargs):

        if 3 < settings.counter < 10:
            self.object_speed = 6
        elif 9 < settings.counter < 20:
            self.object_speed = 8
        elif 19 < settings.counter < 30:
            self.object_speed = 11
        elif settings.counter >= 30:
            self.object_speed = 14

        # Move objects and remove those off-screen
        for object in self.objects:
            object.x -= self.object_speed

        # Remove objects after loop
        for object in self.objects:
            if object.x < -100:
                self.objects.pop(0)
                settings.counter += 1

        # Add tree if fewer than 2 exist
        if len(self.objects) < 3:
            last_object_x = self.objects[-1].x if self.objects else 0
            new_x = max(SCREEN_WIDTH, last_object_x + 350 + random.randint(0, 800))
            random_choice = random.randint(1,2)
            if random_choice == 1:
                new_tree = pygame.Rect(new_x, FLOOR + PLAYER_SIZE - TREE_HEIGHT, TREE_WIDTH, TREE_HEIGHT)
                self.objects.append(new_tree)
            else:
                new_bird = pygame.Rect(new_x, FLOOR, BIRD_WIDTH, BIRD_HEIGHT)
                self.objects.append(new_bird)

    def handle_events(self, **kwargs):
        pass

    def draw(self, surface):
        pygame.draw.rect(surface, WHITE, self.floor)

        for object in self.objects:
            pygame.draw.rect(surface, WHITE, object)

        draw_text(surface, f"{settings.counter}", 15, WHITE, (50,50), True, None)




