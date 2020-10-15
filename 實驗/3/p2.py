import random

def Cards():
    Flowers=['spade','heart','club','diamond']
    Numbers=['A','2','3','4','5','6','7','8','9','10','J','Q','K']
    Cards=['JOKER','joker']
    for i in Flowers:
        for j in Numbers:
            Cards.append(i+j)
    
    return Cards  #創建牌組


def SendCards():
    UsersCard=Cards()
    random.shuffle(UsersCard)  #洗牌
    Under_table=UsersCard[0:3]
    player1=UsersCard[3:20]
    player2=UsersCard[20:37]
    player3=UsersCard[37:54]

    return player1,player2,player3,Under_table


player1_Card,__,__,__=SendCards()
__,player2_Card,__,__=SendCards()
__,__,player3_Card,__=SendCards()
__,__,__,Under_table=SendCards()

print('Player1:',player1_Card,'   TOTAL:',len(player1_Card))
print('Player2:',player2_Card,'   TOTAL:',len(player2_Card))
print('Player3:',player3_Card,'   TOTAL:',len(player1_Card))
print('Under table:',Under_table)