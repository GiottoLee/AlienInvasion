#
# ship.py
# @author bulbasaur
# @description : Ship class
# @created Sun Apr 07 2019 19:26:28 GMT+0800 (中国标准时间)
# @last-modified Mon Apr 08 2019 09:07:43 GMT+0800 (中国标准时间)
#


import pygame

class Ship():
    def __init__(self,screen):
        '''初始化飞船并设置其初始位置'''

        self.screen = screen

        #加载飞船图像并获取其外接矩形
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #将每艘飞船放在屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        '''在指定位置绘制飞船'''
        self.screen.blit(self.image,self.rect)

