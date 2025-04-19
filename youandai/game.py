import os
import sys
import google.generativeai as genai

def get_api_key():
    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        print("❌ Gemini API key not found!")
        print("➡️  Please set it as an environment variable named GEMINI_API_KEY.")
        print("   Or enter it below to use it temporarily for this session.")

        api_key_input = input("🔑 Enter your Gemini API key: ").strip()
        if api_key_input:
            os.environ["GEMINI_API_KEY"] = api_key_input
            print("✅ API key set for this session!")
            return api_key_input
        else:
            print("❌ No API key entered. Exiting the game.")
            sys.exit()
    return api_key

# Initialize Gemini
api_key = get_api_key()
genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-1.5-flash")

print("\n🎮 Welcome to 'You and AI'!")
print("Start your journey by typing your first move.\n")

history = []
response = model.start_chat(history=[])

while True:
    try:
        ai_input = response.send_message("Continue the story. Use max 6-7 words.")
        ai_output = ai_input.text.strip()
        print("\n🧠 AI:", ai_output)

        if any(word in ai_output.lower() for word in ["died", "dead", "you are no more", "killed"]):
            print("💀 Game Over.")
            break

        user_input = input("\n🧍 You: ")
        response.send_message(user_input)

    except KeyboardInterrupt:
        print("\n👋 Game exited.")
        break
    except Exception as e:
        print(f"⚠️  An error occurred: {e}")
        break
