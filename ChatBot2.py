# ChatBot2.py
# Using Starter code for Python Chat Bot Program
# CIT-95 (Mohle) Spring 2024
# last updated: 5/5/24 by BKF

# Working basic chatbot using starter code from dH
# Had to edit because of incompatibility issues with the version and Windows


from openai import OpenAI
import os
os.environ["OPENAI_API_KEY"] = "sk-proj-nv0Umded1IfystKFPzztT3BlbkFJXL9i06a3wdHtFn5LOFQ7"
client = OpenAI()

# User-defined function go here, before the main() function (is a Python coding convention)
def generate_response(user_input):
    try:
        # Call the OpenAI API to generate a response
        response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "system", "content": "Assume the role of a Python teacher, and think step by step. Your name is Skippy Py."},
                      {"role": "user", "content": user_input}
        ],
        temperature=0,
        max_tokens=2024,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
        )

        response_text = print(response.choices[0].message.content)  # type: ignore
        return response_text
    
    except Exception as e:
        # Print an error message if the API call fails
        print("Error generating response:", e)
        return "I'm sorry, I couldn't generate a response."

def main():

    # Print a welcome message
    print("\nWelcome to the Python Study Bot! Type 'quit' to exit.\n")

    # This loop will run until the break after user input "quit"
    while True:
        # Get user input.
        user_input = input("Python student question: ")

        # Check if user wants to quit the chatbot
        if user_input.lower() == "quit":
            print("Exiting Python Study Bot.")
            break

        # Generate a response using OpenAI's GPT-3.5-turbo
        response = generate_response(user_input)

        # Print the response
        # print("Python Study Bot:", response)
    
# Use this common Python idiom to check if your Python code is being run directly or being imported
# as a module into another program. This tells your program to start in a function named "main()"
# main() is not a reserved word in Python, but it is a standard convention and I suggest you use it
# to not confuse your project coworkers.
if __name__ == "__main__":
    main()
