import random

def create_deck():
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    return [{'rank': rank, 'suit': suit} for suit in suits for rank in ranks]

def card_value(card):
    if card['rank'] in ['J', 'Q', 'K']:
        return 10
    elif card['rank'] == 'A':
        return 11
    return int(card['rank'])

def calculate_hand(hand):
    val = sum(card_value(c) for c in hand)
    aces = sum(1 for c in hand if c['rank'] == 'A')
    while val > 21 and aces:
        val -= 10
        aces -= 1
    return val

def format_card(card):
    return f"{card['rank']} of {card['suit']}"

def display_hand(name, hand, hide_first=False):
    if hide_first:
        print(f"{name}'s Hand: [Hidden Card], {format_card(hand[1])}")
    else:
        cards_str = ", ".join(format_card(c) for c in hand)
        print(f"{name}'s Hand: {cards_str} (Total: {calculate_hand(hand)})")

def deal_initial(deck):
    return [deck.pop(), deck.pop()]

def player_turn(deck, player_hand):
    while True:
        display_hand("Player", player_hand)
        val = calculate_hand(player_hand)
        if val >= 21:
            break
        choice = input("Do you want to (H)it or (S)tand? ").strip().lower()
        if choice == 'h':
            player_hand.append(deck.pop())
        elif choice == 's':
            break
        else:
            print("Invalid input. Type H or S.")
    return calculate_hand(player_hand)

def dealer_turn(deck, dealer_hand):
    while calculate_hand(dealer_hand) < 17:
        dealer_hand.append(deck.pop())
    return calculate_hand(dealer_hand)

def play_round(deck):
    player_hand = deal_initial(deck)
    dealer_hand = deal_initial(deck)
    display_hand("Dealer", dealer_hand, hide_first=True)
    
    p_total = player_turn(deck, player_hand)
    if p_total > 21:
        print("\nPlayer Busted! You lose.")
        return -1
        
    print("\nDealer's turn...")
    d_total = dealer_turn(deck, dealer_hand)
    display_hand("Dealer", dealer_hand)
    
    if d_total > 21:
        print("\nDealer Busted! You win!")
        return 1
    elif p_total > d_total:
        print(f"\nYou win! ({p_total} vs {d_total})")
        return 1
    elif d_total > p_total:
        print(f"\nDealer wins! ({d_total} vs {p_total})")
        return -1
    else:
        print(f"\nPush! It's a tie. ({p_total} vs {d_total})")
        return 0

def main():
    print("--- WELCOME TO CONSOLE BLACKJACK ---")
    deck = create_deck()
    random.shuffle(deck)
    score = 0
    
    while True:
        if len(deck) < 10:
            print("\nReshuffling new deck...")
            deck = create_deck()
            random.shuffle(deck)
            
        print(f"\nCurrent Score: {score}")
        result = play_round(deck)
        score += result
        
        again = input("\nPlay another hand? (Y/N): ").strip().lower()
        if again != 'y':
            break
            
    print(f"\nFinal Score: {score}. Thanks for playing!")

if __name__ == '__main__':
    main()