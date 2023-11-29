#### HCDE 310
#### HW5 - Exercises

##############
# Your turn! #
##############
# Now you're ready for the next part, where you retrieve data from an API
# of your choice. Note that you may need to provide an authentication key
# for some APIs. For that, work another file, called  keys.py and add it 
# to .gitignore so that it does not get checked into Git.
#
# You will need to copy a few of the import statements from the top of this
# file. You may copy any helpful functions, too, like safe_get().
#
# See requirements in the README.
#
# Also note that when the sunrise sunset API we used is queried for a
# date that doesn't exist, it gives a 400 error. Some APIs that you may
# use will return JSON-formatted data saying that the requested item
# couldn't be found. You may have to check the contents of the data you 
# get back to see whether a query was successful. You don't have to do
# that with the sunrise sunset API.

import json, random
import requests

from keys import MY_SECRET_API_KEY_1

def get_fooditem():
    ingredients = ["Chicken", "Lettuce", "Tomato", "Cucumber", "Beef", "Pork", "Potato", "Carrot", "Onion", "Garlic",
                   "Chili Pepper", "Eggplant", "Green Pepper", "Broccoli", "Spinach", "Mushroom", "Corn", "Tofu",
                   "Shrimp", "Fish Meat"]
    selected_ingredients = random.sample(ingredients, 10)
    return selected_ingredients


def parse_recipe(data):
    if "choices" in data and len(data["choices"]) > 0:
        content = data["choices"][0]["message"]["content"]

        parts = content.split('- Name: ')
        if len(parts) < 2:
            return "Recipe format is incorrect or missing some parts."

        name_part = parts[1]
        name_and_ingredients = name_part.split('- Ingredients:\n')
        name = name_and_ingredients[0].strip()

        if len(name_and_ingredients) < 2:
            return "Ingredients part is missing."

        ingredients_and_steps = name_and_ingredients[1].split('- Steps:\n')
        ingredients = ingredients_and_steps[0].strip().split('\n')

        if len(ingredients_and_steps) < 2:
            return "Steps part is missing."

        steps_lines = ingredients_and_steps[1].strip().split('\n')
        steps = {}
        for step in steps_lines:
            if step.strip() and step[0].isdigit():
                step_number, step_description = step.split(".", 1)
                steps[step_number.strip()] = step_description.strip()

        return {
            "Name": name,
            "Materials": ingredients,
            "Steps": steps
        }
    else:
        return "No recipe found in the provided data."


def api_fetch():
    api_url = "https://api.openai.com/v1/chat/completions"
    api_key = MY_SECRET_API_KEY_1
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    fooditem = get_fooditem()
    data = {
        "model": "gpt-3.5-turbo",
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": f"I have these ingredients: {', '.join(fooditem)}. Can you give me a recipe using them? Please format the recipe as follows: \n- Name: [Recipe Name]\n- Ingredients: list each ingredient on a new line\n- Steps: start each step on a new line and number them."}
        ]
    }

    try:
        print("Sending Requst, need up to 15seconds to get response..")
        response = requests.post(api_url, headers=headers, data=json.dumps(data))
        if response.status_code == 200:
            response_data = response.json()
            print(json.dumps(response_data, indent=4))
            parse_get_recipe = parse_recipe(response_data)
            print(parse_get_recipe)
        else:
            print("Error:", response.status_code, response.json())
    except requests.exceptions.RequestException as e:
        print("Request failed:", e)


if __name__ == '__main__':
    api_fetch()
