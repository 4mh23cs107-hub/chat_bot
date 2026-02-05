import os
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import SystemMessage, UserMessage
from azure.core.credentials import AzureKeyCredential

def start_chat():
    endpoint = "https://models.github.ai/inference"
    model = "gpt-4o-mini"
    token = os.environ.get("GITHUB_TOKEN")
    
    if not token:
        print("Error: GITHUB_TOKEN environment variable is not set.")
        print("Please set it using: $env:GITHUB_TOKEN='your_token_here'")
        return

    client = ChatCompletionsClient(
        endpoint=endpoint,
        credential=AzureKeyCredential(token),
    )

    print("\n" + "="*50)
    print("✨ AI CHAT BOT READY (Terminal Edition) ✨")
    print("Type 'exit' or 'quit' to end the conversation.")
    print("="*50 + "\n")

    # Conversation history
    messages = [SystemMessage("You are a helpful and friendly AI assistant.")]

    while True:
        try:
            user_input = input("👤 You: ").strip()
            
            if user_input.lower() in ["exit", "quit", "bye"]:
                print("\n🤖 AI: Goodbye! Have a great day!\n")
                break
            
            if not user_input:
                continue

            messages.append(UserMessage(user_input))

            print("⏳ AI is thinking...", end="\r")
            
            response = client.complete(
                messages=messages,
                temperature=1.0,
                top_p=1.0,
                max_tokens=1000,
                model=model
            )

            reply = response.choices[0].message.content
            
            # Clear "is thinking" line and print reply
            print(" " * 20, end="\r") 
            print(f"🤖 AI: {reply}")
            print("-" * 30)

        except KeyboardInterrupt:
            print("\n\nGoodbye!")
            break
        except Exception as e:
            print(f"\n❌ Error: {e}")
            break

if __name__ == "__main__":
    start_chat()
