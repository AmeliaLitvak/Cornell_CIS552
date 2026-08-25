"""
Module for scoring blackjack hands.

In blackjack, face cards are worth 10, number cards are worth their value, and Aces
are worth either 1 or 11, whichever is more advantageous. The latter is what makes
scoring blackjack so tricky.

In this module, we assume that a card hand is represented by a tuple of strings, where
each string is two characters representing a card.  The first character is the rank of
the card: '2'-'9' for numerical cards, 'T' for 10, 'J' for Jack, 'Q' for Queen, 'K' for
King and 'A' for Ace.  The second character is the suit: 'H' for hearts, 'D' for diamonds,
'C' for clubs, and 'S' for spades.

For example ('KS','AD') is a blackjack hand with the King of Spades and Ace of Diamonds.

Author:Amelia Litvak
Date: 08/15/2025
"""
import introcs


def bjack(hand):
    """
    Returns the score of the blackjack hand.
    
    When scoring the hand, number cards are always worth their value and face cards
    (Jack, Queen, King) are always worth 10.  However, Aces are either worth 1 or 11,
    which ever is more advantageous.
    
    When determining how to value a hand, the score should be as high as possible without
    going over 21.  If the hand is worth more than 21 points, then all Aces should be
    worth 1 point.
    
    Examples:
        bjack(('KS','AD')) returns 21
        bjack(('KS','9C','AD')) returns 20
        bjack(('AS','AC','KH')) returns 12
        bjack(('AS','AC','KH','TD')) returns 22
        bjack(()) returns 0
    
    Parameter hand: the blackjack hand to score
    Precondition: hand is a (possibly empty) tuple of 2-character strings representing 
    cards. The first character of each string is '2'-'9', 'T', 'J', 'Q', 'K', or 'A'. 
    The second character of each string is 'H', 'D', 'C', or 'S'.
    """
    # Hint: Keep track of whether you have seen any aces in the hand that are worth 11
    # If so, subtract 10 from the accumulator if you go over.
    score = 0
    ace_count = 0
    x = 0
    while x < len(hand):
        face = hand[x][0]
        if face in ('J','Q','K','T'):
            score = score + 10
        elif face == ('A'):
            score = score + 11
            ace_count = ace_count + 1
        else:
            score = score + int(face)
        x = x + 1

    while score > 21 and ace_count > 0:
        score = score - 10
        ace_count = ace_count - 1

    return score