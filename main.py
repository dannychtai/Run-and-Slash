import pygame
import random

# Khởi tạo Pygame
pygame.init()
# Tạo màn hình đầu tiên
WIDTH = 600
HEIGHT = 300
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Megaman Zero')

WHITE=(255,255,255)
RED=(255,0,0)

clock=pygame.time.Clock()

background_x=0
background_y=0

zero_x=0
zero_y=230

enemy_x = 600
enemy_y= 230

enemy2_x = 700
enemy2_y= 100


thienthachs = []

for i in range(3):
    x = random.randint(0, 600)
    y = random.randint(-500, -40)
    thienthachs.append((x, y))
thienthach_vantoc=0

x_velocity=0 #đơn vị vận tốc
y_velocity=0 


score=0
highscore=0

pausing=True

font=pygame.font.SysFont('san',20)
font1=pygame.font.SysFont('san',40)

background=pygame.image.load('background.png')
background = pygame.transform.scale(background,(600,500))

#load hình nhân vật đứng im quay về phải
zerostandright = pygame.image.load('zero0.png')
zerostandright = pygame.transform.scale(zerostandright, (50, 50))

#load hình nhân vật đứng im quay về trái
zerostandleft = pygame.transform.flip(zerostandright, True, False)

# Load hình ảnh nhân vật chạy lên
zero1 = pygame.image.load('zero1.png')
zero2 = pygame.image.load('zero2.png')
zero3 = pygame.image.load('zero3.png')
zero4 = pygame.image.load('zero4.png')
zero5 = pygame.image.load('zero5.png')

# Scale hình ảnh nhân vật về kích thước 50x50
zero1 = pygame.transform.scale(zero1, (50, 50))
zero2 = pygame.transform.scale(zero2, (50, 50))
zero3 = pygame.transform.scale(zero3, (50, 50))
zero4 = pygame.transform.scale(zero4, (50, 50))
zero5 = pygame.transform.scale(zero5, (50, 50))
# Đặt tốc độ hiển thị cho mỗi hình ảnh
frame_rate = 20

# Tạo danh sách chứa các hình ảnh nhân vật
zeroright = [zero1,zero2,zero3,zero4,zero5]
zeroleft = []
for image in zeroright:
    zeroleft.append(pygame.transform.flip(image, True, False))
# Set frame hiện tại của animation
current_frame = 0

# Load hình ảnh nhân vật tấn công
attack_time = 0

zeroattackright = pygame.image.load("zeroattack.png")
zeroattackright = pygame.transform.scale(zeroattackright, (100, 100))# Scale hình ảnh nhân vật tấn công về kích thước 100x100
zeroattackleft = pygame.transform.flip(zeroattackright, True, False)

# load hình ảnh nhân vật chết
zerodie = pygame.image.load("zerodie.png")
zerodie = pygame.transform.scale(zerodie, (50, 50))# Scale hình ảnh nhân vật tấn công về kích thước 50x50


# load hình ảnh kẻ thù
enemy=pygame.image.load('enemy1.png')
enemydie=pygame.image.load('enemydie.png')

enemy2=pygame.image.load('enemy2.png')
enemydie2=pygame.image.load('enemydie2.png')


# Scale hình ảnh kẻ thù về kích thước 50x50
enemy = pygame.transform.scale(enemy, (50, 50))
enemydie = pygame.transform.scale(enemydie, (50, 50))
enemy2 = pygame.transform.scale(enemy2, (50, 50))
enemydie2 = pygame.transform.scale(enemydie2, (50, 50))

#load thiên thạch rơi
thienthach=pygame.image.load('thienthach.png')
# Scale hình ảnh thiên thạch về kích thước 50x50
thienthach = pygame.transform.scale(thienthach, (50, 50))

#load âm thanh game
soundgame = pygame.mixer.music.load('soundgame.mp3')
pygame.mixer.music.set_volume(0.1)
pygame.mixer.music.play(-1)
sound1=pygame.mixer.Sound('jump.mp3')
sound2=pygame.mixer.Sound('gameover.mp3')
sound3=pygame.mixer.Sound('slash.mp3')
sound4=pygame.mixer.Sound("enemydie1.wav")
sound5=pygame.mixer.Sound("enemydie2.mp3")
sound6=pygame.mixer.Sound("zerodie.mp3")

# Biến boolean để đánh dấu trạng thai của nhân vật
jump=False
zero_run_right=False
zero_run_left=False
zerostandright_check = True
zerostandleft_check=False
zero_attacking = False
zerodie_check = False
# Biến boolean để đánh dấu kẻ địch đã chết hay chưa
enemydie2_check=False
enemydie_check=False
# Biến boolean để đánh dấu âm thanh đã được phát hay chưa
sound_played = False
soundrunning_check = False

#biến để đếm thời gian tăng dộ khó cho game
speed_increment_interval = 900  # 15 giây (60 frame/giây * 15 giây = 900 frame)
speed_increment_counter = 0
# Vòng lặp game
running = True
while running:
    clock.tick(30)
    screen.fill(WHITE)
    background1_rect=screen.blit(background,(background_x,background_y))
    background2_rect=screen.blit(background,(background_x+600,background_y))

    #làm cho nhân vật tấn công
    if zero_attacking and zerostandright_check == True:
        zero_rect = screen.blit(zeroattackright, (zero_x+30, zero_y-50))
        if pygame.time.get_ticks() - attack_time >= 100:
            zero_attacking = False
    elif zero_attacking and zerostandleft_check == True:
        zero_rect = screen.blit(zeroattackleft, (zero_x-50, zero_y-50))
        if pygame.time.get_ticks() - attack_time >= 100:
            zero_attacking = False
    elif zero_attacking and zero_run_right:
        zero_rect = screen.blit(zeroattackright, (zero_x+30, zero_y-50))
        if pygame.time.get_ticks() - attack_time >= 100:
            zero_attacking = False
    elif zero_attacking and zero_run_left:
        zero_rect = screen.blit(zeroattackleft, (zero_x-50, zero_y-50))
        if pygame.time.get_ticks() - attack_time >= 100:
            zero_attacking = False
    #làm cho nhân vật di chuyển
    elif zero_run_right==True:
        zero_x=zero_x+x_velocity
        zero_rect = screen.blit(zeroright[current_frame], (zero_x, zero_y))
    elif zero_run_left==True:
        zero_x=zero_x-(x_velocity*2)
        zero_rect = screen.blit(zeroleft[current_frame], (zero_x, zero_y))
    elif zerostandleft_check == True:
        zero_rect = screen.blit(zerostandleft, (zero_x, zero_y))
        zero_x=zero_x+0
    elif zerostandright_check == True:
        zero_rect = screen.blit(zerostandright, (zero_x, zero_y))
        zero_x=zero_x+0
    elif zerodie_check == True:
        zero_rect = screen.blit(zerodie, (zero_x, zero_y))
        zero_x=zero_x+0
    else:
        zero_rect = screen.blit(zerostandright, (zero_x, zero_y))
        zero_x=zero_x+0
    # Chuyển đổi sang frame hình ảnh tiếp theo sau một khoảng thời gian nhất định
    current_frame = (current_frame + 1) % len(zeroright)
        #làm cho nhân vật nhảy
    if 230>=zero_y>=130:
        if jump==True:
            zero_y-=y_velocity
    else:
        jump=False
    if zero_y<230:
        if jump==False:
            zero_y+=(y_velocity*1.5)
            if zero_y>230:
                zero_y =230
    # Giới hạn di chuyển của nhân vật trong màn hình
    if zero_x < 0:
        zero_x = 0
    elif zero_x > 550:
        zero_x = 550
        
    #xử lý kẻ thù
    if enemydie_check==True:
        enemy_rect = screen.blit(enemydie, (enemy_x, enemy_y))
    else:
        enemy_rect = screen.blit(enemy, (enemy_x, enemy_y))

    if enemydie2_check==True:
        enemy2_rect = screen.blit(enemydie2, (enemy2_x, enemy2_y))
    else:
        enemy2_rect = screen.blit(enemy2, (enemy2_x, enemy2_y))

    #làm cho kẻ thù di chuyển
    enemy_x=enemy_x-x_velocity
    if enemy_x<=-100:
        enemy_x= random.randint(600, 1000)
        enemydie_check=False 

    enemy2_x=enemy2_x-x_velocity
    if enemy2_x<=-100:
        enemy2_x= random.randint(700, 1300)
        enemydie2_check=False 

    #tạo score và highscore
    score_txt=font.render("Score: "+str(score),True,RED)
    screen.blit(score_txt,(5,5))
    score_txt=font.render("HighScore: "+str(highscore),True,RED)
    screen.blit(score_txt,(70,5))
    
    #Xử lý thiên thạch
    for i in range(len(thienthachs)):
        x, y = thienthachs[i]
        y += thienthach_vantoc
        thienthachs[i] = (x, y)
        if y>300:
            y= random.randint(-500, -40)
            x= random.randint(0,600)
        thienthachs[i] = (x, y)
        screen.blit(thienthach, thienthachs[i])
    #làm cho ảnh nền di chuyển
    background_x=background_x-x_velocity
    if background_x+600<=0:
        background_x=0

    #điều kiện thua
    if (zero_rect.colliderect(enemy_rect) and zero_attacking==False and enemydie_check==False) or (zero_rect.colliderect(enemy2_rect) and zero_attacking==False and enemydie2_check==False):
        if not sound_played:
            pygame.mixer.Sound.play(sound2)
            pygame.mixer.Sound.play(sound6)
            sound_played = True
        pausing=True
        gameover_txt=font1.render("GAME OVER!!!!",True,RED)
        screen.blit(gameover_txt,(200,150))
        x_velocity=0 
        y_velocity=0
        thienthach_vantoc=0
        zerodie_check = True
        zerostandright_check = False
        zero_run_left = False
        zero_run_right =False
        zerostandleft_check = False
    for i in thienthachs:
        # Kiểm tra va chạm giữa hai Rect
        thienthach_rect = pygame.Rect(i[0], i[1], 40, 40)
        if zero_rect.colliderect(thienthach_rect):
            if not sound_played:
                pygame.mixer.Sound.play(sound2)
                pygame.mixer.Sound.play(sound6)
                sound_played = True
            gameover_txt=font1.render("GAME OVER!!!!",True,RED)
            screen.blit(gameover_txt,(200,150))
            # Kết thúc trò chơi nếu có va chạm
            pausing = True
            x_velocity=0 
            y_velocity=0
            thienthach_vantoc=0
            zerodie_check = True
            zerostandright_check = False
            zero_run_left = False
            zero_run_right =False
            zerostandleft_check = False
    #xử lý tấn công kẻ thù
    if zero_rect.colliderect(enemy_rect) and zero_attacking == True and not enemydie_check:
        pygame.mixer.Sound.play(sound4)
        score += 1
        enemydie_check=True
        if score>=highscore:
            highscore=score
    if zero_rect.colliderect(enemy2_rect) and zero_attacking == True and not enemydie2_check:
        pygame.mixer.Sound.play(sound5)
        score += 1
        enemydie2_check=True
        if score>=highscore:
            highscore=score

    #Xử lý tăng độ khó cho game
    speed_increment_counter += 1
    if speed_increment_counter >= speed_increment_interval:
        x_velocity = x_velocity + 2  # Tăng tốc độ di chuyển
        thienthach_vantoc = thienthach_vantoc + 2  # Tăng tốc độ rơi của thiên thạch
        speed_increment_counter = 0

    # Các lệnh vẽ và xử lý game ở đây
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
    # Xử lý sự kiện nhấn phím space
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if zero_y == 230:
                    pygame.mixer.Sound.play(sound1)
                    jump = True
                if pausing==True:
                    background_x=0
                    background_y=0
                    zero_x=0
                    zero_y=230
                    enemy_x = random.randint(600, 1000)
                    enemy_y= 230
                    enemy2_x = random.randint(700, 1300)
                    enemy2_y= 100
                    x_velocity=10 
                    y_velocity=10
                    score=0
                    pausing=False
                    sound_played = False
                    enemydie_check=False
                    enemydie2_check=False
                    zerostandright_check = True
                    zero_run_left = False
                    zero_run_right =False
                    zerostandleft_check = False
                    zerodie_check = False
                    for i in range(3):
                        x = random.randint(0, 600)
                        y = random.randint(-500, -40)
                        thienthachs[i] = (x,y)
                    thienthach_vantoc = 5
                    speed_increment_counter = 0
            if pausing==False:
        # Xử lý sự kiện nhấn phím tấn công (phím C)
                if event.key == pygame.K_c:
                    pygame.mixer.Sound.play(sound3)
                    zero_attacking = True
                    attack_time = pygame.time.get_ticks()
                else:
                    zero_attacking = False
        #xử lý sự kiện nhấn phím di chuyển lên
                if event.key == pygame.K_RIGHT:
                    zero_run_right = True
                    zero_run_left = False
                    zerostandleft_check = False
                    zerostandright_check =False
        #xử lý sự kiện nhấn phím di chuyển lui
                if event.key == pygame.K_LEFT:
                    zero_run_left = True
                    zero_run_right = False
                    zerostandleft_check =False
                    zerostandright_check =False

        elif event.type == pygame.KEYUP:
            if pausing == False:
                if event.key == pygame.K_RIGHT:
                    zerostandleft_check = False
                    zero_run_right = False
                    zero_run_left = False
                    zerostandright_check = True
                if event.key == pygame.K_LEFT:
                    zerostandright_check = False
                    zero_run_left = False
                    zero_run_right =False
                    zerostandleft_check = True
    # Cập nhật màn hình
    pygame.display.update()
    # Chờ một khoảng thời gian để hiển thị frame tiếp theo
    pygame.time.delay(int(1000 / frame_rate/2))

# Thoát khỏi Pygame
pygame.quit()