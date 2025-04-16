import pygame

print('Setup Start')
pygame.quit()
window = pygame.display.set_mode(size=(600,600))

print('Loop Start')
while True:
    # Check for all events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
