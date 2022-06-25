
# TODO: EXTRACT TO CONSTANTS FILE
MSG_YOUR_TURN = "Your turn!"
MSG_PENCILS = "How many pencils would you like to use:"
MSG_PLAYER_ORDER = "Who will be the first"
MSG_TURN = "turn:"
MSG_WON = "won!"

# TODO: USE IN CUSTOM EXCEPTIONS
MSG_ERROR_FORMAT_PENCILS = "The number of pencils should be numeric"
MSG_ERROR_ZERO_PENCILS = "The number of pencils should be positive"
MSG_ERROR_UNKNOWN_PLAYER = "Choose between"  # *Name1* and *Name2*
MSG_ERROR_POSSIBLE_VALUES = "Possible values: '1', '2', '3'"
MSG_ERROR_TOO_MANY_PENCILS = "Too many pencils were taken"

name1, name2 = "John", "Jack"

cached_range = set(range(1, 1000, 4))


# TODO: EXTRACT LOGIC INTO CLASSES
def switch_turns(p):
    if p == name1:
        return name2
    return name1


def input_pencils(starting=False, current_pencils_=None):
    while True:
        pencils_ = input()
        if pencils_ not in {'1', '2', '3'} and not starting:
            print(MSG_ERROR_POSSIBLE_VALUES)
        elif not pencils_.isnumeric():
            print(MSG_ERROR_FORMAT_PENCILS)
        elif int(pencils_) <= 0:
            print(MSG_ERROR_ZERO_PENCILS)
        elif current_pencils_ and int(pencils_) > int(current_pencils_):
            print(MSG_ERROR_TOO_MANY_PENCILS)
        else:
            return pencils_


def choose_starting_player():
    print(f'{MSG_PLAYER_ORDER} ({name1}, {name2}):')
    while True:
        name_ = input()
        if name_ not in {name1, name2}:
            print(f'{MSG_ERROR_UNKNOWN_PLAYER} {name1} and {name2}')
        else:
            return name_


def generate_bot_pick(current_pencils_):
    if current_pencils_ in {2, 3, 4}:
        return current_pencils_ - 1
    elif current_pencils_ in cached_range:
        return 1
    elif current_pencils_ not in cached_range:
        if current_pencils_ - 3 in cached_range:
            return 3
        elif current_pencils_ - 2 in cached_range:
            return 2
        else:
            return 1


print(MSG_PENCILS)
total_pencils = int(input_pencils(starting=True))

name = choose_starting_player()
bot = name2

current_pencils = int(total_pencils)
while current_pencils > 0:
    print("|" * current_pencils)
    print(f"{name}'s {MSG_TURN}")

    if bot == name:
        bot_pick = generate_bot_pick(current_pencils)
        print(bot_pick)
        current_pencils -= bot_pick
    else:
        current_pencils -= int(input_pencils(current_pencils_=current_pencils))

    name = switch_turns(name)
else:
    print(f'{name} {MSG_WON}')
