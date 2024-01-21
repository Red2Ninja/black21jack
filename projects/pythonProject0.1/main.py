# BLACKJACK
import data
import random

cont = True
while cont == True:
    play = input("type y to play blackjack else type n to exit: ").lower()
    if play == 'n':
        cont = False
    elif play == 'y':
        print(data.logo)
        you_card_lst = []
        Dlr_card_lst = []
        card_lst = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        card_dict = {'A': 0, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10,
                     'K': 10}
        frst_card = random.choice(card_lst)
        scnd_card = random.choice(card_lst)

        Dfrst_card = random.choice(card_lst)

        you_card_lst.append(frst_card)
        you_card_lst.append(scnd_card)
        Dlr_card_lst.append(Dfrst_card)

        print("Your cards are: ", you_card_lst)
        if frst_card == scnd_card == 'A':
            card_dict['A'] = 12
        elif frst_card == 'A' or scnd_card == 'A':
            A_val = int(input("What value of A do you want to use: 1 or 11? "))
            card_dict['A'] = A_val

        print("Score: ", (card_dict[frst_card] + card_dict[scnd_card]))
        print("The dealers first card is: ", Dfrst_card)

        if (card_dict[frst_card] + card_dict[scnd_card]) == 21:
            print("It's a blackjack...You win!")
            break
        order = 2
        Y = True
        while Y == True:
            thrd_card_choose = input("type y if you want to pick one more card else type n?").lower()
            if thrd_card_choose == 'n':
                Y = False
            if thrd_card_choose == 'y':

                you_card_lst.append(random.choice(card_lst))
                print("The next card is: ", you_card_lst[order])
                if you_card_lst[order] == 'A':
                    A_val = int(input("What value of A do you want to use: 1 or 11? "))
                    card_dict['A'] = A_val
                sum1 = 0
                for i in you_card_lst:
                    for key in card_dict:
                        if i == key:
                            sum1 += card_dict[key]
                print("Score:", sum1)
                if sum1 > 21:
                    print("you lose!")
                    Y = False

                elif sum1 == 21:
                    print("It's a blackjack...you win!.")
                    Y = False
                elif sum1 < 21:
                    Y = True
                order += 1

        sum2 = 0
        for i in you_card_lst:
            for key in card_dict:
                if i == key:
                    sum2 += card_dict[key]
        #print("Your score is: ",sum2)
        if sum2 < 21:
            Dsum = card_dict[Dfrst_card]
            if Dfrst_card == 'A':
                Dsum += 11
            order2 = 1
            X = True
            while X == True:

                Dlr_card_lst.append(random.choice(card_lst))
                if (card_dict[Dfrst_card] + card_dict[Dlr_card_lst[1]]) == 21:
                    print("It's a blackjack...The dealer wins!.")
                    break
                else:
                    print("The dealer's next card is: ", Dlr_card_lst[order2])
                    if Dlr_card_lst[order2] == 'A':
                        if (card_dict[Dfrst_card] + 11) < 21:
                            Dsum = (card_dict[Dfrst_card] + 11)
                        else:
                            Dsum = (card_dict[Dfrst_card] + 1)
                    else:
                        Dsum += card_dict[Dlr_card_lst[order2]]
                    if 16 < Dsum < 21:
                        if sum2 == Dsum:
                            print("Dealer's Score: ", Dsum)
                            print("It's a draw!")
                            X = False
                        elif sum2 > Dsum:
                            print("Dealer's Score: ", Dsum)
                            print("You Win!")
                            X = False
                        elif sum2 < Dsum:
                            print("Dealer's Score: ", Dsum)
                            print("you lose!")
                            X = False
                    elif Dsum == 21:
                        print("Dealer's Score: ", Dsum)
                        print("It's a blackjack!...dealer wins!")
                        break
                    elif Dsum > 21:
                        print("Dealer's Score: ", Dsum)
                        print("You win!")
                        break

                    else:
                        print("Dealer's Score: ", Dsum)
                        continue














