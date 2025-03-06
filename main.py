import pygame


pygame.init() # обезательная программа

window_size=(300,300)#размеры окна
screen=pygame.display.set_mode(window_size)#сделать экран с размерами
pygame.display.set_caption("Undertale")
background_color = (0,0,255)
clock = pygame.time.Clock()#фпс
x = 66
y = 90
while True:#игровой цикл
    screen.fill(background_color) #заливка экрана цветом
    color = (50, 70, 40)
    r = pygame.Rect(x, y, 150, 60)

    pygame.draw.rect(screen,color,r)

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







