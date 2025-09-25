from langchain_community.agent_toolkits import create_sql_agent

from langchain_community.utilities import SQLDatabase
from config_llm import llm, embedding_model
from langchain_core.tools import tool
import sqlite3

#Khởi tạo db
db = SQLDatabase.from_uri(f"sqlite:///db/bookstore.db")
# print(db.get_usable_table_names())
# print(db.run("select * from Books limit 10"))

# Tạo tool xác thực tên sách
from langchain.agents.agent_toolkits import create_retriever_tool
from langchain_community.vectorstores import FAISS
import ast
#chuyen chuoi sang list
def str_to_list(chuoi):
    res_list = ast.literal_eval(chuoi)
    return [row[0] for row in res_list]

title = str_to_list(db.run("select title from Books"))

vectorstore = FAISS.from_texts(title, embedding=embedding_model)
retriever = vectorstore.as_retriever(search_type="similarity", search_kwargs={"k":5})
description = """Dùng để tra cứu các giá trị để lọc. Đầu vào là cách viết gần đúng với danh từ riêng của sách trong cửa hàng. Đầu ra là tên sách hợp lệ.
Hãy sử dụng danh từ có độ tương đồng cao nhất với từ được tìm kiếm."""

retriever_tool = create_retriever_tool(
    retriever,
    description=description,
    name="search_sach"
)

agent = create_sql_agent(llm=llm, 
                        db=db,
                        extra_tools=[retriever_tool],
                        agent_type="openai-tools",
                        # verbose=True,
                        )
# print(agent.invoke("Cho tôi xem những quyển sách thể loại thiếu nhi?"))

@tool
def agent_sql(input_text: str):
    """Truy vấn cơ sở dữ liệu sách qua ngôn ngữ tự nhiên"""
    return agent.invoke(input_text)

@tool
def create_order(book_id: int, customer_name: str, phone: str, address: str, quantity: int):
    """Lưu thông tin đơn hàng mới vào DB"""
    conn = sqlite3.connect("db/bookstore.db")
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO Orders (customer_name, phone, address, book_id, quantity, status) VALUES (?, ?, ?, ?, ?, ?)",
        (customer_name, phone, address, book_id, quantity, "pending")
    )
    conn.commit()
    conn.close()
    return f"✅ Đơn hàng {quantity} bản (book_id={book_id}) đã lưu cho {customer_name} có số {phone} và địa chỉ ở {address}."

