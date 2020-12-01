def openmap():
        import Eden
        Eden.W,Eden.D,Eden.S,Eden.A = 0,0,0,0
        screen = Eden.screen
        pygame = Eden.pygame
        Open = True
        screen.blit(MAP,(0,0))
        font = Eden.pygame.font.SysFont('Calibri', 30, True, False)
        for k in range(10):
            text = font.render(str(k+1), True, Eden.black)
            screen.blit(text, [75*k,0])
        for l in range(10):
            text = font.render(str(l+1), True, Eden.black)
            screen.blit(text, [0,l*75])
        pygame.draw.ellipse(screen,Eden.black,[((1500-Eden.x)/4)-5,((1500-Eden.y)/4)-5,10,10])
        pygame.display.flip()
        while Open:
            for event in pygame.event.get():
                if Eden.controller > 0:
                    if event.type == pygame.JOYBUTTONUP:
                        Open = False
                if event.type == pygame.KEYUP:
                    Open = False
                if event.type == pygame.MOUSEBUTTONUP:
                    Open = False
