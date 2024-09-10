def is_greeting(statement):
    greetings = ["hello", "hi", "hey"]
    return statement.lower() in greetings

def make_decision(weather, resources):
    """
    Determine the action of the AI agent based on weather and resource conditions.
    :param weather: A string representing the weather condition.
    :param resources: A string representing the availability of resources.
    :return: A string indicating the action taken by the agent.
    """
    # Define predicates for decision-making
    is_sunny = weather == "Sunny"
    is_rainy = weather == "Rainy"
    is_cloudy = weather == "Cloudy"
    resources_available = resources == "Available"

    # Decision logic using propositional logic
    if is_sunny and resources_available:
        return "Go for a walk"
    elif is_rainy:
        return "Stay indoors"
    elif is_cloudy and not resources_available:
        return "Stay indoors"
    elif is_cloudy and resources_available:
        return "Gather resources"
    else:
        return "No decision made"

def respond(statement):
    if is_greeting(statement):
        return "Hello! How can I help you today?"
    elif "weather" in statement.lower():
        weather = "Sunny"  # Assuming sunny weather for simplicity
        resources = "Available"  # Assuming resources are available
        action = make_decision(weather, resources)
        return f"Based on the current weather and available resources, I recommend: {action}."
    else:
        return "I'm afraid I don't understand. Could you please rephrase your question or request?"

def chat():
    print("Welcome to the chatbot! Type 'exit' to end the conversation.")
    while True:
        user_input = input("User: ")
        if user_input.lower() == "exit":
            print("Chatbot: Goodbye!")
            break
        response = respond(user_input)
        print(f"Chatbot: {response}")

if __name__ == "__main__":
    chat()