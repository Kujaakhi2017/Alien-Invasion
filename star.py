"""Contains Star class."""
import pygame
from pygame.sprite import Sprite

class Star(Sprite):
    """A class to help create a starry background."""

    def __init__(self, ai_settings, screen):
        """Initialize the star."""
        super(Star, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # load the star image and set its rect attribute.
        self.image = pygame.image.load('images/star.bmp')
        self.rect = self.image.get_rect()

        # start each new star near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # store the star's exact positiion.
        self.x = float(self.rect.x)

    def blitme(self):
        """Draw the star at its current location."""
        self.screen.blit(self.image, self.rect)
