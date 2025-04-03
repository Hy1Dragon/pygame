import pygame

class Food():
    def __init__(self,a,b,c):
        self.image = pygame.image.load(a)# загрузка картинки
        self.rect = self.image.get_rect()# получение прямоугольника от картинки
        self.x = b
        self.y = c

    def draw_image(self):#метод отрисовки картинки
        screen.blit(self.image, (self.x, self.y))


fon = Food('кухня.jpg', 0, 0)
pygame.init()
window_size=(931,495)#размеры окна
screen=pygame.display.set_mode(window_size)#сделать экран с размерами
pygame.display.set_caption("Undertale")
clock = pygame.time.Clock()#фпс

op = Food ('еда 1.png',0,0)
po = Food ('еда 3.png',0,0)
poop = Food('еда4.png',0,0)

while True:#игровой цикл
    fon.draw_image()#приминение метода отрисовки картинки к объкеу-картинки
    op.draw_image()
    po.draw_image()
    poop.draw_image()

    clock.tick(40)#40фпс
    for event in pygame.event.get():#события
        if event.type == pygame.QUIT:#если нажали крест
              pygame.QUIT()# выход из игры
    pygame.display.update()  # оюновление содержимого экрана