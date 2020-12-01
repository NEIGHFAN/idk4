


def go():
    import Eden, time
    from time import sleep
    global on
    B = (0,0,0)
    while Eden.On and on == 1:
        pygame = Eden.pygame
        pygame.init()
        size = [850, 650]
        screen = pygame.display.set_mode(size,pygame.FULLSCREEN)
        if Eden.file == 1:
            cred = open("customredsA.txt","r+")
            cgreen = open("customgreensA.txt","r+")
            cblue = open("custombluesA.txt","r+")
            cclothes = open("customclothesA.txt","r+")
        elif Eden.file == 2:
            cred = open("customredsB.txt","r+")
            cgreen = open("customgreensB.txt","r+")
            cblue = open("custombluesB.txt","r+")
            cclothes = open("customclothesB.txt","r+")
        elif Eden.file == 3:
            cred = open("customredsC.txt","r+")
            cgreen = open("customgreensC.txt","r+")
            cblue = open("custombluesC.txt","r+")
            cclothes = open("customclothesC.txt","r+")
        Eden.cred = [line.rstrip('\n') for line in cred.readlines()]
        Eden.cgreen = [line.rstrip('\n') for line in cgreen.readlines()]
        Eden.cblue = [line.rstrip('\n') for line in cblue.readlines()]
        for i in range(10):
            Eden.cred[i] = int(Eden.cred[i])
            Eden.cgreen[i] = int(Eden.cgreen[i])
            Eden.cblue[i] = int(Eden.cblue[i])
        cred.close()
        cgreen.close()
        cblue.close()
        Cclothes = [line.rstrip('\n') for line in cclothes.readlines()]
        cHat = int(Cclothes[0])
        cDress = int(Cclothes[1])
        cFhair = int(Cclothes[2])
        cclothes.close()
        cface = (Eden.cred[0],Eden.cgreen[0],Eden.cblue[0])
        chat = (Eden.cred[1],Eden.cgreen[1],Eden.cblue[1])
        chatsymbol = (Eden.cred[2],Eden.cgreen[2],Eden.cblue[2])
        chair = (Eden.cred[3],Eden.cgreen[3],Eden.cblue[3])
        cbody = (Eden.cred[4],Eden.cgreen[4],Eden.cblue[4])
        carms = (Eden.cred[5],Eden.cgreen[5],Eden.cblue[5])
        clegs = (Eden.cred[6],Eden.cgreen[6],Eden.cblue[6])
        cshoes = (Eden.cred[7],Eden.cgreen[7],Eden.cblue[7])
        cgloves = (Eden.cred[8],Eden.cgreen[8],Eden.cblue[8])
        cshoulders = (Eden.cred[9],Eden.cgreen[9],Eden.cblue[9])
        x = 0
        X = 0
        Xx = 0
        xX = 0
        y = 0
        Y = -50
        alt = 0
        altB = 0
        altA = 0
        Alt = 0
        W,A,S,D = 0,0,0,0
        DM, AM = 19,19
        clock = pygame.time.Clock()
        coins = []
        for i in range(98):
            coins.append(0)

        #alts1 = [0,0,0,0,0,0,0,0,0,0,-50,-50,-50,50,0,0,0,50,-50,100,-50,-50,250,-50,-50,50,-50,0,0,250,0,0,0,0]

            
        alts1 = [1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,0,3,0,6,0,0,0,0,6,0,0,0,0,0,1,1]
        for i in range(17):
            alts1.append(0)
        coinsx = [5,6,7,8]
        coinsy = [1,2,3,4]
        spikesx = [5]
        spikesy = [3]
        alts2 = [2,1,1,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
        alts = alts1
        for i in range(len(alts)):
                alts[i] = (alts[i]-1)*50
        for i in range(len(coinsx)):
                coinsx[i] = (coinsx[i]-1)*50
                coinsy[i] = 550-(coinsy[i]-1)*50
        for i in range(len(spikesx)):
                spikesx[i] = (spikesx[i]-1)*50
                spikesy[i] = 550-(spikesy[i]-1)*50
        
        seconds = 0
        start_ticks = pygame.time.get_ticks()
        time = 100
        end = len(alts*50)-700
        alive = 1
        moved = 0
        bdire = 1
        title = 1
        Tcol = 1
        while title == 1:
            if Tcol == 1:
                Acol = (255,255,0)
                Bcol = (0,255,0)
                Tcol = 0
            elif Tcol == 0:
                Bcol = (255,255,0)
                Acol = (0,255,0)
                Tcol = 1
            screen.fill((0,255,255))
            #for i in range(50):
                #pygame.draw.line(screen,(0,255-(3*i),255),[0,600+i],[850,600+i])
            mh = pygame.image.load('manhole.png')
            screen.blit(mh,(0,0))
            
            #pygame.draw.ellipse(screen,(0,0,0),[125,25,600,600])
            #pygame.draw.ellipse(screen,(127,127,127),[128,28,594,594])
            #for i in range(30):
                #pygame.draw.ellipse(screen,(0,0,0),[130+(i*10),30+(i*10),590-(i*20),590-(i*20)],1)
            font = pygame.font.SysFont('Comic sans MS', 100, True, True)
            Text = font.render("SCOOTER", True, (0,0,0))
            screen.blit(Text, [175,130])
            Text = font.render("SCOOTER", True, Acol)
            screen.blit(Text, [175,125])
            Text = font.render("MANHOLE", True, (0,0,0))
            screen.blit(Text, [150,250])
            Text = font.render("MANHOLE", True, Bcol)
            screen.blit(Text, [150,245])
            Text = font.render("BRO", True, (0,0,0))
            screen.blit(Text, [300,375])
            Text = font.render("BRO", True, Acol)
            screen.blit(Text, [300,370])
            pygame.display.flip()
            sleep(0.05)
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    title = 0
                if event.type == pygame.MOUSEBUTTONDOWN:
                    title = 0
            
            
        while on == 1:
            if bdire == 1:
                moved += 0.5
            if bdire == 0:
                moved -= 0.5
            if moved == 0:
                bdire = 1
            if moved == 50:
                bdire = 0

            x = (((X)//50)*50)-50
            xX = X+2.5
            Xx = X-2.5 
            y = (Y//50)*50

            if X != x+50:
                if alts[int((-x/50))] < alts[int((-x/50)-1)]:
                        alt = alts[int((-x/50)-1)]
                        altB = alts[int((-x-50)/50)+1]
                        altA = alts[int((-x-50)/50)-1]
                else:
                    alt = alts[int(-x/50)]
                    altB = alts[int(((-x-50)/50)+2)]
                    altA = alts[int((-x-50)/50)]
            else:
                alt = alts[int(-x/50)]
                altB = alts[int(((-x-50)/50)+2)]
                altA = alts[int((-x-50)/50)]
            seconds = time-((pygame.time.get_ticks()-start_ticks)/1000)
            for event in pygame.event.get():
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_w or event.key == pygame.K_UP:
                        W = 0
                    elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                        D = 0
                    elif event.key == pygame.K_ESCAPE:
                        seconds = 0
                if event.type == pygame.KEYDOWN:
                    if (event.key == pygame.K_w or event.key == pygame.K_UP) and -y==alt:
                                W = 1
                                Alt = alt
                    elif (event.key == pygame.K_d or event.key == pygame.K_RIGHT):
                        D = 1
##                    elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
##                        if 1800 <= -x <= 1900 and y == 0:
##                            alts = alts2
##                            X = 0
##                            Y = -600
##                            for i in range(len(alts)):
##                                alts[i] = (alts[i]-1)*50
##                    elif event.key == pygame.K_RETURN:
##                        alts = alts2
##                        X = 0
##                        Y = -600
##                        for i in range(len(alts)):
##                            alts[i] = (alts[i]-1)*50
                        
                    
            if W == 1 and -Y < Alt+250:
                Y -= 2.5
                if -Y == Alt +250:
                    W = 0
                    Alt = alt
            if D == 1  and -X < end-100:
                    if -y >= alt:
                        if altB > alt and (-y-50) < altB:
                            if X != x+50:
                                X -= 2.5
                        else:
                             X -= 2.5
            if -x > -X:
                if W == 0 and -y > alt:
                    Y += 2.5
            if x == X:
                if W == 0 and -y > alts[int((-x/50)+1)]:
                    Y += 2.5
            if -Y < alt and W == 0:
                Y += 2.5
            if Y >= 50 or seconds <= 0:
                screen.fill((0,0,0))
                pygame.display.flip()
                Eden.time.sleep(1)
                Eden.size = [850, 750]
                Eden.screen = Eden.pygame.display.set_mode(Eden.size,pygame.FULLSCREEN)
                on = 0
                Eden.W = 0
                Eden.player_direction = 1


            
                    
            #print("a:"+str(alt)+"x:"+str(x)+"y:"+str(y)+"AM:"+str(AM)+"DM:"+str(DM)+"X:"+str(X)+"Y:"+str(Y)+"Xx:"+str(Xx)+"xX:"+str(xX))
            #print("a:"+str(alt)+" aB:"+str(altB)+" aA:"+str(altA)+" y:"+str(Y)+" x:"+str(x)+" X:"+str(X))

            #BACKGROUND
            if alts == alts1:
                screen.fill((0,255,255))
                for i in range(50):
                    pygame.draw.line(screen,(0,255-(4*i),255),[0,625+i/2],[850,625+i/2])
                sign = pygame.image.load('sign.png')
                screen.blit(sign,(X,500))
##                pygame.draw.rect(screen,(190,127,63),[X+160,470,30,130])
##                pygame.draw.rect(screen,(0,0,0),[X+160,470,30,130],2)
##                pygame.draw.rect(screen,(190,127,63),[X+125,475,100,75])
##                pygame.draw.rect(screen,(0,0,0),[X+125,475,100,75],2)
##                pygame.draw.polygon(screen,(255,0,0),[[X+145,500],[X+180,500],[X+180,490],[X+210,512.5],[X+180,535],[X+180,525],[X+145,525]])
##                pygame.draw.polygon(screen,(255,255,255),[[X+145,500],[X+180,500],[X+180,490],[X+210,512.5],[X+180,535],[X+180,525],[X+145,525]],4)


            if alts == alts2:
                screen.fill((50,50,50))
                for i in range(50):
                    pygame.draw.line(screen,(50-i,50-i,50-i),[0,600+i],[end,600+i])


            
            #ENTITIES        
            for i in range(len(coinsx)):
                if coinsx[i] <= (-x) < coinsx[i]+100 and coinsy[i] <= (550+y) < coinsy[i]+100:
                    coins[i] = 1
                if coins[i] == 0:
                    coin = pygame.image.load('coin.png')
                    screen.blit(coin,(X+coinsx[i],coinsy[i]))
                    #pygame.draw.ellipse(screen,(0,0,0),[X+coinsx[i],coinsy[i],50,50])
                    #pygame.draw.ellipse(screen,(255,255,0),[X+coinsx[i]+2,coinsy[i]+2,46,46])

            for i in range(len(spikesx)):
                if spikesx[i] <= (-X)+100 < spikesx[i]+100 and spikesy[i] <= (600+Y) < spikesy[i]+150:
                    alive = 0
                if alive == 0:
                    W,A,D = 0,0,0
                    if Y != 50:
                        Y += 2.5
                spike = pygame.image.load('spike.png')
                screen.blit(spike,(X+spikesx[i],spikesy[i]))
                #pygame.draw.polygon(screen,(127,127,127),[[X+spikesx[i],spikesy[i]+25],[X+spikesx[i]+25,spikesy[i]],[X+spikesx[i]+50,spikesy[i]+25],[X+spikesx[i]+25,spikesy[i]+50]])
                #pygame.draw.rect(screen,(127,127,127),[X+spikesx[i]+7,spikesy[i]+7,36,36])
                #pygame.draw.rect(screen,(0,0,0),[X+spikesx[i]+7,spikesy[i]+7,36,36],1)
                #pygame.draw.polygon(screen,(0,0,0),[[X+spikesx[i],spikesy[i]+25],[X+spikesx[i]+25,spikesy[i]],[X+spikesx[i]+50,spikesy[i]+25],[X+spikesx[i]+25,spikesy[i]+50]],2)
                

            #GROUND
            if alts == alts1:
                for i in range(len(alts1)):
                    if (i-17)*50 <= -X <= (i+1)*50: 
                        if alts1[i] != -50:
                            gtop = pygame.image.load('grass top.png')
                            screen.blit(gtop,((i*50)+X,600-alts1[i]))
                            s = pygame.Surface((48,10))
                            s.set_alpha(140)
                            s.fill(Eden.grass)
                            screen.blit(s,((i*50)+X+1,600-alts1[i]+1))
                            dirt = pygame.image.load('dirt.png')
                            for j in range(int(alts1[i]/50)):
                                screen.blit(dirt,((i*50)+X,600-alts1[i]+(j+1)*50))
                        if alts1[i] < alts1[i+1]:
                            pygame.draw.line(screen,(0,0,0),[((i+1)*50)+X-1,600-alts1[i+1]],[((i+1)*50)+X-1,600-alts1[i]],1)
                        if alts1[i+1] < alts1[i]:
                            pygame.draw.line(screen,(0,0,0),[((i+1)*50)+X,600-alts1[i+1]],[((i+1)*50)+X,600-alts1[i]],1)
                                
                                

                                
                            #pygame.draw.rect(screen,(0,0,0),[(i*50)+X,600-alts1[i],50,alts1[i]+50])
                            #pygame.draw.rect(screen,(0,255,0),[(i*50)+1+X,601-alts1[i],48,(alts1[i]+50)-2])
                            
            if alts == alts2:
                pygame.draw.rect(screen,(0,0,127),[X+50,550,100,50])
                for i in range(len(alts2)):
                    if alts2[i] != -50:
                        pygame.draw.rect(screen,(0,0,0),[(i*50)+X,600-alts2[i],50,alts2[i]+50])
                        pygame.draw.rect(screen,(63,63,63),[(i*50)+1+X,601-alts2[i],48,(alts2[i]+50)-2])


            #PLAYER
            pygame.draw.rect(screen,cbody,[68,Y+520,14,35])
            pygame.draw.rect(screen,B,[68,Y+520,14,35],1)
            pygame.draw.ellipse(screen,cface,[63,Y+500,24,24])
            pygame.draw.ellipse(screen,B,[63,Y+500,24,24],1)
            pygame.draw.rect(screen,(190,190,190),[95,Y+525,5,65])
            pygame.draw.rect(screen,B,[95,Y+525,5,65],1)
            pygame.draw.rect(screen,(190,190,190),[50,Y+585,50,10])
            pygame.draw.rect(screen,B,[50,Y+585,50,10],1)
            pygame.draw.ellipse(screen,(0,0,0),[50,Y+590,10,10])
            pygame.draw.ellipse(screen,(0,0,0),[90,Y+590,10,10])
            pygame.draw.rect(screen,clegs,[70,Y+555,10,25])
            pygame.draw.rect(screen,B,[70,Y+555,10,25],1)
            if cHat == 2:
                pygame.draw.polygon(screen,chat,[[62,Y+510],[75,Y+475],[87,Y+510]])
                pygame.draw.polygon(screen,B,[[62,Y+510],[75,Y+475],[87,Y+510]],1)
            if cDress == 1:
                pygame.draw.polygon(screen,clegs,[[55,Y+580],[68,Y+555],[82,Y+555],[95,Y+580]])
                pygame.draw.polygon(screen,B,[[55,Y+580],[68,Y+555],[82,Y+555],[95,Y+580]],1)
            pygame.draw.ellipse(screen,cshoes,[75,Y+580,10,10])
            pygame.draw.ellipse(screen,B,[75,Y+580,10,10],1)
            pygame.draw.rect(screen,cshoes,[70,Y+580,10,10])
            pygame.draw.line(screen,B,[70,Y+580],[80,Y+580])
            pygame.draw.line(screen,B,[70,Y+580],[70,Y+590])
            pygame.draw.line(screen,B,[70,Y+590],[80,Y+590])
            if cHat == 1:
                pygame.draw.rect(screen,chat,[75,Y+508,20,3])
                pygame.draw.rect(screen,B,[75,Y+508,20,3],1)
            if cFhair == 1:
                pygame.draw.rect(screen,chair,[81,Y+518,4,2])
            pygame.draw.ellipse(screen,cgloves,[91,Y+526,8,8])
            pygame.draw.ellipse(screen,B,[91,Y+526,8,8],1)
            
            pygame.draw.ellipse(screen,cshoulders,[66,Y+526,8,8])
            pygame.draw.ellipse(screen,B,[66,Y+526,8,8],1)
            
            pygame.draw.rect(screen,carms,[71,Y+526,23,8])
            pygame.draw.rect(screen,cshoulders,[70,Y+526,4,8])
            pygame.draw.rect(screen,cgloves,[91,Y+526,4,8])
            pygame.draw.line(screen,B,[71,Y+526],[95,Y+526])
            pygame.draw.line(screen,B,[71,Y+534],[95,Y+534])

            pygame.draw.polygon(screen,chair,[[63,Y+510],[77,Y+510],[71,Y+516],[63,Y+516]])
            pygame.draw.polygon(screen,B,[[63,Y+510],[77,Y+510],[71,Y+516],[63,Y+516]],1)
            
            pygame.draw.polygon(screen,chat,[[62,Y+510],[66,Y+502],[75,Y+499],[84,Y+502],[88,Y+510]])
            pygame.draw.polygon(screen,B,[[62,Y+510],[66,Y+502],[75,Y+499],[84,Y+502],[88,Y+510]],1)
            pygame.draw.rect(screen,chatsymbol,[82,Y+503,4,3])
   
            #MANHOLE
##            if alts == alts1:
##                pygame.draw.rect(screen,(0,0,0),[X+1850,595,50,5])
##                pygame.draw.rect(screen,(127,127,127),[X+1851,596,48,3])


            collected = {i:coins.count(i) for i in coins}
            font = pygame.font.SysFont('Calibri', 30, True, False)
            Text = font.render(str(len(coins)-int(collected[0])), True, (0,0,0))
            screen.blit(Text, [0,0])
            Text = font.render(str(len(coins)-int(collected[0])), True, (255,255,0))
            screen.blit(Text, [2,0])
            Text = font.render(str(int(seconds)), True, (0,0,0))
            screen.blit(Text, [815,0])
            Text = font.render(str(int(seconds)), True, (255,255,0))
            screen.blit(Text, [817,0])



            
            pygame.display.flip()
            
            clock.tick(120)













