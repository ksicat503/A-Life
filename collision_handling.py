import pygame
from a_life_sim import X_PX_SIZE, Y_PX_SIZE


def collision_check(moving_organism, all_organisms, original_pos):
    """
    Checks moving_organism against all_organisms

    If collision happens, apply appropriate actions depending on animal_type
    and whether it is a self-encounter (skip collision check)

    :param moving_organism: The current organism that is currently moving
    :param all_organisms: A list of all organisms in the simulation.
    :param original_pos: Tuple of original position of moving_organism.

    :return: Boolean, returns False if no collision, True after collision and
            appropriate collision-specific actions
    """
    for check_organism in all_organisms:
        if not check_organism.is_alive:
            continue
        # check to avoid self-collision
        if moving_organism is check_organism:
            continue
        moving_org = pygame.Rect(moving_organism.x_pos,
                                 moving_organism.y_pos,
                                 X_PX_SIZE,
                                 Y_PX_SIZE)
        check_org = pygame.Rect(check_organism.x_pos,
                                check_organism.y_pos,
                                X_PX_SIZE,
                                Y_PX_SIZE)

        if moving_org.colliderect(check_org):
            # manage herbivore and carnivore collisions
            if (
                moving_organism.animal_type == 1 and
                check_organism.animal_type == 2
            ):
                moving_organism.is_alive = False
                check_organism.days_since_fed = 0
                return True
            if (
                moving_organism.animal_type == 2 and
                check_organism.animal_type == 1
            ):
                check_organism.is_alive = False
                moving_organism.days_since_fed = 0
                return True
            # when same animal_type collides, revert back the
            # moving_organism to its original position
            else:
                (moving_organism.x_pos,
                    moving_organism.y_pos) = (original_pos)
