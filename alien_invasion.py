# alien_invasion.py -- Main file
"""Contains the run function of Alien Invasion game."""

import pygame                 # third party game library.
import game_functions as gf
from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from ship import Ship
from pygame.sprite import Group

def run_game():
    """Used to run the game."""
    # initialize game and create a screen object.
    pygame.init()
    # create instance of settings class.
    ai_settings = Settings()
    # create display window. surface of game.
    screen = pygame.display.set_mode(
             (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # make the Play button.
    play_button = Button(ai_settings, screen, "Play")
    
    # create an instance to store game statistics and create a scoreboard.
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)
    
    # make a ship. create b4 while loop to avoid unnecessary repeat instances.
    ship = Ship(ai_settings, screen)
    # make a group to store bullets in.
    bullets = Group()
    # make a group of stars.
    stars = Group()
    # create the stars.
    gf.create_stars(ai_settings, screen, stars)
    # make a group of aliens.
    aliens = Group()
    # create the fleet of aliens.
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # start the main loop for the game.
    while True:
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens,
                        bullets)

        if stats.game_active:
            ship.update() # update ship's position.
            gf.update_bullets(ai_settings, screen, stats, sb,
                              ship, aliens, bullets)
            gf.update_aliens(ai_settings, screen, stats, sb,
                             ship, aliens, bullets)

        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, stars,
                         bullets, play_button)
        
# call function to run game.
run_game()
