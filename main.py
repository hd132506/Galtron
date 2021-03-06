#Created by Matt Boan
import sys
from _pickle import load
import pygame as pg
from pygame.sprite import Group

#import self made classes
from settings import Settings
import gameFunctions as gf #Event checker and update screen
import mainMenu as mm #Main menu
import twoPlayer as tp #two player mode
import about as About
from ship import Ship
from alien import Alien
from gameStats import GameStats #Game stats that are changed during the duration of the game
from button import Button #A button class that can be called for every new button
from selector import Selector #Import the main menu selector
from scoreboard import Scoreboard #Score board for points, high score, lives, level ect.



def runGame():
	#Initialize game and create a window
	pg.init()
	#create a new object using the settings class
	setting = Settings()
	#creaete a new object from pygame display
	screen = pg.display.set_mode((setting.screenWidth, setting.screenHeight))
	#set window caption using settings obj
	pg.display.set_caption(setting.windowCaption)

	playBtn = Button(setting, screen, "PLAY", 200)
	menuBtn = Button(setting, screen, "MENU", 250)
	twoPlayBtn = Button(setting, screen, "2PVS", 250)
	setBtnbtn = Button(setting, screen, "SETTING", 400)
	aboutBtn = Button(setting, screen, "ABOUT", 300)
	quitBtn = Button(setting, screen, "QUIT", 350)
	#make slector for buttons
	sel = Selector(setting, screen)
	sel.rect.x = playBtn.rect.x + playBtn.width + 10
	sel.rect.centery = playBtn.rect.centery

	#Create an instance to stor game stats
	stats = GameStats(setting)
	sb = Scoreboard(setting, screen, stats)

	#Make a ship
	ship = Ship(setting, screen)
	#Ships for two player
	ship1 = Ship(setting, screen)
	ship2 = Ship(setting, screen)

	#make a group of bullets to store
	bullets = Group()
	eBullets = Group()

	#Make an alien
	aliens = Group()
	gf.createFleet(setting, screen, ship, aliens)
	pg.display.set_icon(pg.transform.scale(ship.image, (32, 32)))

	#plays bgm
	pg.mixer.music.load("galtron.mp3")
	pg.mixer.music.set_volume(0.25)
	pg.mixer.music.play(-1)

	runGame = True

	#Set the two while loops to start mainMenu first
	while runGame:
		#Set to true to run main game loop
		while stats.mainMenu:
			mm.checkEvents(setting, screen, stats, sb, playBtn, twoPlayBtn, aboutBtn, quitBtn, menuBtn, sel, ship, aliens, bullets, eBullets)
			mm.drawMenu(setting, screen, sb, playBtn, menuBtn, twoPlayBtn, aboutBtn, quitBtn, sel)

		while stats.mainGame:
			#Game functions
			gf.checkEvents(setting, screen, stats, sb, playBtn, quitBtn, sel, ship, aliens, bullets, eBullets) #Check for events
			if stats.gameActive:
				gf.updateAliens(setting, stats, sb, screen, ship, aliens, bullets, eBullets) #Update aliens
				gf.updateBullets(setting, screen, stats, sb, ship, aliens, bullets, eBullets) #Update collisions
				ship.update() #update the ship
			gf.updateScreen(setting, screen, stats, sb, ship, aliens, bullets, eBullets, playBtn, menuBtn, quitBtn, sel) #Update the screen

		while stats.mainAbout:
			About.checkEvents(setting, screen, stats, sb, playBtn, quitBtn, menuBtn, sel, ship, aliens, bullets, eBullets)
			About.drawMenu(setting, screen, sb, menuBtn, quitBtn, sel)

		while stats.twoPlayer:
			"""
			tp.checkEvents(setting, screen, stats, playBtn, quitBtn, sel, bullets, eBullets, ship1, ship2)
			if stats.gameActive:
				ship1.update()
				tp.updateBullets(setting, screen, stats, ship1, ship2, bullets, eBullets)
			tp.updateScreen(setting, screen, stats, bullets, eBullets, playBtn, menuBtn, quitBtn, sel, ship1, ship2)
			"""
		while stats.mainGame:
			if runGame == True:
				print("test")
#init bgm mixer
pg.mixer.pre_init(44100,16,2,4096)
#run the runGame method to run the game
runGame()
