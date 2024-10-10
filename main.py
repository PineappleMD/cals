def main():
  
  fat = 0.0
  
  carbohydrates = 0.0

  fat = float(input("Enter your daily consumption of grams of fat:"))

  carbohydrates = float(input("Enter your daily consumption of grams of carbohydrates:"))

  calories_from_fat = fat * 9

  calories_from_carbs = carbohydrates * 4
  print('-' * 25)
  print("Your daily intake of calories from fat is:", calories_from_fat)
  print("Your daily intake of calories from carbohydrates is:" , calories_from_carbs)

main()
