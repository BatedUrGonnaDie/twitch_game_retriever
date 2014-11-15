#! /usr/bin/python2.7
# -*- coding: utf-8 -*-

# This script takes a very long time to run, do not start it if you do not have over 30 minutes to spare
# Select the save type, and then it will just run until it runs out of games to find
# Twitch uses giantbomb to generate their games, so this will retrieve them all from the source
# Script sleeps so you do not spam their api as hard, but it is the part reason for how long it takes

import requests
import time
import json
import os

games = []
offset = 0
api_key = os.environ["gb_api_key"] #giantbomb api key

while True:
    save_type = raw_input("How would you like to save the data (txt/json)? ")
    if save_type.lower() == "txt" or save_type.lower() == "json":
        break

while True:
    print offset # I use this as a measure to see how much longer it might take
    try:
        url = "http://www.giantbomb.com/api/games/?api_key={}&format=json&offset={}".format(api_key, offset)
        data = requests.get(url).json()
    except:
        time.sleep(20) # If something goes wrong try the same call in 20 seconds

    if data['results']:
        for i in data['results']:
            games.append(i['name'])
        offset += 100
    else:
        break


    time.sleep(1)

#sort alphabetically
dump = sorted(games)

if save_type == "txt":
    with open("games_list.txt", 'w') as dump_file:
        for i in dump:
            string_to_dump = i.encode("utf-8") + '\n'
            dump_file.write(string_to_dump)
else:
    with open("games_list.json", 'w') as dump_file:
        json.dump(dump, dump_file, sort_keys = True, indent = 4, ensure_ascii=False, encoding = "utf-8")

raw_input("All done, hit enter to conitnue.")
