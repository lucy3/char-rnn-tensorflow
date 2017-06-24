"""
Convert joke jsons to a txt, 
where there is one joke per line. 

Filters out bad jokes (reddit score < 10, 
stupid stuff rating < 3).
"""
import json
import csv

all_jokes = set()
max_length = 1000

reddit_file = open("./reddit_jokes.json")
reddit = json.load(reddit_file)
for joke in reddit:
    if joke['score'] >= 10:
        j = joke['title'] + ' ' + joke['body']
        if len(j) <= max_length: 
            all_jokes.add(j)

stupid_file = open("./stupidstuff.json")
stupid = json.load(stupid_file)
for joke in stupid:
    if joke['rating'] >= 3:
        j = joke['body']
        if len(j) <= max_length: 
            all_jokes.add(j)

wocka_file = open("./wocka.json")
wocka = json.load(wocka_file)
for joke in wocka:
    j = joke['body']
    if len(j) <= max_length: 
        all_jokes.add(j)

with open("./shortjokes.csv", "r") as short_file:
    reader = csv.DictReader(short_file, delimiter=',') 
    for row in reader:
        j = row['Joke']
        if len(j) <= max_length: 
            all_jokes.add(j)

print "Num jokes:", len(all_jokes)
all_jokes.remove('')
all_jokes = list(all_jokes)
for i, joke in enumerate(all_jokes):
    all_jokes[i] = joke.ljust(max_length-len(joke))

output = open("../data/jokes/input.txt", "w")
for joke in all_jokes:
    output.write(joke.encode('ascii', 'ignore').decode('ascii'))
