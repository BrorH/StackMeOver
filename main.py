#!/usr/bin/env python3
from googlesearch import search
from bs4 import BeautifulSoup
import os 
import requests
import sys
import argparse


parser = argparse.ArgumentParser(description='Executes the first StackOverflow code snippet matching your query')
parser.add_argument('query', metavar='query', type=str, nargs=1,help='The query you wish to search for')
parser.add_argument('--y', action="store_true", help="YOLO mode - runs the retrieved command without asking for confirmation or even telling you what it is")
args = parser.parse_args()

query = args.query[0]
print(f"Querying '{query}'")

for url in search(f"{query} site:stackoverflow.com"):
    r = requests.get(url)

soup = BeautifulSoup(r.text, features="lxml")
answer = soup.find_all('div', attrs={'id':"answers"})[0]
codeblock = answer.find_all('pre')[0]
command = codeblock.find_all('code')[0].get_text()

# strip potential $
command = command.lstrip("$")

# run command
if not args.y:
    print(f"Do you wish to run the command: \n {command}")
    user_input = ""
    while user_input.lower() not in ["y", "n"]:
        user_input = input("(y/n): ").lower().strip(" ")
        if user_input == "y":
            os.system(command)
        elif user_input == "n":
            print("That's probably the smartest choice anyway...")
        else:
            print("Invalid input")
else:
    print("YOLO mode activated B)")
    os.system(command)
    



