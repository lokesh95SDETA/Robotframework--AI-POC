import json
import logging
from RobotFrameworkAI.modules.real_test_data_generator.test_data_generators.TestDataGenerator import TestDataGenerator

logger = logging.getLogger(__name__)

class GeneralTestDataGenerator(TestDataGenerator):
    """
    Generates any type of test data based on a user-provided prompt.
    """
    def __init__(self) -> None:
        super().__init__()
        self.type = "general"

    def create_prompt_messages(self, amount:int, format:str, kwargs:dict):
        """
        Constructs AI system and user messages dynamically.
        """
        prompt = kwargs.get("prompt", "Generate generic test data.")
        system_message = f"""
            You are a test data generator. Create {amount} test data entries based on the prompt below.
            Return JSON with a key 'test_data', and make sure the format is correct.
        """
        user_message = prompt
        return system_message, user_message

    def format_response(self, response):
        """
        Parses AI response and extracts structured test data.
        """
        response = response.message
        try:
            test_data = json.loads(response)
        except json.JSONDecodeError as e:
            error = f"Could not parse response: {response}. Error: {e}"
            logger.error(error)
            raise
        return test_data.get("test_data", [])
