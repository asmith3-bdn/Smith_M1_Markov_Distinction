"""
A'myah Smith
M1: A Markov Distinction
"""

import numpy as np
import random
import matplotlib.pyplot as plt
from PIL import Image

"""
Class that defines the 
"""
class OutfitOrderGenerator:
    #defines the attributes for the generator object
    def __init__(self, transition_matrix):
        self.transition_matrix = transition_matrix
        self.outfit_items = list(transition_matrix.keys())
    
    """
    The get_next_outfit_item function determines the next category that is going to be added in the 
    outfit order based on the outfit_order_options matrix, return value will be added to the
    outfit category order list
    """
    def get_next_outfit_item(self, current_category, outfit_order):
        transition_probabilites = self.transition_matrix[current_category]

        for category in outfit_order:
            transition_probabilites[category] = 0

        total = sum(transition_probabilites.values())

        normalized_probabilites = []
        for category in self.outfit_items:
            probability = transition_probabilites[category]
            normalized = probability / total
            normalized_probabilites.append(normalized)

        return np.random.choice(self.outfit_items, p = normalized_probabilites)

    """
    The compose_outfit_order function builds the outfit category order by 
    utlizing get_next_outfit_item() until a full outfit can be built, return value will be used
    to get the actaul clothing items
    """
    def compose_outfit_order(self):
        outfit_order = []

        outfit_categories = ["Top", "Bottom", "Dress", "Shoes"]
        current_category = random.choice(outfit_categories)
        outfit_order.append(current_category)

        if current_category == "Dress":
            outfit_order_length = 2
        else: 
            outfit_order_length = 3

        while len(outfit_order) < outfit_order_length:
             next_category = self.get_next_outfit_item(current_category, outfit_order)
             outfit_order.append(next_category)
             current_category = next_category

        return outfit_order


"""
Class for our top objects, attribues to them, name, image_tag, and color
"""
class Top:
    def __init__(self, name, image_tag, color):
        self.name = name
        self.tag = image_tag
        self.color = color

top_1 = Top("Top_1", "Top1.jpg", "orange")
top_2 = Top("Top_2", "Top2.jpg", "green")
top_3 = Top("Top_3", "Top3.jpg", "red")
top_4 = Top("Top_4", "Top4.jpg", "violet")
top_5 = Top("Top_5", "Top5.jpg", "yellow")
top_6 = Top("Top_6", "Top6.jpg", "blue")

#List of all top objects
tops = [top_1, top_2, top_3, top_4, top_5, top_6]

"""
Class for our bottom objects, attribues to them, name, image_tag, and color
"""
class Bottom:
    def __init__(self, name, image_tag, color):
        self.name = name
        self.tag = image_tag
        self.color = color

bottom_1 = Bottom("bottom_1", "Bottom1.jpg", "blue")
bottom_2 = Bottom("bottom_1", "Bottom2.jpg", "blue")
bottom_3 = Bottom("bottom_3", "Bottom3.jpg", "yellow")
bottom_4 = Bottom("bottom_4", "Bottom4.jpg", "green")
bottom_5 = Bottom("bottom_5", "Bottom5.jpg", "blue")
bottom_6 = Bottom("bottom_6", "Bottom6.jpg", "red")
bottom_7 = Bottom("bottom_7", "Bottom7.jpg", "orange")

#List of all bottom objects
bottoms = [bottom_1, bottom_2, bottom_3, bottom_4, bottom_5, bottom_6, bottom_7]

"""
Class of our bottom objects, attribues to them, name, image_tag, and color
"""
class Dress:
    def __init__(self, name, image_tag, color):
        self.name = name
        self.tag = image_tag
        self.color = color

dress_1 = Dress("dress_1", "Dress1.jpg", "violet")
dress_2 = Dress("dress_2", "Dress2.jpg", "blue")
dress_3 = Dress("dress_3", "Dress3.jpg", "red")
dress_4 = Dress("dress_4", "Dress4.jpg", "green")
dress_5 = Dress("dress_5", "Dress5.jpg", "yellow")

#List of all dress objects
dresses = [dress_1, dress_2, dress_3, dress_4, dress_5]

"""
Class for our Shoes objects, attribues to them, name, image_tag, and color
"""
class Shoes:
    def __init__(self, name, image_tag, color):
        self.name = name
        self.tag = image_tag
        self.color = color

shoes_1 = Shoes("shoes_1", "Shoes1.jpg", "red")
shoes_2 = Shoes("shoes_2", "Shoes2.jpg", "green")
shoes_3 = Shoes("shoes_3", "Shoes3.jpg", "yellow")
shoes_4 = Shoes("shoes_4", "Shoes4.jpg", "blue")
shoes_5 = Shoes("shoes_5", "Shoes5.jpg", "violet")
shoes_6 = Shoes("shoes_6", "Shoes6.jpg", "orange")

#List of all shoes objects
shoes = [shoes_1, shoes_2, shoes_3, shoes_4, shoes_5, shoes_6]

"""
Complimentary color matrix is globally declared so that it may be used by the functions
that will be choosing which items from each category get chosen
"""
complimentary_color_matrix = {
  "red" : {"red": 0.1, "green": 0.4, "blue": 0.2, "orange":0.1, "yellow": 0.1, "violet": 0.1}, 
  "orange" : {"orange": 0.1, "blue": 0.5, "red": 0.1, "yellow":0.1, "violet": 0.1, "green": 0.1},
  "yellow" : {"yellow": 0.1, "violet": 0.4, "blue": 0.2, "orange":0.1, "green": 0.1, "red": 0.1},
  "green" : {"green": 0.1, "red": 0.4, "blue": 0.2, "orange":0.1, "yellow": 0.1, "violet": 0.1},
  "violet" : {"violet": 0.1, "green": 0.4, "blue": 0.2, "orange":0.1, "yellow": 0.1, "red": 0.1},
  "blue" : {"green": 0.4, "blue": 0.2, "orange":0.1, "yellow": 0.1, "violet": 0.1, "red": 0.1}
  }

"""
    The generate_outfit function builds the outfit itself order by 
    utlizing clothing_by_color() until an item from each category is chosen, 
    the return value will be displayed
    """
def generate_outfit(outfit_order):
    outfit = []
    current_color = None

    index = 0
    while index < len(outfit_order):
        category = outfit_order[index]

        if category == "Top":
            item_list = tops
        elif category == "Bottom":
            item_list = bottoms
        elif category == "Dress":
            item_list = dresses
        elif category == "Shoes":
            item_list = shoes

        if index == 0:
            selected_item = random.choice(item_list)
        else:
            selected_item = clothing_by_color(item_list, current_color)

        outfit.append((category, selected_item))

        current_color = selected_item.color

        index += 1

    return outfit

"""
clothing_by_color function uses the color matrix to get use probabilites
to determine the next order in the markov chain that chooses which clothing item
get chosen
"""
def clothing_by_color(item_list, current_color):
    transition_probabilities = complimentary_color_matrix[current_color]
    
    total_probabilites = 0
    item_probabilities = []
    
    for item in item_list:
        color_probability = transition_probabilities.get(item.color, 0)
        item_probabilities.append(color_probability)
        total_probabilites += color_probability

    if total_probabilites == 0:
        item_probabilities = [1 / len(item_list)] * len(item_list)
    else:
        item_probabilities = [p / total_probabilites for p in item_probabilities]

    return np.random.choice(item_list, p = item_probabilities)

"""
The display_outfit function uses the matplotlib to output the visuals of the outfit item
"""
def display_outfit(outfit):
    plt.figure(figsize=(5, 10))
    
    for category, item in outfit:
        img = Image.open("assets/" + item.tag)
        if category == "Dress":
            subplot_index = 2
        else:
            subplot_index = {
                "Top": 1,
                "Bottom": 2,
                "Shoes": 3
            }[category]

        plt.subplot(3, 1, subplot_index)
        plt.imshow(img)
        plt.axis('off')

    plt.tight_layout()
    plt.show()

"""

"""
def main():
  outfit_order_options = OutfitOrderGenerator({
    "Top": {"Top": 0, "Bottom": 0.7, "Dress": 0, "Shoes": 0.3},
    "Bottom": {"Top": 0.8, "Bottom": 0, "Dress": 0, "Shoes": 0.2},
    "Dress": {"Top": 0, "Bottom": 0, "Dress": 0, "Shoes": 1},
    "Shoes": {"Top": 0.4, "Bottom": 0.3, "Dress": 0.3, "Shoes": 0}
    })
  
  outfit_order = outfit_order_options.compose_outfit_order()

  print(outfit_order)

  outfit = generate_outfit(outfit_order)

  display_outfit(outfit)


if __name__ == "__main__":
  main()