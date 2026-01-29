from typing import Dict, Any

from langchain_google_vertexai import ChatVertexAI
from langchain.schema import SystemMessage, HumanMessage
from langchain.output_parsers import PydanticOutputParser

from utils.prompt_loader import load_prompt
from utils.schema_loader import load_output_schema
from agents.cdd_crp_analyser.user_message_builder import (
    build_cdd_crp_user_message
)


class CDDCRPAnalyserAgent:
    """
    CDD / CRP Analyser Agent
    """

    def __init__(
        self,
        model_name: str = "gemini-1.5-pro",
        temperature: float = 0.0,
        project: str | None = None,
        location: str | None = None,
    ):
        # Load prompts
        self.system_cfg = load_prompt("cdd_crp_analyser", "system")
        self.user_cfg = load_prompt("cdd_crp_analyser", "user")

        # Load output schema
        self.output_schema = load_output_schema(
            "schemas.cdd_crp_analyser_output.CDDCRPAnalysisOutput"
        )

        self.parser = PydanticOutputParser(
            pydantic_object=self.output_schema
        )

        # LLM
        self.llm = ChatVertexAI(
            model_name=model_name,
            temperature=temperature,
            project=project,
            location=location,
        )

    def run(
        self,
        alert_info: Dict[str, Any],
        cdd_files: list[Dict[str, Any]],
        rfi_list: list[str],
        additional_context: str = "",
    ) -> Any:
        """
        Run CDD/CRP analysis.
        """

        user_message = build_cdd_crp_user_message(
            user_template=self.user_cfg["template"],
            alert_information=alert_info,
            cdd_crp_files=cdd_files,
            rfi_list=rfi_list,
            additional_context=additional_context,
        )

        messages = [
            SystemMessage(content=self.system_cfg["prompt"]),
            HumanMessage(content=user_message),
        ]

        # Call LLM
        response = self.llm(messages)

        # Parse + validate output
        return self.parser.parse(response.content)
