import random
import blackjackart
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

continue_playing = True
while continue_playing:
    players_hand = []
    computers_hand = []
    def player_draw():
        players_hand.append(random.choice(cards))

    def computer_draw():
        computers_hand.append(random.choice(cards))

    def final_score():
        print(f"Your final hand: {players_hand}, final score: {current_score}")
        print(f"Computer's final hand: {computers_hand}, final score {computer_score}")



    play_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
    print("\n" * 20)
    if play_game == "y":
        print(blackjackart.logo)
        player_draw()
        player_draw()
        current_score = sum(players_hand)
        print(f"Your cards: {players_hand}, current score: {current_score}")
        computer_draw()
        computer_draw()
        computer_score = sum(computers_hand)
        print(f"Computer's first card: {computers_hand[0]}")
        while computer_score < 17:
            computer_draw()
            computer_score = sum(computers_hand)
            for card in computers_hand:
                ace = 11
                if current_score > 10 and ace in computers_hand:
                    computers_hand.remove(11)
                    computers_hand.append(1)
        hit = True
        while hit:
            hit_stay = input("Type 'y' to hit type 'n' to stay: ").lower()
            if hit_stay == "y":
                player_draw()
                current_score = sum(players_hand)
                for card in players_hand:
                    ace = 11
                    if current_score > 10 and ace in players_hand:
                        players_hand.remove(11)
                        players_hand.append(1)
                current_score = sum(players_hand)
                if current_score > 21:
                   hit = False
                else:
                    print(f"Your cards: {players_hand}, current score: {current_score}")
            else:
                hit = False
        if current_score > 21:
            print(f"Your final hand: {players_hand}, final score: {current_score}")
            print("You bust!")
        elif current_score <= 21:
            if computer_score == current_score:
                final_score()
                print("Draw")
            elif computer_score == 21:
                final_score()
                print("Computer has Blackjack, you lose!")
            elif current_score > computer_score:
                final_score()
                print("You Win!")
            elif computer_score > current_score and computer_score <= 21:
                final_score()
                print("You lose!")
            elif computer_score > 21:
                final_score()
                print("You Win!")
    else:
        continue_playing = False

