# config.py
import os
from dotenv import load_dotenv

load_dotenv()

INSTANCE_ID    = os.getenv("GREEN_API_INSTANCE_ID")
API_TOKEN      = os.getenv("GREEN_API_API_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
DATABASE_URL   = os.getenv("DATABASE_URL")

for var in ("INSTANCE_ID", "API_TOKEN", "OPENAI_API_KEY", "DATABASE_URL"):
    if not globals()[var]:
        raise RuntimeError(f"Environment variable {var} is not set")
