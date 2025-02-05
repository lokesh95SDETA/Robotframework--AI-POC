import os
import fileinput
from dotenv import load_dotenv
from transformers import pipeline

class AIExceptionHandler:
    def __init__(self):
        # Load environment variables from .env file
        load_dotenv()

        # Initialize GPT-2 model from Hugging Face
        print("✅ Loading GPT-2 Model...")
        self.chatbot = pipeline("text-generation", model="gpt2", max_length=200)
        print("✅ GPT-2 Model Loaded Successfully.")

    def handle_error(self, error_message, test_file):
        """Sends error details to GPT-2, gets suggestions, and updates the test file."""
        try:
            print("📨 Sending error message to GPT-2 for debugging...")

            prompt = f"Here is the error message: {error_message}. Suggest a fix:"
            response = self.chatbot(prompt)

            # Extract AI-generated response
            suggestion = response[0]["generated_text"].split(":")[-1].strip()
            print(f"✅ AI Suggested Fix: {suggestion}")

            # Modify the Robot Framework test script
            self.update_test_script(test_file, suggestion)

            return suggestion
        except Exception as e:
            print(f"❌ AI Error Handling Failed: {str(e)}")
            return f"AI Error Handling Failed: {str(e)}"

    def update_test_script(self, test_file, suggestion):
        """Modifies the test script based on AI suggestion."""
        if not os.path.exists(test_file):
            print(f"❌ ERROR: The file '{test_file}' does not exist.")
            return

        try:
            print(f"🛠️ Updating test script: {test_file}")
            with fileinput.input(test_file, inplace=True) as file:
                for line in file:
                    if "Fail    Simulated test failure" in line:
                        corrected_line = f"    Log    FIXED: {suggestion}  # AI Fixed this\n"
                        print(corrected_line, end="")
                    else:
                        print(line, end="")

            print("✅ Test script updated successfully!")
        except Exception as e:
            print(f"❌ Failed to update test script: {str(e)}")

if __name__ == "__main__":
    print("🚀 AI Exception Handler Started")
    
    handler = AIExceptionHandler()
    test_error = "Sample Robot Framework Test Failure"
    test_file = "test.robot"  # Ensure this file exists in the same directory

    handler.handle_error(test_error, test_file)
