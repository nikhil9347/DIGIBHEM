import pygame
import sys
import random
pygame.init()


# Constants
WIDTH, HEIGHT = 400, 400
GRID_SIZE = 20
GRID_WIDTH = WIDTH // GRID_SIZE
GRID_HEIGHT = HEIGHT // GRID_SIZE
score =0
head_x = 0
head_y = 0
food_x =0
food_y =0

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255) 

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

class Snake:
    def __init__(self):
        self.body = [(GRID_WIDTH // 2, GRID_HEIGHT // 2)]
        self.direction = (1, 0)  # Initial direction: right

    def move(self, food):
        # Move the snake by adding a new head in the current direction
        new_head = ((self.body[0][0] + self.direction[0]) % GRID_WIDTH, (self.body[0][1] + self.direction[1]) % GRID_HEIGHT)
        self.body.insert(0, new_head)

        # Check if the snake ate the food
        if self.body[0] == food:
            return True
        else:
            self.body.pop()  # Remove the tail
            return False

    def change_direction(self, new_direction):
        # Prevent the snake from reversing
        if (new_direction[0], new_direction[1]) != (-self.direction[0], -self.direction[1]):
            self.direction = new_direction
            
class Food:            

      def __init__(self):
        self.position = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))

      def respawn(self):
        self.position = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))
class snake_eats_food:        
      def snake_eats_food(head_x, head_y, food_x, food_y):
    # Check if the snake's head coordinates match the food coordinates
       if head_x == food_x and head_y == food_y:
        return True
       else:
        return False  
snake = Snake()
food = Food()
game_over = False

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                snake.change_direction((0, -1))
            elif event.key == pygame.K_DOWN:
                snake.change_direction((0, 1))
            elif event.key == pygame.K_LEFT:
                snake.change_direction((-1, 0))
            elif event.key == pygame.K_RIGHT:
                snake.change_direction((1, 0))
            if snake_eats_food():
             score += 10
                
            if event.key == pygame.K_r:
                # Restart the game
                game_over = False
                score = 0    


    food_eaten = snake.move(food.position)

    if food_eaten:
        food.respawn()

    # Check for collisions with walls or itself
    # Assuming snake_head_x and snake_head_y are the coordinates of the snake's head
# screen_width and screen_height are the dimensions of the game screen

    if (head_x>= GRID_WIDTH or head_x < 0 or
        head_y>= GRID_HEIGHT  or head_y < 0):
      game_over = True
    # Clear the screen
    screen.fill(WHITE)

    # Draw the snake
    for segment in snake.body:
        pygame.draw.rect(screen, GREEN, (segment[0] * GRID_SIZE, segment[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE))
        # Draw the snake's head (you can use a different color if you like)
        head_x, head_y = snake.body[0]
    pygame.draw.rect(screen, BLUE, (head_x * GRID_SIZE, head_y * GRID_SIZE, GRID_SIZE, GRID_SIZE))      
    # Draw the food
    pygame.draw.rect(screen, RED, (food.position[0] * GRID_SIZE, food.position[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE))

    pygame.display.update()

    pygame.time.delay(150)  # Delay to control the game speed
    # Display the final score
font = pygame.font.Font(None, 36)
text = font.render(f"Score: {score}", True, (255, 255, 255))
text_rect = text.get_rect()
text_rect.center = (GRID_WIDTH // 2, GRID_HEIGHT // 2)
screen.blit(text, text_rect)
pygame.display.update()
    

pygame.quit()
sys.exit()



