#
# alien_invasion.py
# @author Giotto Lee
# @description : Main function
# @created Sun Apr 07 2019 18:56:32 GMT+0800 (中国标准时间)
# @last-modified Mon Apr 08 2019 11:46:06 GMT+0800 (中国标准时间)
#


import sys
import pygame
import game_functions as gf
from settings import Settings
from ship import Ship
from pygame.sprite import Group

def run_game():
    #初始化pygame、设置、屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    #设置背景色
    bg_color = (230,230,230)

    #创建一艘飞船
    ship = Ship(ai_settings,screen)

    #创建一个用于存储子弹的编组
    bullets = Group()
    
    #开始游戏主循环
    while True:
        #监视键盘和鼠标事件
        gf.check_events(ai_settings,screen,ship,bullets)
        ship.update()
        bullets.update()
        gf.update_screen(ai_settings,screen,ship,bullets)
run_game()