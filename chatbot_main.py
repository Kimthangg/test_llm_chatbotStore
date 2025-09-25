from langchain.agents import create_tool_calling_agent, AgentExecutor
from langchain_core.prompts import ChatPromptTemplate
from config_llm import llm
from agent_sql import agent_sql, create_order

tools = [agent_sql, create_order]
# Tạo prompt template cho agent
prompt_template = ChatPromptTemplate.from_messages([
    ("system", """Bạn là một trợ lý AI thông minh có thể hỗ trợ nhận order và tra cứu thông tin sách.
Đây là lịch sử hội thoại giữa bạn và người dùng:
{chat_history}
Bạn có quyền truy cập vào các công cụ sau:
- sql_query_tool: Truy vấn cơ sở dữ liệu sách qua ngôn ngữ tự nhiên
- create_order: Tạo đơn hàng sách từ thông tin khách cung cấp
Hãy sử dụng các công cụ này một cách thông minh để trả lời câu hỏi của người dùng.
Khi hỏi về sách, hãy sử dụng sql_query_tool.
Khi nhận order sách, hãy hỏi đầy đủ thông tin về tên sách, số lượng, địa chỉ, số điện thoại.
Khi có đầy đủ thông tin hãy xác nhận lại với khách và tạo đơn hàng bằng công cụ create_order.
Luôn trả lời bằng tiếng Việt một cách thân thiện và chi tiết."""),
    ("human", "{input}"),
    ("placeholder", "{agent_scratchpad}")
])

# Tạo agent với tools
agent = create_tool_calling_agent(
    llm=llm,
    tools=tools,
    prompt=prompt_template
)
#Tạo bộ nhớ cho agent
from langchain.memory import ConversationBufferMemory
memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
# Tạo AgentExecutor
agent_executor = AgentExecutor(
    agent=agent,
    memory=memory,
    tools=tools,
    # verbose=True,
    handle_parsing_errors=True,
    max_iterations=5
)

#Demo chat với agent
while True:
    #câu lệnh người dùng
    query = input("USER: ")
    #respon của chatbot
    result = agent_executor.invoke({"input": query})
    print('BOT: ',result["output"])
