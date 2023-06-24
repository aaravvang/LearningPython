"""Create a class hierarchy for a restaurant. The Restaurant class should have properties name and location, and a method get_menu() that returns a list of menu items. Create a subclass named ItalianRestaurant that inherits from the Restaurant class, and has additional properties chef_name and cuisine. Override the get_menu() method to return a list of Italian menu items. Create a subclass named JapaneseRestaurant that inherits from the Restaurant class, and has additional properties sushi_chef_name and cuisine. Override the get_menu() method to return a list of Japanese menu items."""

class restaurant:
  name = "Aarav's bakeria"
  def location(self):
    print("India")
  def getName(self):
    return self.name
  def get_menu(self):
    menu = ["chicken nuggets", "pizza", "pasta", "chicken 65", "butter paneer"]
    return menu

class ItalianRestaurant(restaurant):
  def get_menu(self):
    menu = ["pizza", "pasta", "raviolli", "bruschetta"]
    return menu
class JapaneseRestaurant(restaurant):
  sushi_chef_name = "Hitoshi"
  cuisine = "japanese"
  def getChefName(self):
    return self.sushi_chef_name
  def getCuisine(self):
    return self.cuisine
  def get_menu(self):
    menu = ["sushi", "natto", "rice cake", "spring rolls"]
    return menu
Aarav = restaurant()
print(Aarav.location())
print(Aarav.getName())
print(Aarav.get_menu())
Aarush = ItalianRestaurant()
print("\nItalian: \n")
print(Aarush.get_menu())
Harsh = JapaneseRestaurant()
print("\nJapanese:")
print("\n")
print(Harsh.getChefName())
print(Harsh.get_menu())  