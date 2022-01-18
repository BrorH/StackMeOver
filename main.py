from googlesearch import search
from bs4 import BeautifulSoup
import os 
import requests
import sys

try:
    query = sys.argv[1]
    assert len(sys.argv) == 2
except IndexError:
    print("No query given")
    sys.exit(1)
except AssertionError:
    print("If query contains several words, it must be passed as a string")
    sys.exit(1)


print(f"Querying '{query}'")
for url in search(f"{query} site:stackoverflow.com", stop=1):
    r = requests.get(url)

soup = BeautifulSoup(r.text, features="lxml")
answer = soup.find_all('div', attrs={'id':"answers"})[0]
codeblock = answer.find_all('pre')[0]
command = codeblock.find_all('code')[0].get_text()

# strip potential $
command = command.lstrip("$")

# run command
print(f"Do you wish to run the command: \n $ {command}")
user_input = ""
while user_input.lower() not in ["y", "n"]:
    user_input = input("(y/n): ").lower().strip(" ")
    if user_input == "y":
        os.system(command)
    elif user_input == "n":
        print("That's probably the smartest choice anyway...")
    else:
        print("Invalid input")
    



