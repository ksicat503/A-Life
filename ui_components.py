import pygame


class Button():
    def __init__(self, x, y, image, scale):
        """ Initalize class variables"""
        self.image = pygame.transform.scale(
            image,
            (int(image.get_width()*scale), int(image.get_height())*scale))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.scale = scale

    def draw(self, window, can_click):
        """Draws button on the screen and returns if it is clicked"""
        action = False
        if can_click:
            mouse_pos = pygame.mouse.get_pos()

            # Checks if button is clicked
            if self.rect.collidepoint(mouse_pos):
                if pygame.mouse.get_pressed()[0]:
                    self.clicked = True
                    action = True

        window.blit(self.image, self.rect)
        return action


class Text():
    def __init__(self, x, y, font_size, center=True):
        """ Initalize class variables"""
        self.font = pygame.font.Font(
            "./assets/Audiowide-Regular.ttf", font_size)
        self.position = (x, y)
        self.center = center

    def draw(self, window, text):
        """ Draws text to the window"""
        text = self.font.render(text, True, (221, 250, 249))
        if self.center:
            rect = text.get_rect(center=self.position)
        else:
            # Want to center on height but be left justified
            height_center = text.get_rect().height // 2
            rect = text.get_rect(
                topleft=(self.position[0], self.position[1]-height_center))
        window.blit(text, rect)


class Toggle():
    def __init__(self, x, y, images, scale):
        """ Initalize class variables"""

        self.images = [pygame.transform.scale(
            image,
            (int(image.get_width()*scale), int(image.get_height())*scale))
            for image in images]
        self.rect = self.images[0].get_rect()
        self.rect.center = (x, y)
        self.scale = scale
        self.current_index = 0

    def draw(self, window, can_click):
        """Draws button on the screen and returns if it is clicked"""
        action = False
        if can_click:
            mouse_pos = pygame.mouse.get_pos()

            # Checks if button is clicked
            if self.rect.collidepoint(mouse_pos):
                if pygame.mouse.get_pressed()[0]:
                    action = True
                    self.current_index = self.current_index + 1 \
                        if self.current_index + 1 != len(self.images) else 0

        window.blit(self.images[self.current_index], self.rect)
        return action
