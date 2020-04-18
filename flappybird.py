import pygame
import gamebox
import random

camera = gamebox.Camera(800, 600)
cameratop = 600
camerabottom = 0
cameraleft = 0
cameraright = 800
camera_middlex, camera_middley = camera.width // 2 - 1, camera.height // 2 - 1

background = gamebox.from_image(camera_middlex, camera_middley,
                                "https://batchloaf.files.wordpress.com/2014/03/background.png")
bird = gamebox.from_image(camera_middlex, camera_middley,
                          "https://vignette.wikia.nocookie.net/fantendo/images/8/85/Flappy_Bird.png")
bird.scale_by(.3)

tube_top = gamebox.from_color(700, 450, 'green', 75, random.randint(100, 400))
tube_bottom = gamebox.from_color(700, 50, 'green', 75, random.randint(100, 400))


ticks = 0
tubes = []


def tick(keys):
    """

    :param keys: user input of hitting the space bar or clicking
    :return: the flappy bird game
    """

    global ticks
    ticks += 1

    if pygame.K_SPACE in keys:
        bird.speedy = 0
        bird.speedy -= 15
        bird.y += bird.speedy
        keys.remove(pygame.K_SPACE)

    if camera.mouseclick:
        bird.speedy = 0
        bird.speedy -= 15
        bird.y += bird.speedy

    bird.x += 7
    bird.speedy += 2
    bird.move_speed()

    camera.x = bird.x
    background.x = camera.x + 15

    camera.draw(background)
    camera.draw(bird)

    if ticks % 50 == 0:
        new_tube_bottom = gamebox.from_color(camera.right + 100, 450, 'green', 75, random.randint(100, 300))
        new_tube_top = gamebox.from_color(camera.right + 100, 50, 'green', 75, random.randint(100, 300))
        tubes.append(new_tube_bottom)
        tubes.append(new_tube_top)

    for tube in tubes:
        if tube.right < camera.left - 5:
            tubes.remove(tube)
        camera.draw(tube)
        bird.move_to_stop_overlapping(tube)

    if ticks > 75:
        score = gamebox.from_text(bird.x, 50, str((ticks - 75) // 50), 50, 'white')
        camera.draw(score)

    if bird.y > cameratop or bird.y < camerabottom:
        game_over = gamebox.from_text(bird.x, 100, 'GAME OVER', 50, 'red')
        camera.draw(game_over)
        gamebox.pause()

    for tube in tubes:
        if bird.touches(tube):
            game_over = gamebox.from_text(bird.x, 100, 'GAME OVER', 50, 'red')
            camera.draw(game_over)
            gamebox.pause()

    camera.display()


ticks_per_second = 30
gamebox.timer_loop(30, tick)
