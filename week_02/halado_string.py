#!/usr/bin/env python3

def main():
    header_info = ['Original Game', 'Year', 'Remake', 'Year']

    games_info = [('Gruntz', 1999, 'Gruntz Unityverse', 'TBA'),
                  ('The Binding of Isaac', 2011, 'The Binding of Isaac: Rebirth', 2014),
                  ('Shadow of the Colossus', 2005, 'Shadow of the Colossus', 2018),
                  ('Dead Space', 2009, 'Dead Space', 2023),
                  ('Half-Life', 1998, 'Black Mesa', 2020)]

    pretty_print(header_info, games_info)

def pretty_print(header, data):
    print ("| {0:30} | {1:<5} || {2:30} | {3:<5} |".format(header[0], header[1], header[2], header[3]))
    print_char_line('#', 83)
    for game in data:
        print ("| {0:30} | {1:<5} || {2:30} | {3:<5} |".format(game[0], game[1], game[2], game[3]))
        print_char_line('-', 83)

def print_char_line(len, char):
    print(char * len)

if __name__ == '__main__':
    main()
