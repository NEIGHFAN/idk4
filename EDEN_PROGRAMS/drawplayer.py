def go():
    import pygame,time,Eden,os,random
    global P,player
    P = Eden.PF
    pygame.init()
##    foot1 = pygame.mixer.Sound('foot1.wav')
##    foot2 = pygame.mixer.Sound('foot2.wav')
##    foot3 = pygame.mixer.Sound('foot3.wav')
##    foot4 = pygame.mixer.Sound('foot4.wav')
##    foot5 = pygame.mixer.Sound('foot5.wav')
    feet = [foot1,foot2,foot3,foot4,foot5]
    foot = feet[random.randint(0,4)]
    FACE = (255,0,0,255)
    EYES = (0,127,255,255)
    HAT = (255,0,255,255)
    HAIR = (127,0,255,255)
    FHAIR = (255,255,0,255)
    HATS = (255,0,127,255)
    HATB = (0,255,127,255)
    BODY = (0,0,255,255)
    SHOULDERS = (127,0,0,255)
    ARMS = (127,0,127,255)
    GLOVES = (0,0,0,255)
    LEGS = (0,255,0,255)
    DRESS = (127,255,0,255)
    SHOES = (0,255,255,255)
    cred = Eden.cred
    cgreen = Eden.cgreen
    cblue = Eden.cblue
    face = (cred[0],cgreen[0],cblue[0],255)
    hat = (cred[1],cgreen[1],cblue[1],255) 
    hats = (cred[2],cgreen[2],cblue[2],255)
    hair = (cred[3],cgreen[3],cblue[3],255)
    body = (cred[4],cgreen[4],cblue[4],255) 
    arms = (cred[5],cgreen[5],cblue[5],255) 
    legs = (cred[6],cgreen[6],cblue[6],255) 
    shoes = (cred[7],cgreen[7],cblue[7],255) 
    gloves = (cred[8],cgreen[8],cblue[8],255) 
    shoulders = (cred[9],cgreen[9],cblue[9],255)
    os.chdir('../EDEN_PICS')
    pI  = pygame.image.load('playerB-i.png')
    pB  = pygame.image.load('playerB.png')
    pB1 = pygame.image.load('playerB-r1.png')
    pB2 = pygame.image.load('playerB-r2.png')
    pB3 = pygame.transform.flip(pB1,True,False)
    pB4 = pygame.transform.flip(pB2,True,False)
    pw = [pB,pB1,pB2,pB1,pB,pB3,pB4,pB3]
    pF = pygame.image.load('playerF.png')
    pF1 = pygame.image.load('playerF-r1.png')
    pF2 = pygame.image.load('playerF-r2.png')
    pF3 = pygame.transform.flip(pF1,True,False)
    pF4 = pygame.transform.flip(pF2,True,False)
    ps = [pF,pF1,pF2,pF1,pF,pF3,pF4,pF3]
    pL = pygame.image.load('playerS.png')
    pL1 = pygame.image.load('playerS-r1.png')
    pL2 = pygame.image.load('playerS-r2.png')
    pL3 = pygame.image.load('playerS-r3.png')
    pL4 = pygame.image.load('playerS-r4.png')
    pa = [pL,pL1,pL2,pL1,pL,pL3,pL4,pL3]
    pR = pygame.transform.flip(pL,True,False)
    pR1 = pygame.transform.flip(pL1,True,False)
    pR2 = pygame.transform.flip(pL2,True,False)
    pR3 = pygame.transform.flip(pL3,True,False)
    pR4 = pygame.transform.flip(pL4,True,False)
    pd = [pR,pR1,pR2,pR1,pR,pR3,pR4,pR3]
    if Eden.player_direction == 0:
        player = pB
        if Eden.W == 1 and Eden.moveup == 1:
            player = pw[P]
            if P == (2 or 6):
                Eden.channel2.play(foot)
            P += 1
            if P >= len(pw):
                P = 0
    elif Eden.player_direction == 1:
        player = pF
        if Eden.S == 1 and Eden.movedown == 1:
            player = ps[P]
            if P == (2 or 6):
                Eden.channel2.play(foot)
            P += 1
            if P >= len(ps):
                P = 0
    elif Eden.player_direction == 2:
        player = pR
        if Eden.D == 1 and Eden.moveright == 1:
            player = pd[P]
            if P == (2 or 6):
                Eden.channel2.play(foot)
            P += 1
            if P >= len(pd):
                P = 0
    elif Eden.player_direction == 3:
        player = pL
        if Eden.A == 1 and Eden.moveleft == 1:
            player = pa[P]
            if P == (2 or 6):
                Eden.channel2.play(foot)
            P += 1
            if P >= len(pa):
                P = 0
    if Eden.doing == 1:
        if Eden.igrid[Eden.gy][Eden.gx] == 1:
            player = pI
            Eden.player_direction = 0
        elif Eden.igrid[Eden.gy][Eden.gx] == 2:
            player = pI
            Eden.player_direction = 0
        elif Eden.igrid[Eden.gy][Eden.gx] == 3:
            player = pI
            Eden.player_direction = 0
        elif Eden.igrid[Eden.gy][Eden.gx] == 4:
            player = pI
            Eden.player_direction = 0
        elif Eden.igrid[Eden.gy][Eden.gx] == 5:
            player = pI
            Eden.player_direction = 0
        elif Eden.igrid[Eden.gy][Eden.gx] == 6:
            player = pI
            Eden.player_direction = 0
        elif Eden.igrid[Eden.gy][Eden.gx] == 7:
            player = pI
            Eden.player_direction = 0
        elif Eden.igrid[Eden.gy][Eden.gx] == 8:
            player = pI
            Eden.player_direction = 0
        elif Eden.igrid[Eden.gy][Eden.gx] == 9:
            player = pI
            Eden.player_direction = 0
        elif Eden.igrid[Eden.gy][Eden.gx] == 10:
            player = pI
            Eden.player_direction = 0
    bplayer = player
    col = []
    for i in range(30):
        col.append(0)
    row = []
    for i in range(30):
        row.append(col)
    for i in range(30):
        for j in range(30):
            row[i][j] = (player.get_at((i,j)))
            if row[i][j] == FACE:
                player.set_at((i,j),face)
            elif row[i][j] == HAT:
                if Eden.Hat == 1:
                    player.set_at((i,j),hat)
                else:
                    player.set_at((i,j),hair)
            elif row[i][j] == HATS:
                if Eden.Hat == 1:
                    player.set_at((i,j),hats)
                else:
                    player.set_at((i,j),hair)
            elif row[i][j] == HATB:
                if Eden.Hat == 1:
                    player.set_at((i,j),hat)
                else:
                    player.set_at((i,j),(0,0,0,0))
            elif row[i][j] == HAIR:
                player.set_at((i,j),hair)
            elif row[i][j] == FHAIR:
                if Eden.Fhair == 1:
                    player.set_at((i,j),hair)
                else:
                    player.set_at((i,j),face)
            elif row[i][j] == BODY:
                player.set_at((i,j),body)
            elif row[i][j] == SHOULDERS:
                player.set_at((i,j),shoulders)
            elif row[i][j] == ARMS:
                player.set_at((i,j),arms)
            elif row[i][j] == GLOVES:
                player.set_at((i,j),gloves)
            elif row[i][j] == LEGS:
                player.set_at((i,j),legs)
            elif row[i][j] == DRESS:
                if Eden.Dress == 1:
                    player.set_at((i,j),legs)
                else:
                    player.set_at((i,j),(0,0,0,0))
            elif row[i][j] == SHOES:
                player.set_at((i,j),shoes)
            elif row[i][j] == EYES:
                player.set_at((i,j),(0,0,0,255))
            else:
                player.set_at((i,j),(0,0,0,0))

    #if player.get_at((0,0)) == (0,0,0,255):
      #  go()
    if Eden.custom == 1:
        player = pygame.transform.scale(player, (300, 300))
        Eden.screen.blit(player,(390,225))
    elif Eden.custom == 0:            
        Eden.screen.blit(player,(360,360))
##        bplayer.set_colorkey((255,255,255,255))
##        print(bplayer.get_at((0,0)))
##        col = []
##        for i in range(30):
##            col.append(0)
##        row = []
##        for i in range(30):
##            row.append(col)
##        for i in range(30):
##            for j in range(30):
##                row[i][j] = (bplayer.get_at((i,j)))
##                if row[i][j] != (255,255,255):
##                    bplayer.set_at((i,j),(0,0,0,Eden.shade))
##        Eden.screen.blit(bplayer,(360,360))

    Eden.PF = P














