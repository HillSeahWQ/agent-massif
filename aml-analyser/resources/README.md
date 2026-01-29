# Resources Directory

This directory contains all structured output schemas and prompt templates for the AML Alert Analysis Agent System.

## Structure

```
resources/
├── prompts/
│   ├── cdd_crp_analyser                        # CDD/CRP Analyser Agent User and System prompt folder
│       ├── system.yaml
│       ├── user.yaml             
│   ├── transactions_history_analyser           # Transaction History Analyser Agent User and System prompt folder
│       ├── system.yaml
│       ├── user.yaml                   
│   ├── web_search_analyser                     # Web Search Analyser Agent User and System prompt folder
│       ├── system.yaml
│       ├── user.yaml            
│   ├── synthesis_analyser                      # Synthesis Analyser Agent User and System prompt folder
│       ├── system.yaml                      
│       ├── user.yaml            
│   ├── rfi_generator                           # RFI Generator Agent User and System prompt folder
│       ├── system.yaml
│       ├── user.yaml                 
│   └── resolution_generator                    # Resolution Outputs Generator Agent User and System prompt folder
│       ├── system.yaml
│       ├── user.yaml       
└── README.md                        # This file
```

## Usage

Each schema defines the expected structured output for its respective agent.
Each prompt template defines the system prompt and allows for dynamic data insertion.