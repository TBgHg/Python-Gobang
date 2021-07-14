from save import *
from sys import exit

pygame.init()

IMAGE_PATH = 'UI/'

WIDTH = 1130  # 整个框架的宽
HEIGHT = 652
class escmenu_UI(object):
    def __init__(self):
        self.esc_screen=pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)
        pygame.display.set_caption('五子棋')
        self.i0=pygame.image.load(IMAGE_PATH +'title.jpg').convert()
        self.i1=pygame.image.load(IMAGE_PATH +'return_game.jpg').convert()
        self.i1_click=pygame.image.load(IMAGE_PATH +'return_game_click.jpg').convert()
        self.i2=pygame.image.load(IMAGE_PATH +'save_game.jpg').convert()
        self.i2_click=pygame.image.load(IMAGE_PATH +'save_game_click.jpg').convert()
        self.i3=pygame.image.load(IMAGE_PATH +'return_menu.jpg').convert()
        self.i3_click=pygame.image.load(IMAGE_PATH +'return_menu_click.jpg').convert()
        self.bg_image=pygame.image.load(IMAGE_PATH +'background.jpg').convert()
        self.still=False    # 防止跳转页面时鼠标点击重复生效
        self.n_quitgame=False
        self.esc_save=False
    def escmenu_transform (self):
        # 将图片缩放至合适大小
        i0_rect=self.i0.get_rect()
        title_size=(int(i0_rect[2]*3/4),int(i0_rect[3]*3/4))
        self.i0=pygame.transform.scale(self.i0,title_size)
        i_rect=self.i1.get_rect()                     
        size=(int(i_rect[2]*2/3),int(i_rect[3]*2/3)) 
        self.i1=pygame.transform.scale(self.i1,size)
        self.i1_click=pygame.transform.scale(self.i1_click,size)
        self.i2=pygame.transform.scale(self.i2,size)
        self.i2_click=pygame.transform.scale(self.i2_click,size)
        self.i3=pygame.transform.scale(self.i3,size)
        self.i3_click=pygame.transform.scale(self.i3_click,size)
    def escmenu_select(self):
        clock = pygame.time.Clock() 
        n1=True
        while n1:
            for event in pygame.event.get(): 
            # 判断事件类型是否是退出事件
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                elif event.type==pygame.MOUSEBUTTONDOWN:
                    if event.button==1:    # 1代表的是鼠标左键
                        still=True
                elif event.type == KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        n1=False
            clock.tick(30)
            self.esc_screen.blit(self.bg_image,(0,0))
            self.esc_screen.blit(self.i0,(0,0))
            self.esc_screen.blit(self.i1,(70,150))
            self.esc_screen.blit(self.i2,(70,300))
            self.esc_screen.blit(self.i3,(70,450))
            buttons = pygame.mouse.get_pressed()
            x1, y1 = pygame.mouse.get_pos()
            if x1>85 and x1<390 and y1<235 and y1>150:
                self.esc_screen.blit(self.i1_click,(70,150))
                if buttons[0] and still==True:
                    n1=False
            elif x1>85 and x1<390 and y1<385 and y1>290:
                self.esc_screen.blit(self.i2_click,(70,300))
                if buttons[0] and still==True:
                    n1=False
                    self.esc_save=True
            elif x1>85 and x1<390 and y1<535 and y1>465:
                self.esc_screen.blit(self.i3_click,(70,450))
                if buttons[0] and still==True:
                    n1=False
                    self.n_quitgame=True
            else:
                self.esc_screen.blit(self.i1,(70,150))
                self.esc_screen.blit(self.i2,(70,300))
                self.esc_screen.blit(self.i3,(70,450))
            pygame.display.update()