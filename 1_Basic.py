import os
import asyncio
from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.conditions import TextMentionTermination
from autogen_agentchat.teams import RoundRobinGroupChat
from autogen_ext.models.openai import OpenAIChatCompletionClient
from autogen_agentchat.base import TaskResult
from autogen_agentchat.ui import Console

os.environ["OPENAI_BASE_URL"] = "https://yunwu.ai/v1"
os.environ["OPENAI_API_KEY"] = "sk-g3xus7CKnnGTKKzL7DD26BjQXRUAwkzDwRk2gu9oLfGTKO9a"

# 工具函數: 提供股票資訊
async def get_stock(stock: str) -> str:
    return f"The stock {stock} is currently at $150, with a 2% increase today."

async def main() -> None:
    stock_agent = AssistantAgent(
        name="stock_agent",
        model_client=OpenAIChatCompletionClient(model="gpt-4o-mini-2024-07-18"),
        description="提供股票資訊的Agent",
        tools=[get_stock],
    )

    termination = TextMentionTermination("今晚睡公園")

    stock_team = RoundRobinGroupChat(participants=[stock_agent], termination_condition=termination)

    result = await stock_team.run(task="查詢 AAPL 的股價資訊。")
    print(result)

if __name__ == "__main__":
    asyncio.run(main())