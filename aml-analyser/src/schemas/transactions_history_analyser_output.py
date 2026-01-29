"""
Transaction History Analyser Agent Output Schema

Defines the structured output format for transaction history analysis.
"""

from typing import List, Optional, Dict, Any
from datetime import date
from pydantic import BaseModel, Field
from datetime import datetime
from enum import Enum


class RiskLevel(str, Enum):
    """Risk level enumeration"""
    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"
    UNKNOWN = "UNKNOWN"


class TransactionPattern(BaseModel):
    """Suspicious or significant transaction pattern"""
    pattern_type: str = Field(..., description="Type of pattern (e.g., 'Structuring', 'Round Amount', 'Rapid Movement')")
    severity: RiskLevel = Field(..., description="Severity level of this pattern")
    description: str = Field(..., description="Detailed description of the pattern")
    transaction_ids: List[str] = Field(default_factory=list, description="Related transaction IDs")
    date_range: Optional[Dict[str, date]] = Field(
        None,
        description="Start and end date of when the pattern was observed"
    )
    
    # Specific pattern indicators
    frequency_anomaly: Optional[bool] = Field(None, description="Whether there's an unusual frequency")
    amount_anomaly: Optional[bool] = Field(None, description="Whether there's an unusual amount pattern")
    timing_anomaly: Optional[bool] = Field(None, description="Whether there's unusual timing")


class RuleTriggeredAnalysis(BaseModel):
    """Analysis of why the specific rule was triggered"""
    rule_id: str = Field(..., description="ID of the triggered rule")
    rule_description: str = Field(..., description="Description of what the rule detects")
    supporting_transactions: List[str] = Field(default_factory=list, description="Transaction IDs that caused the trigger")
    threshold_breached: Optional[Dict[str, Any]] = Field(None, description="Details of threshold breached (e.g., amount, count)")


class THAnalysisOutput(BaseModel):
    """Complete output schema for Transaction History Analyser Agent"""

    # High-level Narrative Summary
    transaction_summary: str = Field(
        ...,
        description=(
            "A concise but comprehensive narrative description of the transaction history Excel, "
            "including what rule triggered the analysis, overall transaction behaviour, inflow vs outflow characteristics, notable trends "
            "or anomalies, key counterparties, and any high-level patterns observed."
        )
    )

    # Rule Analysis
    rule_triggered_analysis: RuleTriggeredAnalysis = Field(
        ...,
        description="Analysis of the specific rule that triggered this alert"
    )

    # Counterparty Analysis
    counterparties: List[str] = Field(
        default_factory=list,
        description="List of counterparties the investigated company transacted with"
    )
    
    # Pattern Analysis
    suspicious_patterns: List[TransactionPattern] = Field(
        default_factory=list,
        description=(
            "Suspicious or significant transaction patterns identified based on AML rules. "
            "Leave empty if no suspicious patterns are identified."
        )
    )
    
    # Risk Assessment
    overall_transaction_risk: RiskLevel = Field(..., description="Overall risk level based on transaction analysis")
    
    # Key Findings
    key_findings: List[str] = Field(
        default_factory=list,
        description="Key findings from transaction history analysis"
    )
    red_flags: List[str] = Field(
        default_factory=list,
        description=(
            "Transaction-related red flags identified"
            "Leave empty if no red flags are present."
        )
    )
    
    # Metadata
    data_source: str = Field(..., description="Source of transaction data (e.g., 'Core Banking System')")
    analysis_timestamp: datetime  = Field(
        default_factory=lambda: datetime.utcnow().isoformat(),
        description="Timestamp when analysis was completed"
    )
    
    # Additional Context
    notes: Optional[str] = Field(None, description="Any additional notes or context from the analysis")