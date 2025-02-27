import pygame
pygame.init()# обезательная программа
window_size=(300,300)#размеры окна
screen=pygame.display.set_mode(window_size)#сделать экран с размерами
pygame.display.set_caption("Undertale")
background_color = (0,0,255)
screen.fill(background_color)
clock = pygame.time.Clock()#фпс
r = pygame.Rect(90,90,150,60)
while True:#игровой цикл
     clock.tick(40)#40фпс\с
     pygame.display.update()#оюновление содержимого экрана
     for event in pygame.event.get():#события
         if event.type == pygame.QUIT:#если нажали крест
             pygame.QUIT()# выход из игры
         color=(50,70,40)
         pygame.draw.rect(screen,color,r)





