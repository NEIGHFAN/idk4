def filesetup():#RED,GREEN,BLUE,CLOTHES,COORDS,Tools,Items,Keys):
    if Eden.file == 1:
        des = 'A'
    elif Eden.file == 2:
        des = 'B'
    elif Eden.file == 3:
        des = 'C'
    cred = open('customreds'+des+'.txt','r+')
    cgreen = open('customgreens'+des+'.txt','r+')
    cblue = open('customblues'+des+'.txt','r+')
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
    cclothes = open('customclothes'+des+'.txt','r+')
    Cclothes = [line.rstrip('\n') for line in cclothes.readlines()]
    Eden.cHat = int(Cclothes[0])
    Eden.cDress = int(Cclothes[1])
    Eden.cFhair = int(Cclothes[2])
    cclothes.close()
    coor = open('coordinates'+des+'.txt','a+')
    if os.path.getsize('coordinates'+des+'.txt') == 0 :
        coor.write('0'+'\n'+'0'+'\n'+'0'+'\n')
    coor.close()
    coor = open('coordinates'+des+'.txt','r+')
    Coor = [line.rstrip('\n') for line in coor.readlines()]
    coor.close()
    Eden.x = int(Coor[0])
    Eden.y = int(Coor[1])
    Eden.gx = int(((Eden.x-1500)/-15))-1
    Eden.gy = int(((Eden.y-1500)/-15))-1
    Eden.player_direction = int(Coor[2])
    tools = open('tools'+des+'.txt','a+')
    if os.path.getsize('tools'+des+'.txt') == 0 :
        for i in range(10):
            tools.write('0\n')
    tools.close()
    tools = open('tools'+des+'.txt','r+')
    Eden.TOOLS = [line.rstrip('\n') for line in tools.readlines()]
    tools.close()
    for i in range(10):
        Eden.TOOLS[i] = int(Eden.TOOLS[i])
    items = open('items'+des+'.txt','a+')
    if os.path.getsize('items'+des+'.txt') == 0 :
        for i in range(11):
            items.write('0\n')
    items.close()
    items = open('items'+des+'.txt','r+')
    Eden.ITEMS = [line.rstrip('\n') for line in items.readlines()]
    items.close()
    for i in range(11):
        Eden.ITEMS[i] = int(Eden.ITEMS[i])
    Eden.money = int(Eden.ITEMS[10])
    keys = open('keys'+des+'.txt','a+')
    if os.path.getsize('keys'+des+'.txt') == 0 :
        for i in range(10):
            keys.write('0\n')
    keys.close()
    keys = open('keys'+des+'.txt','r+')
    Eden.KEYS = [line.rstrip('\n') for line in keys.readlines()]
    keys.close()
    for i in range(10):
        Eden.KEYS[i] = int(Eden.KEYS[i])

        
def go():
    global os,Eden
    import os
    os.chdir('...')
    import Eden
    Eden.doing = 0
    Eden.W,Eden.S,Eden.D,Eden.A = 0,0,0,0
    Eden.legup,Eden.legdown, Eden.legleft, Eden.legright = 0,0,0,0
    Eden.leg = 1
    Eden.PF = 0
    Eden.px, Eden.py = 375,375
    os.chdir('./SAVE_FILES')
    filesetup()
##    if Eden.file == 1:
##        filesetup('customredsA.txt','customgreensA.txt','custombluesA.txt','customclothesA.txt',
##                      'coordinatesA.txt','toolsA.txt','itemsA.txt','keysA.txt')
##    elif Eden.file == 2:
##        filesetup('customredsB.txt','customgreensB.txt','custombluesB.txt','customclothesB.txt',
##                      'coordinatesB.txt','toolsB.txt','itemsB.txt','keysB.txt')
##    elif Eden.file == 3:
##        filesetup('customredsC.txt','customgreensC.txt','custombluesC.txt','customclothesC.txt',
##                      'coordinatesC.txt','toolsC.txt','itemsC.txt','keysC.txt')
    #(RED,GREEN,BLUE,CLOTHES,COORDS,TOOLS,ITEMS)
    Eden.cface = (Eden.cred[0],Eden.cgreen[0],Eden.cblue[0])
    Eden.chat = (Eden.cred[1],Eden.cgreen[1],Eden.cblue[1])
    Eden.chatsymbol = (Eden.cred[2],Eden.cgreen[2],Eden.cblue[2])
    Eden.chair = (Eden.cred[3],Eden.cgreen[3],Eden.cblue[3])
    Eden.cbody = (Eden.cred[4],Eden.cgreen[4],Eden.cblue[4])
    Eden.carms = (Eden.cred[5],Eden.cgreen[5],Eden.cblue[5])
    Eden.clegs = (Eden.cred[6],Eden.cgreen[6],Eden.cblue[6])
    Eden.cshoes = (Eden.cred[7],Eden.cgreen[7],Eden.cblue[7])
    Eden.cgloves = (Eden.cred[8],Eden.cgreen[8],Eden.cblue[8])
    Eden.cshoulders = (Eden.cred[9],Eden.cgreen[9],Eden.cblue[9])
    Eden.KEYS.append(int(1))
    Eden.buildingsW = []
    Eden.buildingsA = []
    Eden.buildingsS = []
    Eden.buildingsD = []
    Eden.lakes = []
    Eden.wells = []
    Eden.flowers = [] 
    Eden.stacks = []
    Eden.trees = []
    Eden.pens = []
    Eden.digsites = []
    Eden.pines = []
    Eden.rocks = []
    Eden.ruins = []
    #buildings = []
    grid = []
    igrid = []
    for i in range(201):
        grid.append([])
        igrid.append([])
        for j in range(201):
            if MAP.get_at((j,i)) == (255,255,255):
                grid[i].append(0)
            elif MAP.get_at((j,i)) == (0,0,0):
                grid[i].append(1)
            elif MAP.get_at((j,i)) == (0,0,255):
                Eden.lakes.append((j,i))
                grid[i].append(0)
            elif MAP.get_at((j,i)) == (0,255,255):
                Eden.wells.append((j,i))
                grid[i].append(0)
            elif MAP.get_at((j,i)) == (255,0,0):
                Eden.flowers.append((j,i))
                grid[i].append(0)
            elif MAP.get_at((j,i)) == (255,255,0):
                Eden.stacks.append((j,i))
                grid[i].append(0)
            elif MAP.get_at((j,i)) == (0,255,0):
                Eden.trees.append((j,i))
                grid[i].append(0)
            elif MAP.get_at((j,i)) == (127,63,0):
                Eden.pens.append((j,i))
                grid[i].append(1)
            elif MAP.get_at((j,i)) == (255,127,0):
                Eden.digsites.append((j,i))
                grid[i].append(0)
            elif MAP.get_at((j,i)) == (0,127,0):
                Eden.pines.append((j,i))
                grid[i].append(0)
            elif MAP.get_at((j,i)) == (255,0,255):
                Eden.rocks.append((j,i))
                grid[i].append(1)
            elif MAP.get_at((j,i)) == (127,127,127):
                Eden.ruins.append((j,i))
                grid[i].append(0)
            elif MAP.get_at((j,i)) == (127,0,0):
                #buildings.append((j,i))
                grid[i].append(0)
                
            if iMAP.get_at((j,i)) == (255,255,255) or iMAP.get_at((j,i)) == (0,0,0):
                igrid[i].append(0)
            elif iMAP.get_at((j,i)) == (0,0,255):
                igrid[i].append(1)
            elif iMAP.get_at((j,i)) == (0,255,255):
                igrid[i].append(2)
            elif iMAP.get_at((j,i)) == (255,0,0):
                igrid[i].append(3)
            elif iMAP.get_at((j,i)) == (255,255,0):
                igrid[i].append(4)
            elif iMAP.get_at((j,i)) == (0,255,0):
                igrid[i].append(5)
            elif iMAP.get_at((j,i)) == (127,63,0):
                igrid[i].append(6)
            elif iMAP.get_at((j,i)) == (255,127,0):
                igrid[i].append(7)
            elif iMAP.get_at((j,i)) == (0,127,0):
                igrid[i].append(8)
            elif iMAP.get_at((j,i)) == (255,0,255):
                igrid[i].append(9)
            elif iMAP.get_at((j,i)) == (127,127,127):
                igrid[i].append(10)


    Eden.grid = grid
    Eden.igrid = igrid
    buildings = [(84,90),(127,88),(72,85),(123,75),(60,76),(116,63),(67,64),(104,57),(79,60),(91,59),
                 (107,88)]



    
##    Eden.lakes = [(27,16),(174,55),(27,149),(123,181),(123,125)]
##    Eden.wells = [(8,26),(128,9),(8,89),(97,81),(174,84),(66,128),(157,134),(8,192),(92,173),(191,191)]
##    Eden.flowers = [(15,40),(18,39),(20,41),(110,109),(108,111),(112,111),(110,113),(137,168),(139,165),(142,168)]
##    Eden.stacks = [(75,25),(81,26),(76,29),(80,31),(127,58),(131,56),(131,60),(25,115),(28,109),(33,112)]
##    Eden.sheeps = [(113,29),(117,26),(120,30),(145,103),(152,105),(146,108),(151,113),(95,149),(102,147),(97,153)]
##    Eden.digsites = 
##    Eden.trees = [(45,45),(49,47),(176,37),(180,39),(173,147),(178,149),(183,147),(64,168),(69,170),(74,168)]
##    Eden.pines = [(14,62),(18,66),(24,63),(29,67),(141,23),(143,32),(149,28),(135,148),(141,144),(147,151)]



    
    Eden.buildingsn = ["G1","G2","G3","G4","G5","G6","G7","G8","G9","G10","SHOP"]
    Eden.buildingsc = [(127,63,0),(127,0,127),(255,0,255),(0,255,255),(0,0,255),
                       (0,127,0),(0,255,0),(255,255,0),(255,127,0),(255,0,0),(255,255,255)]
    for i in range(11):
        Eden.buildingsW.append((buildings[i][1]*-15)+1125)
        Eden.buildingsA.append((buildings[i][0]*-15)+1125)
        Eden.buildingsS.append(((buildings[i][1]-10)*-15)+1125)
        Eden.buildingsD.append(((buildings[i][0]-10)*-15)+1125)
    Eden.controller = 0


    

    
    

            
            
    
    

    
