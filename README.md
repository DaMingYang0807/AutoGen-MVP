# AutoGen-MVP
##AssistantAgent Multi-Agent Examples

This repository provides four examples demonstrating the use of the autogen_agentchat library to implement intelligent agent systems. Each example showcases unique scenarios involving single or multiple agents, tools, and team collaboration.

Features

	•	Single and Multi-Agent Scenarios: Examples include single-agent setups and multi-agent collaboration.
	•	Tool Integration: Agents utilize tools like stock price retrieval to enhance functionality.
	•	Interactive User Feedback: Simulated user input enables dynamic interactions.
	•	Task Handoff: Demonstrates fallback mechanisms when agents cannot complete tasks.

Examples Overview

File Name	Description
single_agent_stock_info.py	Single agent fetching stock information.
dual_agent_investment_advice.py	Dual agents collaborating to provide investment advice.
interactive_user_feedback.py	User interaction simulation with real-time feedback.
single_agent_task_handoff.py	Single agent transferring tasks to users when unresolved.

Prerequisites

	1.	Python 3.8+.
	2.	Install required dependencies:

pip install autogen-agentchat


	3.	Set environment variables for the OpenAI API:

export OPENAI_BASE_URL="https://your-api-url/v1"
export OPENAI_API_KEY="your-api-key"

How to Run

	1.	Clone the repository:

git clone https://github.com/your-username/assistant-agent-examples.git
cd assistant-agent-examples


	2.	Run any of the scripts:

python single_agent_stock_info.py

Key Concepts

	•	Agent Definition: Define agents with distinct roles using AssistantAgent.
	•	Team Collaboration: Use RoundRobinGroupChat to enable cooperation between agents.
	•	Termination Conditions: Control dialogue flow with triggers such as text mentions, message limits, or task handoffs.

Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request to improve these examples or add new ones.

License

This project is licensed under the MIT License.
