# IMPORTS
import pygame as pg
import os
from Dealer import Dealer
from Player import Player
from Button import Button

# INITIALIZATION
pg.init()

# SETTING CAPTION
pg.display.set_caption("Blackjack")

# WINDOW DIMENSIONS
WIDTH = 900
HEIGHT = 500

#SETTING UP THE WINDOW
WIN = pg.display.set_mode((WIDTH, HEIGHT))

# COLORS
GREEN = (151, 221, 151)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# GAME MECHANICS
FPS = 60
CLOCK = pg.time.Clock()

# set up the font
font = pg.font.SysFont(None, 48)  # use the system font, size 48

# IMAGES
Card_Back = pg.image.load(os.path.join("images", "card_image.png"))
start_img = pg.image.load('images/start_btn.png').convert_alpha()
exit_img = pg.image.load('images/exit_btn.png').convert_alpha()
hit_img = pg.image.load('images/hit_btn.png').convert_alpha()
stay_img = pg.image.load('images/stay_btn.png').convert_alpha()
reset_img = pg.image.load('images/restart_btn.png').convert_alpha()

# CARD DIMENSIONS
CARD_HEIGHT = Card_Back.get_height()
CARD_WIDTH = Card_Back.get_width()



# BUTTON INSTANCES
start_button = Button(WIDTH // 2 - 100, 200, start_img, 0.3)
hit_button = Button(WIDTH // 2 - 25, 200, hit_img, 0.3)
stay_button = Button(WIDTH // 2 + 75, 200, stay_img, 0.3)
exit_button = Button(WIDTH // 2 + 150, 255, exit_img, 0.3)
restart_button = Button(WIDTH // 2 + 150, 200, reset_img, 0.3)

# DEALER INSTANCE
dealer = Dealer()
# PLAYER INSTANCE
player = Player()

#CONDITIONS
start_clicked = False
hit_clicked = False
stay_clicked = False
restart_clicked = False
exit_clicked = False
is_dealers_turn = False
current_stage = "start"
game_over = False
player_busted = False

winner = "none"

def reset_conditions():
    global current_stage, start_clicked, hit_button, hit_clicked, stay_clicked, is_dealers_turn, game_over, restart_clicked, exit_clicked, player_busted, winner
    start_clicked = False
    hit_clicked = False
    stay_clicked = False
    restart_clicked = False
    exit_clicked = False
    is_dealers_turn = False
    current_stage = "start"
    game_over = False
    player_busted = False
    winner = "none"

# ALL DRAWING TO WINDOW
def draw_window():
    global current_stage, start_clicked, hit_button, hit_clicked, stay_clicked, is_dealers_turn, game_over, restart_clicked, exit_clicked, player_busted, winner
    WIN.fill(GREEN)
    WIN.blit(Card_Back, (WIDTH // 2 - CARD_WIDTH // 2 - 200, HEIGHT // 2 - CARD_HEIGHT // 2))
    player_score_text = font.render("PLAYER: " + str(player.total), True, (255, 255, 255)) 
    dealer_score_text = font.render("DEALER: " + str(dealer.total), True, (255, 255, 255))
    winner_text = font.render("WINNER: " + winner, True, (255, 255, 255))
    WIN.blit(player_score_text, (710, 10))
    WIN.blit(dealer_score_text, (705, 450))
    WIN.blit(winner_text, (0, 0))
    if (current_stage == "start"):
        start_clicked = start_button.draw(WIN)
        if (start_clicked == True):
            current_stage = "in-game"
            start_clicked = True
    elif (current_stage == "in-game"):
        offset = 0
        for card in player.hand:
            chosen_card = pg.image.load(os.path.join("images", str(card) + ".png"))
            chosen_card = pg.transform.scale(chosen_card, (CARD_WIDTH, CARD_HEIGHT))
            WIN.blit(chosen_card, (WIDTH // 2 - CARD_WIDTH + offset, 10))
            offset += chosen_card.get_width()
        offset = 0
        if (is_dealers_turn == False):
            dealer_card = pg.image.load(os.path.join("images", str(dealer.hand[0]) + ".png"))
            dealer_card = pg.transform.scale(dealer_card, (CARD_WIDTH, CARD_HEIGHT))
            WIN.blit(Card_Back, (WIDTH // 2 - CARD_WIDTH, HEIGHT - CARD_HEIGHT - 10))
            WIN.blit(dealer_card, (WIDTH // 2 - CARD_WIDTH + 50, HEIGHT - CARD_HEIGHT - 10))
            offset += dealer_card.get_width()
        else:
            for card in dealer.hand:
                chosen_card = pg.image.load(os.path.join("images", str(card) + ".png"))
                chosen_card = pg.transform.scale(chosen_card, (CARD_WIDTH, CARD_HEIGHT))
                WIN.blit(chosen_card, (WIDTH // 2 - CARD_WIDTH + offset, HEIGHT - CARD_HEIGHT - 10))
                offset += chosen_card.get_width()
        
        if (is_dealers_turn == False):
            hit_clicked = hit_button.draw(WIN)
            stay_clicked = stay_button.draw(WIN)

        if (stay_clicked == True or player_busted == True):
            is_dealers_turn = True

        if is_dealers_turn and game_over == False:
            for card in dealer.hand:
                chosen_card = pg.image.load(os.path.join("images", str(card) + ".png"))
                chosen_card = pg.transform.scale(chosen_card, (CARD_WIDTH, CARD_HEIGHT))
                WIN.blit(chosen_card, (WIDTH // 2 - CARD_WIDTH + offset, HEIGHT - CARD_HEIGHT - 10))
                offset += chosen_card.get_width()
        if game_over == True:
            restart_clicked = restart_button.draw(WIN)
            exit_clicked = exit_button.draw(WIN)
    pg.display.update()


def handle_events():
    global start_clicked, hit_clicked, stay_clicked, player_busted, game_over, restart_clicked, winner
    running = True
    
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                running = False
    
    if start_clicked == True:
        dealer.deal_card(player)
        dealer.deal_card(player)
        dealer.calculate_total(player)
        dealer.deal_card(dealer)
        dealer.deal_card(dealer)
        start_clicked = False
    if hit_clicked == True and player_busted == False:
        dealer.deal_card(player)
        dealer.calculate_total(player)
        print("player total: " + str(player.total))
        print("dealer total: " + str(dealer.total))
        hit_clicked = False
    if stay_clicked == True or player_busted == True and game_over == False:
        dealer.calculate_total(dealer)
        while dealer.total < 17:
            dealer.deal_card(dealer)
            dealer.calculate_total(dealer)
        game_over = True
        stay_clicked = False
    if player.total > 21:
        player_busted = True
    if restart_clicked == True:
        reset_conditions()
        player.reset()
        dealer.reset()
        restart_clicked = False
    if exit_clicked == True:
        running = False
    if game_over == True:
        if player.total > 21 and dealer.total <= 21:
            winner = "Dealer"
        elif player.total > 21 and dealer.total > 21:
            winner = "Draw"
        elif player.total <= 21 and dealer.total > 21:
            winner = "Player"
        elif player.total <= 21 and dealer.total <= 21:
            if player.total > dealer.total:
                winner = "Player"
            if dealer.total > player.total:
                winner = "Dealer"
        elif player.total == dealer.total:
            winner = "Draw"

    return running


def main():
    running = True
    while running:
        running = handle_events()
        draw_window()
        CLOCK.tick(FPS)


if __name__ == "__main__":
    main()
    pg.quit()
