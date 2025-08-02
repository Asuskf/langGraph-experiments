from pathlib import Path
from pydantic_settings import BaseSettings
from pydantic import ValidationError
from pydantic import  field_validator
import logging
from typing import List

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")


class OpenAISettings(BaseSettings):
    """Pydantic model to validate OpenAI API key from environment variables."""
    OPENAI_API_KEY: str
    
    @field_validator("OPENAI_API_KEY")
    def check_api_key_prefix(cls, value: str) -> str:
        if not value.startswith("sk-proj-"):
            raise ValueError("The OPENAI_API_KEY exists but does not have the expected 'sk-proj-' prefix.")
        return value
    
    model_config = {
        "env_file": ".env",
        "env_prefix": "",
        "case_sensitive": True,
    }

class OpenAIEnvChecket:
    """Class responsible for checking the presence and validity of the .env file and API key."""
    def __init__(self, parent_dir: Path = Path(".")) -> None:
        self.parent_dir = parent_dir
        self.env_path = self.parent_dir / ".env"
    
    def check_env_file(self) -> None:
        """Check if the .env file exists and validate the OpenAI API key."""        
        if self.env_path.exists() and self.env_path.is_file():
            logging.info(".env file found.")
            self._validate_api_key()
        else:
            logging.error(f"The .env file was not found in the expected directory: '{self.parent_dir.resolve()}'")
            self._suggest_possible_misnamed_files()
            
    def _validate_api_key(self) -> None:
        """Validate the API key using Pydantic."""
        try:
            OpenAISettings()
            logging.info("✅ SUCCESS: OPENAI_API_KEY found and has the correct prefix.")
        except ValidationError as e:
            logging.warning(f"⚠️ OPENAI_API_KEY validation issue: {e}")
    
    def _suggest_possible_misnamed_files(self) -> None:
        """Suggest files that might be misnamed .env files."""
        possible_files: List[Path] = list(self.parent_dir.glob("*.env"))
        if possible_files:
            logging.warning("No '.env' file found, but the following files containing '.env' were detected:")
            for file in possible_files:
                logging.info(f" -> {file.name}")
                
if __name__ == "__main__":
    checker = OpenAIEnvChecket()
    checker.check_env_file()