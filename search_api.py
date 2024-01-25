import requests

def search(search_term='luke'):
  base_url = 'https://swapi.dev/api/people/?search='
  search_url = f'{base_url}{search_term}'
  resp = requests.get(search_url)
  resp_json = resp.json()
  if resp_json.get('results'):
    return resp.json()['results']
  else:
    return None

# Extract the name from JSON data and store it. Then return it.

def parse_name(person):
  name = person.get('name')
  return name


# Extract the planet URL which is stored under the 'homeworld' key.
# Then make another API call with the requests package.
# Convert the response to JSON and return the value associated with 
# the 'name' key, which is a string of the planet’s name

def parse_planet(person):
  planet_url = person.get('homeworld')
  resp = requests.get(planet_url)
  planet = resp.json().get('name')
  return planet


# The fetch_title function gets the film’s URL and converts the results to JSON. 
# Then get the value associated with the 'title' key.

def fetch_title(url):
  film_json = requests.get(url).json()
  film_title = film_json.get('title')
  return film_title

# Create the parse_films function and pass it the argument person 
# Set film_urls to the value of 'films', which will be a list of URLs. 
# Using a list comprehension create a list of strings. 
# Use the helper function fetch_title to convert the URL to a string.

def parse_films(person):
  film_urls = person.get('films')
  films =[fetch_title(film_url) for film_url in film_urls]
  return films

# Create the format_titles function that takes a list of movie titles. 
# With a list comprehension, add a newline character (\n) to the end. 
# Use the string method join() to create a string of all of the titles 
# Place ' * ' between each element.

def format_titles(titles):
  new_lines = [title + '\n' for title in titles]
  formatted_titles = '  * ' + '  * '.join(new_lines)
  return formatted_titles

# The person_description function builds the final description. 
# Using an f-string, name the character, where they are from, 
# and the movies in which they appear. Return this string.

def person_description(name, planet, titles):
  description = f'{name} is from the planet {planet}. They appear in the following films:\n{titles}'
  return description

if __name__ == '__main__':
  import pprint

  person = search()
  name = parse_name(person)
  planet = parse_planet(person)
  film_list = parse_films(person)
  titles = format_titles(film_list)
  description = person_description(name, planet, titles)

#  pprint.pprint(film_list)
#  pprint.pprint(name)
  
  print(description)



