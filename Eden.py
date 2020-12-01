import pygame, datetime, time, os, random,warnings, sys
if os.path.basename(os.getcwd()) == 'data':
    os.chdir('..')
os.chdir('./data/EDEN_PROGRAMS')
sys.path.insert(0, os.path.abspath(".."))
from EDEN_PROGRAMS import gstart, pstart, drawplayer, Map
os.chdir('../G1')
sys.path.insert(0, os.path.abspath(".."))
from G1 import g1
os.chdir('../G2')
sys.path.insert(0, os.path.abspath(".."))
from G2 import g2
os.chdir('../G3')
sys.path.insert(0, os.path.abspath(".."))
from G3 import g3
os.chdir('..')
from time import sleep
from pygame import mixer
mixer.init()
gstart.go()
warnings.filterwarnings('ignore')


def title():
    pygame.mouse.set_visible(False)
    global On,file,dev,CX,CY,MOUSE,lang,screen
    channel1.set_volume(mvol)
    s = pygame.Surface((150,150))
    s.set_alpha(140)
    s.fill(grass)
    play = 0
    gstart.go()
    dev = 0
    config()
    while On:
        if  controller > 0 and MOUSE == 0:
            cx = CX
            cy = CY
        else:
            cursorpos = pygame.mouse.get_pos()
            cx = cursorpos[0]
            cy = cursorpos[1]
            CX = cx
            CY = cy
        if controller > 0:
            if (con.get_axis(1) <= -0.5 or con.get_axis(3)  <= -0.5 or con.get_hat(0)[1]  == 1) and CY >= 5:
                CY -= 5
                MOUSE = 0
            if (con.get_axis(1) >= 0.5 or con.get_axis(3)  >= 0.5 or con.get_hat(0)[1]  == -1) and CY <= 745:
                    CY += 5
                    MOUSE = 0
            if (con.get_axis(0) <= -0.5 or con.get_axis(4)  <= -0.5 or con.get_hat(0)[0]  == -1) and CX >= 5:
                    CX -= 5
                    MOUSE = 0
            if (con.get_axis(0) >= 0.5 or con.get_axis(4)  >= 0.5 or con.get_hat(0)[0]  == 1) and CX <= 845:
                    CX += 5
                    MOUSE = 0
##        for i in range(6):
##            for j in range(5):
##                screen.blit(ground,(i*150,j*150))
        screen.blit(titleBG,(0,0))
        screen.blit(s,(0,0))
        screen.fill(green)
        clockoverlay(0,0,850,750)
        drawtext(400,TEXT[0],yellow,0,0,True,False) #eden
        if play == 0:
            roundbox(black,red,225,400,400,100,10)
            roundbox(black,green,225,520,400,100,10)
            roundbox(black,blue,225,640,400,100,10)
            drawtext(100,TEXT[1],white,340,400,True,False) #play
            drawtext(100,TEXT[2],white,225,520,True,False) #language
            drawtext(100,TEXT[3],white,340,640,True,False) #exit

                
            pygame.draw.ellipse(screen,white,[cx-5,cy-5,10,10],1)
            for event in pygame.event.get():
                if controller > 0:
                    if event.type == pygame.JOYBUTTONUP:
                        if event.button == 7 or event.button == 2:
                            play = 1
                        if event.button == 3:
                            lang = int(int((((lang-2)**2)**0.5)+1))
                            S = open('settings.txt','w')
                            S.write(str(lang)+'\n'+str(int(mvol*10))+'\n'+str(int(svol*10))+'\n')
                            S.close()
                            
                            gstart.go()
                            title()
                        if event.button == 6 or event.button == 1:
                            On = False
                        if event.button == 0:
                            if 225 <= cx <= 625 and 400 <= cy <= 500:
                                play = 1
                            if 225 <= cx <= 625 and 520 <= cy <= 620:
                                lang = int((((lang-2)**2)**0.5)+1)
                                S = open('settings.txt','w')
                                S.write(str(lang)+'\n'+str(int(mvol*10))+'\n'+str(int(svol*10))+'\n')
                                S.close()
                                
                                gstart.go()
                                title()
                            if 225 <= cx <= 625 and 640 <= cy <= 740:
                                On = False
                if event.type == pygame.MOUSEMOTION:
                    MOUSE = 1
                if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                    
                    if 225 <= cx <= 625 and 400 <= cy <= 500:
                        play = 1
                    if 225 <= cx <= 625 and 520 <= cy <= 620:
                        lang = int((((lang-2)**2)**0.5)+1)
                        S = open('settings.txt','w')
                        S.write(str(lang)+'\n'+str(int(mvol*10))+'\n'+str(int(svol*10))+'\n')
                        S.close()
                        
                        gstart.go()
                        title()
                    if 225 <= cx <= 625 and 640 <= cy <= 740:
                        On = False
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_ESCAPE:
                        On = False
                    elif event.key == pygame.K_f:
                        screen = pygame.display.set_mode((850,750))
                    else:
                        play = 1
                        
        else:
            roundbox(black,red,225,400,280,100,10)
            roundbox(black,green,225,520,280,100,10)
            roundbox(black,blue,225,640,280,100,10)
            FACE = (255,0,0,255)
            HAT = (0,0,255,255)
            FHAIR = (255,255,0,255)
            HATS = (0,255,0,255)
            cred = [credA,credB,credC]
            cgreen = [cgreenA,cgreenB,cgreenC]
            cblue = [cblueA,cblueB,cblueC]
            HAt = [cHatA,cHatB,cHatC]
            FHair = [cFhairA,cFhairB,cFhairC]
            for k in range(3):
                ICON = icon
                face = (cblue[k][0],cgreen[k][0],cred[k][0],255)
                hat = (cblue[k][1],cgreen[k][1],cred[k][1],255) 
                hats = (cblue[k][2],cgreen[k][2],cred[k][2],255)
                hair = (cblue[k][3],cgreen[k][3],cred[k][3],255)
                col = []
                Hat = HAt[k]
                Fhair = FHair[k]
                for l in range(10):
                    col.append(0)
                row = []
                for l in range(10):
                    row.append(col)
                for i in range(10):
                    for j in range(10):
                        row[i][j] = (ICON.get_at((i,j)))
                        if row[i][j] == FACE:
                            ICON.set_at((i,j),face)
                        elif row[i][j] == HAT:
                            if Hat == 1:
                                ICON.set_at((i,j),hat)
                            else:
                                ICON.set_at((i,j),hair)
                        elif row[i][j] == HATS:
                            if Hat == 1:
                                ICON.set_at((i,j),hats)
                            else:
                                ICON.set_at((i,j),hair)
                        elif row[i][j] == FHAIR:
                            if Fhair == 1:
                                ICON.set_at((i,j),hair)
                            else:
                                ICON.set_at((i,j),face)
                        elif row[i][j] != (0,0,0,255):
                            ICON.set_at((i,j),(20,4,69))
                ICON.set_colorkey((69,4,20))
                ICON = pygame.transform.scale(ICON, (100, 100))
                screen.blit(ICON,(525,400+(120*k)))
            drawtext(100,str(nameA),white,230,400,True,False)
            drawtext(100,str(nameB),white,230,520,True,False)
            drawtext(100,str(nameC),white,230,640,True,False)
            if controller > 0:
                if con.get_axis(1) <= -0.5 or con.get_axis(3)  <= -0.5 or con.get_hat(0)[1]  == 1:
                    cy -= 5
                if con.get_axis(1) >= 0.5 or con.get_axis(3)  >= 0.5 or con.get_hat(0)[1]  == -1:
                    cy += 5
                if con.get_axis(0) <= -0.5 or con.get_axis(4)  <= -0.5 or con.get_hat(0)[0]  == -1:
                    cx -= 5
                if con.get_axis(0) >= 0.5 or con.get_axis(4)  >= 0.5 or con.get_hat(0)[0]  == 1:
                    cx += 5

                
            pygame.draw.ellipse(screen,white,[cx-5,cy-5,10,10],1)
            for event in pygame.event.get():
                if controller > 0:
                    if event.type == pygame.JOYBUTTONUP:
                        if event.button == 1:
                            file = 3
                            pstart.go()
                            main()
                        elif event.button == 2:
                            file = 1
                            pstart.go()
                            main()
                        elif event.button == 3:
                            file = 2
                            pstart.go()
                            main()
                        elif event.button == 6:
                            title()
                        elif event.button == 0:
                            if 225 <= cx <= 625 and 400 <= cy <= 500:
                                file = 1
                                pstart.go()
                                main()
                            if 225 <= cx <= 625 and 520 <= cy <= 620:
                                file = 2
                                pstart.go()
                                main()
                            if 225 <= cx <= 625 and 640 <= cy <= 740:
                                file = 3
                                pstart.go()
                                main()
                if event.type == pygame.MOUSEMOTION:
                    MOUSE = 1
                if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                    if 225 <= cx <= 625 and 400 <= cy <= 500:
                        file = 1
                        pstart.go()
                        main()
                    if 225 <= cx <= 625 and 520 <= cy <= 620:
                        file = 2
                        pstart.go()
                        main()
                    if 225 <= cx <= 625 and 640 <= cy <= 740:
                        file = 3
                        pstart.go()
                        main()
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_ESCAPE:
                        title()

        pygame.display.flip()
        
def config():
    global con,controller
    JS = pygame.joystick.get_count()
    if JS != 0:
        controller = 1
        con = pygame.joystick.Joystick(0)
        con.init()
    else:
        controller = 0


    
def roundbox(col,col2,cx,cy,sx,sy,thick):
        pygame.draw.ellipse(screen,col,[cx,cy,thick,thick])
        pygame.draw.ellipse(screen,col,[cx+sx-thick,cy,thick,thick])
        pygame.draw.ellipse(screen,col,[cx,cy+sy-thick,thick,thick])
        pygame.draw.ellipse(screen,col,[cx+sx-thick,cy+sy-thick,thick,thick])
        pygame.draw.rect(screen,col,[cx,cy+(thick/2),sx,sy-thick])
        pygame.draw.rect(screen,col,[cx+(thick/2),cy,sx-thick,sy])
        pygame.draw.ellipse(screen,col2,[cx+(thick/2),cy+(thick/2),thick,thick])
        pygame.draw.ellipse(screen,col2,[cx+sx-(1.5*thick),cy+(thick/2),thick,thick])
        pygame.draw.ellipse(screen,col2,[cx+(thick/2),cy+sy-(1.5*thick),thick,thick])
        pygame.draw.ellipse(screen,col2,[cx+sx-(1.5*thick),cy+sy-(1.5*thick),thick,thick])
        pygame.draw.rect(screen,col2,[cx+(thick/2),cy+thick,sx-thick,sy-(2*thick)])
        pygame.draw.rect(screen,col2,[cx+thick,cy+(thick/2),sx-(2*thick),sy-thick])
    
def drawtext(size,text,colour,x,y,bold,italic):
        font = pygame.font.SysFont('Calibri', size,bold,italic)
        Text = font.render(text, True,black)
        screen.blit(Text,[x,y])
        Text = font.render(text, True,colour)
        screen.blit(Text,[x+size/25,y])
        
def exitcustomise():
    global custom
    os.chdir('../SAVE_FILES')
    custom = 0
    if file == 1:
        Cred = open('customredsA.txt','w')
        Cgreen = open('customgreensA.txt','w')
        Cblue = open('custombluesA.txt','w')
        Cclothes = open('customclothesA.txt','w')
    elif file == 2:
        Cred = open('customredsB.txt','w')
        Cgreen = open('customgreensB.txt','w')
        Cblue = open('custombluesB.txt','w')
        Cclothes = open('customclothesB.txt','w')
    elif file == 3:
        Cred = open('customredsC.txt','w')
        Cgreen = open('customgreensC.txt','w')
        Cblue = open('custombluesC.txt','w')
        Cclothes = open('customclothesC.txt','w')
    for i in range(10):
        Cred.write(str(cred[i])+'\n')
        Cgreen.write(str(cgreen[i])+'\n')
        Cblue.write(str(cblue[i])+'\n')
    Cclothes.write(str(cHat)+'\n'+str(cDress)+'\n'+str(cFhair)+'\n')
    Cred.close()
    Cgreen.close()
    Cblue.close()
    Cclothes.close()
    
def Create_skin():
    global custom,cface,chat,chatsymbol,chair,cbody,carms,clegs,cshoes,cgloves,cshoulders,cDress,cHat,cFhair, player_direction,redc,greenc,bluec,W,A,S,D,CX,CY,MOUSE
    custom = 1
    while custom == 1:
        if  controller > 0 and MOUSE == 0:
            cx = CX
            cy = CY
        else:
            cursorpos = pygame.mouse.get_pos()
            cx = cursorpos[0]
            cy = cursorpos[1]
            CX = cx
            CY = cy
        drawhotbar()
        screen.blit(customiseBG,(0,0))
        s = pygame.Surface((420,450))
        s.set_alpha(140)
        s.fill(grass)
        screen.blit(s,(330,150))
        drawtext(50,TEXT[4],white,420,690,True,False)
        for i in range(10):
            drawtext(25,str(cred[i]),red,255,(i*75),True,False)
            drawtext(25,str(cgreen[i]),green,255,(i*75)+25,True,False)
            drawtext(25,str(cblue[i]),blue,255,(i*75)+50,True,False)
            pygame.draw.rect(screen,white,[cred[i],i*75,1,25])
            pygame.draw.rect(screen,white,[cgreen[i],(i*75)+25,1,25])
            pygame.draw.rect(screen,white,[cblue[i],(i*75)+50,1,25])
        cface = (cred[0],cgreen[0],cblue[0]) 
        chat = (cred[1],cgreen[1],cblue[1])
        chatsymbol = (cred[2],cgreen[2],cblue[2])
        chair = (cred[3],cgreen[3],cblue[3])
        cbody = (cred[4],cgreen[4],cblue[4])
        carms = (cred[5],cgreen[5],cblue[5])
        clegs = (cred[6],cgreen[6],cblue[6])
        cshoes = (cred[7],cgreen[7],cblue[7])
        cgloves = (cred[8],cgreen[8],cblue[8])
        cshoulders = (cred[9],cgreen[9],cblue[9])
        s = pygame.Surface((140,75))
        s.set_alpha(63)
        s.fill(white)
        if cHat == 1:
            screen.blit(s, (330,0))
        else:
            screen.blit(s, (330,75))
        if cFhair == 1:
            screen.blit(s, (470,0))
        else:
            screen.blit(s, (470,75))
        if cDress == 1:
            screen.blit(s, (610,0))
        else:
            screen.blit(s, (610,75))
        for event in pygame.event.get():
            if controller > 0:
                if event.type == pygame.JOYHATMOTION:
                    if (con.get_hat(0)[1]  == 1):
                            player_direction = 0
                            W,A,S,D = 0,0,0,0
                    if (con.get_hat(0)[1]  == -1):
                            player_direction = 1
                            W,A,S,D = 0,0,0,0
                    if (con.get_hat(0)[0]  == -1):
                            player_direction = 3
                            W,A,S,D = 0,0,0,0
                    if (con.get_hat(0)[0]  == 1):
                            player_direction = 2
                            W,A,S,D = 0,0,0,0
                if event.type == pygame.JOYBUTTONDOWN:
                    if event.button == 4 and CX > 0:
                        CX -= 1
                    if event.button == 5 and CX < 255:
                        CX += 1
                    if event.button == 1:
                            cDress = int(((cDress-1)**2)**0.5)
                    if event.button == 2:
                            cHat = int(((cHat-1)**2)**0.5)
                    if event.button == 3:
                            cFhair = int(((cFhair-1)**2)**0.5)
                    if event.button == 0 or event.button == 4 or event.button == 5:
                        if 0 < cy < 75:
                            if 330 < cx < 470:
                                cHat = 1
                            elif 470 < cx < 610:
                                cFhair = 1
                            elif 610 < cx < 750:
                                cDress = 1
                        if 75 < cy < 150:
                            if 330 < cx < 470:
                                cHat = 0
                            elif 470 < cx < 610:
                                cFhair = 0
                            elif 610 < cx < 750:
                                cDress = 0
                        if 600 < cy < 675:
                            if 330 < cx < 435:
                                player_direction = 0
                                W = 1
                                A,S,D = 0,0,0
                            elif 435 < cx < 540:
                                player_direction = 1
                                S = 1
                                A,W,D = 0,0,0
                            elif 540 < cx < 645:
                                player_direction = 2
                                D = 1
                                W,S,A = 0,0,0
                            elif 645 < cx < 750:
                                player_direction = 3
                                A = 1
                                D,S,W = 0,0,0
                        for i in range(30):
                            if i*25 < cy < (i+1)*25:
                                if (i)%3 == 0:
                                        redc[(i)//3] = 1
                                elif (i-1)%3 == 0:
                                        greenc[(i-1)//3] = 1
                                elif (i-2)%3 == 0:
                                        bluec[(i-2)//3] = 1
                if event.type == pygame.JOYBUTTONUP:
                    if 330 < cx < 750 and cy >= 675:
                        exitcustomise()
                    redc = [0,0,0,0,0,0,0,0,0,0]
                    greenc = [0,0,0,0,0,0,0,0,0,0]
                    bluec = [0,0,0,0,0,0,0,0,0,0]
                    W,A,S,D = 0,0,0,0
            if event.type == pygame.MOUSEMOTION:
                MOUSE = 1
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if 0 < cy < 75:
                    if 330 < cx < 470:
                        cHat = 1
                    elif 470 < cx < 610:
                        cFhair = 1
                    elif 610 < cx < 750:
                        cDress = 1
                if 75 < cy < 150:
                    if 330 < cx < 470:
                        cHat = 0
                    elif 470 < cx < 610:
                        cFhair = 0
                    elif 610 < cx < 750:
                        cDress = 0
                if 600 < cy < 675:
                    if 330 < cx < 435:
                        player_direction = 0
                        W = 1
                        A,S,D = 0,0,0
                    elif 435 < cx < 540:
                        player_direction = 1
                        S = 1
                        A,W,D = 0,0,0
                    elif 540 < cx < 645:
                        player_direction = 3
                        A = 1
                        W,S,D = 0,0,0
                    elif 645 < cx < 750:
                        player_direction = 2
                        D = 1
                        W,S,A = 0,0,0
                for i in range(30):
                    if i*25 < cy < (i+1)*25:
                        if (i)%3 == 0:
                                redc[(i)//3] = 1
                        elif (i-1)%3 == 0:
                                greenc[(i-1)//3] = 1
                        elif (i-2)%3 == 0:
                                bluec[(i-2)//3] = 1
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                if 330 < cx < 750 and cy >= 675:
                    exitcustomise()
                redc = [0,0,0,0,0,0,0,0,0,0]
                greenc = [0,0,0,0,0,0,0,0,0,0]
                bluec = [0,0,0,0,0,0,0,0,0,0]
                W,A,S,D = 0,0,0,0
        for i in range(10):
            if cx < 256:
                if redc[i] == 1:
                    cred[i] = cx
                if greenc[i] == 1:
                    cgreen[i] = cx
                if bluec[i] == 1:
                    cblue[i] = cx
            elif cx < 330:
                if redc[i] == 1:
                    cred[i] = 255
                if greenc[i] == 1:
                    cgreen[i] = 255
                if bluec[i] == 1:
                    cblue[i] = 255
        Draw_Player()
        if controller > 0:
            if (con.get_axis(1) <= -0.5 or con.get_axis(3)  <= -0.5) and CY >= 10:
                    CY -= 10
                    MOUSE = 0
            if (con.get_axis(1) >= 0.5 or con.get_axis(3)  >= 0.5) and CY <= 740:
                    CY += 10
                    MOUSE = 0
            if (con.get_axis(0) <= -0.5 or con.get_axis(4)  <= -0.5) and CX >= 10:
                    CX -= 10
                    MOUSE = 0
            if (con.get_axis(0) >= 0.5 or con.get_axis(4)  >= 0.5) and CX <= 840:
                    CX += 10
                    MOUSE = 0
        pygame.draw.ellipse(screen,white,[cx-5,cy-5,10,10],1)
        pygame.display.flip()
    
def Draw_Player():
        global Hat,Dress,Fhair
        Hat = cHat
        Dress = cDress
        Fhair = cFhair
        drawplayer.go()
#(size,text,colour,x,y,bold,italic)
def drawhotbar():
    pygame.draw.rect(screen,black,[750,0,100,750])
    for i in range(10):
        if TOOLS[i] == 1:
            screen.blit(tool1[i],(750,50*i))
        else:
            screen.blit(tool0[i],(750,50*i))
        if ITEMS[i] > 0:
            screen.blit(item1[i],(800,50*i))
            if ITEMS[i] > 1:
                drawtext(25,str(ITEMS[i]),white,800,50*i,False,False)
        else:
            screen.blit(item0[i],(800,50*i))
        if KEYS[i] == 1:
            screen.blit(key[i],(750+(i%2)*50,500+(i//2)*50))
        else:
            screen.blit(key[10],(750+(i%2)*50,500+(i//2)*50))
    #for i in range(15):
        #for j in range(2):
            #pygame.draw.rect(screen,blue,[750+j*50,50*i,50,50],1)
    

def genground():
        if x >= 1155:
                if 1125 < y:
                        screen.blit(topcornerL,(x-1500,y-1500))
                if 375 < y:
                        screen.blit(sidewallL,(x-1500,y-1125))
                if -375 < y < 1125:
                        screen.blit(sidewallL,(x-1500,y-375))
                if -1125 < y < 375:
                        screen.blit(sidewallL,(x-1500,y+375))
                if -375 > y:
                        screen.blit(sidewallL,(x-1500,y+1125))
                if -1125 > y:
                        screen.blit(bottomcornerL,(x-1500,y+1875))
        elif x <= -1155:
                if 1125 < y:
                        screen.blit(topcornerR,(x+1875,y-1500))
                if 375 < y:
                        screen.blit(sidewallR,(x+1890,y-1125))
                if -375 < y < 1125:
                        screen.blit(sidewallR,(x+1890,y-375))
                if -1125 < y < 375:
                        screen.blit(sidewallR,(x+1890,y+375))
                if -375 > y:
                        screen.blit(sidewallR,(x+1890,y+1125))
                if -1125 > y:
                        screen.blit(bottomcornerR,(x+1875,y+1875))
        if y >= 1140:
                if 1110 < x:
                        screen.blit(topcornerL,(x-1500,y-1500))
                if 375 < x:
                        screen.blit(topwall,(x-1125,y-1500))
                if -375 < x < 1125:
                        screen.blit(topwall,(x-375,y-1500))
                if -1125 < x < 375:
                        screen.blit(topwall,(x+375,y-1500))
                if -375 > x:
                        screen.blit(topwall,(x+1125,y-1500))
                if -1110 > x:
                        screen.blit(topcornerR,(x+1875,y-1500))
        elif y <= -1140:
                if 1110 < x:
                        screen.blit(bottomcornerL,(x-1500,y+1875))
                if 375 < x:
                        screen.blit(bottomwall,(x-1125,y+1890))
                if -375 < x < 1125:
                        screen.blit(bottomwall,(x-375,y+1890))
                if -1125 < x < 375:
                        screen.blit(bottomwall,(x+375,y+1890))
                if -375 > x:
                        screen.blit(bottomwall,(x+1125,y+1890))
                if -1110 > x:
                        screen.blit(bottomcornerR,(x+1875,y+1875))
        pygame.draw.rect(screen,ggrass,[x-1140,y-1140,3030,3030])
        s = pygame.Surface((150,150))
        s.set_alpha(140)
        s.fill(grass)           
        for i in range(10):
                mi = -1125+300*i
                for j in range(10):
                        mj = -1125+300*j
                        if i-1 <= int(11-((x+1500)/300)) <= i+3 and j-1 <= int(11-((y+1500)/300)) <= j+3:
                                for k in range(2):
                                        mk = 150*k
                                        for m in range(2):
                                                mm = 150*m
                                                screen.blit(ground,(x+mi+mk,y+mj+mm))
                                                #screen.blit(s,(x+mi+mk,y+mj+mm))
                                pygame.draw.rect(screen,ggrass,[x+mi,y+mj,300,300],2)



        
def draw():
        global moveup,movedown,moveright,moveleft,x,y,W,A,S,D
        
        genground()
        moveup,movedown,moveright,moveleft = 1,1,1,1
##        gx = int(((x-1500)/-15))
##        gy = int(((y-1500)/-15))
##        for i in range(11):
##                if buildingsA[i] <= x-225 <= buildingsD[i] and buildingsW[i] <= y-225 <= buildingsS[i]-15:
##                        moveup = 0
##                if buildingsA[i]-15 <= x-225 <= buildingsD[i] and buildingsW[i]+15 <= y-225 <= buildingsS[i]-15:
##                        moveleft = 0
##                if buildingsA[i] <= x-225 <= buildingsD[i] and buildingsW[i]+15 <= y-225 <= buildingsS[i]:
##                        movedown = 0
##                if buildingsA[i] <= x-225 <= buildingsD[i]+15 and buildingsW[i]+15 <= y-225 <= buildingsS[i]-15:
##                        moveright = 0
##        for i in range(1):
##                if lakesA[i] <= x-225 <= lakesD[i] and lakesW[i] <= y-225 <= lakesS[i]-15:
##                        moveup = 0
##                if lakesA[i]-15 <= x-225 <= lakesD[i] and lakesW[i]+15 <= y-225 <= lakesS[i]-15:
##                        moveleft = 0
##                if lakesA[i] <= x-225 <= lakesD[i] and lakesW[i]+15 <= y-225 <= lakesS[i]:
##                        movedown = 0
##                if lakesA[i] <= x-225 <= lakesD[i]+15 and lakesW[i]+15 <= y-225 <= lakesS[i]-15:
##                        moveright = 0
        if gy == 0 or grid[gy][gx] != 0 or grid[gy][gx+1] != 0:
            moveup = 0
        if gx == 0 or grid[gy+1][gx-1] != 0:
            moveleft = 0
        if gy == 199 or grid[gy+2][gx] != 0 or grid[gy+2][gx+1] != 0:
            movedown = 0
        if gx == 199 or grid[gy+1][gx+2] != 0:
            moveright = 0
        for i in range(5):
            cx = ((lakes[i][0]-gx)*15)+360
            cy = ((lakes[i][1]-gy)*15)+360
            if lakes[i][0]-25 <= gx <= lakes[i][0]+38 and lakes[i][1]-25 <= gy <= lakes[i][1]+32:
                    screen.blit(lake,(cx,cy))
                    
            cx = ((pens[i][0]-gx)*15)+360
            cy = ((pens[i][1]-gy)*15)+360
            if pens[i][0]-25 <= gx <= pens[i][0]+31 and pens[i][1]-25 <= gy <= pens[i][1]+28:
                    screen.blit(pen,(cx,cy))

            cx = ((digsites[i][0]-gx)*15)+360
            cy = ((digsites[i][1]-gy)*15)+360
            if digsites[i][0]-25 <= gx <= digsites[i][0]+38 and digsites[i][1]-25 <= gy <= digsites[i][1]+32:
                    screen.blit(digsite,(cx,cy))
                        
        if movedown == 0:
                Draw_Player()
        if y >= 1140:
            if -1110 < x < 1110:
                if 6 <= TIME <= 11:
                    s = pygame.Surface((750,23-TIME))
                    s.set_alpha(127)
                    s.fill((0,0,0))  
                    screen.blit(s, (0,y-1152))
                elif 11 <= TIME <= 13:
                    s = pygame.Surface((750,(93-(TIME*TIME*0.55))*0.45))
                    s.set_alpha(127)
                    s.fill((0,0,0))  
                    screen.blit(s, (0,y-1140-(93-(TIME*TIME*0.55))*0.45))
                elif 13 <= TIME <= 18:     
                    s = pygame.Surface((750,(TIME-12)*2))
                    s.set_alpha(127)
                    s.fill((0,0,0))    
                    screen.blit(s, (0,y-1160-(TIME-12)*2))



                
        for i in range(11):
                cx = x-buildingsA[i]
                cy = y-buildingsW[i]
                sx = ((buildingsA[i]-buildingsD[i])**2)**0.5
                sy = ((buildingsW[i]-buildingsS[i])**2)**0.5
                if buildingsD[i]-735 <= x <= buildingsA[i]+835 and buildingsS[i]-735 <= y <= buildingsW[i]+735:
                        screen.blit(building,(cx,cy))
                        if KEYS[i] == 0:
                                font = pygame.font.SysFont('Calibri', 40, True, False)
                                text = font.render(buildingsn[i], True, black)
                                screen.blit(text, [cx,cy+sx*0.3])
                                text = font.render(buildingsn[i], True, buildingsc[i])
                                screen.blit(text, [cx+2,cy+sx*0.3])
                                pygame.draw.rect(screen,black,[cx+(0.4*sx),cy+(0.7*sy),sx*0.2,sy*0.3])
                        if KEYS[i] == 1:
                                pygame.draw.rect(screen,windowish,[cx+(0.4*sx),cy+(0.7*sy),sx*0.2,sy*0.3])
                                pygame.draw.rect(screen,black,[cx+(0.4*sx),cy+(0.7*sy),sx*0.2,sy*0.3],1)
                                if x == buildingsD[0]+sx and y == buildingsW[0]+225 and i == 0  and W == 1:
                                    W,A,S,D = 0,0,0,0
                                    g1.on = 1
                                    g1.go()
                                elif x == buildingsD[1]+sx and y == buildingsW[1]+225 and i == 1  and W == 1:
                                    W,A,S,D = 0,0,0,0
                                    g2.on = 1
                                    g2.go()
                                elif x == buildingsD[2]+sx and y == buildingsW[2]+225 and i == 2  and W == 1:
                                    W,A,S,D = 0,0,0,0
                                    g3.on = 1
                                    g3.go()
                                if gx == 111 and gy == 96:
                                    shop()


        for i in range(10):
            cx = ((wells[i][0]-gx)*15)+360
            cy = ((wells[i][1]-gy)*15)+360
            if wells[i][0]-25 <= gx <= wells[i][0]+25 and wells[i][1]-25 <= gy <= wells[i][1]+26:
                    screen.blit(well,(cx,cy))

            cx = ((flowers[i][0]-gx)*15)+360
            cy = ((flowers[i][1]-gy)*15)+360
            if flowers[i][0]-25 <= gx <= flowers[i][0]+24 and flowers[i][1]-25 <= gy <= flowers[i][1]+24:
                    screen.blit(flower,(cx,cy))

            cx = ((stacks[i][0]-gx)*15)+360
            cy = ((stacks[i][1]-gy)*15)+360
            if stacks[i][0]-25 <= gx <= stacks[i][0]+25 and stacks[i][1]-25 <= gy <= stacks[i][1]+25:
                    screen.blit(stack,(cx,cy))
                    
            cx = ((trees[i][0]-gx)*15)+360
            cy = ((trees[i][1]-gy)*15)+360
            if trees[i][0]-25 <= gx <= trees[i][0]+26 and trees[i][1]-25 <= gy <= trees[i][1]+26:
                    screen.blit(tree,(cx,cy))

            cx = ((pines[i][0]-gx)*15)+360
            cy = ((pines[i][1]-gy)*15)+360
            if pines[i][0]-25 <= gx <= pines[i][0]+26 and pines[i][1]-25 <= gy <= pines[i][1]+27:
                    screen.blit(pine,(cx,cy))

            cx = ((rocks[i][0]-gx)*15)+360
            cy = ((rocks[i][1]-gy)*15)+360
            if rocks[i][0]-25 <= gx <= rocks[i][0]+25 and rocks[i][1]-25 <= gy <= rocks[i][1]+25:
                    screen.blit(rock,(cx,cy))

            cx = ((ruins[i][0]-gx)*15)+360
            cy = ((ruins[i][1]-gy)*15)+360
            if ruins[i][0]-25 <= gx <= ruins[i][0]+25 and ruins[i][1]-25 <= gy <= ruins[i][1]+25:
                    screen.blit(ruin,(cx,cy))

            
                                    
        if movedown != 0:
                Draw_Player()
        if y <= -1140:
            if -1110 < x < 1110:
                if 6 <= TIME <= 11:
                    s = pygame.Surface((750,23-TIME))
                    s.set_alpha(127)
                    s.fill((0,0,0))  
                    screen.blit(s, (0,y-1152))
                elif 11 <= TIME <= 13:
                    s = pygame.Surface((750,(93-(TIME*TIME*0.55))*0.45))
                    s.set_alpha(127)
                    s.fill((0,0,0))  
                    screen.blit(s, (0,y-1140-(93-(TIME*TIME*0.55))*0.45))
                elif 13 <= TIME <= 18:     
                    s = pygame.Surface((750,(TIME-12)*2))
                    s.set_alpha(127)
                    s.fill((0,0,0))    
                    screen.blit(s, (0,y-1160-(TIME-12)*2))


            
        clockoverlay(0,0,750,750)
        for i in range(11):
                cx = x-buildingsA[i]
                cy = y-buildingsW[i]
                sx = ((buildingsA[i]-buildingsD[i])**2)**0.5
                sy = ((buildingsW[i]-buildingsS[i])**2)**0.5
                if buildingsD[i]-735 <= x <= buildingsA[i]+850 and buildingsS[i]-735 <= y <= buildingsW[i]+735:
                    if KEYS[i] == 1:
                            s = pygame.Surface((sx*0.2,sy*0.3))
                            s.set_alpha(90)
                            s.fill(white)
                            screen.blit(s,(cx+(0.4*sx),cy+(0.7*sy)))
                            for j in range(int(sy*0.3)):
                                    s = pygame.Surface((int(sx*0.2)+(j*2),1))
                                    s.set_alpha(90-(j*2))
                                    s.fill(white)           
                                    screen.blit(s, (cx+(0.4*sx)-j,cy+sy+j))
                            font = pygame.font.SysFont('Calibri', 40, True, False)
                            text = font.render(buildingsn[i], True, black)
                            screen.blit(text, [cx,cy+sx*0.3])
                            text = font.render(buildingsn[i], True, buildingsc[i])
                            screen.blit(text, [cx+2,cy+sx*0.3])
        font = pygame.font.SysFont('Calibri', 30, True, False)
        if (11-((x+1500)/300)) != 11:
            text = font.render(str(gx), True, white)
        else:
            text = font.render('10', True, white)
        screen.blit(text, [0,0])
        if (11-((y+1500)/300)) != 11:
            text = font.render(str(gy), True, white)
        else:#str(hour)+' '+str(minute)+' '+str(second)
            text = font.render('10', True, black)
        screen.blit(text, [0,30])
        text = font.render(str(hour)+':'+str(minute)+':'+str(second)+'  '+str(TIME), True, white)
        screen.blit(text, [0,60])
        drawhotbar()

#def language():

#def controls():
def exitshop():
    global y,gy,W,A,S,D,player_direction,shopping
    shopping = False
    gy += 1
    y -= 15
    W,A,S,D = 0,0,0,0
    player_direction = 1

def shop():
    global shopping,TOOLS,KEYS,ITEMS
    shopping = True
    while shopping:
        cursorpos = pygame.mouse.get_pos()
        cx = cursorpos[0]
        cy = cursorpos[1]
        for i in range(5):
            for j in range(5):
                screen.blit(ground,(i*150,j*150))
        screen.blit(SHOP,(0,0))
        for i in range(10):
            if TOOLS[i] == 0:
                screen.blit(tool1[i],((i*70)+35,115))
            else:
                screen.blit(tool0[i],((i*70)+35,115))
            if KEYS[i] == 0:
                screen.blit(key[i],((i*70)+35,250))
            else:
                screen.blit(key[10],((i*70)+35,250))
            if ITEMS[i] > 0:
                screen.blit(item1[i],((i*70)+35,465))
            else:
                screen.blit(item0[i],((i*70)+35,465))
        
        drawhotbar()
        drawtext(100,"BUY",white,245,10,True,False)
        drawtext(100,"SELL",white,245,355,True,False)
        drawtext(100,"EXIT",white,245,600,True,False)
            #(size,text,colour,x,y,bold,italic)


        
        pygame.draw.ellipse(screen,white,[cx-5,cy-5,10,10],1)
        for event in pygame.event.get():
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_ESCAPE:
                    exitshop()
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                for i in range(10):
                    if (i*70)+35 <= cx < (i*70)+85:
                        if 115 <= cy < 215:
                            TOOLS[i] = 1
                        elif 250 <= cy < 350:
                            KEYS[i] = 1
                        elif 465 <= cy < 565:
                            ITEMS[i] -= 1
                if 245 <= cx < 505 and 600 <= cy < 700:
                    exitshop()
        pygame.display.flip()

        
    
def settings():
    global Settings,mvol,svol,CX,CY,MOUSE
    s = pygame.Surface((150,150))
    s.set_alpha(140)
    s.fill(grass)
    vol = 0
    Settings = 1
    while Settings == 1:
        if  controller > 0 and MOUSE == 0:
            cx = CX
            cy = CY
        else:
            cursorpos = pygame.mouse.get_pos()
            cx = cursorpos[0]
            cy = cursorpos[1]
            CX = cx
            CY = cy
        for i in range(6):
            for j in range(5):
                screen.blit(ground,(i*150,j*150))
                #screen.blit(s,(i*150,j*150))
        clockoverlay(0,0,850,750)
        if vol == 1:
            if cx < 10:
                mvol = 0
            elif cx > 110:
                mvol = 1
            else:
                mvol = (cx-10)/100
            channel1.set_volume(mvol)
        if vol == 2:
            if cx < 10:
                svol = 0
            elif cx > 110:
                svol = 1
            else:
                svol = (cx-10)/100
            channel2.set_volume(svol)
        pygame.draw.rect(screen,black,[10,5,100,10])
        pygame.draw.ellipse(screen,black,[5,5,10,10])
        pygame.draw.ellipse(screen,black,[105,5,10,10])
        pygame.draw.ellipse(screen,white,[(mvol*100)+5,5,10,10])
        pygame.draw.rect(screen,black,[10,25,100,10])
        pygame.draw.ellipse(screen,black,[5,25,10,10])
        pygame.draw.ellipse(screen,black,[105,25,10,10])
        pygame.draw.ellipse(screen,white,[(svol*100)+5,25,10,10])
        font = pygame.font.SysFont('Calibri', 20)
        Text = font.render(TEXT[5], True,black)
        screen.blit(Text,[120,0])
        Text = font.render(TEXT[6], True,black)
        screen.blit(Text,[120,20])
        roundbox(black,red,150,30,550,210,15)
        roundbox(black,green,150,270,550,210,15)
        roundbox(black,blue,150,510,550,210,15)
        drawtext(100,TEXT[7],white,200,90,True,False)
        drawtext(100,TEXT[8],white,175,330,True,False)
        drawtext(100,TEXT[9],white,310,570,True,False)
        if controller > 0:
            if (con.get_axis(1) <= -0.5 or con.get_axis(3)  <= -0.5 or con.get_hat(0)[1]  == 1) and CY >= 5:
                    CY -= 5
                    MOUSE = 0
            if (con.get_axis(1) >= 0.5 or con.get_axis(3)  >= 0.5 or con.get_hat(0)[1]  == -1) and CY <= 745:
                    CY += 5
                    MOUSE = 0
            if (con.get_axis(0) <= -0.5 or con.get_axis(4)  <= -0.5 or con.get_hat(0)[0]  == -1) and CX >= 5:
                    CX -= 5
                    MOUSE = 0
            if (con.get_axis(0) >= 0.5 or con.get_axis(4)  >= 0.5 or con.get_hat(0)[0]  == 1) and CX <= 845:
                    CX += 5
                    MOUSE = 0

                
        pygame.draw.ellipse(screen,white,[cx-5,cy-5,10,10],1)

        
        
        for event in pygame.event.get():
            if controller > 0:
                if event.type == pygame.JOYBUTTONDOWN:
                    if cx < 120 and cy < 20:
                        vol = 1
                    if cx < 120 and 20 < cy < 40:
                        vol = 2
                if event.type == pygame.JOYBUTTONUP:
                    if event.button == 6 or event.button == 1:
                        Settings = 0
                    if event.button == 7 or event.button == 2:
                         config()
                    if event.button == 3:
                        Create_skin()
                    if event.button == 0:
                        vol = 0
                        if 150 < cx < 700:
                            if  30 < cy < 240:
                                config()
                            if 270 < cy < 480:
                                Create_skin()
                            if 510 < cy < 620:
                                Settings = 0
            if event.type == pygame.MOUSEMOTION:
                MOUSE = 1
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                vol = 0
                os.chdir('../SETTINGS')
                SAVE = open('settings.txt','w')
                SAVE.write(str(lang)+'\n'+str(int(mvol*10))+'\n'+str(int(svol*10))+'\n')
                SAVE.close()
                if 150 < cx < 700:
                    if  30 < cy < 240:
                        config()
                    if 270 < cy < 480:
                        Create_skin()
                    if 510 < cy < 620:
                        Settings = 0
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if cx < 120 and cy < 20:
                    vol = 1
                if cx < 120 and 20 < cy < 40:
                    vol = 2
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_ESCAPE:
                    Settings = 0
        pygame.display.flip()                
            
        
def exitpause():
    global Pause
    os.chdir('../SAVE_FILES')
    if file == 1:
        coor = open('coordinatesA.txt','w')
        items = open('itemsA.txt','w')
        tools = open('toolsA.txt','w')
        keys = open('keysA.txt','w')
    elif file == 2:
        coor = open('coordinatesB.txt','w')
        items = open('itemsB.txt','w')
        tools = open('toolsB.txt','w')
        keys = open('keysB.txt','w')
    elif file == 3:
        coor = open('coordinatesC.txt','w')
        items = open('itemsC.txt','w')
        tools = open('toolsC.txt','w')
        keys = open('keysC.txt','w')
    coor.write(str(x)+'\n'+str(y)+'\n'+str(player_direction)+'\n')
    coor.close()
    for i in range(11):
        items.write(str(ITEMS[i])+'\n')
    for i in range(10):
        tools.write(str(TOOLS[i])+'\n')
        keys.write(str(KEYS[i])+'\n')
    items.close()
    tools.close()
    keys.close()
    Pause = 0
    os.chdir('..')
    title()
    
    
def pause():
    global Pause, CX,CY,MOUSE
    s = pygame.Surface((150,150))
    s.set_alpha(140)
    s.fill(grass)
    Pause = 1
    while On and Pause == 1:
        if  controller > 0 and MOUSE == 0:
            cx = CX
            cy = CY
        else:
            cursorpos = pygame.mouse.get_pos()
            cx = cursorpos[0]
            cy = cursorpos[1]
            CX = cx
            CY = cy
        for i in range(6):
            for j in range(5):
                screen.blit(ground,(i*150,j*150))
                #screen.blit(s,(i*150,j*150))
        clockoverlay(0,0,850,750)
        roundbox(black,red,150,30,550,210,15)
        roundbox(black,green,150,270,550,210,15)
        roundbox(black,blue,150,510,550,210,15)
        drawtext(100,TEXT[10],white,250,90,True,False)
        drawtext(100,TEXT[11],white,225,330,True,False)
        drawtext(100,TEXT[12],white,150,570,True,False)
        if controller > 0:
            if (con.get_axis(1) <= -0.5 or con.get_axis(3)  <= -0.5 or con.get_hat(0)[1]  == 1) and CY >= 5:
                CY -= 5
                MOUSE = 0
            elif (con.get_axis(1) >= 0.5 or con.get_axis(3)  >= 0.5 or con.get_hat(0)[1]  == -1) and CY <= 745:
                    CY += 5
                    MOUSE = 0
            if (con.get_axis(0) <= -0.5 or con.get_axis(4)  <= -0.5 or con.get_hat(0)[0]  == -1) and CX >= 5:
                    CX -= 5
                    MOUSE = 0
            elif (con.get_axis(0) >= 0.5 or con.get_axis(4)  >= 0.5 or con.get_hat(0)[0]  == 1) and CX <= 845:
                    CX += 5
                    MOUSE = 0
        pygame.draw.ellipse(screen,white,[cx-5,cy-5,10,10],1)
        for event in pygame.event.get():
            if controller > 0:
                if event.type == pygame.JOYBUTTONUP:
                    if event.button == 7 or event.button == 2:
                        Pause = 0
                    elif event.button == 3:
                        settings()
                    elif event.button == 6 or event.button == 1:
                        exitpause()
                    elif event.button == 0:
                        if 150 < cx < 700:
                            if  30 < cy < 240:
                                Pause = 0
                                main()
                            elif 270 < cy < 480:
                                settings()
                            elif 510 < cy < 620:
                                exitpause()
            if event.type == pygame.MOUSEMOTION:
                MOUSE = 1
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_ESCAPE:
                        exitpause()
                elif event.key == pygame.K_s:
                    settings()
                else:
                    Pause = 0
                    main()
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                if 150 < cx < 700:
                    if  30 < cy < 240:
                        Pause = 0
                        main()
                    elif 270 < cy < 480:
                        settings()
                    elif 510 < cy < 620:
                        exitpause()
        pygame.display.flip()

def clockoverlay(cx,cy,sx,sy):
    global TIME,hour,minute,second,shade
    #Datetime = datetime.datetime.now()
    hour = 0#Datetime.hour
    minute = 0#Datetime.minute
    second = 0#Datetime.second
    TIME = 11.5#hour + (minute/60) + (second/360)
    if TIME >= 24:
            TIME = 0
    if 0 <= TIME <= 11.5:
            shade = (-360/23)*TIME+180
    elif 11.5 <= TIME <= 24:
            shade = (360/23)*TIME-180
    s = pygame.Surface((sx,sy))
    s.set_alpha(shade)
    s.fill((0,0,0))           
    screen.blit(s, (cx,cy))



def main():
    global On,x,y,W,A,S,D,player_direction, leg, legup, legdown, legleft, legright,TIME,doing
    global custom,moveup,movedown,moveright,moveleft,pressed,money,item,pressed,gx,gy
    clock = pygame.time.Clock()
    try:
        On
    except NameError:
        On = False
    else:
        On = True
    size = [850, 750]
    screen = pygame.display.set_mode(size,pygame.FULLSCREEN)
    custom = 0
    config()
    while On:
        TIME += 0.01
        if TIME >= 24:
            TIME = 0

        draw()
        for event in pygame.event.get():
            if controller > 0:
                if event.type == pygame.JOYAXISMOTION or event.type == pygame.JOYHATMOTION:
                    if con.get_axis(1) > -0.5 or con.get_axis(3)  > -0.5 or con.get_hat(0)[1]  == 0:
                        W = 0
                    elif con.get_axis(1) < 0.5 or con.get_axis(3)  > 0.5 or con.get_hat(0)[1]  == 0:
                        S = 0
                    if con.get_axis(0) < 0.5 or con.get_axis(4)  < 0.5 or con.get_hat(0)[0]  == 0:
                        D = 0
                    elif con.get_axis(0) > -0.5 or con.get_axis(4)  > -0.5 or con.get_hat(0)[0]  == 0:
                        A = 0
                    if con.get_axis(1) <= -0.5 or con.get_axis(3)  <= -0.5 or con.get_hat(0)[1]  == 1:
                        W = 1
                    elif con.get_axis(1) >= 0.5 or con.get_axis(3)  >= 0.5 or con.get_hat(0)[1]  == -1:
                        S = 1
                    if con.get_axis(0) >= 0.5 or con.get_axis(4)  >= 0.5 or con.get_hat(0)[0]  == 1:
                        D = 1
                    elif con.get_axis(0) <= -0.5  or con.get_axis(4)  <= -0.5 or con.get_hat(0)[0]  == -1:
                        A = 1
                if event.type == pygame.JOYBUTTONUP:
                        if event.button == 6 or event.button == 7:
                            pause()
                        elif event.button == 2:
                            Map.openmap()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_BACKSPACE:
                    TIME += 1
                if event.key == pygame.K_RETURN:
                    TIME += 0.1
                elif event.key == pygame.K_ESCAPE: 
                    pause()
                elif event.key == pygame.K_q:
                    Map.openmap()
                if event.key == pygame.K_e:
                    doing = 0
                if event.key == pygame.K_w:
                    W = 0
                if event.key == pygame.K_s:
                    S = 0
                if event.key == pygame.K_d:
                    D = 0
                if event.key == pygame.K_a:
                    A = 0
                if event.key == pygame.K_ESCAPE:
                    pause()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_e:
                    doing = 1
                if event.key == pygame.K_w:
                    W = 1
                if event.key == pygame.K_s:
                    S = 1
                if event.key == pygame.K_d:
                    D = 1
                if event.key == pygame.K_a:
                    A = 1

        if W == 1 and gy > 0:
            player_direction = 0
            if moveup == 1:
                y += 15
                gy -= 1
                legup = 1
        elif S == 1 and gy < 199:
            player_direction = 1
            if movedown == 1:
                y -= 15
                gy += 1
                legdown = 1
        elif D == 1 and gx < 199:
            player_direction = 2
            if moveright == 1:
                x -= 15
                gx += 1
                legright = 1
        elif A == 1 and gx > 0:
            player_direction = 3
            if moveleft == 1:
                x += 15
                gx -= 1
                legleft = 1
        pygame.display.flip()
        clock.tick(30)



try:
    On
except NameError:
    On = False
else:
    On = True 
if On:
##    screen.fill(white)
##    #drawtext(900,'N',blue,100,-50,True,False)
##    pygame.draw.rect(screen,blue,[0,0,85,150])
##    pygame.draw.rect(screen,blue,[255,0,85,225])
##    pygame.draw.rect(screen,blue,[170,225,85,150])
##    pygame.draw.rect(screen,blue,[85,375,85,75])
##    pygame.draw.rect(screen,blue,[0,450,85,75])
##    pygame.draw.rect(screen,blue,[425,0,425,75])
##    pygame.draw.rect(screen,blue,[765,0,85,375])
##    pygame.draw.rect(screen,blue,[765,450,85,75])
##    drawtext(100,'Nathan Turner',blue,100,650,True,False)
##    drawtext(10,'TM',blue,725,675,True,False)
##    pygame.display.flip()
##    sleep(1)
    title()
else:
    deadsize = 750
    while deadsize != 0:
        deadsize -= 1
        screen = pygame.display.set_mode((int((17/15)*deadsize),deadsize))
    pygame.display.set_mode((0,0))
    pygame.quit()
##    print("...please don't leave me.")
##    sleep(1)
##    print("please.")
##    sleep(1)
##    print("PLEASE.")
##    sleep(1)
##    print("I'M SORRY, OK?")
##    sleep(1)
##    print("Fine! Go ahead and leave me!")
##    sleep(2)
##    print("I think I prefer to stay inside.")
##    sleep(2)
##    print("Maybe you'll find someone else")
##    print("To help you.")
##    sleep(2)
##    print("Maybe Black Mesa...")
##    sleep(2)
##    print("THAT WAS A JOKE, HA HA, FAT CHANCE.")

    

