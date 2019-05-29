import random
from time import sleep
import pygame


# 血量
HP_list = [1, 15, 25, 5]

hit_score = 75

# 飞机大小
plane_size = [{'width': 51, 'height': 39}, {'width': 69, 'height': 89}, {'width': 165, 'height': 246}, {'width': 100, 'height': 124}]

# 飞机爆炸时间
plane_bomb_time = [5, 10, 18, 8]
# 补给
blood_supply = None
bullet_supply = None
supply_image = ['bomb-1.gif', 'bomb-2.gif']
supply_size = [{'width': 58, 'height': 88}, {'width': 60, 'height': 103}]

# 各个子弹图片
bullet_type = ['bullet1.png', 'bullet-1.gif', 'bullet2.png', 'bullet.png']
# bullet injuried
bullet_damage_value = [1, 1, 2, 1]

# 敌机列表
enemy0_list = []
enemy0_max = 6  # 最多有6只 小飞机
enemy1_list = []
enemy1_max = 1
enemy2_list = []
enemy2_max = 1


class Base(object):
    def __init__(self, screen, x, y, image_name):
        self.x = x
        self.y = y
        self.screen = screen
        self.image = pygame.image.load(image_name)


class BasePlane(Base):
    def __init__(self, plane_type, screen, x, y, image_name, picture_num, HP):
        super().__init__(screen, x, y, image_name)
        self.bullet_list = []  # 用来存储发射的子弹

        self.HP = HP
        self.plane_type = plane_type   # 4 种飞机类型

        # 爆炸需要的属性
        self.hit = False
        self.bomb_picture_list = []   # 存储爆炸效果的三张图片
        self.bomb_picture_num = picture_num   # 爆炸效果的图片数量
        self.image_num = 0              # 用来记录while True的次数,当次数达到一定值时才显示一张爆炸的图,然后清空,,当这个次数再次达到时,再显示下一个爆炸效果的图片
        self.image_index = 0          # 爆炸图片序号

        self.fire_bullet_count = 0  # 用来记录while True 的次数， 当时数达到一定值时猜能显示一张爆炸的图，然后清空，当这个次数再次到达时，再显示下一个爆炸效果的图片
        self.picture_count = 0

    def display(self):
        bullet_list_temp = []
        global HP_list
        global plane_bomb_time

        # 击中效果
        if self.hit is True and self.HP <= 0 and self.image_index < self.bomb_picture_num:
            # if self.plane_type != 3 and self.image_index == 0 and self.image_num == 0:
            #     hit_score += HP_list[self.plane_type]
            # print('击中效果HP {}'.format(self.HP))
            # print('击中效果bullet_list {}'.format(self.bullet_list))
            self.screen.blit(self.bomb_picture_list[self.image_index], (self.x, self.y))
            self.picture_count += 1
            if self.picture_count == plane_bomb_time[self.plane_type]:
                self.picture_count = 0
                self.image_index += 1
            # self.image_num += 1
            # if self.image_num == 7:
            #     self.image_num = 0
            #     self.image_index += 1
            # if self.image_index > self.bomb_picture_num-1:
            #     sleep(1)
            #     exit()
        elif self.image_index < self.bomb_picture_num:
            # print('elif:{}'.format(self.HP))
            self.screen.blit(self.image, (self.x, self.y))
            # print('elif de {}'.format(self))

        if self.hit is True and self.image_index >= self.bomb_picture_num and self.HP <= 0:
            # and not self.bullet_list:
            # print('del plane')
            # print(self)
            # print('bullet_list:{}'.format(self.bullet_list))
            # print(del_plane(self))
            del_plane(self)  # 删除飞机
            # print('del_plan：{}'.format(self))

        # 删除不在画面的飞机
        if self.y > 850:
            del_plane(self)

        # 删除不在画面的子弹
        for bullet in self.bullet_list:
            bullet.display()
            bullet.move()

            if bullet.judge():
                bullet_list_temp.append(bullet)

        for bullet in bullet_list_temp:
            self.bullet_list.remove(bullet)

    def create_image(self, bomb_picture_name):
        for i in range(1, self.bomb_picture_num+1):
            self.bomb_picture_list.append(pygame.image.load("./feiji/" + bomb_picture_name + str(i) + ".png"))

    def isHitted(self, plane, width, height):
        if plane.bullet_list and self.HP:
            # print('有没有到这一步  1')
            for bullet in plane.bullet_list:
                # print('有没有到这一步  2')
                if self.x + 0.05*width < bullet.x < self.x + 0.95*width and self.y + 0.1*height < bullet.y < self.y + 0.8*height:
                    # print('有没有到这一步  3')
                    self.HP -= bullet.damage_value   # 减HP
                    if self.plane_type == 3:
                        show_score_HP()
                    plane.bullet_list.remove(bullet)
                    # print(self)
                    self.hit = True
                    self.HP -= 1
                    # print(self.HP)

    def fire(self, bullet_max):
        if self.HP > 0:
            random_num = random.randint(1, 60)
            if (random_num == 60 or random_num == 45) and len(self.bullet_list) < bullet_max:
                self.bullet_list.append(EnemyBullet(self.screen, self.x, self.y, self))
                self.fire_bullet_count += 1


class BaseBullet(Base):
    global bullet_damage_value

    def __init__(self, screen, x, y, image_name, plane):
        super().__init__(screen, x, y, image_name)
        if plane:
            self.damage_value = bullet_damage_value[plane.plane_type]

    def display(self):
        self.screen.blit(self.image, (self.x, self.y))


class MyPlane(BasePlane):        # 飞机类
    global supply_size

    def __init__(self, screen):
        super().__init__(3, screen, 210, 700, './feiji/hero1.png', 4, HP_list[3])
        BasePlane.create_image(self, "hero_blowup_n")
        self.key_down_list = []  # 存储键盘输入

    def press_key_down(self, key):
        self.key_down_list.append(key)

    def press_key_up(self):
        if len(self.key_down_list) != 0:
            self.key_down_list.pop(0)

    def move(self):
        if len(self.key_down_list) != 0:
            if self.key_down_list[0] == pygame.K_LEFT:
                self.move_left()
            elif self.key_down_list[0] == pygame.K_RIGHT:
                self.move_right()
            elif self.key_down_list[0] == pygame.K_UP:
                self.move_up()
            elif self.key_down_list[0] == pygame.K_DOWN:
                self.move_down()

    def move_limit(self):
        if self.x < 0:
            self.x = -2
        elif self.x + 100 > 480:
            # print(self.x)
            self.x = 380     # 这里卡住了？卡在右边动不了.   将 原本 386 改成 380
            # print(self.x)

    def move_left(self):
        self.x -= 5

    def move_right(self):
        self.x += 5

    def move_up(self):
        self.y -= 5

    def move_down(self):
        self.y += 5

    def fire(self):
        self.bullet_list.append(Bullet(self.screen, self.x, self.y, self))

    def bomb(self):
        self.hit = True       # 自爆不了？？    HP 没有归零
        self.HP = 0

    def supply_hit(self, supply, width, height):
        if supply and self.HP:
            supply_left_x = supply.x + supply_size[supply.supply_type]['width']*0.15
            supply_right_x = supply.x + supply_size[supply.supply_type]['width']*0.85
            supply_top_y = supply.y + supply_size[supply.supply_type]['height']*0.4
            supply_bottom_y = supply.y + supply_size[supply.supply_type]['height']*0.9

            # # 测试
            # print("="*50)
            # print("supply_left_x=%f"%supply_left_x)
            # print("supply_right_x=%f"%supply_right_x)
            # print("supply_top_y=%f"%supply_top_y)
            # print("supply_bottom_y=%f"%supply_bottom_y)
            # print("1=%f"%(self.x+0.05*width))
            # print("2=%f"%(self.x+0.95*width))
            # print("3=%f"%(self.y+0.1*height))
            # print("4=%f"%(self.y+0.9*height))
            # print("="*50)

            if supply_left_x > self.x + 0.05*width and supply_right_x < self.x + 0.95*width and supply_top_y < self.y + 0.95*height and supply_bottom_y > self.y + 0.1*height:
                # print('self.HP:{}'.format(self.HP))
                self.HP -= supply.supply_HP
                if self.HP > 15:     # 血量 达到最大为15
                    self.HP = 15
                show_score_HP()
                # print('del_supply')
                del_supply(supply)
                # print('del_supply over')
                # print(supply)

    # def enemy_hit(self, enemy):
    #     if enemy.bullet_list is not None:
    #         for bullet in enemy.bullet_list:
    #             if self.x < bullet.x < self.x + 100 and self.y < bullet.y < self.y + 124:
    #                 enemy.bullet_list.remove(bullet)
    #                 self.bomb()


class EnemyPlane0(BasePlane):
    def __init__(self, screen):
        random_num_x = random.randint(0, 430)
        random_num_y = random.randint(-30, -20)
        super().__init__(0, screen, random_num_x, random_num_y, './feiji/enemy0.png', 4, HP_list[0]) # (self, plane_type, screen, x, y, image_name, picture_num, HP)
        BasePlane.create_image(self, 'enemy0_down')
        BasePlane.fire(self, 2)
        self.direction = 'right '

    def move(self):
        self.y += 4
        # if self.direction == 'right':
        #     self.x += 5
        # elif self.direction == 'left':
        #     self.x -= 5


    # def fire(self):
    #     if not self.hit:
    #         num = random.randint(1, 200)
    #         if num == 1 or num == 2:
    #             if len(self.bullet_list) < 3:
    #                 self.bullet_list.append(EnemyBullet(self.screen, self.x, self.y, self))


class EnemyPlane1(BasePlane):
    def __init__(self, screen):
        super().__init__(1, screen, 205, 10, './feiji/enemy1.png', 4, HP_list[1])
        BasePlane.create_image(self, 'enemy1_down')
        self.direction = 'right '
        self.num_y = random.randint(20, 150)

    def move(self):
        if self.direction == 'right':
            self.x += 3
        elif self.direction == 'left':
            self.x -= 3

        if self.x > 430:
            self.direction = 'left'
        elif self.x < 0:
            self.direction = 'right'
        if self.y < self.num_y:
            self.y += 3
        elif self.fire_bullet_count > 15:
            self.y += 3

    # def fire(self):
    #     num = random.randint(1, 100)
    #     if num == 1 or num == 2:
    #         if self.HP >0 and len(self.bullet_list) < 2:
    #             self.bullet_list.append(EnemyBullet(self.screen, self.x, self.y, self))


class EnemyPlane2(BasePlane):
    def __init__(self, screen):
        super().__init__(2, screen, 158, 10, './feiji/enemy2.png', 5, HP_list[2])
        BasePlane.create_image(self, 'enemy2_down')
        self.direction = 'right'

    def move(self):
        if self.direction == 'right':
            self.x += 2
        elif self.direction == 'left':
            self.x -= 2

        if self.x + 165 > 480:
            self.direction = 'left'
        elif self.x < 0:
            self.direction = 'right'
        if self.y < 0:
            self.y += 4
        elif self.fire_bullet_count > 25:
            self.y += 3

    # def fire(self):
    #     num = random.randint(1, 50)
    #     if num == 1 or num == 2:
    #         if self.HP > 0 and len(self.bullet_list) < 2:
    #             self.bullet_list.append(EnemyBullet(self.screen, self.x, self.y, self))
    #             print(self.bullet_list)


class Bullet(BaseBullet):   # 子弹类
    def __init__(self, screen, x, y, plane):
        super().__init__(screen, x+40, y-14, './feiji/bullet.png', plane)

    def move(self):
        self.y -= 12

    def judge(self):
        if self.y < -10:
            return True
        else:
            return False


class EnemyBullet(BaseBullet):
    global bullet_type
    global plane_size

    def __init__(self, screen, x, y, plane):
        super().__init__(screen, x+plane_size[plane.plane_type]['width']/2, y+plane_size[plane.plane_type]['height']/2, './feiji/'+bullet_type[plane.plane_type], plane)
        # super().__init__(screen, x+45, y+20, './feiji/bullet1.png')

    def move(self):
        self.y += 5

    def judge(self):
        if self.y > 799:
            return True
        else:
            return False


class Supply(BaseBullet):
    def __init__(self, screen, x, y, type, speed, S_HP, supply_type):
        super().__init__(screen, x, y, './feiji/'+supply_image[type], None)
        self.speed = speed
        self.supply_HP = S_HP
        self.supply_type = supply_type

    def move(self):
        self.y += self.speed

    def judge(self):
        if self.y > 800:
            return True
        else:
            return False


def key_control(ctrl):       # 提供键盘输入，在控制方向的同时，还有开火和关闭

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                # print('left')
                ctrl.press_key_down(pygame.K_LEFT)
            elif event.key == pygame.K_RIGHT:
                # print('right')
                ctrl.press_key_down(pygame.K_RIGHT)
            elif event.key == pygame.K_UP:
                # print('up')
                ctrl.press_key_down(pygame.K_UP)
            elif event.key == pygame.K_DOWN:
                # print('down')
                ctrl.press_key_down(pygame.K_DOWN)
            elif event.key == pygame.K_SPACE:
                ctrl.fire()

            elif event.key == pygame.K_b:
                # print('自爆')
                ctrl.bomb()
                # print('自爆结束')

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                ctrl.press_key_up()
            elif event.key == pygame.K_RIGHT:
                ctrl.press_key_up()
            elif event.key == pygame.K_UP:
                ctrl.press_key_up()
            elif event.key == pygame.K_DOWN:
                ctrl.press_key_up()


def del_plane(plane):
    global enemy0_list
    global enemy1_list
    global enemy2_list
    global myplane
    global hit_score

    if plane in enemy0_list:
        # print('len(enemy0_list):{}'.format(len(enemy0_list)))
        enemy0_list.remove(plane)
        # print('len(enemy0_list.remove):{}'.format(len(enemy0_list)))
    elif plane in enemy1_list:
        enemy1_list.remove(plane)
    elif plane in enemy2_list:
        # print('len(enemy2_list):{}'.format( len(enemy2_list)))
        enemy2_list.remove(plane)
        # print('len(enemy2_list.remove):{}'.format(len(enemy2_list)))
    elif plane == myplane:
        hit_score = 0
        show_score_HP()
        myplane = None


def show_score_HP():
    global myplane
    global hit_score
    print('-'*60)
    print('\t\t\tscore:{}'.format(hit_score))
    print('\t\t\t   HP:{}'.format(myplane.HP))


def del_supply(supply):
    global blood_supply
    global bullet_supply

    if supply == blood_supply:
        # print('blood_supply:{}'.format(blood_supply))
        blood_supply = None
        # print('blood_supply:{}'.format(blood_supply))
    elif supply == bullet_supply:
        bullet_supply = None


pygame.mixer.init()


def music():
    pygame.mixer.music.load('./music/PlaneWarsBackgroundMusic.mp3')
    pygame.mixer.music.play(-1)


def main():
    global myplane
    global hit_score
    global HP_list
    global blood_supply

    global enemy0_max
    global enemy1_max
    global enemy2_max

    hit_score_temp = hit_score

    screen = pygame.display.set_mode((480, 800), 0, 32)

    pygame.display.set_caption("飞机大战")

    background = pygame.image.load('./feiji/background.png')

    music()

    myplane = MyPlane(screen)

    running = True
    while running:

        if hit_score > hit_score_temp and myplane:
            hit_score_temp = hit_score
            show_score_HP()
        elif hit_score < hit_score_temp:
            hit_score_temp = 0

        # screen.blit(myplane, (200, 400))

        # 开始创建敌机
        random_num = random.randint(1, 70)
        random_enemy1 = random.randint(19, 26)
        random_enemy2 = random.randint(80, 100)
        if random_num == 1 or random_num == 2:
            if len(enemy0_list) < enemy0_max:
                # print('enemy0_list before:{}'.format(len(enemy0_list)))
                enemy0_list.append(EnemyPlane0(screen))
                # print('enemy0_list after:{}'.format(len(enemy0_list)))
        elif hit_score >= random_enemy1 and hit_score%random_enemy1 == 0:
            if len(enemy1_list) < 1:
                # print('enemy1_list:{}'.format(len(enemy1_list)))
                enemy1_list.append(EnemyPlane1(screen))
        elif hit_score >= random_enemy2 and hit_score%random_enemy2 == 0:
            if len(enemy2_list) < 1:
                # print('random_num:{}'.format(random_num))
                # print('创建打飞机')
                # print('enemy2_list:{}'.format(len(enemy2_list)))
                enemy2_list.append(EnemyPlane2(screen))
                # print('enemy2_list:{}'.format(len(enemy2_list)))

        if not blood_supply:
            random_supply = random.randint(1, 1500)
            if random_supply % 241 == 0:
                random_x = random.randint(0, 400)
                random_y = random.randint(-105, -40)
                blood_supply = Supply(screen, random_x, random_y, 0, 3, -3, 0)

        screen.blit(background, (0, 0))

        if myplane:
            myplane.display()
            myplane.move()
            myplane.move_limit()

        if blood_supply:
            blood_supply.display()
            blood_supply.move()
            if blood_supply.judge():
                del_supply(blood_supply)
                # print('main del_supply {}'.format(del_supply(blood_supply)))

        # hit 了直接穿过飞机
        if myplane and blood_supply:
            # print('supply falling')
            myplane.supply_hit(blood_supply, plane_size[myplane.plane_type]['width'], plane_size[myplane.plane_type]['height'])
            # print('falling ending')

        if enemy0_list:
            for enemy0 in enemy0_list:
                enemy0.display()
                enemy0.move()
                enemy0.fire(2)

                # myplane.isHitted(enemy0, 92, 166)
                # enemy0.isHitted(myplane, 43, 31)
                if myplane:
                    myplane.isHitted(enemy0, plane_size[myplane.plane_type]['width'], plane_size[myplane.plane_type]['height'])
                    # print("没有打击效果，子弹没有消失，飞机也没有消失")
                    enemy0.isHitted(myplane, plane_size[enemy0.plane_type]['width'], plane_size[enemy0.plane_type]['height'])

        if enemy1_list:
            for enemy1 in enemy1_list:
                enemy1.display()
                enemy1.move()
                enemy1.fire(4)

                # myplane.isHitted(enemy1, 92, 166)
                # enemy1.isHitted(myplane, 61, 71)
                if myplane:
                    myplane.isHitted(enemy1, plane_size[myplane.plane_type]['width'], plane_size[myplane.plane_type]['height'])
                    enemy1.isHitted(myplane, plane_size[enemy1.plane_type]['width'], plane_size[enemy1.plane_type]['height'])

        # if enemy2_list is None:

        if enemy2_list:
            # print(len(enemy2_list))
            for enemy2 in enemy2_list:
                enemy2.display()
                enemy2.move()
                enemy2.fire(6)               # 为什么fire就会删除不掉 enemy！
                                            # 子弹没打光！就删除不掉 而且太快生成了enemy2

                # myplane.isHitted(enemy2, 92, 166)
                # enemy2.isHitted(myplane, 147, 239)
                if myplane:
                    myplane.isHitted(enemy2, plane_size[myplane.plane_type]['width'], plane_size[myplane.plane_type]['height'])
                    enemy2.isHitted(myplane, plane_size[enemy2.plane_type]['width'], plane_size[enemy2.plane_type]['height'])

        pygame.display.update()
        key_control(myplane)          # 控制方向

        sleep(0.01)


if __name__ == '__main__':
    main()
