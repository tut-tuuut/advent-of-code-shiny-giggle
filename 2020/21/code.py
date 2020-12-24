import utils as u

with open(__file__ + ".input.txt", "r+") as file:
    raw_input = file.read()

example = """mxmxvkd kfcds sqjhc nhms (contains dairy, fish)
trh fvjkl sbzzf mxmxvkd (contains dairy)
sqjhc fvjkl (contains soy)
sqjhc mxmxvkd sbzzf (contains fish)"""

# part 1 -'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,_


def extract_ingredients_and_allergens(raw_input: str):
    foods = []
    for row in raw_input.splitlines():
        ingredients, allergens = row[:-1].split(" (contains ")
        foods.append([set(ingredients.split()), set(allergens.split(", "))])
    return foods


def search_allergens_in_ingredients(foods: list):
    all_allergens = set()
    all_ingredients = set()
    allergen_ingredients = dict()
    for ingredients, allergens in foods:
        all_allergens.update(allergens)
        all_ingredients.update(ingredients)
    print(
        f"{len(all_allergens)} allergen to find in {len(all_ingredients)} ingredients..."
    )
    while len(allergen_ingredients) < len(all_allergens):
        for allergen in all_allergens:
            ingredient_candidates = all_ingredients.copy()
            for food_ingredients, food_allergens in foods:
                if allergen in food_allergens:
                    ingredient_candidates &= food_ingredients
            if len(ingredient_candidates) == 1:
                guilty = ingredient_candidates.pop()
                allergen_ingredients[allergen] = guilty
                all_ingredients.remove(guilty)
    return allergen_ingredients


def count_non_allergen_ingredients_occurrences(allergen_ingredients: dict, foods: list):
    guilties = set(allergen_ingredients.values())
    return sum(
        1
        for (ingredients, _) in foods
        for ingredient in ingredients
        if ingredient not in guilties
    )


example_foods = extract_ingredients_and_allergens(example)
example_allergen_ingredients = search_allergens_in_ingredients(example_foods)
u.assert_equals(
    count_non_allergen_ingredients_occurrences(
        example_allergen_ingredients, example_foods
    ),
    5,
)
my_foods = extract_ingredients_and_allergens(raw_input)
allergen_ingredients = search_allergens_in_ingredients(my_foods)
u.answer_part_1(
    count_non_allergen_ingredients_occurrences(allergen_ingredients, my_foods)
)

# part 2 -'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,_


def generate_canonical_dangerous_list(allergen_ingredients: dict):
    return ",".join(
        allergen_ingredients[allergen] for allergen in sorted(allergen_ingredients)
    )


u.assert_equals(
    generate_canonical_dangerous_list(example_allergen_ingredients),
    "mxmxvkd,sqjhc,fvjkl",
)

u.answer_part_2(generate_canonical_dangerous_list(allergen_ingredients))