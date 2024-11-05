def main():

    import pygame

    pygame.init()
    screen = pygame.display.set_mode((640,480))
    pygame.display.set_caption("Trampoline jump")
    background = pygame.Surface(screen.get_size())
    background.fill(pygame.Color(173, 216, 230))
  
    
    lucas = pygame.image.load("lucas.png")
    lucas = lucas.convert_alpha()
    lucas = pygame.transform.scale(lucas, (55,155))
    lucas_x = 300
    lucas_y = 100
    
    trampoline = pygame.image.load("trampoline.png")
    trampoline = trampoline.convert_alpha()
    trampoline = pygame.transform.scale(trampoline, (200,100))


    clock = pygame.time.Clock()
    keepGoing = True
    movingUp = False
    while keepGoing:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
    
        screen.blit(background, (0,0))
        screen.blit(lucas, (lucas_x,lucas_y))
        screen.blit(trampoline, (220,380))
        
        pygame.display.flip()
        
        
        
        if movingUp:
            lucas_y -= 5
            if lucas_y < 0:
                movingUp = False
        else:
            lucas_y += 5
            if lucas_y > 260:
                movingUp = True
            
             

main()
pygame.quit()
