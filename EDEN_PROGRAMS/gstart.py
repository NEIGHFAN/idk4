def configimages():
    os.chdir('../EDEN_PICS')
    Eden.titleBG = pygame.image.load('grass.png')
    Eden.customiseBG = pygame.image.load('custom background.png')
    Eden.icon = pygame.image.load('icon.png')
    Eden.sidewallR = pygame.image.load('side wall.png')
    Eden.sidewallL = pygame.transform.flip(Eden.sidewallR, True, False)
    Eden.topcornerR = pygame.image.load('top corner.png')
    Eden.topcornerL = pygame.transform.flip(Eden.topcornerR, True, False)
    Eden.topwall = pygame.image.load('top wall.png')
    Eden.bottomwall = pygame.image.load('bottom wall.png')
    Eden.bottomcornerR = pygame.image.load('bottom corner.png')
    Eden.bottomcornerL = pygame.transform.flip(Eden.bottomcornerR, True, False)
    Eden.ground = pygame.image.load('grass.png')
    Eden.building = pygame.image.load('building.png')
    Eden.lake = pygame.image.load('lake.png')
    Eden.well = pygame.image.load('well.png')
    Eden.flower = pygame.image.load('flower.png')
    Eden.stack = pygame.image.load('stack.png')
    Eden.tree = pygame.image.load('tree.png')
    Eden.pen = pygame.image.load('pen.png')
    Eden.digsite = pygame.image.load('digsite.png')
    Eden.pine = pygame.image.load('pine.png')
    Eden.rock = pygame.image.load('rock.png')
    Eden.ruin = pygame.image.load('ruin.png')
    MAP = pygame.image.load('map.png')
    Eden.Map.MAP = pygame.transform.scale(MAP,(750,750))
    Eden.pstart.MAP = pygame.image.load('abstract map.png')
    Eden.pstart.iMAP = pygame.image.load('interaction map.png')
    Eden.SHOP = pygame.image.load('shop.png')
    os.chdir('../HOTBAR_ICONS')
    rod1 = pygame.image.load('rod1.png')
    bucket1 = pygame.image.load('bucket1.png')
    net1 = pygame.image.load('net1.png')
    pitch1 = pygame.image.load('pitch1.png')
    ladder1 = pygame.image.load('ladder1.png')
    shears1 = pygame.image.load('shears1.png')
    spade1 = pygame.image.load('spade1.png')
    axe1= pygame.image.load('axe1.png')
    pick1= pygame.image.load('pick1.png')
    hammer1= pygame.image.load('hammer1.png')
    rod0 = pygame.image.load('rod0.png')
    bucket0 = pygame.image.load('bucket0.png')
    net0 = pygame.image.load('net0.png')
    pitch0 = pygame.image.load('pitch0.png')
    ladder0 = pygame.image.load('ladder0.png')
    shears0 = pygame.image.load('shears0.png')
    spade0 = pygame.image.load('spade0.png')
    axe0= pygame.image.load('axe0.png')
    pick0= pygame.image.load('pick0.png')
    hammer0= pygame.image.load('hammer0.png')
    fish1 = pygame.image.load('fish1.png')
    water1 = pygame.image.load('water1.png')
    rabbit1 = pygame.image.load('rabbit1.png')
    hay1 = pygame.image.load('hay1.png')
    apple1 = pygame.image.load('apple1.png')
    wool1 = pygame.image.load('wool1.png')
    bone1 = pygame.image.load('bone1.png')
    log1 = pygame.image.load('log1.png')
    geode1 = pygame.image.load('geode1.png')
    gem1 = pygame.image.load('gem1.png')
    fish0 = pygame.image.load('fish0.png')
    water0 = pygame.image.load('water0.png')
    rabbit0 = pygame.image.load('rabbit0.png')
    hay0 = pygame.image.load('hay0.png')
    apple0 = pygame.image.load('apple0.png')
    wool0 = pygame.image.load('wool0.png')
    bone0 = pygame.image.load('bone0.png')
    log0 = pygame.image.load('log0.png')
    geode0 = pygame.image.load('geode0.png')
    gem0 = pygame.image.load('gem0.png')
    key1 = pygame.image.load('key1.png')
    key2 = pygame.image.load('key2.png')
    key3 = pygame.image.load('key3.png')
    key4 = pygame.image.load('key4.png')
    key5 = pygame.image.load('key5.png')
    key6 = pygame.image.load('key6.png')
    key7 = pygame.image.load('key7.png')
    key8 = pygame.image.load('key8.png')
    key9 = pygame.image.load('key9.png')
    key10 = pygame.image.load('key10.png')
    key0 = pygame.image.load('key0.png')
    Eden.tool1 = [rod1,bucket1,net1,pitch1,ladder1,shears1,spade1,axe1,pick1,hammer1]
    Eden.tool0 = [rod0,bucket0,net0,pitch0,ladder0,shears0,spade0,axe0,pick0,hammer0]
    Eden.item1 = [fish1,water1,rabbit1,hay1,apple1,wool1,bone1,log1,geode1,gem1]
    Eden.item0 = [fish0,water0,rabbit0,hay0,apple0,wool0,bone0,log0,geode0,gem0]
    Eden.key = [key1,key2,key3,key4,key5,key6,key7,key8,key9,key10,key0]
    
    

def configaudio():
    os.chdir('../EDEN_SOUNDS')
    Eden.drawplayer.foot1 = pygame.mixer.Sound('foot1.wav')
    Eden.drawplayer.foot2 = pygame.mixer.Sound('foot2.wav')
    Eden.drawplayer.foot3 = pygame.mixer.Sound('foot3.wav')
    Eden.drawplayer.foot4 = pygame.mixer.Sound('foot4.wav')
    Eden.drawplayer.foot5 = pygame.mixer.Sound('foot5.wav')
    


    
def go():
    global os,pygame,Eden
    import os
    #os.chdir('...')
    import Eden, pygame
    os.chdir('./SAVE_FILES')
    Eden.On = True
    Eden.pygame.init()
    Eden.size = [850, 750]
    Eden.screen = Eden.pygame.display.set_mode(Eden.size,Eden.pygame.FULLSCREEN)
    Eden.black = (0,0,0)
    Eden.white = (255,255,255)
    Eden.beige = (255,255,127)
    Eden.brown = (127,63,0)
    Eden.green = (0,255,0)
    Eden.red = (255,0,0)
    Eden.dred = (127,0,0)
    Eden.brickish = (170,63,63)
    Eden.windowish = (250,250,255)
    Eden.yellow = (255,255,0)
    Eden.orange = (255,127,0)
    Eden.cyan = (0,255,255)
    Eden.purple = (127,0,127)
    Eden.blue = (0,0,255)
    Eden.magenta = (255,0,255)
    Eden.grey = (127,127,127)
    Eden.lgrey = (170,170,170)
    Eden.flesh = (255,170,170)
    Eden.pink = (255,63,127)
    Eden.grass = (0,255,63)
    Eden.ggrass = (0,170,63)

    Eden.redc = [0,0,0,0,0,0,0,0,0,0]
    Eden.greenc = [0,0,0,0,0,0,0,0,0,0]
    Eden.bluec = [0,0,0,0,0,0,0,0,0,0]
    Eden.file = 0
    os.chdir('../SAVE_FILES')
    credA = open("customredsA.txt","a+")
    cgreenA = open("customgreensA.txt","a+")
    cblueA = open("custombluesA.txt","a+")
    if os.path.getsize('./customredsA.txt') == 0 :
        credA.write("0"+'\n'+"0"+'\n'+"0"+'\n'+"0"+'\n'+"0"+'\n'+"0"+'\n'+"0"+'\n'+"0"+'\n'+"0"+'\n'+"0"+'\n')
    if os.path.getsize('./customgreensA.txt') == 0 :
        cgreenA.write("0"+'\n'+"0"+'\n'+"0"+'\n'+"0"+'\n'+"0"+'\n'+"0"+'\n'+"0"+'\n'+"0"+'\n'+"0"+'\n'+"0"+'\n')
    if os.path.getsize('./custombluesA.txt') == 0 :
        cblueA.write("0"+'\n'+"0"+'\n'+"0"+'\n'+"0"+'\n'+"0"+'\n'+"0"+'\n'+"0"+'\n'+"0"+'\n'+"0"+'\n'+"0"+'\n')
    credA.close()
    cgreenA.close()
    cblueA.close()
    credA = open("customredsA.txt","r+")
    cgreenA = open("customgreensA.txt","r+")
    cblueA = open("custombluesA.txt","r+")
    Eden.credA = [line.rstrip('\n') for line in credA.readlines()]
    Eden.cgreenA = [line.rstrip('\n') for line in cgreenA.readlines()]
    Eden.cblueA = [line.rstrip('\n') for line in cblueA.readlines()]
    for i in range(10):
        Eden.credA[i] = int(Eden.credA[i])
        Eden.cgreenA[i] = int(Eden.cgreenA[i])
        Eden.cblueA[i] = int(Eden.cblueA[i])
    credA.close()
    cgreenA.close()
    cblueA.close()

    credB = open("customredsB.txt","a+")
    cgreenB = open("customgreensB.txt","a+")
    cblueB = open("custombluesB.txt","a+")
    if os.path.getsize('./customredsB.txt') == 0 :
        credB.write("0"+'\n'+"0"+'\n'+"0"+'\n'+"0"+'\n'+"0"+'\n'+"0"+'\n'+"0"+'\n'+"0"+'\n'+"0"+'\n'+"0"+'\n')
    if os.path.getsize('./customgreensB.txt') == 0 :
        cgreenB.write("0"+'\n'+"0"+'\n'+"0"+'\n'+"0"+'\n'+"0"+'\n'+"0"+'\n'+"0"+'\n'+"0"+'\n'+"0"+'\n'+"0"+'\n')
    if os.path.getsize('./custombluesB.txt') == 0 :
        cblueB.write("0"+'\n'+"0"+'\n'+"0"+'\n'+"0"+'\n'+"0"+'\n'+"0"+'\n'+"0"+'\n'+"0"+'\n'+"0"+'\n'+"0"+'\n')
    credB.close()
    cgreenB.close()
    cblueB.close()
    credB = open("customredsB.txt","r+")
    cgreenB = open("customgreensB.txt","r+")
    cblueB = open("custombluesB.txt","r+")
    Eden.credB = [line.rstrip('\n') for line in credB.readlines()]
    Eden.cgreenB = [line.rstrip('\n') for line in cgreenB.readlines()]
    Eden.cblueB = [line.rstrip('\n') for line in cblueB.readlines()]
    for i in range(10):
        Eden.credB[i] = int(Eden.credB[i])
        Eden.cgreenB[i] = int(Eden.cgreenB[i])
        Eden.cblueB[i] = int(Eden.cblueB[i])
    credB.close()
    cgreenB.close()
    cblueB.close()

    credC = open("customredsC.txt","a+")
    cgreenC = open("customgreensC.txt","a+")
    cblueC = open("custombluesC.txt","a+")
    if os.path.getsize('./customredsC.txt') == 0 :
        credC.write("0"+'\n'+"0"+'\n'+"0"+'\n'+"0"+'\n'+"0"+'\n'+"0"+'\n'+"0"+'\n'+"0"+'\n'+"0"+'\n'+"0"+'\n')
    if os.path.getsize('./customgreensC.txt') == 0 :
        cgreenC.write("0"+'\n'+"0"+'\n'+"0"+'\n'+"0"+'\n'+"0"+'\n'+"0"+'\n'+"0"+'\n'+"0"+'\n'+"0"+'\n'+"0"+'\n')
    if os.path.getsize('./custombluesC.txt') == 0 :
        cblueC.write("0"+'\n'+"0"+'\n'+"0"+'\n'+"0"+'\n'+"0"+'\n'+"0"+'\n'+"0"+'\n'+"0"+'\n'+"0"+'\n'+"0"+'\n')
    credC.close()
    cgreenC.close()
    cblueC.close()
    credC = open("customredsC.txt","r+")
    cgreenC = open("customgreensC.txt","r+")
    cblueC = open("custombluesC.txt","r+")
    Eden.credC = [line.rstrip('\n') for line in credC.readlines()]
    Eden.cgreenC = [line.rstrip('\n') for line in cgreenC.readlines()]
    Eden.cblueC = [line.rstrip('\n') for line in cblueC.readlines()]
    for i in range(10):
        Eden.credC[i] = int(Eden.credC[i])
        Eden.cgreenC[i] = int(Eden.cgreenC[i])
        Eden.cblueC[i] = int(Eden.cblueC[i])
    credC.close()
    cgreenC.close()
    cblueC.close()

    cclothesA = open("customclothesA.txt","a+")
    if os.path.getsize('./customclothesA.txt') == 0 :
        cclothesA.write("0"+'\n'+"0"+'\n'+"0"+'\n')
    cclothesA.close()
    cclothesA = open("customclothesA.txt","r+")
    CclothesA = [line.rstrip('\n') for line in cclothesA.readlines()]
    Eden.cHatA = int(CclothesA[0])
    Eden.cDressA = int(CclothesA[1])
    Eden.cFhairA = int(CclothesA[2])
    cclothesA.close()
    
    cclothesB = open("customclothesB.txt","a+")
    if os.path.getsize('./customclothesB.txt') == 0 :
        cclothesB.write("0"+'\n'+"0"+'\n'+"0"+'\n')
    cclothesB.close()
    cclothesB = open("customclothesB.txt","r+")
    CclothesB = [line.rstrip('\n') for line in cclothesB.readlines()]
    Eden.cHatB = int(CclothesB[0])
    Eden.cDressB = int(CclothesB[1])
    Eden.cFhairB = int(CclothesB[2])
    cclothesB.close()

    cclothesC = open("customclothesC.txt","a+")
    if os.path.getsize('./customclothesC.txt') == 0 :
        cclothesC.write("0"+'\n'+"0"+'\n'+"0"+'\n')
    cclothesC.close()
    cclothesC = open("customclothesC.txt","r+")
    CclothesC = [line.rstrip('\n') for line in cclothesC.readlines()]
    Eden.cHatC = int(CclothesC[0])
    Eden.cDressC = int(CclothesC[1])
    Eden.cFhairC = int(CclothesC[2])
    cclothesC.close()

    nameA =  open("A.txt","a+")
    if os.path.getsize('./A.txt') == 0 :
        nameA.write('A')
    nameA.close()
    nameA =  open("A.txt","r+")
    Eden.nameA = nameA.read(3)
    nameB =  open("B.txt","a+")
    if os.path.getsize('./B.txt') == 0 :
        nameB.write('B')
    nameB.close()
    nameB =  open("B.txt","r+")
    Eden.nameB = nameB.read(3)
    nameC =  open("C.txt","a+")
    if os.path.getsize('./C.txt') == 0 :
        nameC.write('C')
    nameC.close()
    nameC =  open("C.txt","r+")
    Eden.nameC = nameC.read(3)
    os.chdir('../SETTINGS')
    settings = open('settings.txt','a+')
    if os.path.getsize('./settings.txt') == 0:
        settings.write('1'+'\n'+'1'+'\n'+'5'+'\n')
    settings.close()
    settings = open('settings.txt','r+')
    settings = [line.rstrip('\n') for line in settings.readlines()]
    Eden.lang = int(settings[0])
    Eden.mvol = int(settings[1])/10
    Eden.svol = int(settings[2])/10

    if Eden.lang == 1:
        LANG =  open("English.txt","r+")
    if Eden.lang == 2:
        LANG =  open("Spanish.txt","r+")
    Eden.TEXT = [line.rstrip('\n') for line in LANG.readlines()]




    Eden.channel1 = pygame.mixer.Channel(0)
    Eden.channel2 = pygame.mixer.Channel(1)
    os.chdir('../EDEN_SOUNDS')
    Eden.bgmusic = pygame.mixer.Sound('background.wav')
    
    Eden.channel1.set_volume(Eden.mvol)
    Eden.channel2.set_volume(Eden.svol)
    Eden.channel1.play(Eden.bgmusic,-1)
    Eden.CX,Eden.CY = 425,375
    Eden.MOUSE = 1
    configimages()
    configaudio()
    os.chdir('..')
    
