'''
Kaicheng Liu
CSC110
Project -1
This program creates a story about moving, using user-specified words.
'''

def create_story(person_one, street_name, person_two,
                  object_name, vehicle, adjective):
    '''
    This function creates a moving story with the given words.
    Args:
        person_one: str, name of the person who is moving.
        street_name: str, the street of the new condo.
        person_two: str, name of the friend helping.
        object_name: str, object that needs to be moved.
        vehicle: str, type of vehicle rented.
        adjective: str, descriptive word for the vehicle.
    Returns:
        str, a complete story with the given words.
    '''
    
    # concatenate all parts to form the story
    story = person_one + " decided to move from their apartment on 5th\n" + \
            "to a condo on " + street_name + ". They called their friend " + \
            person_two + "\nfor help. However, they could not fit " + \
            object_name + " into\nthe moving truck, so they had to rent a " + \
            adjective + " " + vehicle + "\nin order to move it!"
    
    return story

def main():
    '''
    This function runs the move story example with preset variables.
    Args:
        None
    Returns:
        None
    '''
    
    # define variables for the story
    person_one = "Janet"
    street_name = "Loopdydoo Avenue"
    person_two = "Richard"
    object_name = "Christmas tree"
    vehicle = "Horse-drawn carriage"
    adjective = "Off-road"
    
    story = create_story(person_one, street_name, person_two,
                         object_name, vehicle, adjective)
    print(story)

main()
