# HCDE 310 - Homework 5

## Program Description

This program is designed to fetch and display recipes using a set of ingredients. It uses the OpenAI API to generate recipes based on user-provided ingredients. The main functionality is encapsulated in the `api_fetch()` function, which sends a request to the OpenAI API with a set of ingredients and retrieves a formatted recipe. 

The program starts by selecting a random set of ingredients using the `get_fooditem()` function. It then constructs a request for the OpenAI API, asking for a recipe that uses these ingredients. The recipe is expected to be formatted with a name, a list of ingredients, and a series of steps. After sending the request, the program processes the response and prints out the formatted recipe using the `parse_recipe()` function.

If an error occurs during the API request, the program prints the error details. The program's output includes both the raw JSON response from the API and the formatted recipe.

## Sample Output
1. If the return format is expected.
```commandline
{
    "id": "chatcmpl-8Q2bwAUZlBOFLpXN6uFk1fovnWRoU",
    "object": "chat.completion",
    "created": 1701217256,
    "model": "gpt-3.5-turbo-0613",
    "choices": [
        {
            "index": 0,
            "message": {
                "role": "assistant",
                "content": "- Name: Spicy Tofu and Shrimp Stir-Fry\n- Ingredients:\n\u5927\u849c (Garlic)\n\u8c46\u8150 (Tofu)\n\u571f\u8c46 (Potato)\n\u9ec4\u74dc (Cucumber)\n\u867e (Shrimp)\n\u8fa3\u6912 (Chili Pepper)\n\u8611\u83c7 (Mushroom)\n\u756a\u8304 (Tomato)\n\u6d0b\u8471 (Onion)\n\u9c7c\u8089 (Fish)\n\n- Steps:\n1. Prepare the ingredients by cleaning and cutting them. Mince the garlic, slice the tofu, dice the potato and cucumber, devein and peel the shrimp, slice the chili pepper, halve the mushroom, chop the tomato, and thinly slice the onion.\n2. Heat some oil in a wok or large pan over medium heat. Stir-fry the minced garlic until fragrant.\n3. Add the sliced tofu and stir-fry for a few minutes until lightly browned.\n4. Next, add the diced potato and stir-fry until the edges start to become golden.\n5. Add the sliced cucumber, shrimp, chili pepper, mushroom, and onion. Stir-fry for a few minutes until the shrimp start to turn pink.\n6. Stir in the chopped tomato and continue cooking for a few more minutes until the vegetables are tender and the shrimp are fully cooked.\n7. Adjust the seasoning by adding salt, pepper, soy sauce, or any other desired flavors to taste.\n8. Serve the spicy tofu and shrimp stir-fry hot with steamed rice or noodles. Enjoy!"
            },
            "finish_reason": "stop"
        }
    ],
    "usage": {
        "prompt_tokens": 130,
        "completion_tokens": 325,
        "total_tokens": 455
    }
}
{'Name': 'Spicy Tofu and Shrimp Stir-Fry', 'Materials': ['大蒜 (Garlic)', '豆腐 (Tofu)', '土豆 (Potato)', '黄瓜 (Cucumber)', '虾 (Shrimp)', '辣椒 (Chili Pepper)', '蘑菇 (Mushroom)', '番茄 (Tomato)', '洋葱 (Onion)', '鱼肉 (Fish)'], 'Steps': {'1': 'Prepare the ingredients by cleaning and cutting them. Mince the garlic, slice the tofu, dice the potato and cucumber, devein and peel the shrimp, slice the chili pepper, halve the mushroom, chop the tomato, and thinly slice the onion.', '2': 'Heat some oil in a wok or large pan over medium heat. Stir-fry the minced garlic until fragrant.', '3': 'Add the sliced tofu and stir-fry for a few minutes until lightly browned.', '4': 'Next, add the diced potato and stir-fry until the edges start to become golden.', '5': 'Add the sliced cucumber, shrimp, chili pepper, mushroom, and onion. Stir-fry for a few minutes until the shrimp start to turn pink.', '6': 'Stir in the chopped tomato and continue cooking for a few more minutes until the vegetables are tender and the shrimp are fully cooked.', '7': 'Adjust the seasoning by adding salt, pepper, soy sauce, or any other desired flavors to taste.', '8': 'Serve the spicy tofu and shrimp stir-fry hot with steamed rice or noodles. Enjoy!'}}

```
2. If the format of the response is not expected.
```
Sending Requst, need up to 15seconds to get response..
{
    "id": "chatcmpl-8Q2VREFOANUWb3GvX7X8KlUV8QrQ1",
    "object": "chat.completion",
    "created": 1701216853,
    "model": "gpt-3.5-turbo-0613",
    "choices": [
        {
            "index": 0,
            "message": {
                "role": "assistant",
                "content": "- Name: Spicy Fish Stir-Fry\n\nIngredients:\n- Spinach\n- Garlic\n- Lettuce\n- Green Pepper\n- Fish Meat\n- Chili Pepper\n- Broccoli\n- Corn\n- Pork\n\nSteps:\n1. Prepare all the ingredients by washing and chopping them.\n2. Heat a large frying pan or wok over medium-high heat.\n3. Add some oil to the pan and let it heat up.\n4. Stir-fry the garlic and chili pepper for about 1 minute until fragrant.\n5. Add the pork and cook until it's browned and cooked through.\n6. Add the fish meat and stir-fry for another 2-3 minutes until it's cooked.\n7. Add the green pepper, corn, and broccoli to the pan and stir-fry for about 4-5 minutes until the vegetables are tender-crisp.\n8. Add the spinach and lettuce, then continue stir-frying for another 1-2 minutes until the greens have wilted.\n9. Adjust the seasoning with salt or soy sauce to your taste.\n10. Serve the spicy fish stir-fry hot with steamed rice or noodles. Enjoy!"
            },
            "finish_reason": "stop"
        }
    ],
    "usage": {
        "prompt_tokens": 99,
        "completion_tokens": 240,
        "total_tokens": 339
    }
}
Ingredients part is missing.
```
