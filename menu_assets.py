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
        self.clicked = False

    def draw(self, window):
        """Draws button on the screen and returns if it is clicked"""
        action = False
        mouse_pos = pygame.mouse.get_pos()

        # Checks if button is clicked
        if self.rect.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0] and self.clicked is False:
                self.clicked = True
                action = True
        # Reset button
        if pygame.mouse.get_pressed()[0] is False:
            self.clicked = False

        window.blit(self.image, self.rect)

        return action


class Text():
    def __init__(self, x, y, font_size):
        """ Initalize class variables"""
        self.font = pygame.font.Font(
            "./assets/Audiowide-Regular.ttf", font_size)
        self.center = (x, y)

    def draw(self, window, text):
        """ Draws text to the window"""
        text = self.font.render(text, True, (221, 250, 249))
        rect_center = text.get_rect(center=self.center)
        window.blit(text, rect_center)
