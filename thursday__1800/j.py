import pygame #импортируем код в pygame
from random import *

class Food():#создание класса
    def __init__(self,a,b,c):#создание конструктора, в нем создается свойства,он вызывается при создании объекта
        self.img = pygame.image.load(a)#создание картинки,ЭТО СВОЙСТВО

        self.rect = self.img.get_rect()# получение прямоугольника от картинки,ЭТО СВОЙСТО
        self.rect.x = b#создание координат,ЭТО СВОЙСТВО
        self.rect.y = c#создание координат,ЭТО СВОЙСТВО

    def draw_image(self):#метод отрисовки картинки
        screen.blit(self.img, (self.rect.x, self.rect.y))

    def move_food(self):
        self.rect.y += 5

    def move_plate(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= 5
        elif keys[pygame.K_RIGHT]:
            self.rect.x += 5

y4=randint(-500,0)
y2=randint(-500,0)
y=randint(-500,0)
food3 = Food("еда 1.png",200,y4)
food2 = Food("еда 3.png",300, y)
food1 = Food("еда4.png",500,y2)
fon = Food('кухня.jpg', 0, 0)# создание фона
plate = Food('plate.png', 360, 450)# создание фона
pygame.init()#обезательная программа
window_size=(940,500)#размеры окна
screen=pygame.display.set_mode(window_size)#сделать экран с размерами
clock = pygame.time.Clock() #фпс

while True:#игровой цикл
    fon.draw_image()#приминение метода отрисовки картинки к объкеу klassa Food (фон)
    plate.draw_image() #приминение метода отрисовки картинки к объкеу klassa Food (тарелка)
    food1.draw_image()
    food2.draw_image()
    food3.draw_image()
    food1.move_food()
    food2.move_food()
    food3.move_food()
    plate.move_plate()# применение метода к объкту
    clock.tick(40)#40фпс
    for event in pygame.event.get():#события
        if event.type == pygame.QUIT:#если нажали крест
              pygame.QUIT()# выход из игры
    pygame.display.update()  # обновление содержимого экрана