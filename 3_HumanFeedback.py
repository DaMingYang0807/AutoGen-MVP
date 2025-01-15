import os
import asyncio
from autogen_agentchat.agents import AssistantAgent, UserProxyAgent
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
    stock_agent = AssistantAgent(
        name="stock_agent",
        model_client=OpenAIChatCompletionClient(model="gpt-4o-mini-2024-07-18"),
        description="提供股票資訊的Agent。",
    )

    user_proxy = UserProxyAgent(
        name="user_proxy",
        input_func=lambda _: "我認為今天股價可能還會上漲。",
    )

    termination = TextMentionTermination("今晚睡公園") | MaxMessageTermination(4)

    interactive_team = RoundRobinGroupChat(participants=[stock_agent, user_proxy], termination_condition=termination)

    stream = interactive_team.run_stream(task="查詢 TSLA 的股價資訊並根據市場趨勢提供建議。")
    async for message in stream:
        print(message)

if __name__ == "__main__":
    asyncio.run(main())