import sys
from optimizer import *
best_distance = []
# Initialize Pygame
pygame.init()
# Set the dimensions of the window

screen = pygame.display.set_mode((width, height))

# Set the background color to black
background_color = (0, 0, 0, 100)
GENERATION = 500 * N
# Main game loop
if __name__ == "__main__":

    optimizer = Optimizer(screen)
    generation = 1
    while generation <= GENERATION:
        print(f"----------------Generation: {generation}")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Fill the screen with the background color
        screen.fill(background_color)

        # Other game logic and drawing would go here
        optimizer.createPopulation()
        optimizer.prepareMatingPool()
        best_distance.append(optimizer.draw())
        # Update the display
        pygame.display.flip()
        pygame.time.delay(2)
        generation += 1

    # Quit Pygame
    print_(f"Shortest Distance : {best_distance[-1]}")
    plt.plot(list(range(GENERATION)), best_distance)
    plt.show()
    pygame.quit()
    sys.exit()
