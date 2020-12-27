import re
from functools import reduce


def parse_line(line, parser):
    raw_ingredients, raw_allergens = parser.search(line).groups()
    return set(raw_ingredients.split(' ')), raw_allergens.split(', ')


if __name__ == '__main__':
    parser = re.compile('([^(]+) \(contains ([^)]+)')
    allergen_to_ingredient_sets = {}
    all_ingredients = []
    with open('input', 'r') as f:
        for line in f.readlines():
            ingredients, allergens = parse_line(line, parser)
            all_ingredients.extend(ingredients)
            for allergen in allergens:
                allergen_to_ingredient_sets[allergen] = allergen_to_ingredient_sets.get(allergen, []) + [ingredients]

    allergen_to_posible_ingredients = {}
    for allergen, ingredient_sets in allergen_to_ingredient_sets.items():
        allergen_to_posible_ingredients[allergen] = reduce(lambda s1, s2: s1 & s2, ingredient_sets)

    allergen_to_ingredient = {}
    while tmp := dict(sorted(allergen_to_posible_ingredients.items(), key=lambda i: len(i[1]))):
        for allergen, ingredients in tmp.items():
            if len(ingredients) == 1:
                allergen_to_ingredient[allergen] = next(iter(ingredients))
                del allergen_to_posible_ingredients[allergen]
            else:
                allergen_to_posible_ingredients[allergen] -= set(allergen_to_ingredient.values())
    print(','.join(ingredient for _, ingredient in sorted(allergen_to_ingredient.items(), key=lambda item: item[0])))
