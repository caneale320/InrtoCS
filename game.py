# Curtis Gore jcg8ma and Caleb Neale can4ku
import pygame
import gamebox
import random

camera = gamebox.Camera(800, 600)
cameratop = 600
camerabottom = 0
cameraleft = 0
cameraright = 800
camera_middlex, camera_middley = camera.width // 2 - 1, camera.height // 2 - 1

student_names = gamebox.from_text(camera_middlex, camera_middley - 80, "Curtis Gore (jcg8ma), Caleb Neale (can4ku)", 40, "green", True)
game_title = gamebox.from_text(camera_middlex, camera_middley - 160, "Frogger", 90, "green", True)
instructions1 = gamebox.from_text(camera_middlex, camera_middley - 30, "Use the arrow keys to get the frog to avoid the obstacles and get the frog to the targets!", 20, "green")
instructions2 = gamebox.from_text(camera_middlex, camera_middley, "Pick up the coin for extra points, and don't let the frog fall in the water! You have 60 seconds to cross.", 20, "green")
startgame = gamebox.from_text(camera_middlex, camera_middley + 30, "Press space to begin!", 20, "green")

camera.clear('black')
camera.draw(student_names)
camera.draw(game_title)
camera.draw(instructions1)
camera.draw(instructions2)
camera.draw(startgame)
camera.display()
start = False
lives = 3
time = 1800
score = 0
reach_mid = False
car1_row1 = gamebox.from_image(500, 510, 'http://images.clipartpanda.com/car-20clip-20art-nTBnoxETA.png')
car1_row1.size = (40,39)
car2_row1 = car1_row1.copy_at(300,510)
car3_row1 = car1_row1.copy_at(100,510)
truck1_row2 = gamebox.from_image(500,470, 'http://images.clipartpanda.com/dump-truck-clipart-black-and-white-dumptruck.png')
truck1_row2.size = (60,39)
truck2_row2 = truck1_row2.copy_at(300,470)
truck3_row2 = truck1_row2.copy_at(100,470)
car1_row3 = gamebox.from_image(500,430, 'http://images.clipartpanda.com/car-20clip-20art-ferrari_car_red.png')
car1_row3.size = (40,39)
car2_row3 = car1_row3.copy_at(300,430)
car3_row3 = car1_row3.copy_at(100,430)
truck1_row4 = truck1_row2.copy_at(500,390)
truck2_row4 = truck1_row2.copy_at(300,390)
truck3_row4 = truck1_row2.copy_at(100,390)
bus1_row5 = gamebox.from_image(500,350, 'https://clipartix.com/wp-content/uploads/2016/04/Cute-school-bus-clip-art-free-clipart-images-3.png')
bus1_row5.size = (80,39)
bus2_row5 = bus1_row5.copy_at(200,350)
turtle1_row7 = gamebox.from_image(600,270, 'http://sweetclipart.com/multisite/sweetclipart/files/turtle_green.png')
turtle1_row7.size = (40,115)
turtle1_row7.rotate(90)
turtle2_row7 = turtle1_row7.copy_at(200,270)
turtle3_row7 = turtle1_row7.copy_at(50,270)
turtle4_row7 = turtle1_row7.copy_at(420,270)
log1_row8 = gamebox.from_image(500,230, 'https://cdn.pixabay.com/photo/2017/01/31/14/13/firewood-2024457_1280.png')
log1_row8.size = (60,35)
log2_row8 = log1_row8.copy_at(350,230)
log3_row8 = log1_row8.copy_at(200,230)
log1_row9 = log1_row8.copy_at(500,190)
log1_row9.size = (160,35)
log2_row9 = log1_row8.copy_at(0,190)
log2_row9.size = (160,35)
turtle1_row10 = turtle1_row7.copy_at(600,150)
turtle2_row10 = turtle1_row7.copy_at(400,150)
turtle3_row10 = turtle1_row7.copy_at(250,150)
turtle4_row10 = turtle1_row7.copy_at(100,150)
log1_row11 = log1_row8.copy_at(500,110)
log1_row11.size = (80,35)
log2_row11 = log1_row8.copy_at(250,110)
log2_row11.size = (80,35)
log3_row11 = log1_row8.copy_at(50,110)
log3_row11.size = (80,35)
water = gamebox.from_color(400, 180, 'dark blue', 800, 230)
start_line = gamebox.from_color(400, 600, 'purple', 800, 135)
mid_line = gamebox.from_color(400, 310, 'purple', 800, 35)
safety = gamebox.from_color(400, 37, 'dark green', 800, 100)
frog = gamebox.from_image(400, 550,'http://pngriver.com/wp-content/uploads/2017/12/download-frog-png-transparent-images-transparent-backgrounds-PNGRIVER-COM-frog-001.png')
frog.size = (40, 40)
time_left = gamebox.from_text(620, 585, 'Time Left:', 40, 'black')
lives_left = gamebox.from_text(120, 585, 'Lives Left:', 40, 'black')
target1 = gamebox.from_image(80, 64,'http://www.stickpng.com/assets/images/58568add4f6ae202fedf2715.png')
target1.size = (40, 40)
target2 = target1.copy_at(240,64)
target2.size = (40, 40)
target3 = target1.copy_at(400,64)
target3.size = (40, 40)
target4 = target1.copy_at(560,64)
target4.size = (40, 40)
target5 = target1.copy_at(720,64)
target5.size = (40, 40)
coin = gamebox.from_image(random.randint(50, 750), random.randint(100, 500),
                        'https://opengameart.org/sites/default/files/styles/thumbnail/public/Coin1.png')
coin.size = (30, 30)

coincount = 0
numwins = 0
ylist = []

def tick(keys):
    """
    :param keys: user input of hitting the keyboard
    :return: Frogger the game
    """

    global start, lives, time, score
    global ylist
    river_safe = False
    if pygame.K_SPACE in keys:
        start = True
    if start == True:
    # Drawing all of the obstacles and background
        camera.clear('black')
        camera.draw(start_line)
        camera.draw(car1_row1)
        camera.draw(car2_row1)
        camera.draw(car3_row1)
        camera.draw(truck1_row2)
        camera.draw(truck2_row2)
        camera.draw(truck3_row2)
        camera.draw(car1_row3)
        camera.draw(car2_row3)
        camera.draw(car3_row3)
        camera.draw(truck1_row4)
        camera.draw(truck2_row4)
        camera.draw(truck3_row4)
        camera.draw(bus1_row5)
        camera.draw(bus2_row5)
        camera.draw(water)
        camera.draw(mid_line)
        camera.draw(turtle1_row7)
        camera.draw(turtle2_row7)
        camera.draw(turtle3_row7)
        camera.draw(turtle4_row7)
        camera.draw(log1_row8)
        camera.draw(log2_row8)
        camera.draw(log3_row8)
        camera.draw(log1_row9)
        camera.draw(log2_row9)
        camera.draw(turtle1_row10)
        camera.draw(turtle2_row10)
        camera.draw(turtle3_row10)
        camera.draw(turtle4_row10)
        camera.draw(log1_row11)
        camera.draw(log2_row11)
        camera.draw(log3_row11)
        camera.draw(safety)
        camera.draw(target1)
        camera.draw(target2)
        camera.draw(target3)
        camera.draw(target4)
        camera.draw(target5)
        camera.draw(coin)
        camera.draw(frog)
    # Setting the moving speeds for all of the obstacles
        car1_row1.x -= 6
        car2_row1.x -= 6
        car3_row1.x -= 6
        truck1_row2.x += 5
        truck2_row2.x += 5
        truck3_row2.x += 5
        car1_row3.x -= 8
        car2_row3.x -= 8
        car3_row3.x -= 8
        truck1_row4.x += 7
        truck2_row4.x += 7
        truck3_row4.x += 7
        bus1_row5.x += 8
        bus2_row5.x += 8
        turtle1_row7.x -= 5
        turtle2_row7.x -= 5
        turtle3_row7.x -= 5
        turtle4_row7.x -=5
        log1_row8.x += 5
        log2_row8.x += 5
        log3_row8.x += 5
        log1_row9.x += 5
        log2_row9.x += 5
        turtle1_row10.x -= 5
        turtle2_row10.x -= 5
        turtle3_row10.x -= 5
        turtle4_row10.x -= 5
        log1_row11.x += 5
        log2_row11.x += 5
        log3_row11.x += 5
    # Movement commands for keyboard input
        if pygame.K_UP in keys:
            if frog.y >= 80:
                frog.y -= 40
                keys.clear()
        elif pygame.K_DOWN in keys:
            if frog.y <= 540:
                frog.y += 40
                keys.clear()
        elif pygame.K_RIGHT in keys:
            if frog.x <= 740:
                frog.x += 40
                keys.clear()
        elif pygame.K_LEFT in keys:
            if frog.x >= 60:
                frog.x -= 40
                keys.clear()
        if frog.touches(coin):
            global coincount
            coincount += 1
            coin.center = (1000, 1000)
    # Instructions for when frog touches a vehicle
        if frog.touches(car1_row1) or frog.touches(car2_row1) or frog.touches(car3_row1):
            frog.center = (400,550)
            lives -= 1
            time = 1800
        elif frog.touches(truck1_row2) or frog.touches(truck2_row2) or frog.touches(truck3_row2):
            frog.center = (400,550)
            lives -= 1
            time = 1800
        elif frog.touches(car1_row3) or frog.touches(car2_row3) or frog.touches(car3_row3):
            frog.center = (400,550)
            lives -= 1
            time = 1800
        elif frog.touches(truck1_row4) or frog.touches(truck2_row4) or frog.touches(truck3_row4):
            frog.center = (400,550)
            lives -= 1
            time = 1800
        elif frog.touches(bus1_row5) or frog.touches(bus2_row5):
            frog.center = (400,550)
            lives -= 1
            time = 1800
    # Instructions for when frog touches water and not a turtle, log, or target
        if frog.touches(turtle1_row7) or frog.touches(turtle2_row7) or frog.touches(turtle3_row7) or frog.touches(turtle4_row7):
            river_safe = True
        elif frog.touches(log1_row8) or frog.touches(log2_row8) or frog.touches(log3_row8):
            river_safe = True
        elif frog.touches(log1_row9) or frog.touches(log2_row9):
            river_safe = True
        elif frog.touches(turtle1_row10) or frog.touches(turtle2_row10) or frog.touches(turtle3_row10) or frog.touches(turtle4_row10):
            river_safe = True
        elif frog.touches(log1_row11) or frog.touches(log2_row11) or frog.touches(log3_row11):
            river_safe = True
        elif frog.touches(target1) or frog.touches(target2) or frog.touches(target3) or frog.touches(target4) or frog.touches(target5):
            river_safe = True
        elif frog.touches(water, -10) and river_safe is False:
            frog.center = (400,550)
            lives -= 1
            time = 1800
        elif frog.touches(safety, -10) and river_safe is False:
            frog.center = (400,550)
            lives -= 1
            time = 1800
    # Making the enemies loop
        if car1_row1.x < -20:
            car1_row1.move(820, 0)
        if car2_row1.x < -20:
            car2_row1.move(820,0)
        if car3_row1.x < -20:
            car3_row1.move(820, 0)
        if truck1_row2.x > 820:
            truck1_row2.move(-830, 0)
        if truck2_row2.x > 820:
            truck2_row2.move(-830,0)
        if truck3_row2.x > 820:
            truck3_row2.move(-830, 0)
        if car1_row3.x < -20:
            car1_row3.move(810, 0)
        if car2_row3.x < -20:
            car2_row3.move(810,0)
        if car3_row3.x < -20:
            car3_row3.move(810, 0)
        if truck1_row4.x > 820:
            truck1_row4.move(-820, 0)
        if truck2_row4.x > 820:
            truck2_row4.move(-820,0)
        if truck3_row4.x > 820:
            truck3_row4.move(-820, 0)
        if bus1_row5.x > 840:
            bus1_row5.move(-820,0)
        if bus2_row5.x > 840:
            bus2_row5.move(-820,0)
        if turtle1_row7.x < -20:
            turtle1_row7.move(820, 0)
        if turtle2_row7.x < -20:
            turtle2_row7.move(820,0)
        if turtle3_row7.x < -20:
            turtle3_row7.move(820, 0)
        if turtle4_row7.x < -20:
            turtle4_row7.move(820,0)
        if log1_row8.x > 840:
            log1_row8.move(-820,0)
        if log2_row8.x > 840:
            log2_row8.move(-820,0)
        if log3_row8.x > 840:
            log3_row8.move(-820,0)
        if log1_row9.x > 860:
            log1_row9.move(-820,0)
        if log2_row9.x > 860:
            log2_row9.move(-820,0)
        if turtle1_row10.x < -20:
            turtle1_row10.move(820, 0)
        if turtle2_row10.x < -20:
            turtle2_row10.move(820,0)
        if turtle3_row10.x < -20:
            turtle3_row10.move(820, 0)
        if turtle4_row10.x < -20:
            turtle4_row10.move(820,0)
        if log1_row11.x > 840:
            log1_row11.move(-820,0)
        if log2_row11.x > 840:
            log2_row11.move(-820,0)
        if log3_row11.x > 840:
            log3_row11.move(-820,0)



    # Drawing and creating all of the items at the bottom of the screen
        if time == 0:
            lives -= 1
            time = 1800
        global numwins
        ylist.append((550 - frog.y) // 40)
        score = (max(ylist)) + (numwins * 20) + (coincount * 20)
        frac = str(int((time % ticks_per_second) / ticks_per_second * 10))
        seconds = str(int((time / ticks_per_second) % 60)).zfill(2)
        concat_timer = seconds + ":" + frac
        timer = gamebox.from_text(720, 585, concat_timer, 40, 'black')
        camera.draw(timer)
        camera.draw(time_left)
        life_str = str(lives)
        life_bar = gamebox.from_text(200, 585, life_str, 40, 'black')
        score_str = str(score)
        score_display = gamebox.from_text(400, 585, 'Score: '+score_str, 40, 'black')
        camera.draw(score_display)
        camera.draw(life_bar)
        camera.draw(lives_left)
        if frog.touches(target2) or frog.touches(target3) or frog.touches(target4) or frog.touches(target5) or frog.touches(target1):
            coinx = random.randint(50, 750)
            coiny = random.randint(100, 500)
            coin.center = (coinx, coiny)
            frog.center = (400, 550)
            numwins += 1
            ylist = []
            time = 1800

        if lives == 0:
            end = gamebox.from_text(400,310, 'Game Over', 40, 'black')
            camera.draw(end)
            gamebox.pause()
    camera.display()
    time -= 1

ticks_per_second = 30
gamebox.timer_loop(30, tick)



