import os
import asyncio
from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.base import Handoff
from autogen_agentchat.conditions import TextMentionTermination, HandoffTermination
from autogen_agentchat.teams import RoundRobinGroupChat
from autogen_ext.models.openai import OpenAIChatCompletionClient
from autogen_agentchat.ui import Console

os.environ["OPENAI_BASE_URL"] = "https://yunwu.ai/v1"
os.environ["OPENAI_API_KEY"] = "sk-g3xus7CKnnGTKKzL7DD26BjQXRUAwkzDwRk2gu9oLfGTKO9a"

model_client = OpenAIChatCompletionClient(
    model="gpt-4o-mini-2024-07-18"
)
async def main() -> None:
    stock_agent = AssistantAgent(
        name="stock_agent",
        model_client=OpenAIChatCompletionClient(model="gpt-4o-mini-2024-07-18"),
        description="提供股票資訊的Agent",
        system_message="當無法解答問題時，將問題移交給用戶。",
        handoffs=[Handoff(target="user", message="問題已移交給用戶。")],
    )

    termination = TextMentionTermination("今晚睡公園") | HandoffTermination(target="user")

    stock_team = RoundRobinGroupChat(participants=[stock_agent], termination_condition=termination)

    stream = stock_team.run_stream(task="查詢不存在的股票代碼 XYZ 的資訊。")
    async for message in stream:
        print(message)

if __name__ == "__main__":
    asyncio.run(main())