
MSG_YOUR_TURN = "Your turn!"
MSG_PENCILS = "How many pencils would you like to use:"
MSG_PLAYER_ORDER = "Who will be the first"
MSG_TURN = "turn:"

name1, name2 = "John", "Jack"


def switch_turns(p):
    if p == name1:
        return name2
    return name1


print(MSG_PENCILS)
total_pencils = int(input())
current_pencils = total_pencils
print(f'{MSG_PLAYER_ORDER} ({name1}, {name2}):')
name = input()
while current_pencils > 0:
    if current_pencils < total_pencils:
        name = switch_turns(name)
    pencils = "|" * current_pencils
    print(pencils)
    print(f"{name}'s {MSG_TURN}")
    pencils_per_turn = int(input())
    current_pencils -= pencils_per_turn
