import random as r
import os

class Dealer:
    def __init__(self,):
        self.name = "Диллер"
        self.hand = []
        self.points = 0
        pass

    def count_points(self):
        self.points = 0
        for i in range(0, len(self.hand)):
            pictures = 'JQKA'
            if str(self.hand[i]) in pictures:
                if self.hand[i] == 'A':
                    if self.points > 10:
                        self.points += 1
                    else:
                        self.points += 10
                else:
                    self.points += 10
            else:
                self.points += int(self.hand[i])

    def take_cards(self,deck):
        self.count_points()
        while self.points<18: 
            self.hand.append(deck.give_card())
            self.count_points()
        pass
    
    def refresh(self):
        self.hand = []
        self.points = 0
        pass
    
    def __str__(self):
        return f"Рука Диллера :{self.hand[0]}, ?"
    
class Player:
    def __init__(self,name):
        self.name = name
        self.hand = []
        self.points = 0
        self.win_streak=0
        pass

    def count_points(self):
        self.points = 0
        for i in range(0, len(self.hand)):
            pictures = 'JQKA'
            if str(self.hand[i]) in pictures:
                if self.hand[i] == 'A':
                    if self.points > 10:
                        self.points += 1
                    else:
                        self.points += 10
                else:
                    self.points += 10
            else:
                self.points += int(self.hand[i])

    def take_cards(self,deck):
        while True:
            self.count_points()
            if self.points>21:
                print(f"Перебор, у вас {player.points} очков")
                break
            print(f'У вас {self.points} очков')
            print('Возьмёте карту?(y|n)')
            choice = input() 
            if choice=='y' or choice=='n':
                if choice=='y': 
                    self.hand.append(deck.give_card())
                elif choice == 'n': break
            else:
                print('Нормально пиши, даун')
                pass 

    def refresh(self):
        self.hand = []
        self.points = 0
        pass
    
    def __str__(self):
        return f"Имя игрока = {self.name}, рука :{self.hand}"



class Deck:
    def __init__(self):
        self.cards = [2,3,4,5,6,7,8,9,10,'J','Q','K','A']*4
        pass
    
    def shuffle(self):
        r.shuffle(self.cards) 
        pass
    
    def refresh(self):
        self.cards = [2,3,4,5,6,7,8,9,10,'J','Q','K','A']*4
        pass
    
    def __str__(self):
        return str(self.cards)
    
    def give_card (self):
       return self.cards.pop(0)

def clear_terminal():
    os.system('cls')

        
#Инициализация  объектов     
print("Введите имя игрока")
player = Player(input())
dealer = Dealer()
deck = Deck()


while True:
    
    #Мешаем карты
    deck.shuffle()
    
    #Выдаём стартовую руку
    player.hand.append(deck.give_card())
    player.hand.append(deck.give_card())
    dealer.hand.append(deck.give_card())
    dealer.hand.append(deck.give_card())
    print(dealer)

    #Пускай здесь набирают карты
    player.take_cards(deck)
    dealer.take_cards(deck)

    #Выбираем победителя
    if player.points<=21 and dealer.points<=21:
        if player.points>dealer.points:
            print(f"{player.name} выиграл")
            player.win_streak+=1
        elif player.points<dealer.points:
            player.win_streak=0
            print(f"{dealer.name} выиграл, его счёт равен {dealer.points}")
        else:
            print("Ничья")

    elif player.points>21 and dealer.points>21:
        if player.points<dealer.points:
            print(f"{player.name} выиграл")
            player.win_streak+=1
        elif player.points>dealer.points:
            player.win_streak=0
            print(f"{dealer.name} выиграл, его счёт равен {dealer.points}")
        else:
            print("Ничья")

    else:
        if dealer.points>21 and player.points<=21:
            player.win_streak+=1
            print(f"{player.name} выиграл, у диллера перебор")
        elif dealer.points<=21 and player.points>21:
            print(f"{dealer.name} выиграл, его счёт равен {dealer.points}")
            player.win_streak=0

    print(player.points,player.hand)
    print(dealer.points,dealer.hand)

    print(f"Хотите продолжить?(y|n), стрик:{player.win_streak}")
    descision = input()
    if descision=='y' or descision=='n':
        if descision=='y':
            player.refresh()
            dealer.refresh()
            deck.refresh()
            clear_terminal()
            pass
        else:break
    else:
        print("Даун ебанный, писать научишься перезвонишь")
        break
