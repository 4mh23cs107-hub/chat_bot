from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

if __name__ == "__main__":
    app.run(debug=True)

#from ai import get_ai_response

#print("AI chatbot - Type 'quit' to exit")

#while True:
    #user_input = input("You: ")
    #if user_input.lower() == "quit":
        #break
    #response = get_ai_response(user_input)
    #print("AI: ", response)