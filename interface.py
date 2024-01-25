import fire
from tinydb import TinyDB, Query
import search_api

db = TinyDB('db.json')
User = Query()

# Fire requires that you instantiate a fire object in the __name__ == '__main__' conditional. 
# Put the search function in parentheses, which exposes this to the end user. That means a user can only run the search function. 
# All other functions we create will be hidden from them. 
# When you run the script, Fire will automatically run the search function.

def search(name='luke'):
  characters = search_api.search(name)
  if characters is not None:
    check_db(characters)
  else:
    print(f'Cannot find the character "{name}"')

# The check_db function lists the names of the characters
# Uses the search method on the database object to check if it's empty.
# Create the description variable by calling the parse_char function.
# Else collects the information from the database, not from the API.

def check_db(chars):
  for char in chars:
    char_name = search_api.parse_name(char)
    results = db.search(User.name == char_name)
    if not results:
      description = parse_char(char)
    else:
      name = results[0]['name']
      planet = results[0]['planet']
      titles = results[0]['titles']
      description = search_api.person_description(name, planet, titles)
    print(description)

# The parse_char function is only called if the character is not in the database. 
# Before returning the description, adds a line that inserts the formatted vars to the database 

def parse_char(char):
  char_name = search_api.parse_name(char)
  planet= search_api.parse_planet(char)
  film_list = search_api.parse_films(char)
  titles = search_api.format_titles(film_list)
  description = search_api.person_description(char_name, planet, titles)
  return description

# We need to parse a list of characters. Create the function parse_char_list that takes a list of characters. Iterate over the list. 
# Create variables for the character’s name, planet, list of films, formatted string of film titles, and the final description. 
# Call the appropriate function from the search_api module.

#def parse_char_list(char):
#  char_name = search_api.parse_name(char)
#  planet= search_api.parse_planet(char)
#  film_list = search_api.parse_films(char)
#  titles = search_api.format_titles(film_list)
#  description = search_api.person_description(char_name, planet, titles)
#  db.insert({'name':char_name, 'planet':planet, 'titles':titles})
#  return description

if __name__ == '__main__':
  fire.Fire(search)
  