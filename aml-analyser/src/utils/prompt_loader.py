from pathlib import Path
import yaml
from typing import Dict, Any

BACKEND_DIR = Path(__file__).resolve().parents[2]

PROMPTS_DIR = BACKEND_DIR / "resources" / "prompts"

def load_prompt(agent_name: str, prompt_type: str) -> Dict[str, Any]:
    """
    Load system prompt YAML for a given agent.

    Args:
        agent_name: folder name under resource/prompts
                    e.g. "cdd_crp_analyser"
        prompt_type: system or user prompt

    Returns:
        Parsed YAML content
    """

    path = PROMPTS_DIR / agent_name / f"{prompt_type}.yaml"

    if not path.exists():
        raise FileNotFoundError(
            f"System prompt not found for agent '{agent_name}': {path}"
        )

    with path.open("r", encoding="utf-8") as f:
        return yaml.safe_load(f)