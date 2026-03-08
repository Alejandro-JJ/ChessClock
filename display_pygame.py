import pygame

class PygameDisplay:
    COLORS = {'teal': (0, 153, 153),
              'black': (0, 0, 0),
              'white': (255, 255, 255),
              'sky': (204, 255, 255),
              'grey': {168, 168, 168}}

    WIDTH, HEIGHT = (600, 200)
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("Chess Clock")
        # font for display
        self.font = pygame.font.SysFont(None, 80)
        #self.font = pygame.font.SysFont('tuffy', 72)

    def render_game(self, times: tuple):

        """
        DEPRECATED
        Clears the screen and shows the given label in the center.
        """

        # Fill background (black)
        self.screen.fill(self.COLORS['black'])

        # Render text surface
        text_surface = self.font.render(label, True, self.COLORS['white'])

        # Center text
        text_rect = text_surface.get_rect(center=(self.WIDTH/2, self.HEIGHT/2))

        # Draw text
        self.screen.blit(text_surface, text_rect)

        # Update screen
        pygame.display.flip()


    def render_game_BW(self, times:tuple):
        # Do halfies
        self.screen.fill(self.COLORS['white'], (0,0, self.WIDTH/2, self.HEIGHT))
        self.screen.fill(self.COLORS['black'], (self.WIDTH/2, 0, self.WIDTH/2, self.HEIGHT))

        # Render text surface
        text_surface_P1 = self.font.render(times[0], True, self.COLORS['grey'])
        text_surface_P2 = self.font.render(times[1], True, self.COLORS['grey'])

        # Center text
        text_rect_P1 = text_surface_P1.get_rect(center=(self.WIDTH/4, self.HEIGHT/2))
        text_rect_P2 = text_surface_P2.get_rect(center=(3*self.WIDTH/4, self.HEIGHT/2))

        # Draw text
        self.screen.blit(text_surface_P1, text_rect_P1)
        self.screen.blit(text_surface_P2, text_rect_P2)

        # Update screen
        pygame.display.flip()

    def render_menu(self, label: str):
        """
        Shows each one of the game modes to be selected
        """
        # Fill background (black)
        self.screen.fill(self.COLORS['white'])

        # Render text surfaces
        text_header = self.font.render("Select game mode:", True, self.COLORS['black'])
        text_surface = self.font.render(label, True, self.COLORS['black'])

        # Center text
        text_rect_header = text_header.get_rect(center=(self.WIDTH/2, self.HEIGHT/4))
        text_rect_surface = text_surface.get_rect(center=(self.WIDTH/2, self.HEIGHT/2))

        # Draw text
        self.screen.blit(text_header, text_rect_header)
        self.screen.blit(text_surface, text_rect_surface)

        # Update screen
        pygame.display.flip()


