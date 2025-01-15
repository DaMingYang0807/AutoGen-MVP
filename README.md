# AutoGen-MVP

This repository provides four examples demonstrating the use of the autogen_agentchat library to implement intelligent agent systems. Each example showcases unique scenarios involving single or multiple agents, tools, and team collaboration.

Features

	•	Single and Multi-Agent Scenarios: Examples include single-agent setups and multi-agent collaboration.
	•	Tool Integration: Agents utilize tools like stock price retrieval to enhance functionality.
	•	Interactive User Feedback: Simulated user input enables dynamic interactions.
	•	Task Handoff: Demonstrates fallback mechanisms when agents cannot complete tasks.

Prerequisites

	1.	Python 3.8+.
	2.	Install required dependencies:

pip install autogen-agentchat


	3.	Set environment variables for the OpenAI API:

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

Reference

This repository builds upon the ideas explored in my initial trial of the autogen library, which can be found in the [AutoGenV04Test]([(https://github.com/NanGePlus/AutoGenV04Test/tree/main)](https://github.com/NanGePlus/AutoGenV04Test/tree/main)) repository. 
That project served as the foundation for understanding the potential of multi-agent systems and shaped the approach used in these examples.
