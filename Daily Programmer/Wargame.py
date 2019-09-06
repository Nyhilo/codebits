def war(challengeInput):
    [deck1, deck2] = challengeInput.splitlines()
    deck1 = map(int, deck1.split())
    deck2 = map(int, deck2.split())

    running = True
    winner = 0
    while running:
        # Play your cards
        card1 = deck1.pop(0)
        card2 = deck2.pop(0)

        # Check for Clear Winner
        if card1 > card2:
            deck1.append(card1)
            deck1.append(card2)
        elif card1 < card2:
            deck2.append(card2)
            deck2.append(card1)
        else: # Ladies and Lads we have a tie!
            result = makewar(deck1, deck2)
            # A tied game skips this part and concludes on the next block down
            if result == "deck1":
                deck1.append(card1)
                deck1.append(card2)
            elif result == "deck2":
                deck2.append(card2)
                deck2.append(card1)

        # Check for Win condition
        if len(deck1) == 0 and len(deck2) == 0:
            winner = 0
            running = False
        elif len(deck1) == 0:
            winner = 2
            running = False
        elif len(deck2) == 0:
            winner = 1
            running = False

    return winner

def makewar(deck1, deck2):
    # Check for eligibility
    if len(deck1) == 0 and len(deck2) == 0:
        return "tie"
    elif len(deck1) == 0:
        return "deck2"
    elif len(deck2) == 0:
        return "deck1"

    # Iterative popping
    popAmount = 3
    if min(len(deck1), len(deck2)) < 4:
        # That -1 is reserved for the cards that get compared
        popAmount = min(len(deck1), len(deck2))-1

    # Pop some soldiers
    soldiers1 = []
    soldiers2 = []
    for i in range(popAmount):
        soldiers1.append(deck1.pop(0))
        soldiers2.append(deck2.pop(0))

    card1 = deck1.pop(0)
    card2 = deck2.pop(0)

    # Check for Clear Winner
    if card1 > card2:
        deck1.extend(soldiers1)
        deck1.append(card1)
        deck1.extend(soldiers2)
        deck1.append(card2)
        return "deck1"
    elif card2 > card1:
        deck2.extend(soldiers2)
        deck2.append(card2)
        deck2.extend(soldiers1)
        deck2.append(card1)
        return "deck2"
    else: # Recursive tieing!
        result = makewar(deck1, deck2)
        if result == "tie":
            return "tie"
        elif result == "deck1":
            deck1.extend(soldiers1)
            deck1.append(card1)
            deck1.extend(soldiers2)
            deck1.append(card2)
            return "deck1"
        elif result == "deck2":
            deck2.extend(soldiers2)
            deck2.append(card2)
            deck2.extend(soldiers1)
            deck2.append(card1)
            return "deck2"



output = [war("5 1 13 10 11 3 2 10 4 12 5 11 10 5 7 6 6 11 9 6 3 13 6 1 8 1 \n9 12 8 3 11 10 1 4 2 4 7 9 13 8 2 13 7 4 2 8 9 12 3 12 7 5"),
            war("3 11 6 12 2 13 5 7 10 3 10 4 12 11 1 13 12 2 1 7 10 6 12 5 8 1 \n9 10 7 9 5 2 6 1 11 11 7 9 3 4 8 3 4 8 8 4 6 9 13 2 13 5 "),
            war("1 2 3 4 5 6 7 8 9 10 11 12 13 1 2 3 4 5 6 7 8 9 10 11 12 13 \n1 2 3 4 5 6 7 8 9 10 11 12 13 1 2 3 4 5 6 7 8 9 10 11 12 13 ")]

print(output)

# output = war("3 11 6 12 2 13 5 7 10 3 10 4 12 11 1 13 12 2 1 7 10 6 12 5 8 1 \n9 10 7 9 5 2 6 1 11 11 7 9 3 4 8 3 4 8 8 4 6 9 13 2 13 5 ")
