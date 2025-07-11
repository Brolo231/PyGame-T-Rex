# Menu
import sys
import settings
from settings import *
from utils import draw_text

class Menu:
    def __init__(self, surface):
        self.surface = surface
        self.button = pygame.Rect(SCREEN_WIDTH//2 - BUTTON_WIDTH//2, SCREEN_HEIGHT//2 - BUTTON_HEIGHT//2, BUTTON_WIDTH, BUTTON_HEIGHT)

    def update(self, **kwargs):
        pass

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                print(mouse_pos)

                if self.button.collidepoint(mouse_pos):
                    settings.game_state = "running"


    def draw(self):
        self.surface.fill(GREY)
        pygame.draw.rect(self.surface, LIGHT_GREY, (0, SCREEN_HEIGHT//2, SCREEN_WIDTH, SCREEN_HEIGHT//2))
        draw_text(self.surface,
                  "CROUCH",
                  25,
                  WHITE,
                  (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 4),
                  True,
                  None)
        draw_text(self.surface,
                  "JUMP",
                  25,
                  WHITE,
                  (SCREEN_WIDTH // 2, SCREEN_HEIGHT*3/4),
                  True,
                  None)
        pygame.draw.rect(self.surface, BLACK, self.button)
        draw_text(self.surface,
                  "START",
                  32,
                  WHITE,
                  (SCREEN_WIDTH//2, SCREEN_HEIGHT//2),
                  True,
                  None)
        draw_text(self.surface,
                  f"HIGH SCORE: {settings.high_score}",
                  25,
                  WHITE,
                  (SCREEN_WIDTH//2, SCREEN_HEIGHT//2+50),
                  True,
                  None)


        pygame.display.flip()
