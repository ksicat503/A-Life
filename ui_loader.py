import pygame

from constants import WINDOW_WIDTH, WINDOW_HEIGHT
from ui_components import Button, Text, Toggle


def load_ui_components():
    """ Initalizes all menu components for each menu """
    components = {
        'buttons': {},
        'toggles': {},
        'text': {},
        'background': pygame.transform.scale(
            pygame.image.load('./assets/menu_background.jpg').convert(),
            (WINDOW_WIDTH, WINDOW_HEIGHT))
    }

    # Text sizing/positioning
    components['text']['title'] = Text(WINDOW_WIDTH//2, 150, 50)
    components['text']['features'] = Text(WINDOW_WIDTH//3, 300, 30)
    components['text']['speed'] = Text(WINDOW_WIDTH//3, 400, 30)

    # Starting Menu UI Components
    components['buttons']['new_sim'] = Button(
            WINDOW_WIDTH // 2, 300,
            pygame.image.load('./assets/new_sim_button.png').convert_alpha(),
            0.7
        )
    components['buttons']['load_sim'] = Button(
            WINDOW_WIDTH // 2, 400,
            pygame.image.load('./assets/load_sim_button.png').convert_alpha(),
            0.7
        )
    components['buttons']['exit'] = Button(
            WINDOW_WIDTH // 2, 500,
            pygame.image.load('./assets/exit_button.png').convert_alpha(),
            0.7
        )
    # New Sim Menu UI Components
    components['toggles']['on_off'] = Toggle(
            (WINDOW_WIDTH // 3) * 2, 300,
            [pygame.image.load('./assets/on_button.png').convert_alpha(),
             pygame.image.load('./assets/off_button.png').convert_alpha()],
            0.7
        )
    components['buttons']['start'] = Button(
            WINDOW_WIDTH // 2, 400,
            pygame.image.load('./assets/start_button.png').convert_alpha(),
            0.7
        )
    # Load Sim Menu UI Components
    components['buttons']['sim_1'] = Button(
            WINDOW_WIDTH // 2, 300,
            pygame.image.load('./assets/saved_sim_1_button.png')
            .convert_alpha(),
            0.7
        )
    components['buttons']['sim_2'] = Button(
            WINDOW_WIDTH // 2, 400,
            pygame.image.load('./assets/saved_sim_2_button.png')
            .convert_alpha(),
            0.7
        )
    components['buttons']['sim_3'] = Button(
            WINDOW_WIDTH // 2, 500,
            pygame.image.load('./assets/saved_sim_3_button.png')
            .convert_alpha(),
            0.7
        )
    # Back button for both new and load sim menu
    components['buttons']['back'] = Button(
            WINDOW_WIDTH // 2, 600,
            pygame.image.load('./assets/back_button.png').convert_alpha(),
            0.7
        )

    # Pause Menu UI Components
    components['buttons']['resume'] = Button(
            WINDOW_WIDTH // 2, 300,
            pygame.image.load('./assets/resume_button.png').convert_alpha(),
            0.7
        )
    components['toggles']['speed'] = Toggle(
            (WINDOW_WIDTH // 3) * 2, 400,
            [pygame.image.load('./assets/1x_button.png').convert_alpha(),
             pygame.image.load('./assets/2x_button.png').convert_alpha(),
             pygame.image.load('./assets/4x_button.png').convert_alpha()
             ],
            0.7
        )
    components['buttons']['stat'] = Button(
            WINDOW_WIDTH // 2, 500,
            pygame.image.load('./assets/stats_button.png').convert_alpha(),
            0.7
        )
    components['buttons']['save'] = Button(
            WINDOW_WIDTH // 2, 600,
            pygame.image.load('./assets/save_button.png').convert_alpha(),
            0.7
        )
    components['buttons']['quit'] = Button(
            WINDOW_WIDTH // 2, 700,
            pygame.image.load('./assets/quit_button.png').convert_alpha(),
            0.7
        )
    return components
