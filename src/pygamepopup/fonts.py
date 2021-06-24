"""
Defines fonts that will be used all over the application.
The init_fonts function should be called at the beginning of the application
after pygame initialization.
"""

from typing import Union

import pygame

fonts_description: dict[str, dict[str, Union[str, int]]] = {
    "MENU_TITLE_FONT": {"default": True, "size": 40},
    "DEFAULT_FONT": {"default": True, "size": 20},
}

fonts: dict[str, pygame.font.Font] = {}


def init() -> None:
    """
    Load all fonts registered in fonts_description.
    System font will be load if the keyword 'default' is present in the description provided.
    These fonts will be available in all modules by importing the fonts dictionary.
    """
    global fonts
    for font in fonts_description:
        if "default" in fonts_description[font]:
            # Use pygame's default font
            fonts[font] = pygame.font.SysFont(
                "arial", fonts_description[font]["size"]
            )
        else:
            fonts[font] = pygame.font.Font(
                fonts_description[font]["name"], fonts_description[font]["size"]
            )
