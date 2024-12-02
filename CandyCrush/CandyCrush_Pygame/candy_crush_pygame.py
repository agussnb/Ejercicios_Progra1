import pygame

pygame.init()


screen = pygame.display.set_mode((1000, 800))
pygame.display.set_caption("Candy Crush")


bg_route = 'CandyCrush/CandyCrush_Pygame/images/candy_crash_bg.png'  
try:
    background = pygame.image.load(bg_route)
    background = pygame.transform.scale(background, (1000, 800))
except pygame.error as e:
    print(f"Error al cargar la imagen: {e}")
    pygame.quit()
    quit()
btn_route = 'CandyCrush/CandyCrush_Pygame/images/play_button.png'
try:
    button = pygame.image.load(btn_route)
    button = pygame.transform.scale(button, (100, 200))
except pygame.error as e:
    print(f"Error al cargar la imagen: {e}")
    pygame.quit()
    quit()
button_rect = button.get_rect(center=(500,400))

running = True
while running:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
        if e.type == pygame.MOUSEBUTTONDOWN:
            if button_rect.collidepoint(e.pos):
                pass
    
    screen.blit(background, (0, 0))
    screen.blit(button, button_rect.topleft)
    
    pygame.display.update()

pygame.quit()
