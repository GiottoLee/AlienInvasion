#
# game_functions.py
# @author bulbasaur
# @description : 打包简化程序
# @created Mon Apr 08 2019 08:55:34 GMT+0800 (中国标准时间)
# @last-modified Mon Apr 08 2019 09:35:51 GMT+0800 (中国标准时间)
#


import sys
import pygame

def check_events(ship):
    '''相应按键和鼠标事件'''

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = True
            elif event.key == pygame.K_LEFT:
                ship.moving_left = True

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = False
            if event.key == pygame.K_LEFT:
                ship.moving_left = False

def update_screen(ai_settings,screen,ship):
    '''更新屏幕上的图像，并且换到新屏幕'''
    #每次循环时都重绘屏幕
    screen.fill(ai_settings.bg_color)
    ship.blitme()

    #让最近绘制的屏幕可见
    pygame.display.flip()