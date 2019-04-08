#
# settings.py
# @author bulbasaur
# @description : Setting class
# @created Sun Apr 07 2019 19:08:03 GMT+0800 (中国标准时间)
# @last-modified Mon Apr 08 2019 09:08:08 GMT+0800 (中国标准时间)
#

class Settings():
    '''存储《外星人入侵》的所有设置的类'''

    def __init__(self):
        '''初始化游戏的设置'''
        #屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230,230,230)