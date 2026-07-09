"""
main.py
The main entry point for the ReAct Weather Agent.
Wires together the LLM, Tools, and Prompts using LangChain's modern AgentExecutor.
"""

from langchain_groq import ChatGroq
# Old: from langchain.agents import create_react_agent, AgentExecutor
from langchain_classic.agents import create_react_agent, AgentExecutor
import config  # Ensures API keys are loaded and validated first
from tools import weather_search
from prompts import get_react_prompt

def main():
    print("Initializing Weather Agent...")
    
    # 1. Initialize the LLM
    # We use ChatGroq with the specific Llama 3.3 model requested.
    llm = ChatGroq(
        temperature=0, # 0 means strict and deterministic (no hallucination)
        model_name="llama-3.1-8b-instant",
    )
    
    # 2. Prepare the Tools
    # We pass our custom tool inside a list. You can add more tools here later.
    tools = [weather_search]
    
    # 3. Load the Prompt
    prompt = get_react_prompt()
    
    # 4. Create the ReAct Agent
    # Note: We are using create_react_agent, which is the modern LangChain standard.
    # We DO NOT use the deprecated initialize_agent() function.
    agent = create_react_agent(llm=llm, tools=tools, prompt=prompt)
    
    # 5. Create the Agent Executor
    # verbose=False ensures the internal ReAct reasoning stays hidden from the user,
    # as per your project requirements. Only the final answer will be printed.
    # Set verbose=True temporarily if you ever need to debug the agent's thought process.
    agent_executor = AgentExecutor(
        agent=agent, 
        tools=tools, 
        verbose=False, 
        handle_parsing_errors=True # Gracefully handles formatting mistakes by the LLM
    )
    
    print("\n Weather Agent is ready! (Type 'exit' or 'quit' to stop)")
    print("-" * 50)
    
    # 6. Start the interactive chat loop
    while True:
        try:
            user_input = input("\nYou: ")
            if user_input.lower() in ['exit', 'quit']:
                print("Agent: Goodbye! Stay safe in the weather.")
                break
            
            if not user_input.strip():
                continue
                
            # Invoke the agent executor with the user's input
            response = agent_executor.invoke({"input": user_input})
            
            # Print ONLY the final output
            print(f"\nAgent: {response['output']}")
            
        except KeyboardInterrupt:
            # Handles Ctrl+C cleanly
            print("\nAgent: Goodbye!")
            break
        except Exception as e:
            print(f"\nAgent: Sorry, I encountered an unexpected error: {str(e)}")

if __name__ == "__main__":
    main()