import pygame
import pygame_menu

WINDOW_SIZE = (1000, 800)
MENU_SIZE = (800, 600)

pygame.init()

surface = pygame.display.set_mode((WINDOW_SIZE[0], WINDOW_SIZE[1]))
pygame.display.set_caption("A Life Challenge")


def display_new_sim_menu():
    main_menu.disable()
    new_sim_menu.enable()


def display_load_sim_menu():
    main_menu.disable()
    load_sim_menu.enable()


def start_new_sim():
    new_sim_menu.disable()


def load_sim(id):
    load_sim_menu.disable()


def draw_background():
    surface.fill((255, 255, 255))


main_menu = pygame_menu.Menu(
    'A Life Challenge',
    MENU_SIZE[0], MENU_SIZE[1],
    theme=pygame_menu.themes.THEME_BLUE
)
main_menu.add.button('New Simulation', display_new_sim_menu)
main_menu.add.button('Load Simulation', display_load_sim_menu)
main_menu.add.button('Quit', pygame_menu.events.EXIT)


new_sim_menu = pygame_menu.Menu(
    'New Simulation',
    MENU_SIZE[0], MENU_SIZE[1],
    theme=pygame_menu.themes.THEME_BLUE
)
new_sim_menu.add.text_input('Simulation Name: ', maxchar=20)
new_sim_menu.add.selector(
    'Novel Features: ',
    [('Off', 1), ('On', 2)]
)
new_sim_menu.add.button('Start Simulation', start_new_sim)
new_sim_menu.disable()

# Will need to read json file to get saved sims
sim_loads = ['Saved sim 1', 'Saved sim 2', 'Saved sim 3']
load_sim_menu = pygame_menu.Menu(
    'Load Simulation',
    MENU_SIZE[0], MENU_SIZE[1],
    theme=pygame_menu.themes.THEME_BLUE
)
for index in range(0, len(sim_loads)):
    load_sim_menu.add.button(
        "Name: {}".format(sim_loads[index]),
        load_sim,
        index
    )
load_sim_menu.disable()


while True:
    draw_background()

    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            exit()

    if main_menu.is_enabled():
        main_menu.draw(surface)
        main_menu.update(events)

    if new_sim_menu.is_enabled():
        new_sim_menu.draw(surface)
        new_sim_menu.update(events)

    if load_sim_menu.is_enabled():
        load_sim_menu.draw(surface)
        load_sim_menu.update(events)

    pygame.display.update()
