def get_motivational_quote(user_input):
    """
    Returns a motivational quote based on the user's input.
    """
    quotes = {
        "sad": "What you have endured, has prepared you for what you are yet to receive.",
        "tired": "Your potential to succeed is infinite.",
        "unmotivated": "Small steps every day lead to massive results.",
        "happy": "Happiness is not by chance, but by choice.",
        "stressed": "Stress is the gap between our expectation and reality. More the gap, more the stress. So, expect nothing and accept everything."
    }

    # Default response
    default_quote = "Believe in yourself. You are braver than you think, more talented than you know, and capable of more than you imagine."

    return quotes.get(user_input.lower(), default_quote)


def run_motivational_app():
    print("Welcome to the Motivation Chatbot!")
    name = input("What's your name? ")

    while True:
        user_feeling = input(
            f"\nHello {name}, how are you feeling today? (sad/tired/unmotivated/happy/stressed) \nType 'exit' to close the app.\n")

        if user_feeling.lower() == 'exit':
            print("Thank you for using the Motivation Chatbot. Have a great day!")
            break

        quote = get_motivational_quote(user_feeling)
        print("\nMotivational Quote: " + quote)

run_motivational_app()
