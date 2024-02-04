from pulp import LpMaximize, LpProblem, LpVariable

# Створюємо задачу
model = LpProblem(name="optimal_production", sense=LpMaximize)

# Оголошуємо змінні - кількість "Лимонаду" та "Фруктового соку", які будуть вироблятися
lemonade = LpVariable(name="lemonade", lowBound=0, cat="Integer")
fruit_juice = LpVariable(name="fruit_juice", lowBound=0, cat="Integer")

# Обмеження ресурсів
model += 2 * lemonade + fruit_juice <= 100, "water_constraint"
model += lemonade <= 50, "sugar_constraint"
model += lemonade <= 30, "lemon_juice_constraint"
model += 2 * fruit_juice + lemonade <= 40, "fruit_puree_constraint"

# Функція максимізації загальної кількості продуктів
model += lemonade + fruit_juice

# Розв'язання задачі
model.solve()

# Виведення результатів
print(f"Optimal amount of Lemonade: {lemonade.varValue}")
print(f"Optimal amount of Fruit Juice: {fruit_juice.varValue}")
