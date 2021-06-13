shopping_list = []

# .append(what do you want to add?)

while (True):
  mode = int(input("Enter 1 to add to your shopping list\n2 to remove\n"))

  if mode == 1:
    new_item = input("What do you want to add to your shopping list? \n")
    shopping_list.append(new_item)

  if mode == 2:
    item_to_remove = input("What do you want to remove from your shopping list?\n")
    # .remove(what do you want to remove?)

    # check if this thing even exists
    if item_to_remove in shopping_list:
      shopping_list.remove(item_to_remove)


  print("Your shopping list has " + str( len(shopping_list) ) + " items.")
  print(shopping_list)
  