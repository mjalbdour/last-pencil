
MSG_YOUR_TURN = "Your turn!"
MSG_PENCILS = "How many pencils would you like to use:"
MSG_PLAYER_ORDER = "Who will be the first"

name1, name2 = "Player 1", "Player 2"

# turn = input()
print(MSG_PENCILS)
pencils_count = int(input())
pencils = "|" * pencils_count

print(f'{MSG_PLAYER_ORDER} ({name1}, {name2}):')
name = input()
print(pencils)
print(f'{name} is going first!')
