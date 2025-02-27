# this is the MadLib project
# this is the MadLib project
#focusing on Python string concatenation
import random

print("Choose a theme\nA. Programming\nB. Spritual\nC. Career")
choice = input("Enter your theme: ")

adj = input("Adjective: ")
verb = input("Verb: ")
famous_person = input("Famous Person: ")

def matched_theme(choice.lower()):
    match choice:
        case "programming":
            stories = [f"""Computer programming is so {adj}. More practise you do, better you become in it.
                        It makes me excited all the time because I love to {verb}.
                        So, Stay hydrated like you are a {famous_person}.""",
                        f"Life can be {adj}, but nothing is better than to {verb} like {famous_person}!",
                        f"Once upon a time, a {adj} coder decided to {verb} and became as famous as {famous_person}."]
            print(random.choice(stories))
        case "spritual":
            stories = [f"Life is a {adj} journey. We all have to {verb}",f"Be like {famous_person} and explore your {adj} potential."\
                       ,f"Life becomes {adj} when you {verb} the present moment, just like {famous_person} did."]
            print(random.choice(stories))
        case "career":
            stories = [f"A {adj} career is just one coffee away—unless you're {verb} like {famous_person}. ☕😴",
                       f"Stay {verb}, hustle hard, and maybe one day you'll be as {adj} as {famous_person}—or at least afford extra guac.🥑💸",
                       f"A {adj} attitude can {verb} doors—unless you're {famous_person}, then they open automatically.🚪🤖"]
            print(random.choice(stories))

matched_theme(choice)
