'''
It's Christmas! You had to wait the whole year for this moment.
You can already see all the presents under the Christmas tree.
But you have to wait for the next morning in order to unwrap them.
You really want to know, what's inside those boxes.
But as a clever child, you can do your assumptions already.

You know, you were a good child this year.
So you may assume, that you'll only get things from your wishlist.
You see those presents, you can lift them and you can shake them a bit.
Now you can make you assumptions about what you'll get.

Your Task
You will be given a wishlist (array), containing all possible items.
Each item is in the format:
{name: "toy car", size: "medium", clatters: "a bit", weight: "medium"}
(Ruby version has an analog hash structure, see example below)

You also get a list of presents (array), you see under the christmas tree,
which have the following format each:
{size: "small", clatters: "no", weight: "light"}

Your task is to return the names of all wishlisted presents
that you might have gotten.

Rules
Possible values for size: "small", "medium", "large"
Possible values for clatters: "no", "a bit", "yes"
Possible values for weight: "light", "medium", "heavy"
Don't add any item more than once to the result
The order of names in the output doesn't matter
It's possible, that multiple items from your wish list
have the same attribute values.
If they match the attributes of one of the presents, add all of them.

Example
wishlist = [{'name': "mini puzzle", 'size': "small", 'clatters': "yes", 'weight': "light"},
            {'name': "toy car", 'size': "medium", 'clatters': "a bit", 'weight': "medium"},
            {'name': "card game", 'size': "small", 'clatters': "no", 'weight': "light"}]
presents = [{'size': "medium", 'clatters': "a bit", 'weight': "medium"},
            {'size': "small", 'clatters': "yes", 'weight': "light"}]

guess_gifts(wishlist, presents) # => must return ["Toy Car", "Mini Puzzle"]
'''

def guess_gifts(wishlist, presents):
    list = []
    for present in presents:
        for wish in wishlist:
            if present["size"] == wish["size"] and present["clatters"] == wish["clatters"] and present["weight"] == wish["weight"]:
                if wish["name"] not in list:
                    list.append(wish["name"])
    return list