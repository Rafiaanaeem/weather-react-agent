# Weather Intelligence Agent

An advanced, interactive AI Agent built with LangChain and Llama 3.3 (via Groq) that autonomously fetches and analyzes real-time weather data. 

Unlike standard conversational Large Language Models, this agent utilizes Explicit Tool Binding and a custom ReAct (Reasoning + Acting) loop to connect to the external OpenWeather API, allowing it to ground its responses in real-time, real-world data.

---

## Key Features

* **High-Speed Inference:** Powered by Groq's LPU architecture and the `llama-3.3-70b-versatile` model for near-instant reasoning.
* **Native Tool Calling:** Implements modern LangChain Expression Language (LCEL) and `.bind_tools()` to seamlessly execute Python functions during conversation.
* **Smart Fallback Logic:** Features autonomous error-handling and input sanitization (e.g., automatically defaulting to 'Islamabad' if a user inputs a vague query like "today's weather").
* **Modular Prompt System:** Employs an isolated prompt management system using both markdown and Python configurations for structured persona enforcement.
* **Clean Separation of Concerns:** Rigid segregation between the orchestration engine (`main.py`), system definitions (`prompts.py`), and external API integrations (`tools.py`).

---

## Project Architecture

```text
weather_agent/
│
├── .vscode/             # Editor configurations and localized workspace settings.
├── main.py              # The orchestrator: Initializes the LLM, binds tools, and handles the chat loop.
├── tools.py             # External integrations: Contains the OpenWeather API logic and tool definitions.
├── config.py            # Configuration: Manages application-wide settings and provider fallback flags.
├── prompt.md            # Markdown System Prompt: Defines the raw structured persona of the agent.
├── prompts.py           # Python Prompt Manager: Handles programmatically loading or formatting system rules.
├── requirements.txt     # Dependencies: Exact library versions required for a reproducible environment.
├── .env                 # Environment Secrets: Private API credentials (GROQ and OpenWeather).
└── .gitignore           # Git Rules: Ensures sensitive and local system files are not committed to source control.

Prerequisites
Before running this project, ensure you have the following installed and configured:
Python 3.9+
A valid API Key from Groq
A valid API Key from OpenWeatherMap

3. Install Dependencies
pip install -r requirements.txt

4. Configure Environment Variables
Create a new file named .env in the root directory and add your secret keys exactly as shown below:

GROQ_API_KEY=your_groq_api_key_here
OPENWEATHER_API_KEY=your_openweather_api_key_here

Usage
Execute the core application script from your active terminal session:
python main.py