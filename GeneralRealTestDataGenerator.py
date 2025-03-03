import logging
from robot.api.deco import keyword, library
from RobotFrameworkAI.modules.Module import Module
from RobotFrameworkAI.modules.real_test_data_generator.test_data_generators.GeneralTestDataGenerator import GeneralTestDataGenerator
import importlib
import inspect
import os
import pkgutil

logger = logging.getLogger(__name__)

@library
class GeneralRealTestDataGenerator(Module):
    """
    Generates any type of test data based on user prompts, using AI.
    """
    def __init__(self) -> None:
        super().__init__()
        self.module_name = "general_real_test_data_generator"
        self.generator = GeneralTestDataGenerator()
        self.ai_tool = "text_generator"

    @keyword
    def generate_general_test_data(
            self,
            ai_model: str = "openai",
            model: str = "gpt-4o",
            prompt: str = "Generate real test data.",
            amount: int = 3,
            format: str = None,
            max_tokens: int = 512,
            temperature: float = 1.0,
            top_p: float = 1.0,
            frequency_penalty: float = 0,
            presence_penalty: float = 0,
            **kwargs
    ):
        """
        Generates test data based on a custom prompt.

        Arguments:
        - ai_model: AI model to use (default: "openai")
        - model: Specific AI model version (default: "gpt-3.5-turbo")
        - prompt: The user-defined prompt describing the test data to generate
        - amount: Number of test data entries to generate (default: 3)
        - format: Optional format specification
        - max_tokens: Maximum token limit (default: 512)
        - temperature: AI creativity level (default: 1.0)
        - top_p: Probability sampling threshold (default: 1.0)
        - frequency_penalty: Penalizes frequent tokens (default: 0)
        - presence_penalty: Encourages diversity in responses (default: 0)
        """
        logger.debug(f"Generating test data using prompt: {prompt}")

        system_message, user_message = self.generator.create_prompt_messages(amount, format, {"prompt": prompt})

        ai_prompt = self.create_prompt(
            self.ai_tool,
            ai_model,
            system_message,
            user_message,
            history=None,
            model=model,
            max_tokens=max_tokens,
            temperature=temperature,
            top_p=top_p,
            frequency_penalty=frequency_penalty,
            presence_penalty=presence_penalty,
            response_format={"type": "json_object"}  # Ensures JSON output
        )

        try:
            response = self.ai_interface.call_ai_tool(ai_prompt)
            return self.generator.format_response(response)
        except Exception as e:
            raise ValueError(f"Failed to generate test data: {e}")