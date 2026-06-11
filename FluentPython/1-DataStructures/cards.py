#!/usr/bin/env python3

"""
1.2 纸牌游戏
"""

import collections
from random import choice

# 单张纸牌类
# rank: 点数, suit: 花色
Card = collections.namedtuple('Card', ['rank', 'suit'])

graphs = dict(spades='♠️', hearts='♥️', diamonds='♦️', clubs='♣️')

def print_card(card):
    print(f'{graphs[card.suit]}, {card.rank}')

# 法国纸牌, 52张, 没有鬼牌(大小王)
class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()
    

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                                        for rank in self.ranks]

    def __len__(self):
        return len(self._cards)
    
    def __getitem__(self, pos):
        return self._cards[pos]

beer_card = Card('7', 'diamonds')
print(beer_card)
print_card(beer_card)
print('-' * 16)

deck = FrenchDeck()
# FrenchDeck实现了__len__方法, 可供框架len()方法调用
print(len(deck))
print('-' * 16)

# FrenchDeck实现了__getitem__方法, 支持了array[index]语法
print(deck[0])
print(deck[-1])
print('-' * 16)

# FrenchDeck实际上实现了序列类, _cards本身就是个list choice(),
# 所以可以通过choice()进行随机抽牌(choice参数是非空的序列)
print(choice(deck))
print(choice(deck))
print(choice(deck))
print('-' * 16)

# 因为是序列, 所以支持迭代
for card in deck:
    print(card)
print('-' * 16)

# 纸牌支持排序
# 排序的大小依据是"点数+花色". 花色值从大到小依次是: 黑桃, 红桃, 方块, 梅花
suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)

# FrenchDeck的ranks是从'2','3' ... 'J','Q','K','A'这样的字符串list,
# 通过index()能求出字符串对应的整数值下标, 做为点数使用, 然后再加上花色值权重.
def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    # print(f'card: {card}, rank_value: {rank_value}')
    return rank_value * len(suit_values) + suit_values[card.suit]

for card in sorted(deck, key=spades_high):
    print(card)

