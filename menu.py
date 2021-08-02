import pygame
import os

MENU_IMAGE = pygame.image.load(os.path.join("images", "upgrade_menu.png"))
UPGRADE_IMAGE = pygame.image.load(os.path.join("images", "upgrade.png"))
SELL_IMAGE = pygame.image.load(os.path.join("images", "sell.png"))


class UpgradeMenu:
    def __init__(self, x, y):
        self.menu_image = pygame.transform.scale(MENU_IMAGE, (200, 200))  # image of menu
        self.upgrade_image = pygame.transform.scale(UPGRADE_IMAGE, (80, 40))  # image of upgrade button
        self.sell_image = pygame.transform.scale(SELL_IMAGE, (50, 50))  # image of sell button
        self.rect = self.menu_image.get_rect()  # 以 menu 圖片為基準
        self.rect.center = (x, y)  # center of menu
        self.x = x
        self.y = y
        # (Q2) Add buttons here
        self.__buttons = [Button(self.upgrade_image, "upgrade", self.rect.centerx, self.rect.centery - 75),
                          Button(self.sell_image, "sell", self.rect.centerx, self.rect.centery + 75)]

    def draw(self, win):
        """
        (Q1) draw menu itself and the buttons
        (This method is call in draw() method in class TowerGroup)
        :return: None
        """
        # draw menu
        win.blit(self.menu_image, (self.rect.x, self.rect.y))
        # draw button  # (Q2) Draw buttons here
        win.blit(self.upgrade_image, (self.rect.x + 58, self.rect.y + 9))
        win.blit(self.sell_image, (self.rect.x + 74, self.rect.y + 150))

    def get_buttons(self):
        """
        (Q1) Return the button list.
        (This method is call in get_click() method in class TowerGroup)
        :return: list
        """
        return self.__buttons  # 回傳 button list

class Button:
    def __init__(self, image, name, x, y):
        self.name = name  # button's names
        self.image = image  # button's image
        self.rect = self.image.get_rect()  # button's image center
        self.rect.center = (x, y)  # image center coordinate

    def clicked(self, x, y):
        """
        (Q2) Return Whether the button is clicked
        (This method is call in get_click() method in class TowerGroup)
        :param x: mouse x
        :param y: mouse y
        :return: bool
        """
        # 判斷滑鼠點擊之座標是否在 button's image 中，並回傳
        return True if self.rect.collidepoint(x, y) else False

    def response(self):
        """
        (Q2) Return the button name.
        (This method is call in get_click() method in class TowerGroup)
        :return: str
        """
        # 回傳滑鼠點擊之 button's name
        return self.name







