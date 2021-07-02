# Mad Lib template - https://hobbylark.com/party-games/How-to-Make-Your-Own-Mad-Libs


def main():
    # Ask user for inputs (i.e. verb, noun, etc)
    # Assign inputs to variable
    adjective1 = input('Provide an adjective: ')
    adjective2 = input('Provide an adjective: ')
    type_of_bird = input('Provide a type of bird: ')
    room_in_a_house = input('Provide a room in a house: ')
    verb_past_tense = input('Provide a verb (past tense): ')
    verb2 = input('Provide a verb: ')
    relative_name = input('Provide a relative\'s name: ')
    noun1 = input('Provide a noun: ')
    liquid = input('Provide a liquid: ')
    verb_ending_in_ing1 = input('Provide a verb ending in -ing: ')
    part_of_the_body_plural = input('Provide a part of the body (plural): ')
    plural_noun = input('Provide a plural noun: ')
    verb_ending_in_ing2 = input('Provide a verb ending in -ing: ')
    noun3 = input('Provide a noun: ')

    # print out paragraph with user's inputs
    print(f'\nIt was a {adjective1}, cold November day. I\n'
          f'woke up to the {adjective2} smell of {type_of_bird}\n'
          f'roasting in the {room_in_a_house} downstairs. I\n'
          f'{verb_past_tense} down the stairs to see if I could\n'
          f'help {verb2} the dinner. My mom said,\n'
          f'"See if {relative_name} needs a fresh {noun1}. So I\n'
          f'carried a tray of glasses full of {liquid} into\n'
          f'the {verb_ending_in_ing1} room. When I got there, I\n'
          f'couldn\'t believe my {part_of_the_body_plural}! There were\n'
          f'{plural_noun} {verb_ending_in_ing2} on the {noun3}!')


if __name__ == '__main__':
    main()
