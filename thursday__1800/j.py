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
food6= Food("еда 1.png",250,y4)
food5= Food("еда 1.png",400,y4)
food4 = Food("еда 1.png",600,y4)
food3 = Food("еда 1.png",200,y4)
food2 = Food("еда 3.png",350, y)
food1 = Food("еда4.png",500,y2)

food_list = [food1, food2, food3]
fon = Food('кухня.jpg', 0, 0)# создание фона
plate = Food('plate.png', 360, 450)# создание фона
pygame.init()#обезательная программа
window_size=(930,495)#размеры окна
screen=pygame.display.set_mode(window_size)#сделать экран с размерами
clock = pygame.time.Clock() #фпс


while True:#игровой цикл
    fon.draw_image()#приминение метода отрисовки картинки к объкеу klassa Food (фон)
    plate.draw_image() #приминение метода отрисовки картинки к объкеу klassa Food (тарелка)
    plate.move_plate()# применение метода к объкту
    clock.tick(40)#40фпс
    for i in food_list:
        i.draw_image()
        i.move_food()
        if i.rect.y>700:
            i.rect.y = 0

        if plate.rect.colliderect(i.rect):
            food_list.remove(i)
        if food_list == []:
            pygame.QUIT()
    for event in pygame.event.get():#события
        if event.type == pygame.QUIT:#если нажали крест
            pygame.QUIT()# выход из игры
    pygame.display.update()  # обновление содержимого экрана
