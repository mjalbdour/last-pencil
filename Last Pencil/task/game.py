
MSG_YOUR_TURN = "Your turn!"
MSG_PENCILS = "How many pencils would you like to use:"
MSG_PLAYER_ORDER = "Who will be the first"
MSG_TURN = "turn:"
MSG_WON = "won!"

# TODO: USE THESE IN CUSTOM EXCEPTIONS
MSG_ERROR_FORMAT_PENCILS = "The number of pencils should be numeric"
MSG_ERROR_ZERO_PENCILS = "The number of pencils should be positive"
MSG_ERROR_UNKNOWN_PLAYER = "Choose between"  # *Name1* and *Name2*
MSG_ERROR_POSSIBLE_VALUES = "Possible values: '1', '2', '3'"
MSG_ERROR_TOO_MANY_PENCILS = "Too many pencils were taken"


name1, name2 = "John", "Jack"


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


print(MSG_PENCILS)
total_pencils = int(input_pencils(starting=True))
name = choose_starting_player()
current_pencils = int(total_pencils)
while current_pencils > 0:
    if current_pencils < total_pencils:
        name = switch_turns(name)
    pencils = "|" * current_pencils
    print(pencils)
    print(f"{name}'s {MSG_TURN}")
    pencils_per_turn = int(input_pencils(current_pencils_=current_pencils))
    current_pencils -= pencils_per_turn
else:
    name = switch_turns(name)
    print(f'{name} {MSG_WON}')
