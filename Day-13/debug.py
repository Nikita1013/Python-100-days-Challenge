############DEBUGGING#####################

# # Describe Problem
# def my_function():
# #   for i in range(1, 20): # Given as it will range from 0-19 and will never reach 21
#     for i in range(1, 21):
#         if i == 20:
#             print("You got it")
# my_function()

# # Reproduce the Bug
# from random import randint
# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(1, 6)
# print(dice_imgs[dice_num])

# # Play Computer
# year = int(input("What's your year of birth?"))
# if year > 1980 and year <= 1994: # either make it <= 1994 or
#   print("You are a millenial.")
# elif year > 1994:   # make it here >= 1994
#   print("You are a Gen Z.") 

# # Fix the Errors
# age = int(input("How old are you?")) #Make the input taken to be integer
# if age > 18:
#     print(f"You can drive at age {age}.") #It was the indentation error and f-string.

# #Print is Your Friend
# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page = int(input("Number of words per page: ")) # There is the == operator instead of =
# total_words = int(pages * word_per_page)
# print(f"pages = {pages}")
# print(f"word_per_page = {word_per_page}")
# print(total_words) 

# #Use a Debugger
def mutate(a_list):
    b_list = []
    for item in a_list:
        new_item = item * 2
        b_list.append(new_item)
    print(b_list)

mutate([1,2,3,5,8,13])