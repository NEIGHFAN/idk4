##import pygame,random
##pygame.init()
##size = [850,750]
##screen = pygame.display.set_mode(size,pygame.FULLSCREEN)

def CountDown():
    global seconds
    seconds = 31-(pygame.time.get_ticks()-start_ticks)/1000
    return float(seconds)
def go():
    global pygame,start_ticks
    import os
    os.chdir('..')
    import Eden
    if os.path.exists('./data') == True:
        os.chdir('./data')
    random = Eden.random
    pygame = Eden.pygame
    screen = Eden.screen
    size = Eden.size
    cx = 425
    cy = 375
    x,y = 0,0
    chance = 3
    entrance = 0
    score = 0
    W,A,S,D = 0,0,0,0
    fire =0
    health = 5.1
    ammo = 40.1
    pygame.mouse.set_visible(0)
    zombco = [0,0]
    zombN = pygame.image.load('zombie.png')
    zombL = pygame.image.load('zombie L.png')
    zombR = pygame.image.load('zombie R.png')
    ZOMB = [zombN,zombL,zombN,zombR,zombN,zombL,zombN,zombR]
    zombSN = pygame.image.load('zombieS.png')
    zombSL = pygame.image.load('zombieSL.png')
    zombSR = pygame.image.load('zombieSR.png')
    ZOMBS = [zombSN,zombSL,zombSN,zombSR,zombSN,zombSL,zombSN,zombSR]
    seconds = 30
    on = 1
    title = 1
    gloom = pygame.image.load('gloom.png')
    gloom = pygame.transform.scale(gloom,size)
    screen.blit(gloom,(0,0))
    pygame.display.flip()
    while title == 1:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                title = 0
    start_ticks = pygame.time.get_ticks()
    while ammo > 1 and seconds > 0:
        seconds = CountDown()
        #print(int(seconds))
        if health < 1:
            pygame.display.quit()
        overlay = (0,0,0)
        alpha = 127
        if fire >= 2:
            fire = 0
        cursorpos = pygame.mouse.get_pos()
        mousebox = pygame.draw.ellipse(screen,(255,255,255),[420,370,10,10],1)
        try:
            zomb = zomb
        except:
            zomb = pygame.Surface((0,0))
        zombox = pygame.draw.rect(screen,(255,255,255),[zombco[0],zombco[1],zomb.get_width(),zomb.get_height()])
        screen.fill((0,255,255))
        for event in pygame.event.get():
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    W = 0
                if event.key == pygame.K_a:
                    A = 0
                if event.key == pygame.K_s:
                    S = 0
                if event.key == pygame.K_d:
                    D = 0
##                if event.key == pygame.K_ESCAPE:
##                    pygame.quit()
##                if event.key == pygame.K_RETURN:
##                    entrance = random.randint(1,3)
##                    chance = 1
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    W = 1
                if event.key == pygame.K_a:
                    A = 1
                if event.key == pygame.K_s:
                    S = 1
                if event.key == pygame.K_d:
                    D = 1
                if event.key == pygame.K_SPACE:
                    if fire == 0:
                        fire = 1
                            
            if event.type == pygame.MOUSEMOTION:
                cx = 850-cursorpos[0]
                cy = 750-cursorpos[1]
            if event.type == pygame.MOUSEBUTTONUP:
                if fire == 0:
                    fire = 1
        
                
                        
        #cx,cy = 425,375
        if W == 1 and cy < 745:
            cy += 5
        if A == 1 and cx < 845:
            cx += 5
        if S == 1 and cy > 5:
            cy -= 5
        if D == 1 and cx > 5:
            cx -= 5
        x = (cx-425)/50
        y = (cy-375)/50
        pygame.draw.polygon(screen,(127,63,0),[[cx-200+y,cy-200+x],[cx+200-y,cy-200-x],[cx+200+y,cy+200+x],[cx-200-y,cy+200-x]])
        pygame.draw.polygon(screen,(127,63,0),[[0,0],[cx-200+y,cy-200+x],[cx+200-y,cy-200-x],[850,0]])
        pygame.draw.polygon(screen,(127,63,0),[[0,0],[cx-200+y,cy-200+x],[cx-200-y,cy+200-x],[0,750]])
        pygame.draw.polygon(screen,(127,127,127),[[0,750],[cx-200-y,cy+200-x],[cx+200+y,cy+200+x],[850,750]])
        pygame.draw.polygon(screen,(127,63,0),[[850,0],[cx+200-y,cy-200-x],[cx+200+y,cy+200+x],[850,750]])
        

        #pygame.draw.polygon(screen,(127,63,0),[[cx-350+y,cy-125+x],[cx-300+y,cy-100+x],[cx-300-y,cy+100-x],[cx-350-y,cy+125-x]])
        

        for i in range(7):
            X = (x*-int((i-3)/((((i-3)**2)**0.5)+0.1)))
            Y = (y*-int((i-3)/((((i-3)**2)**0.5)+0.1)))
            pygame.draw.line(screen,(0,0,0),[0,93.75*(i+1)],[cx-200+Y,cy+((i*50)-150)+X],4)
            pygame.draw.line(screen,(0,0,0),[cx-200+Y,cy+((i*50)-150)+X],[cx+200+Y,cy+((i*50)-150)+X],4)
            pygame.draw.line(screen,(0,0,0),[850,93.75*(i+1)],[cx+200+Y,cy+((i*50)-150)+X],4)
        #pygame.draw.polygon(screen,(0,0,0),[[(cx-200+Y)*0.25,(cy-50+X)*0.25],[(cx-100+Y)*0.75,(cy-50+X)*0.75],[(cx-100+Y)*0.75,(cy+50+X)*0.75],[(cx-200+Y)*0.25,(cy+50+X)*0.25]])

        #pygame.draw.line(screen,(0,255,0),[(cx-200+y)/2,(cy-200+x)/2+140],[(cx-200-y)/2,(cy-200-x)/2+360],3)
        #pygame.draw.line(screen,(0,0,255),[(cx-200+y)*0.75,(cy-200+x)*0.75+120],[(cx-200-y)*0.75,(cy-200-x)*0.75+310],3)

        #pygame.draw.polygon(screen,(0,0,0),[[(cx-200+y)*0.75,(cy-200-x/4)*0.75+120],[(cx-200+y)/2,(cy-200+x)/2+140],[(cx-200-y)/2,(cy-200+x)/2+360],[(cx-200-y)*0.75,(cy-200-x/2)*0.75+310]])
        #pygame.draw.polygon(screen,(0,0,0),[[(cx+485-y)*0.75,(cy-200+x/4)*0.75+120],[(cx+1050-y)/2,(cy-200-x)/2+140],[(cx+1050+y)/2,(cy-200-x)/2+360],[(cx+485+y)*0.75,(cy-200+x/2)*0.75+310]])
        pygame.draw.polygon(screen,(0,0,0),[[(cx-200+y)*0.75,(cy-200-x/4)*0.75+120],[(cx-200+y)/2,(cy-200+x)/2+140],[(cx-200-y)/2,(cy-200+x)/2+575],[(cx-200-y)*0.75,(cy-200-x/2)*0.75+485]])
        pygame.draw.polygon(screen,(0,0,0),[[(cx+485-y)*0.75,(cy-200+x/4)*0.75+120],[(cx+1050-y)/2,(cy-200-x)/2+140],[(cx+1050+y)/2,(cy-200-x)/2+575],[(cx+485+y)*0.75,(cy-200+x/2)*0.75+485]])



    ##    pygame.draw.line(screen,(0,0,0),[0,94],[cx-200+y*0.5,cy-150+x*0.5],4)
    ##    pygame.draw.line(screen,(0,0,0),[0,188],[cx-200+y*0.5,cy-100+x*0.5],4)
    ##    pygame.draw.line(screen,(0,0,0),[0,281],[cx-200+y*0.5,cy-50+x*0.5],4)
    ##    pygame.draw.line(screen,(0,0,0),[0,375],[cx-200,cy],4)
    ##    pygame.draw.line(screen,(0,0,0),[0,469],[cx-200-y*0.5,cy+50-x*0.5],4)
    ##    pygame.draw.line(screen,(0,0,0),[0,563],[cx-200-y*0.5,cy+100-x*0.5],4)
    ##    pygame.draw.line(screen,(0,0,0),[0,656],[cx-200-y*0.5,cy+150-x*0.5],4)

    ##    pygame.draw.line(screen,(0,0,0),[cx-200+y*0.5,cy-150+x*0.5],[cx+200-y*0.5,cy-150-x*0.5],4)
    ##    pygame.draw.line(screen,(0,0,0),[cx-200+y*0.5,cy-100+x*0.5],[cx+200-y*0.5,cy-100-x*0.5],4)
    ##    pygame.draw.line(screen,(0,0,0),[cx-200+y*0.5,cy-50+x*0.5],[cx+200-y*0.5,cy-50-x*0.5],4)
    ##    pygame.draw.line(screen,(0,0,0),[cx-200,cy],[cx+200,cy],4)
    ##    pygame.draw.line(screen,(0,0,0),[cx-200-y*0.5,cy+50-x*0.5],[cx+200+y*0.5,cy+50+x*0.5],4)
    ##    pygame.draw.line(screen,(0,0,0),[cx-200-y*0.5,cy+100-x*0.5],[cx+200+y*0.5,cy+100+x*0.5],4)
    ##    pygame.draw.line(screen,(0,0,0),[cx-200-y*0.5,cy+150-x*0.5],[cx+200+y*0.5,cy+150+x*0.5],4)

    ##    pygame.draw.line(screen,(0,0,0),[850,94],[cx+200-y*0.5,cy-150-x*0.5],4)
    ##    pygame.draw.line(screen,(0,0,0),[850,188],[cx+200-y*0.5,cy-100-x*0.5],4)
    ##    pygame.draw.line(screen,(0,0,0),[850,281],[cx+200-y*0.5,cy-50-x*0.5],4)
    ##    pygame.draw.line(screen,(0,0,0),[850,375],[cx+200,cy],4)
    ##    pygame.draw.line(screen,(0,0,0),[850,469],[cx+200+y*0.5,cy+50+x*0.5],4)
    ##    pygame.draw.line(screen,(0,0,0),[850,563],[cx+200+y*0.5,cy+100+x*0.5],4)
    ##    pygame.draw.line(screen,(0,0,0),[850,656],[cx+200+y*0.5,cy+150+x*0.5],4)




    ##    pygame.draw.line(screen,(0,0,0),[106,0],[cx-150+y*0.5,cy-200+x*0.5],4)
    ##    pygame.draw.line(screen,(0,0,0),[213,0],[cx-100+y*0.5,cy-200+x*0.5],4)
    ##    pygame.draw.line(screen,(0,0,0),[319,0],[cx-50+y*0.5,cy-200+x*0.5],4)
    ##    pygame.draw.line(screen,(0,0,0),[425,0],[cx,cy-200],4)
    ##    pygame.draw.line(screen,(0,0,0),[531,0],[cx+50-y*0.5,cy-200-x*0.5],4)
    ##    pygame.draw.line(screen,(0,0,0),[638,0],[cx+100-y*0.5,cy-200-x*0.5],4)
    ##    pygame.draw.line(screen,(0,0,0),[744,0],[cx+150-y*0.5,cy-200-x*0.5],4)

        



        
        pygame.draw.polygon(screen,(0,0,0),[[0,0],[cx-200+y,cy-200+x],[cx+200-y,cy-200-x],[850,0]],7)
        pygame.draw.polygon(screen,(0,0,0),[[0,0],[cx-200+y,cy-200+x],[cx-200-y,cy+200-x],[0,750]],7)
        pygame.draw.polygon(screen,(0,0,0),[[0,750],[cx-200-y,cy+200-x],[cx+200+y,cy+200+x],[850,750]],7)
        pygame.draw.polygon(screen,(0,0,0),[[850,0],[cx+200-y,cy-200-x],[cx+200+y,cy+200+x],[850,750]],7)


    ##    pygame.draw.polygon(screen,(0,0,0),[[450,531.25],[450,625],[700,925],[700,831.25]])
    ##    pygame.draw.polygon(screen,(0,0,0),[[450,531.25],[543.75,500],[793.75,800],[700,831.25]])
    ##    pygame.draw.polygon(screen,(63,63,63),[[450,531.25],[450,625],[700,925],[700,831.25]],5)
    ##    pygame.draw.polygon(screen,(63,63,63),[[450,531.25],[543.75,500],[793.75,800],[700,831.25]],5)
    ##    pygame.draw.rect(screen,(255,255,255),[370,370,20,20])



        pygame.draw.polygon(screen,(0,0,0),[[cx-75+(y/2),cy-100+x/4],[cx+75-(y/2),cy-100-x/4],[cx+75+(y/2),cy+200+x/4],[cx-75-(y/2),cy+200-x/4]])

        if chance >= 2:
            chance = random.randint(1,6)
            entrance = random.randint(1,3)
        if chance < 2:
            zomb = ZOMB[int(((chance-1)*100)//12.5)]
            zombs = ZOMBS[int(((chance-1)*100)//12.5)]
            zombsi = (int((zomb.get_width())*chance),int((zomb.get_height())*chance))
            zomb = pygame.transform.scale(zomb,zombsi)
            zombs = pygame.transform.scale(zombs,zombsi)
            chance += 0.005
            zomb.set_colorkey((255,255,255))
            zombs.set_colorkey((255,255,255))
            zombs.set_alpha(255-(64*(chance**2)))
            if entrance == 1:
                zombco = (cx-zomb.get_width()*0.5,cy+100-zomb.get_height()*0.5)
            if entrance == 2:
                zombco = (cx/2-100,cy/2+300-zomb.get_height()*0.5)
            if entrance == 3:
                zombco = (cx/2+650-zombsi[0]*2,cy/2+300-zomb.get_height()*0.5)
            screen.blit(zomb,zombco)
            screen.blit(zombs,zombco)
    ##    else:
    ##        chance = random.randint(1,1000)
    ##        entrance = random.randint(1,3)
        if 1.95 <= chance < 2:
            health -= 0.1
            overlay = (255,0,0)
            alpha = 190
        


      #  pygame.draw.rect(screen,(255,255,0),[cx-200,cy-200,400,400])
        s = pygame.Surface(size)
        s.set_alpha(alpha)
        s.fill(overlay)           
        screen.blit(s,(0,0))
        font = pygame.font.SysFont('Calibri',50,True,False)
        Text = font.render(str(score),True,(255,255,255))
        screen.blit(Text,[0,0])
        Text = font.render(str(int(health)),True,(255,255,255))
        screen.blit(Text,[0,700])
        Text = font.render(str(int(ammo)),True,(255,255,255))
        if ammo >= 10:
            screen.blit(Text,[800,700])
        else:
            screen.blit(Text,[825,700])
        Text = font.render(str(int(seconds)),True,(255,255,255))
        if seconds >= 10:
            screen.blit(Text,[800,0])
        else:
            screen.blit(Text,[825,0])

        if fire > 0 and ammo >= 1:
            if chance < 2:
                if zombox.contains(mousebox):
                    score += int(((2-chance)*10)//1+1)*100
                    chance = 3
    ##            if entrance == 1:
    ##                if 425-zomb.get_width()*0.5 < cx < 425+zomb.get_width()*0.5 and 275-zomb.get_height()*0.5 < cy < 275+zomb.get_height()*0.5:
    ##                    score += int(((2-chance)*10)//1+1)*100
    ##                    chance = 3
    ##            if entrance == 2 or entrance == 3:
    ##                if 600 < cx:# and 275-zomb.get_height()*0.5 < cy < 275+zomb.get_height()*0.5:
    ##                    score += int(((2-chance)*10)//1+1)*100
    ##                    chance = 3
                        
            ammo -= 0.2
            fire += 0.1
            gun = pygame.image.load('gunfire.png')
            gunco = (245,210)
        else:
            gun = pygame.image.load('gun.png')
            gunco = (365,450)
        gun.set_colorkey((255,255,255,255))
        gun = pygame.transform.scale(gun,(gun.get_width()*2,gun.get_height()*2))
        gun.set_colorkey((255,255,255,255))
        screen.blit(gun,gunco)
        if chance < 2 and zombox.contains(mousebox):
            pygame.draw.ellipse(screen,(255,0,0),[420,370,10,10],1)
        else:
            pygame.draw.ellipse(screen,(255,255,255),[420,370,10,10],1)

        pygame.display.flip()

    while on == 1:
        for event in pygame.event.get():
            if event.type == pygame.KEYUP:
                screen.fill((0,0,0))
                pygame.display.flip()
                Eden.time.sleep(1)
                Eden.size = [850, 750]
                Eden.screen = Eden.pygame.display.set_mode(Eden.size,pygame.FULLSCREEN)
                on = 0
                Eden.W = 0
                Eden.player_direction = 1
                #elif event.key == pygame.K_SPACE:
                    #go()
        font = pygame.font.SysFont('Calibri',100,True,False)
        Text = font.render("Score:"+str(score),True,(255,255,255))
        screen.blit(Text,[0,400])
        pygame.display.flip()
