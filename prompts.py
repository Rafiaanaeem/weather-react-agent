"""
prompts.py
Loads instructions from the prompt.md file and constructs a LangChain PromptTemplate.
"""

from langchain_core.prompts import PromptTemplate

def get_react_prompt() -> PromptTemplate:
    try:
        with open("prompt.md", "r", encoding="utf-8") as file:
            template_content = file.read()
            
        # Create a PromptTemplate.
        # Notice input_variables matches the dynamic fields used inside the ReAct framework
        prompt_template = PromptTemplate(
            template=template_content,
            input_variables=["input", "tools", "tool_names", "agent_scratchpad"]
        )
        return prompt_template
        
    except FileNotFoundError:
        raise FileNotFoundError("CRITICAL ERROR: 'prompt.md' was not found. Ensure it is in the project root directory.")