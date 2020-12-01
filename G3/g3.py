
def showgrid():
    for i in range(10):
        print(Rgrid[i])
    print('')
#showgrid()
def can_placeV():
    empty =0
    for i in range(LENGTH[placed]):
        if grid[(cy//75)+i][(cx//75)] == 0:
            empty += 1
    if empty == LENGTH[placed]:
        return True
    else:
        return False
    
def can_placeH():
    empty =0
    for i in range(LENGTH[placed]):
        if grid[(cy//75)][(cx//75)+i] == 0:
            empty += 1
    if empty == LENGTH[placed]:
        return True
    else:
        return False
def Rcan_placeV():
    empty =0
    for i in range(LENGTH[Rplaced]):
        if Rgrid[ry+i][rx] == 0:
            empty += 1
    if empty == LENGTH[Rplaced]:
        return True
    else:
        return False
    
def Rcan_placeH():
    empty =0
    for i in range(LENGTH[Rplaced]):
        if Rgrid[ry][rx+i] == 0:
            empty += 1
    if empty == LENGTH[Rplaced]:
        return True
    else:
        return False


def Rplace():
    global Rplaced,rx,ry,Rgrid,Rboats,RBOATS,Rtypegrid
    while Rplaced < 10:
        rd = random.randint(0,1)
        rx = random.randint(0,9)
        ry = random.randint(0,9)
        if rd == 0:
            if ry < 10-(LENGTH[Rplaced]-1):
                if Rcan_placeV():
                    Rboats[Rplaced] = (rx,ry,0)
                    for i in range(LENGTH[Rplaced]):
                        Rgrid[ry+i][rx] = 1
                        Rtypegrid[ry+i][rx] = boatID[Rplaced]
                    Rplaced += 1
        if rd == 1:
            if rx < 10-(LENGTH[Rplaced]-1):
                if Rcan_placeH():
                    Rboats[Rplaced] = (rx,ry,0)
                    for i in range(LENGTH[Rplaced]):
                        Rgrid[ry][rx+i] = 1
                        Rtypegrid[ry][rx+i] = boatID[Rplaced]
                    RBOATS[Rplaced] = pygame.transform.rotate(RBOATS[Rplaced],270)
                    Rplaced += 1
    #for i in range(10):
        #print(Rtypegrid[i])
    #showgrid()
def Rshoot():
    global grid,lives,turn,SWITCH,SWITCH2,boatsleft,typegrid
    #print(boatsleft)
    for i in range(10):
        for j in range(10):
            if grid[i][j] == 3:
                if i < 9:
                    #print("W")
                    if grid[i+1][j] < 2:
                        rx = j
                        ry = i+1
                        #print(str(rx)+' '+str(ry))
                        #print("Q")
                if i > 0:
                    if grid[i-1][j] < 2:
                        rx = j
                        ry = i-1
                if j < 9:
                    if grid[i][j+1] < 2:
                        rx = j+1
                        ry = i
                if j > 0:
                    if grid[i][j-1] <2:
                        rx = j-1
                        ry = i
    try:
        rx
    except NameError:
        rx = random.randint(0,9)
        ry = random.randint(0,9)
    #print(str(rx)+' '+str(ry))
    if grid[ry][rx] == 1:
        grid[ry][rx] = 3
        typegrid[ry][rx] = 0
        A2,B2,A3,B3,C3,D3,E3,F3,A4,A5 = 0,0,0,0,0,0,0,0,0,0
        for i in range(10):
            if '2a' in typegrid[i]:
                A2 = 1
            if '2b' in typegrid[i]:
                B2 = 1
            if '3a' in typegrid[i]:
                A3 = 1
            if '3b' in typegrid[i]:
                B3 =1
            if '3c' in typegrid[i]:
                C3 = 1
            if '3d' in typegrid[i]:
                D3 = 1
            if '3e' in typegrid[i]:
                E3 = 1
            if '3f' in typegrid[i]:
                F3 = 1
            if '4a' in typegrid[i]:
                A4 = 1
            if '5a' in typegrid[i]:
                A5 = 1
        boatsleft = [A2+B2,A3+B3+C3+D3+E3+F3,A4,A5]
        #print(boatsleft)
        lives -= 1
        SWITCH = 0
        SWITCH2 = 1
        turn = 0
        
    elif grid[ry][rx] == 0:
        grid[ry][rx] = 2
        SWITCH = 0
        SWITCH2 = 1
        turn = 0
        
    else:
        Rshoot()


def end():
    global on
    screen.blit(background,(0,0))
    #screen.fill((0,0,255))
    #for row in range(10):
        #for column in range(10):
            #pygame.draw.rect(screen,(0,255,255),[75 * column,75 * row,75,75],1)
    #pygame.draw.rect(screen,(127,63,0),[750,0,100,750])
    font = pygame.font.SysFont('Calibri',150,True,False)
    if Rlives == 0:
        text = font.render("YOU WIN!",True,(0,0,0))
        text2 = font.render("YOU WIN!",True,(255,255,255))
        for i in range(10):
            screen.blit(RBOATS[i],(int(Rboats[i][0])*75,int(Rboats[i][1])*75))
        for i in range(10):
            for j in range(10):
                if Rgrid[i][j] == 3:
                    pygame.draw.ellipse(screen,(255,0,0),[75*j,75*i,75,75])
    if lives == 0:
        text = font.render("YOU LOSE!",True,(0,0,0))
        text2 = font.render("YOU LOSE!",True,(255,255,255))
        for i in range(10):
            screen.blit(BOATS[i],(int(boats[i][0])*75,int(boats[i][1])*75))
        for i in range(10):
            for j in range(10):
                if grid[i][j] == 3:
                    pygame.draw.ellipse(screen,(255,0,0),[75*j,75*i,75,75])
    screen.blit(text,[0,0])
    screen.blit(text2,[5,0])
    pygame.display.flip()
    while on == 1:
        for event in pygame.event.get():
            if event.type == pygame.KEYUP:
                screen.fill((0,0,0))
                pygame.display.flip()
                Eden.time.sleep(1)
                Eden.size = [850,750]
                Eden.screen = Eden.pygame.display.set_mode(Eden.size,pygame.FULLSCREEN)
                on = 0
                Eden.W = 0
                Eden.player_direction = 1
    
def go():
    global LENGTH,placed,grid,cy,cx,Rplaced,random,Rgrid,Rboats,pygame,RBOATS,lives,Rlives,turn
    global SWITCH,SWITCH2,screen,BOATS,boats,Eden,Rtypegrid,boatID,typegrid,boatsleft,on
    import os
    os.chdir('..')
    import Eden
    if os.path.exists('./data') == True:
        os.chdir('./data')
    import pygame,random,time
    from time import sleep
    pygame.init()
    screen = pygame.display.set_mode((850,750),pygame.FULLSCREEN)
    boat2 = pygame.image.load('boat2.png')
    boat3 = pygame.image.load('boat3.png')
    boat4  = pygame.image.load('boat4.png')
    boat5 = pygame.image.load('boat5.png')
    BOATS = [boat2,boat2,boat3,boat3,boat3,boat3,boat3,boat3,boat4,boat5]
    RBOATS = [boat2,boat2,boat3,boat3,boat3,boat3,boat3,boat3,boat4,boat5]
    LENGTH = [2,2,3,3,3,3,3,3,4,5]
    boatID = ['2a','2b','3a','3b','3c','3d','3e','3f','4a','5a']
    boattype = [2,3,4,5]
    boatsleft = [2,6,1,1]
    Rboatsleft = [2,6,1,1]
    #boats = [0,1,2,3,4,5,6,7,8,9]
    ##for i in range(10):
    ##    boats.append(input('xyd for boat '+str(i+1)+': '))
    ##    BOATS[i] = pygame.transform.rotate(BOATS[i],90*int(boats[i][2]))
    placed = 0
    Rplaced = 0
    lives = 31
    Rlives = 31
    boats = [0,1,2,3,4,5,6,7,8,9]
    Rboats = [0,1,2,3,4,5,6,7,8,9]
    grid = []
    Rgrid = []
    typegrid = []
    Rtypegrid = []
    for row in range(10):
        grid.append([])
        Rgrid.append([])
        typegrid.append([])
        Rtypegrid.append([])
        for column in range(10):
            grid[row].append(0)
            Rgrid[row].append(0)
            typegrid[row].append(0)
            Rtypegrid[row].append(0)
    turn = -1
    ON = True
    SWITCH = 0
    SWITCH2 = 0
    lastclick = 0
    title = 1
    background = pygame.image.load('bbbackground.png')
    TITLE = pygame.image.load('battle boats.png')
    TITLE = pygame.transform.scale(TITLE,(850,750))
    screen.blit(TITLE,(0,0))
    pygame.display.flip()
    while title == 1:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                title = 0
    while Eden.On and on == 1:
        screen.blit(background,(0,0))
        #screen.fill((0,0,255))
        #pygame.display.set_caption("YOU: " + str(lives) + " LIVES LEFT,ENEMY: "+ str(Rlives) + " LIVES LEFT")
        MOUSE = pygame.mouse.get_pos()
        cx = MOUSE[0]
        cy = MOUSE[1]
        for event in pygame.event.get():
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_ESCAPE:
                    screen.fill((0,0,0))
                    pygame.display.flip()
                    Eden.time.sleep(1)
                    Eden.size = [850,750]
                    Eden.screen = Eden.pygame.display.set_mode(Eden.size,pygame.FULLSCREEN)
                    on = 0
                    Eden.W = 0
                    Eden.player_direction = 1
                #print(boatsleft)
                #showgrid()
                #turn = ((turn-1)**2)**0.5
            if event.type == pygame.MOUSEBUTTONUP:
               # showgrid()
                if placed < 10:
                    if event.button == 1 and cx < 750 and cy < (750-(LENGTH[placed]-1)*75):
                        lastclick = 0
                        if can_placeV():
                            boats[placed] = (cx//75,cy//75,0)
                            for i in range(LENGTH[placed]):
                                grid[(cy//75)+i][(cx//75)] = 1
                                typegrid[(cy//75)+i][(cx//75)] = boatID[placed]
                            placed += 1
                    elif event.button == 3 and cx < (750-(LENGTH[placed]-1)*75):
                        lastclick = 1
                        if can_placeH():
                            boats[placed] = (cx//75,cy//75,0)
                            for i in range(LENGTH[placed]):
                                grid[(cy//75)][(cx//75)+i] = 1
                                typegrid[(cy//75)][(cx//75)+i] = boatID[placed]
                            BOATS[placed] = pygame.transform.rotate(BOATS[placed],270)
                            placed += 1
                    if placed == 10:
                        Rplace()
                        turn = 1
                elif turn == 1:
                    if Rgrid[(cy//75)][(cx//75)] == 1:
                        Rgrid[(cy//75)][(cx//75)] = 3
                        Rtypegrid[(cy//75)][(cx//75)] = 0
                        A2,B2,A3,B3,C3,D3,E3,F3,A4,A5 = 0,0,0,0,0,0,0,0,0,0
                        for i in range(10):
                            if '2a' in Rtypegrid[i]:
                                A2 = 1
                            if '2b' in Rtypegrid[i]:
                                B2 = 1
                            if '3a' in Rtypegrid[i]:
                                A3 = 1
                            if '3b' in Rtypegrid[i]:
                                B3 =1
                            if '3c' in Rtypegrid[i]:
                                C3 = 1
                            if '3d' in Rtypegrid[i]:
                                D3 = 1
                            if '3e' in Rtypegrid[i]:
                                E3 = 1
                            if '3f' in Rtypegrid[i]:
                                F3 = 1
                            if '4a' in Rtypegrid[i]:
                                A4 = 1
                            if '5a' in Rtypegrid[i]:
                                A5 = 1
                        Rboatsleft = [A2+B2,A3+B3+C3+D3+E3+F3,A4,A5]
                        Rlives -= 1
                        SWITCH = 1
                    elif Rgrid[(cy//75)][(cx//75)] == 0:
                        Rgrid[(cy//75)][(cx//75)] = 2
                        SWITCH = 1
        if SWITCH == 1:
            turn -= 0.01

            if 0 < turn < 0.02:
                turn = 0
                Rshoot()
        elif SWITCH2 == 1:
            turn += 0.01
            if 0.98 < turn:
                turn = 1
            
                
        if turn <= 0:
            SWITCH = 0
        #for row in range(10):
            #for column in range(10):
                #pygame.draw.rect(screen,(0,255,255),[75 * column,75 * row,75,75],1)
        #pygame.draw.rect(screen,(127,63,0),[750,0,100,750])
        
        font = pygame.font.SysFont('Calibri',50,True,False)
    
        for i in range(4):
            text = font.render(str(boattype[i])+' x '+str(boatsleft[i]),True,(0,0,0))
            screen.blit(text,(750,(75*i)))
            text = font.render(str(boattype[i])+' x '+str(boatsleft[i]),True,(255,255,255))
            screen.blit(text,(752,(75*i)))
        text = font.render('('+str(lives)+')',True,(0,0,0))
        screen.blit(text,(750,300))
        text = font.render('('+str(lives)+')',True,(255,255,255))
        screen.blit(text,(752,300))
        for i in range(4):
            text = font.render(str(boattype[i])+' x '+str(Rboatsleft[i]),True,(0,0,0))
            screen.blit(text,(750,(75*i)+375))
            text = font.render(str(boattype[i])+' x '+str(Rboatsleft[i]),True,(255,0,0))
            screen.blit(text,(752,(75*i)+375))
        text = font.render('('+str(Rlives)+')',True,(0,0,0))
        screen.blit(text,(750,675))
        text = font.render('('+str(Rlives)+')',True,(255,0,0))
        screen.blit(text,(752,675))
        

        if turn < 1:
            for i in range(placed):
                screen.blit(BOATS[i],(int(boats[i][0])*75,int(boats[i][1])*75))
            for i in range(10):
                for j in range(10):
                    if grid[i][j] == 3:
                        pygame.draw.ellipse(screen,(255,0,0),[75*j,75*i,75,75])
                    if grid[i][j] == 2:
                        pygame.draw.ellipse(screen,(255,255,255),[75*j,75*i,75,75])
        else:
            #for i in range(10):
                #screen.blit(RBOATS[i],(int(Rboats[i][0])*75,int(Rboats[i][1])*75))
            for i in range(10):
                for j in range(10):
                    if Rgrid[i][j] == 3:
                        pygame.draw.ellipse(screen,(255,0,0),[75*j,75*i,75,75])
                    if Rgrid[i][j] == 2:
                        pygame.draw.ellipse(screen,(255,255,255),[75*j,75*i,75,75])
        if placed < 10:
            #s = pygame.Surface((75,75*LENGTH[placed]))
            #s.set_alpha(127)
            #s.fill((255,255,255))
            ghost = BOATS[placed]
            if lastclick == 1:
                ghost = pygame.transform.rotate(BOATS[placed],270)
            screen.blit(ghost,(cx-37.5,cy-37.5))
            #screen.blit(s,(cx-37.5,cy-37.5))
            
        #if turn == 0:
           # Rshoot()
        pygame.draw.ellipse(screen,(0,0,0),[cx-5,cy-5,10,10],1)
        pygame.display.flip()
        if Rlives == 0 or lives == 0:
            ON = False
            end()
#turn()
