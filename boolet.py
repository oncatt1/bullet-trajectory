import pygame
import sys
import math

pygame.init()
width, height = 1400, 600
screen = pygame.display.set_mode((width,height))
clock = pygame.time.Clock()
running = True

font = pygame.font.Font(None, 20)

v0 = 200
angle = 45
g = 9.81

time_steps = 1000
scaling = 5



theta = math.radians(angle)
timeOfFlight = (2 * v0 * math.sin(theta)) / g
trajectory = [] 


for i in range(time_steps + 1):
    t = timeOfFlight * (i / time_steps)
    s = t * v0
    x = v0 * math.cos(theta) * t
    y = (v0 * math.sin(theta) * t) - (0.5 * g * t ** 2)
    trajectory.append(( (x / scaling) + 50, height - (y / scaling) - 40 , t, s))

for point in trajectory:
    print(f"x: {point[0]:.2f}, y: {point[1]:.2f}, time: {point[2]:.2f}s, distance: {point[3]:.2f}m")

print(f"{trajectory[0][0]}, {trajectory[0][1]}")
print(f"{trajectory[time_steps // 2][0]}, {trajectory[time_steps // 2][1]}")
print(f"{trajectory[time_steps][0]}, {trajectory[time_steps][1]}")

screen.blit(font.render(f'{trajectory[time_steps // 2][3]:.0f}',0,"white"),(trajectory[time_steps // 2][0], height - 35))
#screen.blit(font.render(f'{0}',0,"white"),(0,int(trajectory[1] / i)))
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    for point in trajectory:
        if 0 <= point[0] < width and 0 <= point[1] < height:
            screen.set_at((int(point[0]), int(point[1])), (255, 255, 255))

    for i in range(width-20):
        screen.set_at((i+40, height - 40 + 1), "blue")

    for i in range(height-55):
        screen.set_at((40 - 1, i + 15), "blue")

    screen.blit(font.render(f'Initial velocity: {v0}m/s,    Angle: {angle}*,    Gravity: {g}m/s^2', 0, "white"),(10, height - 15))
    screen.blit(font.render('Height [m]', 0, "white"),(0,0))
    screen.blit(font.render('Distance [m]', 0, "white"),(width - 80, height - 15))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()