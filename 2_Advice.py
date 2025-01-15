import os
import asyncio
from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.conditions import MaxMessageTermination, TextMentionTermination
from autogen_agentchat.teams import RoundRobinGroupChat
from autogen_ext.models.openai import OpenAIChatCompletionClient
from autogen_agentchat.ui import Console



os.environ["OPENAI_BASE_URL"] = "https://yunwu.ai/v1"
os.environ["OPENAI_API_KEY"] = "sk-g3xus7CKnnGTKKzL7DD26BjQXRUAwkzDwRk2gu9oLfGTKO9a"

model_client = OpenAIChatCompletionClient(
    model="gpt-4o-mini-2024-07-18"
)

async def main() -> None:
    primary_agent = AssistantAgent(
        name="primary",
        model_client=OpenAIChatCompletionClient(model="gpt-4o-mini-2024-07-18"),
        system_message="你是一个提供股票投資建議的助理。",
    )

    critic_agent = AssistantAgent(
        name="critic",
        model_client=OpenAIChatCompletionClient(model="gpt-4o-mini-2024-07-18"),
        system_message="你是一个提供投資建議的sell side分析師",
    )

    termination = TextMentionTermination("今晚睡公園") | MaxMessageTermination(5)

    stock_team = RoundRobinGroupChat(participants=[primary_agent, critic_agent], termination_condition=termination)

    async for message in stock_team.run_stream(task="對 AAPL 給出 buy/hold/sell 建議。"):
        print(message)

if __name__ == "__main__":
    asyncio.run(main())
