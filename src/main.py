from panda3d.core import loadPrcFileData
loadPrcFileData("", "win-size 800 600")
loadPrcFileData("", "audio-library-name p3openal_audio")
loadPrcFileData('', 'textures-power-2 up')

loadPrcFileData("", "window-title Sleigh Ride!")
from direct.showbase.ShowBase import ShowBase
from direct.gui.OnscreenText import OnscreenText
from direct.gui.DirectGui import *
from panda3d.core import ostream
from panda3d.core import *
from direct.task import Task
from direct.particles.Particles import *
from direct.particles.ParticleEffect import ParticleEffect
from direct.particles.ForceGroup import ForceGroup
class MyApp(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        self.initiatemenu()
    def initiatemenu(self):
        render.getChildren().detach()
        render.clearLight()
        aspect2d.getChildren().detach()
        base.setBackgroundColor(0, 0, 0)
        self.mainFrame = DirectFrame(frameColor=(0, 0, 0, 1), frameSize=(-2, 2, -2, 2), pos=(0, 0, 0))
        self.background = OnscreenImage(image = "images/bg.jpg", pos = (0, 0, 0), scale = (1.5, 1, 1))
        self.background.setTransparency(TransparencyAttrib.MAlpha)
        self.background.reparentTo(self.mainFrame)
        self.title = OnscreenText(text="Sleigh Ride!",pos=(0,0.8), scale=0.2,fg=(1, 1, 1, 1))
        self.startButton = DirectButton(image = "images/play.png", scale=(0.5,0.5,0.15), relief = None, command=self.initiate, pos=(0, 0, -0.8))
        self.startButton.setTransparency(TransparencyAttrib.MAlpha)
        self.creditsButton = DirectButton(image = "images/credits.png", scale=(0.3,0.3,0.08),relief = None,  command=self.initiatecredits, pos=(-1, 0, 0.85))
        self.creditsButton.setTransparency(TransparencyAttrib.MAlpha)
        self.gameInstructions1 = DirectLabel(text="It's Christmas Eve and presents ", text_scale=(0.1, 0.1), relief=None, text_fg=(255, 255, 255, 100), pos=(0, 0, 0.5))
        self.gameInstructions1.reparentTo(aspect2d)
        self.gameInstructions2 = DirectLabel(text="have to be delivered to every house!", text_scale=(0.1, 0.1), relief=None, text_fg=(255, 255, 255, 100), pos=(0, 0, 0.3))
        self.gameInstructions2.reparentTo(aspect2d)
        self.gameInstructions3 = DirectLabel(text="Avoid obstacles and deliver the presents to the houses!", text_scale=(0.1, 0.1), relief=None, text_fg=(255, 255, 255, 100), pos=(0, 0, 0.1))
        self.gameInstructions3.reparentTo(aspect2d)
        self.gameInstructions4 = DirectLabel(text="Do not skip any houses!", text_scale=(0.1, 0.1), relief=None, text_fg=(255, 255, 255, 100), pos=(0, 0, -0.1))
        self.gameInstructions4.reparentTo(aspect2d)
        self.gameInstructions5 = DirectLabel(text="Use the spacebar or button to drop presents!", text_scale=(0.1, 0.1), relief=None, text_fg=(255, 255, 255, 100), pos=(0, 0, -0.3))
        self.gameInstructions5.reparentTo(aspect2d)
        self.gameInstructions6 = DirectLabel(text="Use arrow keys or buttons to move!", text_scale=(0.1, 0.1), relief=None, text_fg=(255, 255, 255, 100), pos=(0, 0, -0.5))
        self.gameInstructions6.reparentTo(aspect2d)
        self.mySound = loader.loadSfx("music/happy-loop.ogg")
        self.mySound.setLoop(True)
        self.mySound.setLoopCount(0)
        self.mySound.play()
    def initiatecredits(self):
        self.mySound.stop()
        render.getChildren().detach()
        render.clearLight()
        aspect2d.getChildren().detach()
        self.mainFrame = DirectFrame(frameColor=(0, 0, 0, 1), frameSize=(-2, 2, -2, 2), pos=(0, 0, 0))
        self.creditsButton = DirectButton(image = "images/menu.png", scale=(0.3,0.3,0.08),relief = None,  command=self.initiatemenu, pos=(-1, 0, 0.9))
        self.background = OnscreenImage(image = "images/credits.jpg", pos = (0, 0, 0), scale = (2, 1, 1))
        self.background.setTransparency(TransparencyAttrib.MAlpha)
        self.background.reparentTo(self.mainFrame)
    def initiate(self):
        self.mySound.stop()
        render.getChildren().detach()
        render.clearLight()
        aspect2d.getChildren().detach()
        self.movingleft = 0
        self.movingright = 0
        self.droppingpresent = 0
        self.speedvar = 5
        self.prevspeed = 5
        self.shipspeed = 650
        self.moveSpeed = 250
        self.presentdropped = 1
        self.presentchecker = 0
        self.seq = 0
        self.candroppresent = 1
        self.dropp = 0
        self.score = 0
        self.goreason = ""
        base.enableParticles()
        self.p = ParticleEffect()
        self.p.loadConfig("snow.ptf")
        self.p.start(parent = render, renderParent = render)      
        alight = AmbientLight("alight")
        alight.setColor((0.2, 0.2, 0.4, 1))
        alnp = render.attachNewNode(alight)
        render.setLight(alnp)
        self.ss = OnscreenText(text="0",pos=(0,0.8), scale=0.15,fg=(1, 1, 1, 1))
        onebutton = DirectButton(image = "images/flatDark23.png",relief = None, text = (""), scale=.2, command=self.setleft)
        onebutton.setPos(-1,0,-0.7)
        onebutton.setTransparency(TransparencyAttrib.MAlpha)
        onebutton1 = DirectButton(image = "images/flatDark24.png",relief = None, text = (""), scale=.2, command=self.setright)
        onebutton1.setPos(1,0,-0.7)
        onebutton1.setTransparency(TransparencyAttrib.MAlpha)
        onebutton2 = DirectButton(image = "images/flatDark10.png",relief = None, text = (""), scale=.2, command=self.droppresent)
        onebutton2.setPos(0,0,-0.7)
        onebutton2.setTransparency(TransparencyAttrib.MAlpha)
        self.moveKeyList = [
            "arrow_left", "arrow_right", "arrow_up", "arrow_down","space","w","s","a","d","q","e"]
        self.moveKeys = {}
        for key in self.moveKeyList:
            self.moveKeys[key] = False
            self.accept(key, self.moveKeyStateChanged, extraArgs = [key, True])
            self.accept(key + "-up", self.moveKeyStateChanged, extraArgs = [key, False])
        base.cTrav = CollisionTraverser()
        #base.cTrav.showCollisions(render)
        base.cTrav.setRespectPrevTransform(True)
        self.ship = loader.loadModel("models/sled")
        self.ship.setScale(0.1)
        self.ship.setZ(4)
        self.ship.setX(18)
        self.ship.setY(-18)
        self.ship.reparentTo(render)
        slight = Spotlight("slight")
        slight.setColor((2, 0, 0, 1))
        lens = PerspectiveLens()
        slight.setLens(lens)
        slnp = render.attachNewNode(slight)
        slnp.setHpr(-0,-30,0)
        render.setLight(slnp)
        slnp.reparentTo(self.ship)
        slight = Spotlight("slight")
        slight.setColor((0, 1, 0.2, 1))
        lens = PerspectiveLens()
        slight.setLens(lens)
        slnp = render.attachNewNode(slight)
        slnp.setHpr(0,0,0)
        render.setLight(slnp)
        slnp.reparentTo(self.ship)        
        base.cam.reparentTo(self.ship)
        base.cam.setPos(0,-300,130)
        base.cam.setHpr(0,-20,0)
        render.setTwoSided(True)
        cs = CollisionSphere(0, 0, 0, 10)
        cnode = CollisionNode("cnode")
        cnode.addSolid(cs)
        self.cnp = render.attachNewNode(cnode)
        self.cnp.reparentTo(self.ship)
        pusher = CollisionHandlerPusher()
        pusher.addCollider(self.cnp, self.ship)
        self.cTrav.addCollider(self.cnp, pusher)
        self.offset = 960
        self.sccener = 1
        self.present = loader.loadModel("models/present")   
        self.scene = base.loader.loadModel("models/lvl1")
        self.scene.reparentTo(base.render)
        self.scene.setScale(3)
        self.scene.setHpr(90,0,0)
        self.scene.setPos(0,0,0)
        self.scene1 = base.loader.loadModel("models/lvl2")
        self.scene1.reparentTo(base.render)
        self.scene1.setScale(3)
        self.scene1.setHpr(90,0,0)
        self.scene1.setPos(0,120,0)
        self.scene2 = base.loader.loadModel("models/lvl3")
        self.scene2.reparentTo(base.render)
        self.scene2.setScale(3)
        self.scene2.setPos(0,240,0)
        self.scene2.setHpr(90,0,0)
        self.scene3 = base.loader.loadModel("models/lvl4")
        self.scene3.reparentTo(base.render)
        self.scene3.setScale(3)
        self.scene3.setHpr(90,0,0)
        self.scene3.setPos(0,360,0)
        self.scene4 = base.loader.loadModel("models/lvl5")
        self.scene4.reparentTo(base.render)
        self.scene4.setHpr(90,0,0)
        self.scene4.setScale(3)
        self.scene4.setPos(0,480,0)
        self.scene5 = base.loader.loadModel("models/lvl6")
        self.scene5.reparentTo(base.render)
        self.scene5.setHpr(90,0,0)
        self.scene5.setScale(3)
        self.scene5.setPos(0,600,0)
        self.scene6 = base.loader.loadModel("models/lvl7")
        self.scene6.reparentTo(base.render)
        self.scene6.setHpr(90,0,0)
        self.scene6.setScale(3)
        self.scene6.setPos(0,720,0)
        self.scene7 = base.loader.loadModel("models/lvl8")
        self.scene7.reparentTo(base.render)
        self.scene7.setHpr(90,0,0)
        self.scene7.setScale(3)
        self.scene7.setPos(0,840,0)
        self.scene8 = base.loader.loadModel("models/lvl9")
        self.scene8.reparentTo(base.render)
        self.scene8.setHpr(90,0,0)
        self.scene8.setScale(3)
        self.scene8.setPos(0,960,0)
        self.mySound = loader.loadSfx("music/winter-wind.ogg")
        self.mySound.setLoop(True)
        self.mySound.setLoopCount(0)
        self.mySound.play()
        self.moveTask = taskMgr.add(self.moveAvatar, "moveAvatar")
    def setleft(self):
        self.movingleft = 1
        self.movingright = 0   
    def setright(self):
        self.movingleft = 0
        self.movingright = 1
    def moveKeyStateChanged(self, key, newState):
        self.moveKeys[key] = newState
    def backtomenu(self):
        self.mySound.stop()
        self.initiatemenu()
    def gameover(self):
        self.movingleft = 0
        self.movingright = 0
        taskMgr.remove("moveAvatar")
        aspect2d.getChildren().detach()
        OnscreenText(text="Game Over",pos=(0,0), scale=0.3,fg=(1, 1, 1, 1))
        OnscreenText(text=self.goreason,pos=(0,-0.1), scale=0.1,fg=(1, 1, 1, 1))
        DirectButton(image = "images/playagain.png", scale=(0.5,0.5,0.15), relief = None, command=self.initiate, pos=(0, 0, -0.8))
        aspect2d.setTransparency(TransparencyAttrib.MAlpha)
        DirectButton(image = "images/menu.png", scale=(0.5,0.5,0.15), relief = None, command=self.backtomenu, pos=(0, 0, 0.8))
    def droppresent(self):
        self.dropp = 1
    def setcandroppresent(self, task):
      self.candroppresent = 1
      return Task.done      
    def checkpresentdrop(self, task):
        self.candroppresent = 1
        if (self.presentdropped == 0):
            self.goreason = "You missed a house!"
            self.gameover()
        return Task.done
    def setpresent(self, task):
        self.presentchecker = 1
        return Task.done   
    def spawnpresent(self):
        self.present = loader.loadModel("models/present")
        self.present.setScale(5)
        self.present.setPos(self.ship.getPos())
        self.present.setX(self.present.getX()-3)
        self.present.reparentTo(render)
    def moveAvatar(self, task):
        dt = globalClock.getDt()
        queue = CollisionHandlerQueue()
        self.cTrav.addCollider(self.cnp, queue)
        self.cTrav.setRespectPrevTransform(True)
        self.cTrav.traverse(render)
        pusher = CollisionHandlerPusher()
        pusher.addCollider(self.cnp, self.ship)
        self.cTrav.addCollider(self.cnp, pusher)
        self.shipspeed + 20
        self.present.setZ(self.present.getZ()-9*dt)
        self.ss.setText(str(self.score))
        # code to detect stop
        if (self.ship.getY() - self.speedvar == 0):
            self.gameover()
        curspeedtemp = self.ship.getY() - self.speedvar
        self.curspeed = curspeedtemp * dt
        self.speedvar = self.ship.getY()
        prevsppedtemp = self.ship.getY() - self.speedvar
        self.prevspeed = prevsppedtemp * dt
        shippy = self.shipspeed + 20
        if (self.movingleft == 1):
            self.ship.setFluidX(self.ship, -dt * self.moveSpeed)
            if (self.ship.getX() <= -18):
                self.ship.setX(-18)
                self.movingleft = 0
        if (self.movingright == 1):
            self.ship.setFluidX(self.ship, dt * self.moveSpeed)
            if (self.ship.getX() >= 18):
                self.ship.setX(18)
                self.movingright = 0   
        # present code
        wearecolliding = 0
        for entry in queue.getEntries():
            # could use a LPoint2i here
            init = entry.getSurfacePoint(entry.getIntoNodePath()).getYz()
            #print(init[1])
            if (init[1] > 0.002):
                self.goreason = "You hit an obstacle!"
                self.gameover()
            if (init[1] < 0):
                self.goreason = "You hit an obstacle!"
                self.gameover()
            wearecolliding = 1
        if self.moveKeys["space"]:
           if (self.candroppresent == 1):
               self.candroppresent = 0
               self.spawnpresent()
               self.droppingpresent = 1
               taskMgr.doMethodLater(0.5, self.setcandroppresent, "CanDropTask")
        if (self.dropp == 1):
            self.dropp = 0
            if (self.candroppresent == 1):
                self.candroppresent = 0
                self.spawnpresent()
                self.droppingpresent = 1
                taskMgr.doMethodLater(0.5, self.setcandroppresent, "CanDropTask")
        if (wearecolliding == 0):
            if (self.seq == 0):
                self.seq = 1
                taskMgr.doMethodLater(1, self.setpresent, "presentTask")  
        # code to drop present
        if (self.droppingpresent == 1):
           self.droppingpresent = 0
           if (wearecolliding == 0):
               self.presentdropped = 1
               self.score = (self.score) + 100
               shippy = self.shipspeed + 100
               self.shipspeed = shippy
               shippy1 = self.moveSpeed + 50
               self.moveSpeed = shippy1
        # uncomment to end game on missed present
          # else:
              # self.gameover()
        if (self.presentchecker == 1):
            if (self.presentdropped == 0):
                self.presentchecker = 0
                self.seq = 0
                self.goreason = "You missed a house!"
                self.gameover()
            if (self.presentdropped == 1):
                self.presentchecker = 0
                self.presentdropped = 0
                self.seq = 0
        #self.presentdropped = 0
        if self.ship.getY() > self.offset-600:
            self.sceeeeen = self.sccener + 1
            self.sccener = self.sceeeeen
            if self.sccener == 1:
                self.scene.setY(self.offset + 120)
            if self.sccener == 2:
                self.scene1.setY(self.offset + 120)
            if self.sccener == 3:
                self.scene2.setY(self.offset + 120)
            if self.sccener == 4:
                self.scene3.setY(self.offset + 120)
            if self.sccener == 5:
                self.scene4.setY(self.offset + 120)
            if self.sccener == 6:
                self.scene5.setY(self.offset + 120)
            if self.sccener == 7:
                self.scene6.setY(self.offset + 120)
            if self.sccener == 8:
                self.scene7.setY(self.offset + 120)
            if self.sccener == 8:
                self.scene8.setY(self.offset + 120)
                self.sccener = 1
            self.offe = self.offset + 120
            self.offset = self.offe
        self.ship.setZ(1)
        if self.moveKeys["arrow_left"]:
            self.setleft()
        elif self.moveKeys["arrow_right"]:
            self.setright()
        if self.moveKeys["a"]:
            self.setleft()
        if self.moveKeys["d"]:
            self.setright()
        self.ship.setFluidY(self.ship, dt * self.shipspeed)
        self.p.setY(self.ship.getY()+200)
        return task.cont
app = MyApp()
app.run()