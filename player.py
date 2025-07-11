# Player
import pygame.draw
import settings
from settings import *

class Player:
    def __init__(self):
        self.player = pygame.Rect(PLAYER_X_CORD, FLOOR, PLAYER_SIZE, PLAYER_SIZE)
        self.is_jumping = False
        self.is_falling = False
        self.slow_down = False
        self.gravity = 0.5
        self.velocity = 0.40
        self.health = 3
        self.mouse_pos = None

    def update(self, objects, **kwargs):

        # change game speed based on progress
        if 3 < settings.counter < 10:
            self.velocity = 0.60
        elif 9 < settings.counter < 20:
            self.velocity = 0.80
        elif 19 < settings.counter < 30:
            self.velocity = 1
        elif settings.counter >= 30:
            self.velocity = 1.5

        keys = pygame.key.get_pressed()

        if keys[pygame.K_DOWN] and self.player.y >= FLOOR:
            if self.player.height != PLAYER_SIZE // 2:
                # Shrink player
                self.player.y += PLAYER_SIZE // 2
                self.player.height = PLAYER_SIZE // 2
        else:
            if self.player.height != PLAYER_SIZE:
                # Grow back to full height
                self.player.y -= PLAYER_SIZE // 2
                self.player.height = PLAYER_SIZE

        self.mouse_pos = pygame.mouse.get_pos()
        if self.mouse_pos[1] < SCREEN_HEIGHT //2 and pygame.mouse.get_pressed()[0] and self.player.y == FLOOR:
            if self.player.height != PLAYER_SIZE // 2:
                # shrink player
                self.player.y += PLAYER_SIZE // 2
                self.player.height = PLAYER_SIZE // 2

        # Reduce player health when colliding with objects
        for object in objects:
            if self.player.colliderect(object):
                self.health -= 1
                objects.pop(0)

        # Change game state to the menu state when player health reaches 0
        if self.health <= 0:
            settings.game_state = "menu"
            settings.restart = True
            if settings.high_score < settings.counter:
                settings.high_score = settings.counter
            settings.counter = 0

        # Beginning of Jump (momentum)
        if self.is_jumping:
            self.player.y -= self.gravity
            self.gravity += self.velocity

        if self.is_jumping and self.player.y <= FLOOR - SLOW_DOWN_HEIGHT:
            self.is_jumping = False
            self.slow_down = True

        # Ending of jump (slowing down)

        if self.slow_down:
            if self.gravity >= 0.5:
                self.player.y -= self.gravity
                self.gravity -= self.velocity
            else:
                self.slow_down = False
                self.is_falling = True

        if self.slow_down and self.player.y <= FLOOR - JUMP_HEIGHT:
            self.gravity = 0.5
            self.is_jumping = False
            self.slow_down = False
            self.is_falling = True


            # Falling
        if self.is_falling:
            self.player.y += self.gravity
            self.gravity += self.velocity

        if self.is_falling and self.player.y >= FLOOR:
            self.player.y = FLOOR
            self.gravity = 0.5
            self.is_jumping = False
            self.is_falling = False


    def handle_events(self, event):


        if event.type == pygame.KEYDOWN:
            if pygame.mouse.get_pressed():
                self.mouse_pos = pygame.mouse.get_pos()

            if (event.key == pygame.K_SPACE and
                    self.player.height == PLAYER_SIZE and
                    not self.is_jumping and
                    not self.is_falling and
                    not self.slow_down):
                self.is_jumping = True

        if (event.type == pygame.MOUSEBUTTONDOWN and
                event.button == 1 and
                pygame.mouse.get_pos()[1] > SCREEN_HEIGHT // 2 and
                self.player.height == PLAYER_SIZE and
                not self.is_jumping and
                not self.is_falling and
                not self.slow_down):
            self.is_jumping = True

    def draw(self, surface):
        pygame.draw.rect(surface, WHITE, self.player)

        for num in range(self.health):
            pygame.draw.circle(surface, WHITE, ((SCREEN_WIDTH - 100) - 50 * num, 50), 15, 1)