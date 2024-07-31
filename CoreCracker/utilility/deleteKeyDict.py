meal = {'fats': 10, 'proteins': 10, 'carbohydrates': 80}
f = [meal.pop(key) for key in ['fats', 'proteins']]

print(meal)
