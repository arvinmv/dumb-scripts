import requests
import random

url = 'https://harry-potter-api-en.onrender.com/characters'

def get_data(url):
    response = requests.get(url)
    data = response.json()
    return data

def get_characters(data):
    characters = []
    for character in data:
        characters.append(character['character'])
    return characters

def remove_spaces(characters):
    characters_without_spaces = []
    for character in characters:
        characters_without_spaces.append(character.replace(' ', ''))
    return characters_without_spaces

def append_pw_requirements(characters):
    characters_with_pw_requirements = []
    numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    special_characters = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')']
    for character in characters:
        random_numbers = ''.join(random.sample(numbers, 2))
        random_special = ''.join(random.sample(special_characters, 2))
        characters_with_pw_requirements.append(character + random_numbers + random_special)
    return characters_with_pw_requirements

def get_random_password(characters_with_pw_requirements):
    random_password = random.choice(characters_with_pw_requirements)
    return random_password

def main():
    data = get_data(url)
    characters = get_characters(data)
    characters_without_spaces = remove_spaces(characters)
    characters_with_pw_requirements = append_pw_requirements(characters_without_spaces)
    random_password = get_random_password(characters_with_pw_requirements)
    print(random_password)

if __name__ == '__main__':
    main()