from phi.agent import Agent
from phi.model.groq import Groq
from dotenv import load_dotenv

load_dotenv()

# Initialize the agent with the specified model
agent = Agent(
    model=Groq(id="llama-3.3-70b-versatile")
)

print("Type 'exit' to end the conversation.")

# Continuously prompt the user for input
while True:
    user_input = input("\nuser : ")
    if user_input.lower() == 'exit':
        print("Ending the conversation. Goodbye!")
        break
    agent.print_response(user_input)
