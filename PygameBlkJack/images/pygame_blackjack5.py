from os import kill
import time
import pygame as pg
import random
from pygame import rect
from pygame import font
from pygame.constants import K_ESCAPE, KEYDOWN
from pygame.locals import(
    RLEACCEL,
    K_h,
    K_s,
    K_ESCAPE
)

class Player(object):
    card_values = {"A❤️": 11, "2❤️": 2, "3❤️": 3, "4❤️": 4, "5❤️": 5, "6❤️": 6, "7❤️": 7, "8❤️": 8, "9❤️": 9, "10❤️": 10, "J❤️": 10, "Q❤️": 10, "K❤️": 10,\
          "A♦️": 11, "2♦️": 2, "3♦️": 3, "4♦️": 4, "5♦️": 5, "6♦️": 6, "7♦️": 7, "8♦️": 8, "9♦️": 9, "10♦️": 10, "J♦️": 10, "Q♦️": 10, "K♦️": 10,\
          "A♠️": 11, "2♠️": 2, "3♠️": 3, "4♠️": 4, "5♠️": 5, "6♠️": 6, "7♠️": 7, "8♠️": 8, "9♠️": 9, "10♠️": 10, "J♠️": 10, "Q♠️": 10, "K♠️": 10,\
          "A♣️": 11, "2♣️": 2, "3♣️": 3, "4♣️": 4, "5♣️": 5, "6♣️": 6, "7♣️": 7, "8♣️": 8, "9♣️": 9, "10♣️": 10, "J♣️": 10, "Q♣️": 10, "K♣️": 10}
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 600
    player_done = False
    screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    def __init__(self, isDealer, x, y):
        self.busted = False
        self.isDealer = isDealer
        self.x = x
        self.y = y
        self.image_height = 150
        self.image_width = 150
        self.total = 0
        self.user_cards = []
        self.card_images = []
        self.PERMANENT_card_values = {"A❤️": 11, "2❤️": 2, "3❤️": 3, "4❤️": 4, "5❤️": 5, "6❤️": 6, "7❤️": 7, "8❤️": 8, "9❤️": 9, "10❤️": 10, "J❤️": 10, "Q❤️": 10, "K❤️": 10,\
          "A♦️": 11, "2♦️": 2, "3♦️": 3, "4♦️": 4, "5♦️": 5, "6♦️": 6, "7♦️": 7, "8♦️": 8, "9♦️": 9, "10♦️": 10, "J♦️": 10, "Q♦️": 10, "K♦️": 10,\
          "A♠️": 11, "2♠️": 2, "3♠️": 3, "4♠️": 4, "5♠️": 5, "6♠️": 6, "7♠️": 7, "8♠️": 8, "9♠️": 9, "10♠️": 10, "J♠️": 10, "Q♠️": 10, "K♠️": 10,\
          "A♣️": 11, "2♣️": 2, "3♣️": 3, "4♣️": 4, "5♣️": 5, "6♣️": 6, "7♣️": 7, "8♣️": 8, "9♣️": 9, "10♣️": 10, "J♣️": 10, "Q♣️": 10, "K♣️": 10}
        self.cards = {"A❤️": "h01.png", "2❤️": "h02.png", "3❤️": "h03.png", "4❤️": "h04.png", "5❤️": "h05.png", "6❤️": "h06.png",\
             "7❤️": "h07.png", "8❤️": "h08.png", "9❤️": "h09.png", "10❤️": "h10.png", "J❤️": "h11.png", "Q❤️": "h12.png", "K❤️": "h13.png",\
                "A♦️": "d01.png", "2♦️": "d02.png", "3♦️": "d03.png", "4♦️": "d04.png", "5♦️": "d05.png", "6♦️": "d06.png",\
             "7♦️": "d07.png", "8♦️": "d08.png", "9♦️": "d09.png", "10♦️": "d10.png", "J♦️": "d11.png", "Q♦️": "d12.png", "K♦️": "d13.png",\
                "A♠️": "s01.png", "2♠️": "s02.png", "3♠️": "s03.png", "4♠️": "s04.png", "5♠️": "s05.png", "6♠️": "s06.png",\
             "7♠️": "s07.png", "8♠️": "s08.png", "9♠️": "s09.png", "10♠️": "s10.png", "J♠️": "s11.png", "Q♠️": "s12.png", "K♠️": "s13.png",\
                "A♣️": "c01.png", "2♣️": "c02.png", "3♣️": "c03.png", "4♣️": "c04.png", "5♣️": "c05.png", "6♣️": "c06.png",\
             "7♣️": "c07.png", "8♣️": "c08.png", "9♣️": "c09.png", "10♣️": "c10.png", "J♣️": "c11.png", "Q♣️": "c12.png", "K♣️": "c13.png"}
    def draw_user_hand(self):
        
        self.surf = pg.image.load("/Users/jasonwilsonrodriguez/Desktop/DESKDOCS/python/pygame_blackjack/card_image.jpeg")
        self.rect = self.surf.get_rect(center=(100, 500))
        Player.screen.blit(self.surf, self.rect)
        try:
            self.image1 = pg.image.load(self.card_images[0])
            self.image1 = pg.transform.scale(self.image1, (self.image_width, self.image_height))
            self.rect1 = self.image1.get_rect()
            self.rect1 = self.rect1.move((self.x, self.y))
            self.image2 = pg.image.load(self.card_images[1])
            self.image2 = pg.transform.scale(self.image2, (self.image_width, self.image_height))
            self.rect2 = self.image2.get_rect()
            self.rect2 = self.rect2.move((self.x + 25, self.y))
            self.image3 = pg.image.load(self.card_images[2])
            self.image3 = pg.transform.scale(self.image3, (self.image_width, self.image_height))
            self.rect3 = self.image3.get_rect()
            self.rect3 = self.rect3.move((self.x + 50, self.y))
            self.image4 = pg.image.load(self.card_images[3])
            self.image4 = pg.transform.scale(self.image4, (self.image_width, self.image_height))
            self.rect4 = self.image4.get_rect()
            self.rect4 = self.rect4.move((self.x + 75, self.y))
            self.image5 = pg.image.load(self.card_images[4])
            self.image5 = pg.transform.scale(self.image5, (self.image_width, self.image_height))
            self.rect5 = self.image5.get_rect()
            self.rect5 = self.rect5.move((self.x + 100, self.y))
        except:
            pass
        try:
            Player.screen.blit(self.image1, self.rect1)
            Player.screen.blit(self.image2, self.rect2)
            Player.screen.blit(self.image3, self.rect3)
            Player.screen.blit(self.image4, self.rect4)
            Player.screen.blit(self.image5, self.rect5)
        except:
            pass
        
    def draw_dealer_hand(self):
        if Player.player_done == False:
            try:
                self.image1 = pg.image.load(self.card_images[0])
                self.image1 = pg.transform.scale(self.image1, (self.image_width, self.image_height))
                self.rect1 = self.image1.get_rect()
                self.rect1 = self.rect1.move((self.x, self.y))
            except:
                pass
            try:
                Player.screen.blit(self.image1, self.rect1)
            except:
                pass
        else:
            try:
                self.image1 = pg.image.load(self.card_images[0])
                self.image1 = pg.transform.scale(self.image1, (self.image_width, self.image_height))
                self.rect1 = self.image1.get_rect()
                self.rect1 = self.rect1.move((self.x, self.y))
                self.image2 = pg.image.load(self.card_images[1])
                self.image2 = pg.transform.scale(self.image2, (self.image_width, self.image_height))
                self.rect2 = self.image2.get_rect()
                self.rect2 = self.rect2.move((self.x + 25, self.y))
                self.image3 = pg.image.load(self.card_images[2])
                self.image3 = pg.transform.scale(self.image3, (self.image_width, self.image_height))
                self.rect3 = self.image3.get_rect()
                self.rect3 = self.rect3.move((self.x + 50, self.y))
                self.image4 = pg.image.load(self.card_images[3])
                self.image4 = pg.transform.scale(self.image4, (self.image_width, self.image_height))
                self.rect4 = self.image4.get_rect()
                self.rect4 = self.rect4.move((self.x + 75, self.y))
                self.image5 = pg.image.load(self.card_images[4])
                self.image5 = pg.transform.scale(self.image5, (self.image_width, self.image_height))
                self.rect5 = self.image5.get_rect()
                self.rect5 = self.rect5.move((self.x + 100, self.y))
            except:
                pass
            try:
                Player.screen.blit(self.image1, self.rect1)
                Player.screen.blit(self.image2, self.rect2)
                Player.screen.blit(self.image3, self.rect3)
                Player.screen.blit(self.image4, self.rect4)
                Player.screen.blit(self.image5, self.rect5)
            except:
                pass
    def erase_everything(self):
        Player.screen.fill((255, 255, 255))
        pg.display.update()
    def add_card(self):
            key = random.choice(list(Player.card_values.keys()))
            trash = Player.card_values[key]
            del(trash)
            self.user_cards.append(key)
            self.card_images.append(self.cards[key])
    def update_total(self):
        self.total = 0
        if self.isDealer == True and len(self.user_cards) < 3 and Player.player_done == False: 
            self.total = self.PERMANENT_card_values[self.user_cards[0]]
        else:
            for x in self.user_cards:
                self.total = self.total + self.PERMANENT_card_values[x]
    def check_player_done(self):
        if self.total > 21:
            Player.player_done = True
    def draw_hand_total_player(self, x, y):
        font_player = pg.font.SysFont('Tahoma', 20)
        text_player = font_player.render(f"Your Total: {self.total}", True, (0, 0, 0))
        Player.screen.blit(text_player, (x, y))
    def draw_hand_total_dealer(self, x, y):
        font_dealer = pg.font.SysFont('Tahoma', 20)
        text_dealer = font_dealer.render(f'Dealer Total: {self.total}', True, (0, 0, 0))
        Player.screen.blit(text_dealer, (x, y))















#main


pg.init()
jason = Player(False, 225, 25)
jason.add_card()
jason.add_card()
jason.update_total()
jason.check_player_done()
dealer = Player(True, 225, 425)
dealer.add_card()
dealer.add_card()
dealer.update_total()
running = True
while running:
    Player.screen.fill((0, 200, 0))
    if Player.player_done == True and dealer.total < 17:
        while dealer.total < 17:
            dealer.add_card()
            dealer.update_total()
    if dealer.total < jason.total and jason.total < 22 and Player.player_done == True:
        end_font = pg.font.SysFont('Tahoma', 20)
        end_text = end_font.render(f"You Win!", True, (0, 0, 0))
        Player.screen.blit(end_text, (300, 300))
    elif dealer.total > jason.total and jason.total < 22 and dealer.total > 21 and Player.player_done == True:
        end_font = pg.font.SysFont('Tahoma', 20)
        end_text = end_font.render(f"You Win!", True, (0, 0, 0))
        Player.screen.blit(end_text, (300, 300))
    elif dealer.total < 22 and jason.total < dealer.total and Player.player_done == True:
        end_font = pg.font.SysFont('Tahoma', 20)
        end_text = end_font.render(f"You Lose!", True, (0, 0, 0))
        Player.screen.blit(end_text, (300, 300))
    elif jason.total > 21:
        end_font = pg.font.SysFont('Tahoma', 20)
        end_text = end_font.render(f"You Lose!", True, (0, 0, 0))
        Player.screen.blit(end_text, (300, 300))
    elif jason.total == dealer.total and Player.player_done == True:
        end_font = pg.font.SysFont('Tahoma', 20)
        end_text = end_font.render(f"Draw!", True, (0, 0, 0))
        Player.screen.blit(end_text, (300, 300))
    jason.draw_user_hand()
    dealer.draw_dealer_hand()
    jason.draw_hand_total_player(225, 185)
    dealer.draw_hand_total_dealer(225, 400)
    for event in pg.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
            elif event.key == K_h:
                if jason.total < 21 and Player.player_done == False:
                    jason.add_card()
                    jason.update_total()
                    jason.check_player_done()
                    if jason.total > 21:
                        jason.busted = True
            elif event.key == K_s:
                Player.player_done = True
                dealer.update_total()
    dealer.update_total()
    pg.display.update()