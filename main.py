import pygame #импортируем код в pygame

class Food():#создание класса
    def __init__(self,a,b,c):#создание конструктора, в нем создается свойства,он вызывается при создании объекта
        self.img = pygame.image.load(a)#создание картинки,ЭТО СВОЙСТВО

        self.rect = self.img.get_rect()# получение прямоугольника от картинки,ЭТО СВОЙСТО
        self.rect.x = b#создание координат,ЭТО СВОЙСТВО
        self.rect.y = c#создание координат,ЭТО СВОЙСТВО

    def draw_image(self):#метод отрисовки картинки
        screen.blit(self.img, (self.rect.x, self.rect.y))


fon = Food('кухня.jpg', 0, 0)# создание фона
plate = Food('plate.png', 360, 450)# создание фона
pygame.init()#обезательная программа
window_size=(940,500)#размеры окна
screen=pygame.display.set_mode(window_size)#сделать экран с размерами
clock = pygame.time.Clock() #фпс

while True:#игровой цикл
    fon.draw_image()#приминение метода отрисовки картинки к объкеу klassa Food (фон)
    plate.draw_image() #приминение метода отрисовки картинки к объкеу klassa Food (тарелка)

    clock.tick(40)#40фпс
    for event in pygame.event.get():#события
        if event.type == pygame.QUIT:#если нажали крест
              pygame.QUIT()# выход из игры
    pygame.display.update()  # обновление содержимого экрана
