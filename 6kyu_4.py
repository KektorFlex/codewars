'''
Introduction
There is a war and nobody knows - the alphabet war!
There are two groups of hostile letters.
The tension between left side letters and right side letters
was too high and the war began. The letters called airstrike
to help them in war - dashes and dots are spreaded
everywhere on the battlefield.

Task
Write a function that accepts fight string consists of
only small letters and * which means a bomb drop place.
Return who wins the fight after bombs are exploded.
When the left side wins return Left side wins!,
when the right side wins return Right side wins!,
in other case return Let's fight again!.

The left side letters and their power:
 w - 4
 p - 3
 b - 2
 s - 1

The right side letters and their power:
 m - 4
 q - 3
 d - 2
 z - 1

The other letters don't have power and are only victims.
The * bombs kills the adjacent letters ( i.e. aa*aa => a___a, **aa** => ______ );

Example
AlphabetWar("s*zz");           //=> Right side wins!
AlphabetWar("*zd*qm*wp*bs*"); //=> Let's fight again!
AlphabetWar("zzzz*s*");       //=> Right side wins!
AlphabetWar("www*www****z");  //=> Left side wins!
'''

# замена символов
# выбрать между pop и replace
# к тому же строка не меняется
# и, мб, лучше перевести в список

'''VER 1.8 - not working'''
# def alphabet_war(fight):
#     left_score = 0
#     right_score = 0
#     left_side = {
#         "w": 4,
#         "p": 3,
#         "b": 2,
#         "s": 1
#     }
#     right_side = {
#         "m": 4,
#         "q": 3,
#         "d": 2,
#         "z": 1
#     }
#     for l in fight:                        # удаление перед и после '*'
#         if l == "*":
#             if fight.index(l) != 0 and fight.index(l) != len(fight) - 1:
#                 next_l = fight[fight.index(l) + 1]
#                 prev_l = fight[fight.index(l) - 1]
#                 if next_l != "*" and prev_l != "*":
#                     fight = fight.replace(prev_l, "_", 1)
#                     fight = fight.replace(next_l, "_", 1)
#                     fight = fight.replace(l, "_", 1)
#                 elif next_l == "*" and prev_l != "*":
#                     fight = fight.replace(prev_l, "_", 1)
#                     fight = fight.replace(l, "_", 1)
#                 elif next_l != "*" and prev_l == "*":
#                     fight = fight.replace(next_l, "_", 1)
#                     fight = fight.replace(l, "_", 1)
#                 else:
#                     fight = fight.replace(l, "_", 1)
#             elif fight.index(l) == 0 and fight[fight.index(l) + 1] != "*":
#                 if len(fight) != 1:
#                     fight = fight.replace(fight[1], "_", 1)
#                     fight = fight.replace(l, "_", 1)
#             elif fight.index(l) == 0 and fight[fight.index(l) + 1] == "*":
#                 fight = fight.replace(l, "_", 1)
#             elif fight.index(l) == len(fight) - 1 and fight[fight.index(l) - 1] != "*":
#                 if len(fight) != 1:
#                     fight = fight.replace(fight[fight.index(l) - 1], "_", 1)
#                     fight = fight.replace(l, "_", 1)
#
#     for l in fight:                         #подсчёт очков
#         if l in left_side:
#             left_score += left_side[l]
#         elif l in right_side:
#             right_score += right_side[l]
#     if left_score > right_score:
#         print("Left side wins!" + fight)
#     elif right_score > left_score:
#         print("Right side wins!" + fight)
#     elif right_score == left_score:
#         print("Let's fight again!" + fight)
#
# alphabet_war("d*agsz***s*z*mw*szzdb*wzpwq")

'''VER 2.4 - not working'''
# def alphabet_war(fight):
#     left_score = 0
#     right_score = 0
#     left_side = {
#         "w": 4,
#         "p": 3,
#         "b": 2,
#         "s": 1
#     }
#     right_side = {
#         "m": 4,
#         "q": 3,
#         "d": 2,
#         "z": 1
#     }
#     start = 0
#     battle = []
#     if len(fight) != 1:
#         for l in fight:
#             if fight.index(l) != 0 and fight.index(l) != len(fight) - 1:
#                 if fight[fight.index(l, start) + 1] == "*" and l != "*":
#                     start = fight.index(l)
#                     fight = fight.replace(l, "_", 1)
#                 elif fight[fight.index(l, start) - 1] == "*" and l != "*":
#                     start = fight.index(l)
#                     fight = fight.replace(l, "_", 1)
#             elif fight.index(l, start) == 0:
#                 if fight[fight.index(l, start) + 1] == "*" and l != "*":
#                     start = fight.index(l)
#                     fight = fight.replace(l, "_", 1)
#             elif fight.index(l) == len(fight) - 1:
#                 if fight[fight.index(l, start) - 1] == "*" and l != "*":
#                     start = fight.index(l)
#                     fight = fight.replace(l, "_", 1)
#             # else:
#             #     battle.append(l)
#             #     fight = fight.replace(l, "_", 1)
#
#     for l in fight:                         #подсчёт очков
#         if l in left_side:
#             left_score += left_side[l]
#         elif l in right_side:
#             right_score += right_side[l]
#     if left_score > right_score:
#         print("Left side wins!" + fight)
#     elif right_score > left_score:
#         print("Right side wins!" + fight)
#     elif right_score == left_score:
#         print("Let's fight again!" + fight)
#
# alphabet_war("sc**bdfdz*pf*pz*wmcz*pp*c")

'''VER 3.3 - OK'''
def alphabet_war(fight):
    left_score = 0
    right_score = 0
    left_side = {
        "w": 4,
        "p": 3,
        "b": 2,
        "s": 1
    }
    right_side = {
        "m": 4,
        "q": 3,
        "d": 2,
        "z": 1
    }

    battle = []
    for l in fight:
        if len(fight) == 1:
            battle.append(l)
            fight = fight.replace(l, "_", 1)
        else:
            if fight.index(l) == 0:
                if fight[fight.index(l) + 1] == "*" and l != "*":
                    fight = fight.replace(l, "_", 1)
                elif fight[fight.index(l) + 1] != "*" and l != "*":
                    battle.append(l)
                    fight = fight.replace(l, "_", 1)
            elif fight.index(l) == len(fight) - 1:
                if fight[fight.index(l) - 1] == "*" and l != "*":
                    fight = fight.replace(l, "_", 1)
                elif fight[fight.index(l) - 1] != "*" and l != "*":
                    battle.append(l)
                    fight = fight.replace(l, "_", 1)
            else:
                if fight[fight.index(l) + 1] == "*" and l != "*":
                    fight = fight.replace(l, "_", 1)
                elif fight[fight.index(l) - 1] == "*" and l != "*":
                    fight = fight.replace(l, "_", 1)
                elif fight[fight.index(l) + 1] != "*" and l != "*":
                    battle.append(l)
                    fight = fight.replace(l, "_", 1)
                elif fight[fight.index(l) - 1] != "*" and l != "*":
                    battle.append(l)
                    fight = fight.replace(l, "_", 1)

    for s in battle:                         #подсчёт очков
        if s in left_side:
            left_score += left_side[s]
        elif s in right_side:
            right_score += right_side[s]
    if left_score > right_score:
        print("Left side wins!" + str(battle))
    elif right_score > left_score:
        print("Right side wins!" + str(battle))
    elif right_score == left_score:
        print("Let's fight again!" + str(battle))

alphabet_war("zz*zzs")

'''Like this solution'''
# def alphabet_war(fight):
#     ls_map = {'w': 4, 'p': 3, 'b': 2, 's': 1}
#     rs_map = {'m': 4, 'q': 3, 'd': 2, 'z': 1}
#     ls_score = 0
#     rs_score = 0
#     for i in range(len(fight)):
#         if (i > 0 and fight[i - 1] == '*') or (i < len(fight) - 1 and fight[i + 1] == '*'):
#             continue
#         else:
#             if fight[i] in ls_map:
#                 ls_score += ls_map[fight[i]]
#             if fight[i] in rs_map:
#                 rs_score += rs_map[fight[i]]
#     if ls_score > rs_score:
#         return "Left side wins!"
#     elif ls_score < rs_score:
#         return "Right side wins!"
#     else:
#         return "Let's fight again!"

'''Best on codewars'''
# import re                                                 #?????????
#
# powers = {
#     'w': -4, 'p': -3, 'b': -2, 's': -1,
#     'm': +4, 'q': +3, 'd': +2, 'z': +1,
# }
#
# def alphabet_war(fight):
#     fight = re.sub('.(?=\*)|(?<=\*).', '', fight)         #?????????
#     result = sum(powers.get(c, 0) for c in fight)
#     if result < 0:
#         return 'Left side wins!'
#     elif result > 0:
#         return 'Right side wins!'
#     else:
#         return "Let's fight again!"