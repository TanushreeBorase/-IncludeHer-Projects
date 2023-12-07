import random

def get_greeting():
    greetings = ["Hello! I'm your travel planner bot.", "Hi there! Ready to plan your next adventure?", "Greetings! Where do you want to go?"]
    return random.choice(greetings)

def get_destination():
    destinations = ["Paris", "Tokyo", "New York", "Barcelona", "Sydney"]
    return random.choice(destinations)

def get_travel_recommendation():
    recommendations = [
        "I recommend visiting the local museums and exploring the historical sites.",
        "Don't forget to try the local cuisine. The food in {destination} is amazing!",
        "Consider taking a guided tour to learn more about the culture and history of {destination}."
    ]
    return random.choice(recommendations)

def get_response(user_input):
    if "hello" in user_input.lower():
        return get_greeting()
    elif "plan my trip" in user_input.lower():
        destination = get_destination()
        return f"Great choice! How about planning a trip to {destination}? {get_travel_recommendation().format(destination=destination)}"
    elif "bye" in user_input.lower():
        return "Goodbye! Have a fantastic trip!"
    else:
        return "I'm here to help you plan your trip. If you want to get started, just say 'Plan my trip.'"

def main():
    print("Chatbot: " + get_greeting())
    
    while True:
        user_input = input("You: ")
        
        if user_input.lower() == 'exit':
            print("Chatbot: Goodbye! Have a fantastic trip!")
            break
        
        response = get_response(user_input)
        print("Chatbot:", response)

if __name__ == "__main__":
    main()
