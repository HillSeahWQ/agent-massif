from typing import Dict, Any, List
from jinja2 import Template


def _format_alert_information(alert_info: Dict[str, Any]) -> str:
    return "\n".join(
        f"- **{k}**: {v}"
        for k, v in alert_info.items()
    )


def _format_cdd_documents(files: List[Dict[str, Any]]) -> str:
    if not files:
        return "No CDD/CRP documents provided."

    blocks = []
    for idx, f in enumerate(files, 1):
        blocks.append(f"### Document {idx}: {f.get('filename', 'Unknown')}")
        blocks.append(f"- **Type**: {f.get('file_type', 'Unknown')}")
        blocks.append(f"- **Description**: {f.get('description', 'N/A')}")

        if "content" in f:
            blocks.append("\n**Content:**")
            blocks.append(f"```\n{f['content']}\n```")
        elif "summary" in f:
            blocks.append(f"\n**Summary:** {f['summary']}")

        blocks.append("")  # spacing

    return "\n".join(blocks)


def _format_rfi_options(rfi_list: List[str]) -> str:
    if not rfi_list:
        return "No predefined RFI options available."

    return "\n".join(
        f"{i}. {rfi}"
        for i, rfi in enumerate(rfi_list, 1)
    )


def build_cdd_crp_user_message(
    user_template: str,
    alert_information: Dict[str, Any],
    cdd_crp_files: List[Dict[str, Any]],
    rfi_list: List[str],
    additional_context: str = ""
) -> str:
    template = Template(user_template)

    return template.render(
        alert_information=_format_alert_information(alert_information),
        cdd_crp_documents=_format_cdd_documents(cdd_crp_files),
        rfi_options=_format_rfi_options(rfi_list),
        additional_context=additional_context
    )