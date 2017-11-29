import card
from card import buildPoker
from card import shuffle
from player import player
from player import displayCards


def cardDistributor(poker, players):
    cardsPerPlayer = len(poker) / len(players)
    for index in range(len(players)):
        players[index].cards = poker[0 + index * cardsPerPlayer: (index + 1) * cardsPerPlayer]
    return players

def addPlayers():
    print '****** Code here *****'

def delPlayer():
    print '****** Code here *****'

def start():
    print '****** Code here *****'

def nextplayer():
    print '****** Code here *****'

def end():
    print '****** Who is the winner ******'


