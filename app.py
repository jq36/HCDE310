from flask import Flask, render_template, request, abort
from functions import api_fetch
import re
app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/results", methods=["GET", "POST"])
def results():
    error_message = None

    if request.method == "POST":
        ingredient_input = request.form.get("ingredient")
        if not ingredient_input:
            error_message = "Please enter at least one ingredient."
        else:
            ingredients_list = [item.strip() for item in ingredient_input.split(',') if item.strip()]
            search_results = api_fetch(ingredients_list)
            
            if not search_results:
                error_message = "No recipes found for the entered ingredients."
            elif isinstance(search_results, dict):
                search_results = [search_results]

            for recipe in search_results:
                for step_number in list(recipe['Steps']):
                    step_text = recipe['Steps'][step_number]
                    cleaned_step_text = re.sub(r'^\d+\.\s*', '', step_text)
                    recipe['Steps'][step_number] = cleaned_step_text

            print(search_results)
            return render_template("results.html", search_results=search_results, ingredients=ingredients_list, error=error_message)

    if request.method == "GET":
        abort(400, description="GET method not allowed for this route.")
    
    return render_template("results.html", search_results=[], ingredients=[], error=error_message)


if __name__ == "__main__":
    app.run()
