import os
import pygame
import sys
import button

pygame.font.init()
my_font = pygame.font.SysFont('ARLRDBD.TTP', 32)
SCREENWIDTH, SCREENHEIGHT = 1200, 700
FPS = 60
screen = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
pygame.display.set_caption("UTRGV Cyber Sercurity Training")
icon = pygame.image.load(os.path.join('Assets/shapes','icon.png')).convert_alpha()
pygame.display.set_icon(icon)

# Import main screen images from Assets folder
# Imports the background image.
BG_IMG = pygame.image.load(os.path.join('Assets','Background.jpg'))
# Imports the main screen image.
MS_IMG = pygame.image.load(os.path.join('Assets/window & elements/edited windows','MSText.png'))
# Imports the level selection image.
LEVEL_SELECTION_BG_IMG = pygame.image.load(os.path.join('Assets/window & elements/Window','Window (1).png'))

############### BUTTONS
# Load button images
# New Game button
NG_IMG = pygame.image.load(os.path.join('Assets/button','New Game.png')).convert_alpha()
# Continue button 
CONT_IMG = pygame.image.load(os.path.join('Assets/button','Continue.png')).convert_alpha()
# Start Game button
SG_IMG = pygame.image.load(os.path.join('Assets/button','startgame.png')).convert_alpha()
# Next Icon button
NX_IMG = pygame.image.load(os.path.join('Assets/button','RightArrow (1).png')).convert_alpha()
# Selection button image
SelB_IMG = pygame.image.load(os.path.join('Assets/button','selectionbuttonclear.png')).convert_alpha()
# Clear selection button image
buttonfill_IMG = pygame.image.load(os.path.join('Assets/button','buttonfill.png')).convert_alpha()
# Password button image
PB_IMG = pygame.image.load(os.path.join('Assets/button','passwordbutton.png')).convert_alpha()
# Yes button image
YES_IMG = pygame.image.load(os.path.join('Assets/button','Ok (1).png')).convert_alpha()
# No button image
NO_IMG = pygame.image.load(os.path.join('Assets/button','No (1).png')).convert_alpha()
# Button image
BTTN_IMG = pygame.image.load(os.path.join('Assets/button','button.png')).convert_alpha()

# Level Selection button
LEVEL_SELECTION_BUTTON_IMG = pygame.image.load(os.path.join('Assets/button','levelbutton.png')).convert_alpha()
# Level 1 button
BASIC_IMG = pygame.image.load(os.path.join('Assets/button','basic.png')).convert_alpha()
# Level 2 button
ADV_IMG = pygame.image.load(os.path.join('Assets/button','advanced.png')).convert_alpha()
# Windows button
WB_IMG = pygame.image.load(os.path.join('Assets/button','windowsbutton.png')).convert_alpha()
# User button
UB_IMG = pygame.image.load(os.path.join('Assets/button','userbutton.png')).convert_alpha()
# Lock button
LB_IMG = pygame.image.load(os.path.join('Assets/button','lockbutton.png')).convert_alpha()

############### BUTTONS
#Loading...
# Vaquero
VQ_IMG = pygame.image.load(os.path.join('Assets/shapes', 'vaquero.png')).convert_alpha()
# Speech Bubble
SB_IMG = pygame.image.load(os.path.join('Assets/shapes', 'speech-bubble1.png')).convert_alpha()
# Thought Bubble
TB_IMG = pygame.image.load(os.path.join('Assets/shapes', 'communication.png')).convert_alpha()

# Criminal
CR_IMG = pygame.image.load(os.path.join('Assets/shapes', 'criminal.png')).convert_alpha()
# Speech Bubble
SB2_IMG = pygame.image.load(os.path.join('Assets/shapes', 'speech-bubble2.png')).convert_alpha()

# Imports the Basic Level images from Assets folder. 
# Imports the Password Security image.
PassSec_IMG = pygame.image.load(os.path.join('Assets/window & elements/edited windows/basic', 'Password Sec.png'))
# Imports the Secure Browsing Habits image.
SecBH_IMG = pygame.image.load(os.path.join('Assets/window & elements/edited windows/basic', 'SecBrowsingHabits.png'))
# Imports the 2nd Secure Browsing Habits image.
SecBH2_IMG = pygame.image.load(os.path.join('Assets/window & elements/edited windows/basic', 'SecBrowsingHabits2.png'))
# Imports the Social Engineering image.
SocialEng_IMG = pygame.image.load(os.path.join('Assets/window & elements/edited windows/basic', 'SocialEng.png'))
# Imports the Phishing image.
Phish_IMG = pygame.image.load(os.path.join('Assets/window & elements/edited windows/basic', 'Phishing.png'))
# Imports the 2nd Phishing image.
Phish2_IMG = pygame.image.load(os.path.join('Assets/window & elements/edited windows/basic', 'Phishing2.png'))
# Imports the 3rd Phishing image.
Phish3_IMG = pygame.image.load(os.path.join('Assets/window & elements/edited windows/basic', 'Phishing3.png'))
# Imports the Device Security image.
DSec_IMG = pygame.image.load(os.path.join('Assets/window & elements/edited windows/basic', 'DeviceSec.png'))
# Imports the second Device Security image.
DSec2_IMG = pygame.image.load(os.path.join('Assets/window & elements/edited windows/basic', 'DeviceSec2.png'))

#Password security assets
PBG_IMG = pygame.image.load(os.path.join('Assets/window & elements', 'passwordbg.png'))
PBG = pygame.transform.scale(PBG_IMG,(SCREENWIDTH, SCREENHEIGHT))

#Secure Browsing Habits assets
FWP_IMG = pygame.image.load(os.path.join('Assets/window & elements', 'fakewebpage.png'))
APU_IMG = pygame.image.load(os.path.join('Assets/window & elements', 'allowpopups.png'))
DPU_IMG = pygame.image.load(os.path.join('Assets/window & elements', 'denypopups.png'))

FWP = pygame.transform.scale(FWP_IMG,(SCREENWIDTH, SCREENHEIGHT))
APU = pygame.transform.scale(APU_IMG,(SCREENWIDTH, SCREENHEIGHT))
DPU = pygame.transform.scale(DPU_IMG,(SCREENWIDTH, SCREENHEIGHT))

#Social Engineering assets
DOOR_IMG = pygame.image.load(os.path.join('Assets/window & elements', 'accessbackgroundimage.png'))
DOOR = pygame.transform.scale(DOOR_IMG,(SCREENWIDTH, SCREENHEIGHT))

#Phishing assets
PH_IMG = pygame.image.load(os.path.join('Assets/window & elements', 'phishimg.png'))
PH = pygame.transform.scale(PH_IMG,(SCREENWIDTH, SCREENHEIGHT))

#Device Security assets
DSBG1_IMG = pygame.image.load(os.path.join('Assets/window & elements', 'ds1.png'))
DSBG2_IMG = pygame.image.load(os.path.join('Assets/window & elements', 'ds2.png'))
DSBG3_IMG = pygame.image.load(os.path.join('Assets/window & elements', 'ds3.png'))
DSBG1 = pygame.transform.scale(DSBG1_IMG,(SCREENWIDTH, SCREENHEIGHT))
DSBG2 = pygame.transform.scale(DSBG2_IMG,(SCREENWIDTH, SCREENHEIGHT))
DSBG3 = pygame.transform.scale(DSBG3_IMG,(SCREENWIDTH, SCREENHEIGHT))




# Imports the Intermediate Level images from Assets folder. 
# Imports the Ransomware Attacks image.
Ransom_IMG = pygame.image.load(os.path.join('Assets/window & elements/edited windows/intermediate', 'Ransomware.png'))
# Imports the DoS Attacks image.
DoS_IMG = pygame.image.load(os.path.join('Assets/window & elements/edited windows/intermediate', 'DoS.png'))
# Imports the Data Breaches image.
DataB_IMG = pygame.image.load(os.path.join('Assets/window & elements/edited windows/intermediate', 'DataBreaches.png'))
# Imports the Insider Threats image.
InsiderT_IMG = pygame.image.load(os.path.join('Assets/window & elements/edited windows/intermediate', 'InsiderThreats.png'))
# Imports the Malware Infections image.
Malware_IMG = pygame.image.load(os.path.join('Assets/window & elements/edited windows/intermediate', 'Malware.png'))

# load basic certificate
BCert_IMG = pygame.image.load(os.path.join('Assets/window & elements', 'certificate.png'))

# Resizes the imported images.
# Scales size of background image to surface size.
BG = pygame.transform.scale(BG_IMG,(SCREENWIDTH, SCREENHEIGHT))
# Scales size of main screen image to surface size
MS = pygame.transform.scale(MS_IMG,(SCREENWIDTH, SCREENHEIGHT))
# levelselction BG
LEVEL_SELECTION_BG = pygame.transform.scale(LEVEL_SELECTION_BG_IMG,(SCREENWIDTH, SCREENHEIGHT))

# Scales size of Password Security image to surface size
PassSec = pygame.transform.scale(PassSec_IMG,(SCREENWIDTH, SCREENHEIGHT))
# Scales size of Secure Browsing Habits image to surface size
SecBH = pygame.transform.scale(SecBH_IMG,(SCREENWIDTH, SCREENHEIGHT))
# Scales size of 2nd Secure Browsing Habits image to surface size
SecBH2 = pygame.transform.scale(SecBH2_IMG,(SCREENWIDTH, SCREENHEIGHT))
# Scales size of Social Engineering image to surface size
SocialEng = pygame.transform.scale(SocialEng_IMG,(SCREENWIDTH, SCREENHEIGHT))
# Scales size of Phishing image to surface size
Phish = pygame.transform.scale(Phish_IMG,(SCREENWIDTH, SCREENHEIGHT))
# Scales size of 2nd Phishing image to surface size
Phish2 = pygame.transform.scale(Phish2_IMG,(SCREENWIDTH, SCREENHEIGHT))
# Scales size of 3rd Phishing image to surface size
Phish3 = pygame.transform.scale(Phish3_IMG,(SCREENWIDTH, SCREENHEIGHT))
# Scales size of Device Security image to surface size
DSec = pygame.transform.scale(DSec_IMG,(SCREENWIDTH,SCREENHEIGHT))
# Scales size of 2nd Device Security image to surface size
DSec2 = pygame.transform.scale(DSec2_IMG,(SCREENWIDTH, SCREENHEIGHT))
# Scales size of Ransomware Attacks image to surface size
Ransom = pygame.transform.scale(Ransom_IMG,(SCREENWIDTH,SCREENHEIGHT))
# Scales size of DoS Attacks image to surface size
DoS = pygame.transform.scale(DoS_IMG,(SCREENWIDTH, SCREENHEIGHT))
# Scales size of Data Breaches image to surface size
DataB = pygame.transform.scale(DataB_IMG,(SCREENWIDTH, SCREENHEIGHT))
# Scales size of Insider Threats image to surface size
InsiderT = pygame.transform.scale(InsiderT_IMG,(SCREENWIDTH, SCREENHEIGHT))
# Scales size of Malware image to surface size
Malware = pygame.transform.scale(Malware_IMG,(SCREENWIDTH, SCREENHEIGHT))

# scale basic certificate
BCertificate = pygame.transform.scale(BCert_IMG,(SCREENWIDTH, SCREENHEIGHT))

############### BUTTONS
# Create button instances
# NEW GAME scaled to 0.4
NG = button.Button(100, 200, NG_IMG, 0.45)
# CONTINUE scaled to 0.4
CONT = button.Button(290, 200, CONT_IMG, 0.45)
# START GAME scaled to 0.4
SG = button.Button(300, 475, SG_IMG, 1)
# NEXT ICON scaled to 0.
NX = button.Button(1054, 576, NX_IMG, 0.6)
# SELECTION BUTTON
SelB = button.Button(347, 261, SelB_IMG, 0.2)
# BUTTON FILL
BF = button.Button(230, 10, buttonfill_IMG, 0.5)
# PASSWORD BUTTON 1
PB1 = button.Button(143, 575, PB_IMG, 1)
# PASSWORD BUTTON 2
PB2 = button.Button(621, 575, PB_IMG, 1)
# YES BUTTON
YES = button.Button(935, 275, YES_IMG, 0.6)
# NO BUTTON
NO = button.Button(1035, 275, NO_IMG, 0.6)
# BUTTON 1
button1 = button.Button(13, 110, BTTN_IMG, 0.4)
# BUTTON 2
button2 = button.Button(57, 168, BTTN_IMG, 0.45)
# BUTTON 3
button3 = button.Button(13, 220, BTTN_IMG, 0.5)
# BUTTON 4
button4 = button.Button(65, 428, BTTN_IMG, 0.15)
# BUTTON 5
button5 = button.Button(751, 440, BTTN_IMG, 0.7)
# BUTTON 6
button6 = button.Button(13, 490, BTTN_IMG, 0.45)
# WINDOWS button
WB = button.Button(13, 670, WB_IMG, 0.5)
# USER button
UB = button.Button(57, 610, UB_IMG, 0.5)
# LOCK button
LB = button.Button(70, 554, LB_IMG, 0.5)
# LEVEL SELECTION ICON 
LEVEL_SELECTION_BUTTON = button.Button(650, 475, LEVEL_SELECTION_BUTTON_IMG, 1)
# LEVEL 1 ICON 
basic_button = button.Button(490, 220, BASIC_IMG, 1)
# LEVEL 2 ICON 
advanced_button = button.Button(490, 370, ADV_IMG, 1)

############### BUTTONS


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
        self.clock = pygame.time.Clock()

        self.gameStateManager = GameStateManager('start')
        self.start = Start(self.screen, self.gameStateManager)
        self.intro = Intro(self.screen, self.gameStateManager)
        self.levelSelection = LevelSelection(self.screen, self.gameStateManager)
        
        #Password Security
        self.passsecinfo = PassSecInfo(self.screen, self.gameStateManager)      
        self.PS = PS(self.screen, self.gameStateManager)  

        #Secure Browsing Habits
        self.secbhinfo1 = SecBHInfo1(self.screen, self.gameStateManager)        
        self.secbhinfo2 = SecBHInfo2(self.screen, self.gameStateManager)
        self.SBH1 = SBH1(self.screen, self.gameStateManager)
        self.SBH2 = SBH2(self.screen, self.gameStateManager)
        self.SBH3 = SBH3(self.screen, self.gameStateManager)                
        
        #Social Engineering
        self.socenginfo = SocEngInfo(self.screen, self.gameStateManager)        
        self.SE = SE(self.screen, self.gameStateManager)

        #Phishing
        self.phishinfo1 = PhishInfo1(self.screen, self.gameStateManager)        
        self.phishinfo2 = PhishInfo2(self.screen, self.gameStateManager)        
        self.phishinfo3 = PhishInfo3(self.screen, self.gameStateManager)
        self.PH = PHI(self.screen, self.gameStateManager)               
        
        #Device Security
        self.dsecinfo1 = DSecInfo1(self.screen, self.gameStateManager)
        self.dsecinfo2 = DSecInfo2(self.screen, self.gameStateManager)
        self.DS1 = DS1(self.screen, self.gameStateManager)
        self.DS2 = DS2(self.screen, self.gameStateManager)
        self.DS3 = DS3(self.screen, self.gameStateManager)
        
        #Basic Certificate
        self.basiccertificate = BasicCertificate(self.screen, self.gameStateManager)


        self.states = {'start':self.start,
                       'levelSelection': self.levelSelection, 
                       'intro':self.intro,
                       'passsecinfo':self.passsecinfo,
                       'socenginfo':self.socenginfo,
                       'phishinfo1':self.phishinfo1,
                       'phishinfo2':self.phishinfo2,
                       'phishinfo3':self.phishinfo3,
                       'secbhinfo1':self.secbhinfo1,
                       'secbhinfo2':self.secbhinfo2,
                       'dsecinfo1':self.dsecinfo1,
                       'dsecinfo2':self.dsecinfo2,
                       'ps':self.PS,
                       'sbh1':self.SBH1,
                       'sbh2':self.SBH2,
                       'sbh3':self.SBH3,
                       'se':self.SE,
                       'ph':self.PH,
                       'ds1':self.DS1,
                       'ds2':self.DS2,
                       'ds3':self.DS3,
                       'basiccertificate':self.basiccertificate}
    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()


                #if event.type == pygame.KEYDOWN:
                    #self.gameStateManager.set_state('start')

            self.states[self.gameStateManager.get_state()].run()

            pygame.display.update()
            self.clock.tick(FPS)

class Vaquero:
    def vaquero(scale):
        VQX, VQY = 5, 100
        width = VQ_IMG.get_width()
        height = VQ_IMG.get_height()
        VQ = pygame.transform.scale(VQ_IMG, (int(width * scale), int(height * scale)))
        screen.blit(VQ, (VQX, VQY))
    
    def speech(scale):
        SBX, SBY = 380, 80
        width = SB_IMG.get_width()
        height = SB_IMG.get_height()
        SB = pygame.transform.scale(SB_IMG, (int(width * scale), int(height * scale)))
        screen.blit(SB, (SBX, SBY))

    def thought(scale):
        TBX, TBY = 80, 30
        width = TB_IMG.get_width()
        height = TB_IMG.get_height()
        TB = pygame.transform.scale(TB_IMG, (int(width * scale), int(height * scale)))
        screen.blit(TB, (TBX, TBY))

class Criminal:
    def criminal(scale):
        CRX, CRY = 5, 100
        width = CR_IMG.get_width()
        height = CR_IMG.get_height()
        CR = pygame.transform.scale(CR_IMG, (int(width * scale), int(height * scale)))
        screen.blit(CR, (CRX, CRY))
    
    def speech(scale):
        SB2X, SB2Y = 380, 10
        width = SB2_IMG.get_width()
        height = SB2_IMG.get_height()
        SB2 = pygame.transform.scale(SB2_IMG, (int(width * scale), int(height * scale)))
        screen.blit(SB2, (SB2X, SB2Y))

class BasicCertificate:
    def __init__(self, display, gameStateManager):
            self.display = display
            self.gameStateManager = gameStateManager
    def run(self):
            self.display.fill('black')
            screen.blit(BCertificate, (0,0))
            #keys = pygame.key.get_pressed()
            if NX.draw(screen):
                    self.gameStateManager.set_state('start')
            pygame.display.update()

class DS3:
    def __init__(self, display, gameStateManager):
        self.display = display
        self.gameStateManager = gameStateManager
    def run(self):
        self.display.fill('black')
        screen.blit(DSBG3, (0,0))
        #keys = pygame.key.get_pressed()
        if LB.draw(screen):
                self.gameStateManager.set_state('basiccertificate')
        pygame.display.update()

class DS2:
    def __init__(self, display, gameStateManager):
        self.display = display
        self.gameStateManager = gameStateManager
    def run(self):
        self.display.fill('black')
        screen.blit(DSBG2, (0,0))
        #keys = pygame.key.get_pressed()
        if UB.draw(screen):
                self.gameStateManager.set_state('ds3')
        pygame.display.update()

class DS1:
    def __init__(self, display, gameStateManager):
        self.display = display
        self.gameStateManager = gameStateManager
    def run(self):
        self.display.fill('black')
        screen.blit(DSBG1, (0,0))
        #keys = pygame.key.get_pressed()
        if WB.draw(screen):
                self.gameStateManager.set_state('ds2')
        pygame.display.update()

class DSecInfo2:
    def __init__(self, display, gameStateManager):
        self.display = display
        self.gameStateManager = gameStateManager
    def run(self):
        self.display.fill('black')
        screen.blit(DSec2, (0,0))
        #keys = pygame.key.get_pressed()
        if NX.draw(screen):
                self.gameStateManager.set_state('ds1')
        pygame.display.update()

class DSecInfo1:
    def __init__(self, display, gameStateManager):
        self.display = display
        self.gameStateManager = gameStateManager
    def run(self):
        self.display.fill('black')
        screen.blit(DSec, (0,0))
        #keys = pygame.key.get_pressed()
        if NX.draw(screen):
                self.gameStateManager.set_state('dsecinfo2')
        pygame.display.update()

class PHI:
    def __init__(self, display, gameStateManager):
        self.display = display
        self.gameStateManager = gameStateManager
    def run(self):
        self.display.fill('black')
        screen.blit(PH, (0,0))
        #keys = pygame.key.get_pressed()
        tally = 0
        if button1.draw(screen):
            tally = tally +1
        if button2.draw(screen):
            tally = tally +1
        if button3.draw(screen):
            tally = tally +1
        if button4.draw(screen):
            tally = tally +1
        if button5.draw(screen):
            tally = tally +1
        if button6.draw(screen):
            tally = tally +1
            self.gameStateManager.set_state('dsecinfo1')

    pygame.display.update()

class PhishInfo3:
    def __init__(self, display, gameStateManager):
        self.display = display
        self.gameStateManager = gameStateManager
    def run(self):
        self.display.fill('black')
        screen.blit(Phish3, (0,0))
        #keys = pygame.key.get_pressed()
        if NX.draw(screen):
            self.gameStateManager.set_state('ph')
    pygame.display.update()

class PhishInfo2:
    def __init__(self, display, gameStateManager):
        self.display = display
        self.gameStateManager = gameStateManager
    def run(self):
        self.display.fill('black')
        screen.blit(Phish2, (0,0))
        #keys = pygame.key.get_pressed()
        if NX.draw(screen):
            self.gameStateManager.set_state('phishinfo3')
    pygame.display.update()

class PhishInfo1:
    def __init__(self, display, gameStateManager):
        self.display = display
        self.gameStateManager = gameStateManager
    def run(self):
        self.display.fill('black')
        screen.blit(Phish, (0,0))
        #keys = pygame.key.get_pressed()
        if NX.draw(screen):
            self.gameStateManager.set_state('phishinfo2')
    pygame.display.update()

class SE:
    def __init__(self, display, gameStateManager):
        self.display = display
        self.gameStateManager = gameStateManager
    def run(self):
        self.display.fill('black')
        screen.blit(DOOR, (0,0))
        Criminal.criminal(1)
        Criminal.speech(0.5)
        #keys = pygame.key.get_pressed()
        if YES.draw(screen):
            text_surface = my_font.render('Try Again', False, ('white'))
            screen.blit(text_surface, (5,5))
        if NO.draw(screen):
            self.gameStateManager.set_state('phishinfo1')
    pygame.display.update()

class SocEngInfo:
    def __init__(self, display, gameStateManager):
        self.display = display
        self.gameStateManager = gameStateManager
    def run(self):
        self.display.fill('black')
        screen.blit(SocialEng, (0,0))
        #keys = pygame.key.get_pressed()
        if NX.draw(screen):
            self.gameStateManager.set_state('se')
    pygame.display.update()

class SBH3:
    def __init__(self, display, gameStateManager):
        self.display = display
        self.gameStateManager = gameStateManager
    def run(self):
        self.display.fill('black')
        screen.blit(DPU, (0,0))
        #keys = pygame.key.get_pressed()
        if NX.draw(screen):
            self.gameStateManager.set_state('socenginfo')
    pygame.display.update()

class SBH2:
    def __init__(self, display, gameStateManager):
        self.display = display
        self.gameStateManager = gameStateManager
    def run(self):
        self.display.fill('black')
        screen.blit(APU, (0,0))
        #keys = pygame.key.get_pressed()
        if SelB.draw(screen):
            self.gameStateManager.set_state('sbh3')
    pygame.display.update()

class SBH1:
    def __init__(self, display, gameStateManager):
        self.display = display
        self.gameStateManager = gameStateManager
    def run(self):
        self.display.fill('black')
        screen.blit(FWP, (0,0))
        #keys = pygame.key.get_pressed()
        if BF.draw(screen):
            self.gameStateManager.set_state('sbh2')
    pygame.display.update()

class SecBHInfo2:
    def __init__(self, display, gameStateManager):
        self.display = display
        self.gameStateManager = gameStateManager
    def run(self):
        self.display.fill('black')
        screen.blit(SecBH2, (0,0))
        #keys = pygame.key.get_pressed()
        if NX.draw(screen):
            self.gameStateManager.set_state('sbh1')
        pygame.display.update()

class SecBHInfo1:
    def __init__(self, display, gameStateManager):
        self.display = display
        self.gameStateManager = gameStateManager
    def run(self):
        self.display.fill('black')
        screen.blit(SecBH, (0,0))
        #keys = pygame.key.get_pressed()
        if NX.draw(screen):
            self.gameStateManager.set_state('secbhinfo2')
    pygame.display.update()

class PS:
    def __init__(self, display, gameStateManager):
        self.display = display
        self.gameStateManager = gameStateManager
    def run(self):
        self.display.fill('black')
        screen.blit(PBG, (0,0))
        #keys = pygame.key.get_pressed()
        if PB1.draw(screen):
            text_surface = my_font.render('Try Again', False, ('white'))
            screen.blit(text_surface, (5,5))
        if PB2.draw(screen):
            self.gameStateManager.set_state('secbhinfo1')

    pygame.display.update()

class PassSecInfo:
    def __init__(self, display, gameStateManager):
        self.display = display
        self.gameStateManager = gameStateManager
    def run(self):
        self.display.fill('black')
        screen.blit(PassSec, (0,0))
        #keys = pygame.key.get_pressed()
        if NX.draw(screen):
            self.gameStateManager.set_state('ps')
    pygame.display.update()

class Intro:
    def __init__(self, display, gameStateManager):
        self.display = display
        self.gameStateManager = gameStateManager
    def run(self):
        self.display.fill('blue')
        screen.blit(BG, (0,0))
        Vaquero.vaquero(1)
        Vaquero.speech(1)
        #keys = pygame.key.get_pressed()
        if NX.draw(screen):
            self.gameStateManager.set_state('passsecinfo')
        pygame.display.update()

class LevelSelection:
  def __init__(self, display, gameStateManager):
    self.display = display
    self.gameStateManager = gameStateManager
    # Load level images or create buttons for each level

  def run(self):
    self.display.fill('black')
    screen.blit(LEVEL_SELECTION_BG, (0, 0))  # Render the background for the level selection screen

    # Draw level images/buttons on the screen
    keys = pygame.key.get_pressed()
    if basic_button.draw(screen):
          self.gameStateManager.set_state('levelSelection')
    if advanced_button.draw(screen):
          self.gameStateManager.set_state('levelSelection')
    pygame.display.flip()

    # Handle user input (mouse/keyboard) to select a level
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Check if the user clicked on a level image/button
            if basic_button.rect.collidepoint(event.pos):
                # Set the game state to the selected level
                self.gameStateManager.set_state('passsecinfo')
            if advanced_button.rect.collidepoint(event.pos):
                self.gameStateManager.set_state('start')
                
            # Add more conditions for other levels

    pygame.display.update()

class Start:
  def __init__(self, display, gameStateManager):
      self.display = display
      self.gameStateManager = gameStateManager

  def run(self):
      self.display.fill('black')
      screen.blit(MS, (0, 0))
      if SG.draw(screen):
          self.gameStateManager.set_state('intro')
      if LEVEL_SELECTION_BUTTON.draw(screen):  # Add a button for level selection
          self.gameStateManager.set_state('levelSelection')
      pygame.display.update()

class GameStateManager:
    def __init__(self, currentState):
        self.currentState = currentState
    def get_state(self):
        return self.currentState
    def set_state(self, state):
        self.currentState = state

if __name__ == '__main__':
    game = Game()
    game.run()