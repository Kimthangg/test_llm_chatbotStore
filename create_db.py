import sqlite3
import os

# Create db directory if it doesn't exist
if not os.path.exists('db'):
    os.makedirs('db')

# Connect to database
conn = sqlite3.connect('db/bookstore.db')
cursor = conn.cursor()

# Create Books table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Books (
        book_id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        author TEXT NOT NULL,
        price REAL NOT NULL,
        stock INTEGER NOT NULL,
        category TEXT NOT NULL
    )
''')

# Create Orders table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Orders (
        order_id INTEGER PRIMARY KEY AUTOINCREMENT,
        customer_name TEXT NOT NULL,
        phone TEXT NOT NULL,
        address TEXT NOT NULL,
        book_id INTEGER NOT NULL,
        quantity INTEGER NOT NULL,
        status TEXT NOT NULL,
        FOREIGN KEY (book_id) REFERENCES Books (book_id)
    )
''')
# Clear existing data
cursor.execute('DELETE FROM Books')

# Insert 100 Vietnamese books
books_data = [
    ('Số đỏ', 'Vũ Trọng Phụng', 120000, 0, 'Tiểu thuyết'),
    ('Tắt đèn', 'Ngô Tất Tố', 95000, 30, 'Tiểu thuyết'),
    ('Truyện Kiều', 'Nguyễn Du', 150000, 40, 'Truyện thơ'),
    ('Lão Hạc', 'Nam Cao', 85000, 35, 'Truyện ngắn'),
    ('Vợ nhặt', 'Kim Lân', 90000, 28, 'Truyện ngắn'),
    ('Chí Phèo', 'Nam Cao', 80000, 32, 'Truyện ngắn'),
    ('Những đứa con trong gia đình', 'Nguyễn Thi', 110000, 22, 'Tiểu thuyết'),
    ('Đời thừa', 'Nam Cao', 75000, 26, 'Truyện ngắn'),
    ('Bước đường cùng', 'Nguyễn Công Hoan', 105000, 18, 'Tiểu thuyết'),
    ('Tôi thấy hoa vàng trên cỏ xanh', 'Nguyễn Nhật Ánh', 125000, 45, 'Thiếu nhi'),
    ('Mắt biếc', 'Nguyễn Nhật Ánh', 115000, 38, 'Tiểu thuyết'),
    ('Có hai con mèo ngồi bên cửa sổ', 'Nguyễn Nhật Ánh', 135000, 33, 'Thiếu nhi'),
    ('Dế mèn phiêu lưu ký', 'Tô Hoài', 98000, 42, 'Thiếu nhi'),
    ('Con chó nhỏ mang giỏ hoa hồng', 'Nguyễn Nhật Ánh', 130000, 29, 'Thiếu nhi'),
    ('Ngôi trường mọi khi', 'Nguyễn Nhật Ánh', 120000, 31, 'Thiếu nhi'),
    ('Những ngày thơ ấu', 'Nguyễn Nhật Ánh', 110000, 24, 'Thiếu nhi'),
    ('Cánh đồng bất tận', 'Nguyễn Ngọc Tư', 140000, 20, 'Truyện ngắn'),
    ('Người lái đò sông Đà', 'Nguyễn Tuân', 88000, 27, 'Truyện ngắn'),
    ('Rừng xà nu', 'Nguyễn Trung Thành', 155000, 16, 'Tiểu thuyết'),
    ('Tuyển tập truyện ngắn Nam Cao', 'Nam Cao', 165000, 21, 'Tuyển tập'),
    
    ('Hoa sữa', 'Nguyễn Minh Châu', 92000, 35, 'Truyện ngắn'),
    ('Chiếc thúng đầy dứa', 'Nguyễn Nhật Ánh', 118000, 40, 'Thiếu nhi'),
    ('Tôi là Bêtô', 'Nguyễn Nhật Ánh', 122000, 36, 'Thiếu nhi'),
    ('Làng', 'Kim Lân', 88000, 29, 'Truyện ngắn'),
    ('Gió lạnh đầu mùa', 'Thạch Lam', 95000, 33, 'Truyện ngắn'),
    ('Nắng đồng bằng', 'Nguyễn Minh Châu', 105000, 28, 'Truyện ngắn'),
    ('Vang bóng một thời', 'Nguyễn Tuân', 98000, 31, 'Truyện ngắn'),
    ('Đoàn thuyền đánh cá', 'Nguyễn Minh Châu', 102000, 26, 'Truyện ngắn'),
    ('Những đứa trẻ đu đưa', 'Nguyễn Nhật Ánh', 128000, 38, 'Thiếu nhi'),
    ('Kính vạn hoa', 'Nguyễn Nhật Ánh', 135000, 42, 'Thiếu nhi'),
    
    ('Đất rừng phương Nam', 'Đoàn Giỏi', 145000, 24, 'Tiểu thuyết'),
    ('Sông Đà', 'Nguyễn Tuân', 92000, 30, 'Truyện ngắn'),
    ('Thép đã tôi thế đấy', 'Nikolai Ostrovsky', 156000, 19, 'Tiểu thuyết'),
    ('Việt Bắc', 'Tố Hữu', 85000, 35, 'Thơ'),
    ('Đồng chí', 'Chính Hữu', 78000, 32, 'Thơ'),
    ('Người mẹ cầm súng', 'Nguyễn Khải', 112000, 27, 'Tiểu thuyết'),
    ('Những cánh buồm', 'Võ Thị Xuân Hà', 96000, 31, 'Truyện ngắn'),
    ('Đất nước đứng lên', 'Nguyễn Đình Thi', 89000, 29, 'Thơ'),
    ('Tiếng hát con tàu', 'Che Lan Viên', 82000, 34, 'Thơ'),
    ('Những bài thơ về Bác Hồ', 'Tố Hữu', 95000, 37, 'Thơ'),
    
    ('Tôi kể em nghe', 'Nguyễn Nhật Ánh', 125000, 41, 'Thiếu nhi'),
    ('Cô gái đến từ hôm qua', 'Nguyễn Nhật Ánh', 132000, 39, 'Thiếu nhi'),
    ('Buổi học cuối cùng', 'Nguyễn Nhật Ánh', 115000, 33, 'Thiếu nhi'),
    ('Thằng quỷ nhỏ', 'Nguyễn Nhật Ánh', 108000, 36, 'Thiếu nhi'),
    ('Lá nằm trong lá', 'Nguyễn Nhật Ánh', 120000, 32, 'Thiếu nhi'),
    ('Cây cam ngọt của tôi', 'José Mauro de Vasconcelos', 148000, 25, 'Thiếu nhi'),
    ('Hoàng tử bé', 'Antoine de Saint-Exupéry', 89000, 45, 'Thiếu nhi'),
    ('Những cuộc phiêu lưu của Tom Sawyer', 'Mark Twain', 135000, 28, 'Thiếu nhi'),
    ('Cuộc phiêu lưu của Huckleberry Finn', 'Mark Twain', 142000, 26, 'Thiếu nhi'),
    ('Alice lạc vào xứ sở thần tiên', 'Lewis Carroll', 118000, 34, 'Thiếu nhi'),
    
    ('Cánh đồng hoang', 'Nguyễn Ngọc Tư', 128000, 22, 'Truyện ngắn'),
    ('Sông mặc áo mưa', 'Nguyễn Ngọc Tư', 135000, 20, 'Truyện ngắn'),
    ('Thị', 'Nguyễn Ngọc Tư', 125000, 24, 'Truyện ngắn'),
    ('Cánh đồng bất tận 2', 'Nguyễn Ngọc Tư', 142000, 18, 'Truyện ngắn'),
    ('Người con gái Nam Xương', 'Nguyễn Huy Thiệp', 115000, 26, 'Truyện ngắn'),
    ('Tướng về hưu', 'Nguyễn Huy Thiệp', 108000, 29, 'Truyện ngắn'),
    ('Muối của rừng', 'Nguyễn Huy Thiệp', 112000, 27, 'Truyện ngắn'),
    ('Con chim xanh biếc bay về', 'Nguyễn Nhật Ánh', 138000, 35, 'Tiểu thuyết'),
    ('Cảm ơn người lớn', 'Nguyễn Nhật Ánh', 126000, 31, 'Thiếu nhi'),
    ('Tôi có một ước mơ', 'Nguyễn Nhật Ánh', 119000, 33, 'Thiếu nhi'),
]

cursor.executemany('''
    INSERT INTO Books (title, author, price, stock, category)
    VALUES (?, ?, ?, ?, ?)
''', books_data)

# Commit changes and close connection
conn.commit()
conn.close()
