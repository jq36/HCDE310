import json, random
import requests
from keys import MY_SECRET_API_KEY_1
import re
def parse_recipe(data):
    if "choices" in data and len(data["choices"]) > 0:
        content = data["choices"][0]["message"]["content"]

        # Use regular expressions to find the parts of the recipe
        name_match = re.search(r'- Name: (.*?)\n', content)
        ingredients_match = re.search(r'- Ingredients:\n(.*?)\n\n- Steps:', content, re.DOTALL)
        steps_match = re.search(r'- Steps:\n(.*?)$', content, re.DOTALL)

        if not name_match:
            return "Recipe format is incorrect or missing some parts."

        name = name_match.group(1).strip()
        ingredients = ingredients_match.group(1).strip().split('\n') if ingredients_match else []
        steps = {}
        
        if steps_match:
            steps_lines = steps_match.group(1).strip().split('\n')
            for step in steps_lines:
                step_match = re.match(r'(\d+)\.\s*(.*)', step.strip())
                if step_match:
                    step_number = step_match.group(1).strip()
                    step_description = step_match.group(2).strip()
                    steps[step_number] = step_description

        return {
            "Name": name,
            "Materials": ingredients,
            "Steps": steps
        }
    else:
        return "No recipe found in the provided data."

def api_fetch(selected_ingredients):
    api_url = "https://api.openai.com/v1/chat/completions"
    api_key = MY_SECRET_API_KEY_1
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    fooditem = selected_ingredients
    data = {
        "model": "gpt-3.5-turbo",
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": f"I have these ingredients: {', '.join(fooditem)}. Please provide a recipe using them. Format the recipe as: \n- Name: [Recipe Name]\n- Ingredients:\n [List each ingredient on a new line]\n- Steps:\n [Start each step on a new line with a number and period, e.g., '1. Step description.']"}
        ]
    }

    try:
        print("Sending Requst, need up to 15seconds to get response..")
        response = requests.post(api_url, headers=headers, data=json.dumps(data))
        if response.status_code == 200:
            response_data = response.json()
            print(json.dumps(response_data, indent=4))
            parse_get_recipe = parse_recipe(response_data)
            return parse_get_recipe
        else:
            print("Error:", response.status_code, response.json())
    except requests.exceptions.RequestException as e:
        print("Request failed:", e)


if __name__ == '__main__':
    api_fetch()
