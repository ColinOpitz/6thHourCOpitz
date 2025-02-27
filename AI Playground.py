import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math
import random

# Initialize pygame
pygame.init()

# Set up window
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT), DOUBLEBUF | OPENGL)
pygame.display.set_caption("First Person Shooter")

# Set up perspective projection
gluPerspective(45, (WIDTH / HEIGHT), 0.1, 50.0)
glTranslatef(0.0, 0.0, -5)

# Player variables
player_pos = [0, 0, 0]
player_rot = [0, 0]  # Rotation in x and y axis for camera view
player_speed = 0.1
player_angle = 0

# Bullet variables
bullets = []
bullet_speed = 0.2

# Enemy variables
enemies = []
enemy_speed = 0.05

# Keybindings
moving_keys = {
    K_a: 'left',
    K_d: 'right',
    K_w: 'forward',
    K_s: 'backward',
}

# Camera movement
def move_camera(keys):
    global player_pos, player_rot, player_angle
    if keys[K_w]:
        player_pos[2] += player_speed * math.cos(math.radians(player_angle))
        player_pos[0] -= player_speed * math.sin(math.radians(player_angle))
    if keys[K_s]:
        player_pos[2] -= player_speed * math.cos(math.radians(player_angle))
        player_pos[0] += player_speed * math.sin(math.radians(player_angle))
    if keys[K_a]:
        player_pos[2] -= player_speed * math.cos(math.radians(player_angle + 90))
        player_pos[0] -= player_speed * math.sin(math.radians(player_angle + 90))
    if keys[K_d]:
        player_pos[2] += player_speed * math.cos(math.radians(player_angle + 90))
        player_pos[0] += player_speed * math.sin(math.radians(player_angle + 90))

def rotate_camera(mouse_x, mouse_y):
    global player_rot, player_angle
    player_rot[0] += mouse_x * 0.1
    player_rot[1] += mouse_y * 0.1

    player_angle = player_rot[0] % 360

# Draw player (as a simple cube for now)
def draw_player():
    glPushMatrix()
    glTranslatef(player_pos[0], player_pos[1], player_pos[2])
    glColor3fv((0, 1, 0))
    glutSolidCube(1)
    glPopMatrix()

# Draw bullet
def draw_bullet(bullet):
    glPushMatrix()
    glTranslatef(bullet[0], bullet[1], bullet[2])
    glColor3fv((1, 1, 1))
    glutSolidSphere(0.1, 20, 20)
    glPopMatrix()

# Shoot bullets
def shoot():
    global bullets
    bullet_x = player_pos[0] + math.sin(math.radians(player_angle))
    bullet_z = player_pos[2] + math.cos(math.radians(player_angle))
    bullets.append([bullet_x, player_pos[1], bullet_z])

# Move bullets
def move_bullets():
    global bullets
    for bullet in bullets[:]:
        bullet[0] += bullet_speed * math.sin(math.radians(player_angle))
        bullet[2] += bullet_speed * math.cos(math.radians(player_angle))
        if bullet[2] > 5 or bullet[2] < -5:  # Bullet out of bounds
            bullets.remove(bullet)

# Enemy movement
def move_enemies():
    global enemies
    for enemy in enemies[:]:
        enemy[2] -= enemy_speed  # Move toward the player
        if enemy[2] < -5:
            enemies.remove(enemy)

# Basic collision detection for shooting
def check_collisions():
    global bullets, enemies
    for bullet in bullets[:]:
        for enemy in enemies[:]:
            if abs(bullet[0] - enemy[0]) < 1 and abs(bullet[2] - enemy[2]) < 1:
                bullets.remove(bullet)
                enemies.remove(enemy)
                break

# Draw the scene
def draw_scene():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()

    glTranslatef(0, 0, -5)  # Move the camera back

    # Player's perspective
    glRotatef(player_rot[1], 1, 0, 0)
    glRotatef(player_rot[0], 0, 1, 0)
    draw_player()

    # Draw bullets
    for bullet in bullets:
        draw_bullet(bullet)

    # Draw enemies
    for enemy in enemies:
        draw_enemy(enemy)

    pygame.display.flip()

# Draw enemy (as a simple cube for now)
def draw_enemy(enemy):
    glPushMatrix()
    glTranslatef(enemy[0], enemy[1], enemy[2])
    glColor3fv((1, 0, 0))
    glutSolidCube(1)
    glPopMatrix()

# Main game loop
def game_loop():
    global player_pos, bullets, enemies

    run_game = True
    while run_game:
        keys = pygame.key.get_pressed()
        mouse_x, mouse_y = pygame.mouse.get_rel()

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run_game = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    shoot()

        move_camera(keys)
        rotate_camera(mouse_x, mouse_y)

        move_bullets()
        move_enemies()
        check_collisions()

        # Spawn enemies
        if random.random() < 0.02:
            enemies.append([random.uniform(-2, 2), 0, random.uniform(5, 10)])

        # Draw the scene
        draw_scene()

        pygame.time.wait(10)

    pygame.quit()

# Start the game
game_loop()
