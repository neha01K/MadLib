# this is the MadLib project
#focusing on Python string concatenation
import random 
adj = input("Adjective: ")
verb = input("Verb: ")
famous_person = input("Famous Person: ")

#List of stories 
stories = [f"""Computer programming is so {adj}. More practise you do, better you become in it.
It makes me excited all the time because I love to {verb}. 
So, Stay hydrated like you are a {famous_person}.""",
f"Life can be {adj}, but nothing is better than to {verb} like {famous_person}!",
f"Once upon a time, a {adj} coder decided to {verb} and became as famous as {famous_person}."]

#chooses random story from the list and present it to user
print(random.choice(stories))