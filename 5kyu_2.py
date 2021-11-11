'''
Introduction
There is a war and nobody knows - the alphabet war!
There are two groups of hostile letters.
The tension between left side letters and right side letters
was too high and the war began. The letters have discovered a new unit -
a priest with Wo lo looooooo power.

Task
Write a function that accepts fight string consists of only small letters
and return who wins the fight. When the left side wins
return Left side wins!, when the right side wins return Right side wins!,
in other case return Let's fight again!.

The left side letters and their power:
 w - 4
 p - 3
 b - 2
 s - 1
 t - 0 (but it's priest with Wo lo loooooooo power)

The right side letters and their power:
 m - 4
 q - 3
 d - 2
 z - 1
 j - 0 (but it's priest with Wo lo loooooooo power)

The other letters don't have power and are only victims.

The priest units t and j change the adjacent letters
from hostile letters to friendly letters with the same power.
mtq => wtp
wjs => mjz

A letter with adjacent letters j and t is not converted i.e.:
tmj => tmj
jzt => jzt

The priests (j and t) do not convert the other priests ( jt => jt ).

Example
alphabet_war("z")         #=>  "z"  => "Right side wins!"
alphabet_war("tz")        #=>  "ts" => "Left side wins!"
alphabet_war("jz")        #=>  "jz" => "Right side wins!"
alphabet_war("zt")        #=>  "st" => "Left side wins!"
alphabet_war("azt")       #=> "ast" => "Left side wins!"
alphabet_war("tzj")       #=> "tzj" => "Right side wins!"
'''

def alphabet_war(fight):
    conv_of_t = {
        "m": "w",
        "q": "p",
        "d": "b",
        "z": "s"
        }
    conv_of_j = {
        "w": "m",
        "p": "q",
        "b": "d",
        "s": "z"
        }
    left_side = {
        "w": 4,
        "p": 3,
        "b": 2,
        "s": 1,
        "t": 0
        }
    right_side = {
        "m": 4,
        "q": 3,
        "d": 2,
        "z": 1,
        "j": 0
        }

    l_score = 0
    r_score = 0

    for l in range(len(fight)):
        if l > 0 and l < len(fight) - 1 and\
                ((fight[l - 1] == "t" and fight[l + 1] == "j") or (fight[l - 1] == "j" and fight[l + 1] == "t")):
            continue
        elif (l > 0 and fight[l - 1] == "t") or (l < len(fight) - 1 and fight[l + 1] == "t"):
            if fight[l] in right_side:
                fight = fight.replace(fight[l], conv_of_t[fight[l]], 1)
        elif (l > 0 and fight[l - 1] == "j") or (l < len(fight) - 1 and fight[l + 1] == "j"):
            if fight[l] in left_side:
                fight = fight.replace(fight[l], conv_of_j[fight[l]], 1)
        else:
            continue

    for let in fight:
        if let in left_side:
            l_score += left_side[let]
        elif let in right_side:
            r_score += right_side[let]
    if l_score > r_score:
        return "Left side wins!"
    elif r_score > l_score:
        return "Right side wins!"
    else:
        return "Let's fight again!"
