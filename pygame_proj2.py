import pygame
import math
import random

############################### Game initializing start ###############################

pygame.init()

clock = pygame.time.Clock()

# Game window setup
window_width = 800
window_height = 600
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Jewel Guardian")

############################### Game initializing end ###############################

############################### Game util start ###############################

def gameOver(score):
    '''
    Function to animate the Game Over screen, providing a textbox to show
    the player that the game has ended and another one showing the player 
    the score they got at the end of the round.
    '''
    game_over_font = pygame.font.Font(None, 74)
    game_over_text = game_over_font.render("Game Over", True, pygame.Color(255, 255, 255))
    score_text = game_over_font.render(f"Score: {score}", True, pygame.Color(255, 255, 255))
    window.fill(pygame.Color(0, 0, 0) )
    window.blit(game_over_text, (200, 200))
    window.blit(score_text, (200, 300))
    pygame.display.flip()
    pygame.time.wait(3000)
    pygame.quit()

def isCollision(game_object1, game_object2):
    '''
    Function to figure out if two game objects are in contact.
    '''
    distance = math.sqrt((math.pow(game_object1.x - game_object2.x, 2)) +
                         (math.pow(game_object1.y - game_object2.y, 2)))
    return distance <= 40

def spawn_enemy():
    '''
    Function to spawn an Enemy object from outside the screen at random
    locations and add them to a list of currently active enemy objects.
    '''
    side = random.choice(['left', 'right', 'top', 'bottom'])
    if side == 'left':
        enemy_x = -30 
        enemy_y = random.randint(0, window_height)
    elif side == 'right':
        enemy_x = window_width + 30  
        enemy_y = random.randint(0, window_height)
    elif side == 'top':
        enemy_x = random.randint(0, window_width)
        enemy_y = -30  
    else:  
        enemy_x = random.randint(0, window_width)
        enemy_y = window_height + 30 

    enemies.append(Enemy("/Users/vedramesh/Desktop/enemies.jpg", enemy_x, enemy_y, width=30, height=30, speed=enemy_speed))

############################### Game object init start ###############################

class GameObject:
    def __init__(self, image_path, position_X, position_Y, dx=0, dy=0, width=50, height=50):
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (width, height))  # Resize the image
        self.x = position_X
        self.y = position_Y
        self.dx = dx
        self.dy = dy

    def move(self):
        '''
        Updates the users position by aggregating the change in x or y distance.
        '''
        self.x += self.dx
        self.y += self.dy

    def draw(self, surface):
        '''
        Draws the object or entity onto the screen at the specific position.
        '''
        surface.blit(self.image, (self.x, self.y))

class Player(GameObject):
    def __init__(self, image_path, player_X, player_Y, width=50, height=50, speed=5):
        GameObject.__init__(self, image_path, player_X, player_Y, width=width, height=height)
        self.speed = speed  

    def update(self, keys_pressed, jewel):
        '''
        Updates movement of player depending on which arrow key is pressed.
        Eg. if up arrow key is pressed, then it updates the change of the players
        position in the y axis. Then the change is aggregated to the players current
        position. However if the player has collided with the jewel it reverts back
        to the original position due to the fact that the jewel isn't penetrable.
        '''
        original_x = self.x
        original_y = self.y

        if keys_pressed[pygame.K_LEFT]:
            self.dx = -self.speed
        elif keys_pressed[pygame.K_RIGHT]:
            self.dx = self.speed
        else:
            self.dx = 0

        if keys_pressed[pygame.K_UP]:
            self.dy = -self.speed
        elif keys_pressed[pygame.K_DOWN]:
            self.dy = self.speed
        else:
            self.dy = 0

        self.move()

        if isCollision(self, jewel):
            self.x = original_x
            self.y = original_y

class Enemy(GameObject):
    def __init__(self, image_path, enemy_X, enemy_Y, width=30, height=30, speed=2):
        GameObject.__init__(self, image_path, enemy_X, enemy_Y, width=width, height=height)
        self.speed = speed  

    def move_towards_jewel(self, jewel):
        '''
        Alters the enemy's movements to make them move towards the jewel from 
        where they spawn from.
        '''
        if self.x < jewel.x:
            self.dx = self.speed
        elif self.x > jewel.x:
            self.dx = -self.speed
        if self.y < jewel.y:
            self.dy = self.speed
        elif self.y > jewel.y:
            self.dy = -self.speed
        self.move()

class Jewel(GameObject):
    def __init__(self, image_path, jewel_X, jewel_Y):
        GameObject.__init__(self, image_path, jewel_X, jewel_Y)

class Bullet:
    def __init__(self, x, y, direction, speed=5):
        self.x = x
        self.y = y
        self.direction = direction
        self.speed = speed
        self.width = 20
        self.height = 10
        self.color = pygame.Color(255, 0, 0)

    def move(self):
        '''
        Moves the bullet horizontally across the screen in different directions.
        The direction attribute is either left (-1) or right (1).
        '''
        self.x += self.speed * self.direction

    def draw(self, surface):
        '''
        Draws the bullet in the form of a triangle using pygame.draw. 
        The triangle would need to be rotated depending on which direction
        it is moving in so that the vertex is facing the direction of movement.
        '''
        if self.direction == 1:  
            points = [(self.x, self.y), (self.x, self.y + self.height), (self.x + self.width, self.y + self.height // 2)]
        else:  
            points = [(self.x + self.width, self.y), (self.x + self.width, self.y + self.height), (self.x, self.y + self.height // 2)]
        pygame.draw.polygon(surface, self.color, points)

player = Player("/Users/vedramesh/Desktop/racecar.jpg", window_width // 2 - 25, window_height // 2 + 200, speed=7)
jewel = Jewel("/Users/vedramesh/Desktop/jewel.jpg", window_width // 2 - 25, window_height // 2 - 25)
enemies = []  # Initial empty list of enemies
bullets = []  # List to hold active bullets shot
bullet_timer = 0  # Timer to control when new bullets spawn
enemy_spawn_timer = 0  # Timer to control when new enemies spawn
jewel_protection_timer = 0  # Timer to track points for protecting the jewel
score = 0 # Initialize the player's score
enemy_speed = 2  # Speed for all enemies

############################### Game object init end ###############################

# Game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update game logic
    keys_pressed = pygame.key.get_pressed()
    player.update(keys_pressed, jewel)

    # Spawn enemies outside the screen
    enemy_spawn_timer += 1
    if enemy_spawn_timer > 60:
        spawn_enemy()
        enemy_spawn_timer = 0

    # Move enemies toward the jewel
    for enemy in enemies[:]:
        enemy.move_towards_jewel(jewel)
        if isCollision(player, enemy):
            enemies.remove(enemy)  # Remove enemy when collided with player
            score += 3  # Add 3 points for destroying an enemy
        elif isCollision(enemy, jewel):
            gameOver(score)

    # Spawn bullets randomly from left or right every 2 seconds
    bullet_timer += 1
    if bullet_timer > 120:  
        y_position = random.randint(0, window_height - 10)
        if random.choice([True, False]):
            bullets.append(Bullet(0, y_position, direction=1))  # From the left
        else:
            bullets.append(Bullet(window_width, y_position, direction=-1))  # From the right
        bullet_timer = 0

    for bullet in bullets:
        bullet.move()
        if isCollision(player, bullet):  
            gameOver(score)

    jewel_protection_timer += 1
    if jewel_protection_timer >= 600:  
        score += 5  
        jewel_protection_timer = 0

    window.fill(pygame.Color(0, 0, 0) ) 
    jewel.draw(window)
    player.draw(window)

    for enemy in enemies:
        enemy.draw(window)

    for bullet in bullets:
        bullet.draw(window)

    font = pygame.font.Font(None, 36)
    score_text = font.render(f"Score: {score}", True, pygame.Color(255, 255, 255))
    window.blit(score_text, (10, 10))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
