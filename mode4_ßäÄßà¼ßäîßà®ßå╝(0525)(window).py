# 5월 21일
# mode2 + 위치 랜덤

import turtle as t
import random

#######################################
# 게임 설정
#######################################
score = 0
maxscore = 5
life = 3

# ===== 모니아: 적 피격 상태 변수 =====
#적 상태 변수 (피격 여부 관리)
enemy_hit = [False, False, False, False]
bubble_active = [False, False, False, False, False]
#######################################
# 첫번째 : 화면 객체
#######################################
screen = t.Screen()
screen.setup(600, 500)   	# 화면 크기(폭,높이)
screen.bgpic('C:\\/bg.png')   # C:\\ 바로밑에, D:\\ 바로밑에
screen.bgcolor("black")

imgta = "C:\\ta.gif"
imgbk = "C:\\blank.gif"

imge1 = "C:\\enemy1.gif"
imge2 = "C:\\enemy2.gif"
imge3 = "C:\\enemy3.gif"
imge4 = "C:\\enemy4.gif"

imgb1 = "C:\\bubble1.gif"
imgb2 = "C:\\bubble2.gif"
imgb3 = "C:\\bubble3.gif"
imgb4 = "C:\\bubble4.gif"
imgb5 = "C:\\bubble5.gif"

imgi1 = "C:\\einb1.gif"
imgi2 = "C:\\einb2.gif"
imgi3 = "C:\\einb3.gif"
imgi4 = "C:\\einb4.gif"

screen.register_shape(imgta)
screen.register_shape(imgbk)
screen.register_shape(imge1)
screen.register_shape(imge2)
screen.register_shape(imge3)
screen.register_shape(imge4)
screen.register_shape(imgb1)
screen.register_shape(imgb2)
screen.register_shape(imgb3)
screen.register_shape(imgb4)
screen.register_shape(imgb5)
screen.register_shape(imgi1)
screen.register_shape(imgi2)
screen.register_shape(imgi3)
screen.register_shape(imgi4)

screen.listen( )         	# 키보드 이벤트 등 활성화

#######################################
# 두번째 : 텍스트 객체
#######################################
# 목숨
texta = t.Turtle()
texta.penup()
texta.hideturtle()
texta.goto(-150,200)
texta.color("white")
texta.write("목숨 : 3︎",False,"center",("굴림체",16))
# 점수
textscore = t.Turtle()
textscore.penup()
textscore.hideturtle()
textscore.goto(150,200)
textscore.color("white")
textscore.write("점수 : 0",False,"center",("굴림체",16))

#######################################
# 세번째 : 거북이 객체
#######################################
# 1. 주인공 거북이 ta 설정
ta = t.Turtle()
ta.shape(imgta)
ta.speed(0)   
ta.up()
ta.goto(0, -180)

# 2. 악당 거북이 enemy
# ===== 모니아: 적 4마리 생성 =====
enemy1 = t.Turtle() 	# 악당 거북이()
enemy1.shape(imge1)
enemy1.speed(0)
enemy1.up()
enemy1.goto(random.randint(-260, 260), random.randint(300, 800))

enemy2 = t.Turtle()
enemy2.shape(imge2)
enemy2.speed(0)
enemy2.up()
enemy2.goto(random.randint(-260, 260), random.randint(300, 800))

enemy3 = t.Turtle()
enemy3.shape(imge3)
enemy3.speed(0)
enemy3.up()
enemy3.goto(random.randint(-260, 260), random.randint(300, 800))

enemy4 = t.Turtle()
enemy4.shape(imge4)
enemy4.speed(0)
enemy4.up()
enemy4.goto(random.randint(-260, 260), random.randint(300, 800))

#여러 적을 리스트로 관리
enemies = [enemy1, enemy2, enemy3, enemy4]
enemy_img = [imge1, imge2, imge3, imge4]
enemy_img_hit = [imgi1, imgi2, imgi3, imgi4]

# 3. 버블 item
bubble1 = t.Turtle() 
bubble1.shape(imgb1)
bubble1.speed(0)
bubble1.up()
bubble1.goto(0, -1000)     # 화면 밖으로 숨김

bubble2 = t.Turtle() 
bubble2.shape(imgb2)
bubble2.speed(0)
bubble2.up()
bubble2.goto(0, -1000)     # 화면 밖으로 숨김

bubble3 = t.Turtle() 
bubble3.shape(imgb3)
bubble3.speed(0)
bubble3.up()
bubble3.goto(0, -1000)     # 화면 밖으로 숨김

bubble4 = t.Turtle() 
bubble4.shape(imgb4)
bubble4.speed(0)
bubble4.up()
bubble4.goto(0, -1000)     # 화면 밖으로 숨김

bubble5 = t.Turtle() 
bubble5.shape(imgb5)
bubble5.speed(0)
bubble5.up()
bubble5.goto(0, -1000)     # 화면 밖으로 숨김

bubbles = [bubble1, bubble2, bubble3, bubble4, bubble5]

#######################################
# 함수 정의
#######################################
# 1.키보드 이벤트 관련 함수 정의
def turn_right():      # 오른쪽으로 방향을 바꿉니다.
    if ta.xcor() < 260:
        ta.setheading(0)
        ta.setx(ta.xcor() + 10)

def turn_left():    # 왼쪽으로 방향을 바꿉니다.
    if ta.xcor() > -260:
        ta.setheading(180)        
        ta.setx(ta.xcor() - 10)

# 2.목숨과 점수를 표시하는 함수
def ftext():
    global score, life
    
    texta.clear()
    postext = "목숨 : "+str( life )
    texta.write( postext, False, "center", ("굴림체",16) )
    textscore.clear()
    textscore.write( "점수 : "+str(score), False, "center", ("굴림체",16) )

# 3. 가장자에 도착하면 방향을 뒤집
'''
    def clamp(t):
    if t.xcor() >= 280:
        t.setheading(180)

    if t.xcor() <= -280:
        t.setheading(0)
'''

# 4. 공격
def shoot():
    global bubble_active
    for i, bubble in enumerate(bubbles):
        if not bubble_active[i]:                       # 버블이 대기중일 때만 발사
            bubble_active[i] = True
            bubble.goto(ta.xcor(), ta.ycor())               # 플레이어 위치에서 시작
            break

# 재시작
def restart():
    global score, life, enemy_hit, bubble_active

    score = 0
    life = 3

    enemy_hit = [False, False, False, False]
    bubble_active = [False, False, False, False, False]

    ta.goto(0, -180)

    for i, enemy in enumerate(enemies):
        # enemy.goto(enemy_starts[i])
        enemy.shape(enemy_img[i])

    for bubble in bubbles:
        bubble.goto(0, -1000)
    
    texta.clear()
    textscore.clear()
    texta.goto(-150, 200)                    # ← 원래 위치로
    ftext()
    play()

# 5.play 함수 정의 : 0.1초마다 실행됩니다.
def play():     	# 게임을 실제로 플레이하는 함수입니다.
    global score, maxscore, life, enemy_hit, bubble_active

    for i, enemy in enumerate(enemies):
        if not enemy_hit[i]: # 피격 아니면

            if enemy.ycor() > -150:
                ang = enemy.towards(ta.pos())
                enemy.setheading(ang)             	# 악당 거북이의 방향을 주인공 거북이를 향하도록 맞춥니다
            
            else:
                enemy.setheading(270)


            if ta.distance(enemy) < 10 :
                life -= 1
                enemy_hit[i] = True
                enemy.shape(imgbk)                
                enemy.setheading(270)
                enemy.sety(enemy.ycor() - 50)


        else: # 피격이면
            enemy.setheading(270)

            if ta.distance(enemy) < 10 :
                score += 1
                enemy.goto(0, -1000)  # 바로 제거
                enemy_hit[i] = False
                enemy.shape(enemy_img[i])
                enemy.goto(random.randint(-260, 260), random.randint(300, 800))

        enemy.forward(9)

        if enemy.ycor() < -300:
            enemy_hit[i] = False
            enemy.shape(enemy_img[i])
            enemy.goto(random.randint(-260, 260), random.randint(300, 800))


    for i, bubble in enumerate(bubbles):
        if bubble_active[i]:
            bubble.sety(bubble.ycor() + 10)          # y값 10씩 증가

        if bubble.ycor() > 250:                      # 최상단 도달
            bubble.goto(0, -1000)                   # 보이지 않는 위치로
            bubble_active[i]  = False
            continue
    
        for j, enemy in enumerate(enemies):
            if not enemy_hit[j] and bubble.distance(enemy) < 20:
                bubble.goto(0, -1000)
                bubble_active[i] = False
                enemy_hit[j] = True
                enemy.shape(enemy_img_hit[j])
                break

    ftext()  # 주인공과 악당의 좌표를 보여줍니다.

    if life > 0 and score < maxscore:
        screen.ontimer(play, 100)           # 0.1초후 play 함수를 실행합니다(게임을 계속 합니다).

    if life <= 0:
        texta.goto(0, -50)
        texta.color("white")
        texta.write("YOU LOSE\nRESTART: PRESS 'R'", False, "center", ("굴림체", 48, "bold"))

    if score >= maxscore:
        texta.goto(0, -50)
        texta.color("white")
        texta.write("YOU WIN\nRESTART: PRESS 'R'", False, "center", ("굴림체", 48, "bold"))


#######################################
# 이벤트 정의 및 play( ) 함수 호출
#######################################
# 키보드 클릭 이벤트
screen.onkeypress(turn_right, "Right")
screen.onkeypress(turn_left, "Left")
screen.onkeypress(shoot, "s")
screen.onkeypress(restart, "r")


# play( ) 함수 호출
play()
screen.mainloop()

