def get_score():
    """
    Get user input for the score and return it as a float.
    """
    return float(input("Enter score: "))

def determine_score_status(score):
    """
    Determine and print the status based on the given score.
    """
    if score < 0 or score > 100:
        print("Invalid score")
    else:
        if score > 90:
            print("Excellent")
        elif score > 50:
            print("Passable")
        else:
            print("Bad")

user_score = get_score()
determine_score_status(user_score)
