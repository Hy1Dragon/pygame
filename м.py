import pygame

class Food():
    def __init__(self,a,b,c):
        self.pic = pygame.image.load(a)
        self.rect = self.pic.get_rect()
        self.x = b
        self.y = c

    def draw_pic(self):
        screen.blit(self.pic, (self.x, self.y))


pygame.init()# обязательная программа



food = Food('кухня.jpg', 0, 0)

window_size=(1000,720)#размеры окна
screen=pygame.display.set_mode(window_size)#сделать экран с размерами
pygame.display.set_caption("Undertale")
background_color = (0,0,255)
clock = pygame.time.Clock()#фпс
x = 66
y = 90
while True:#игровой цикл
    food.draw_pic()
    clock.tick(40)#40фпс\с
    pygame.display.update()#оюновление содержимого экрана
    for event in pygame.event.get():#события
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                x = x - 5
            if event.key == pygame.K_w:
                y = y - 5
            if event.key == pygame.K_s:
                y = y + 5
            if event.key == pygame.K_d:
                x = x + 5

        if event.type == pygame.QUIT:#если нажали крест
              pygame.QUIT()# выход из игры
