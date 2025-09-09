'''
Kaicheng Liu
CSC110
Project -1
This program creates a vacation story with user-specified words.
'''

def create_story(person_one, person_two, pet_name, 
                 animal, place, adjective, verb, adverb):
    '''
    This function creates a vacation story using the provided words.
    Args:
        person_one: str, first friend's name.
        person_two: str, second friend's name.
        pet_name: str, name of the pet.
        animal: str, type of animal.
        place: str, vacation destination.
        adjective: str, descriptive word for the pet.
        verb: str, verb describing pet behavior.
        adverb: str, adverb describing how the trip was taken.
    Returns:
        str, a complete story with the given words.
    '''
    
    story = person_one + " and " + person_two + " were best friends.\n" + \
            "One day " + person_one + " and " + person_two + \
            " decided to go on a\nvacation to " + place + \
            ". However, they didn't know\nwhat to do with their " + \
            adjective + " pet " + animal + " named " + pet_name + ".\n" + \
            pet_name + " had been causing problems, due to constant " + \
            verb + "ing.\n" + person_one + \
            " found a sitter for their pet, and " + adverb + \
            " went on the trip."
    
    return story

def main():
    '''
    This function runs the vacation story example with preset variables.
    Args:
        None
    Returns:
        None
    '''
    
    # define variables for the story
    person_one = "Joe"
    person_two = "Lily"
    pet_name = "Poncho"
    animal = "polar bear"
    place = "Madagascar"
    adjective = "Ridiculous"
    verb = "plank"
    adverb = "spastically"
    
    # create and print the story
    story = create_story(person_one, person_two, pet_name, animal,
                         place, adjective, verb, adverb)
    print(story)

main()
