import sqlalchemy
from sqlalchemy import create_engine, text

# SQLite 데이터베이스 파일 설정
DATABASE_URL = "sqlite:///test_database.db"
engine = create_engine(DATABASE_URL)

# 데이터베이스 테이블 생성 및 스키마 변경
with engine.connect() as conn:
    # branches 테이블 생성
    conn.execute(text("""
        CREATE TABLE IF NOT EXISTS branches (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            email TEXT NOT NULL
        );
    """))
    # products 테이블 생성 및 color 컬럼 추가
    conn.execute(text("""
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            color TEXT NOT NULL,
            code TEXT NOT NULL
        );
    """))
    # orders 테이블 생성
    conn.execute(text("""
        CREATE TABLE IF NOT EXISTS orders (
            id INTEGER PRIMARY KEY,
            order_date DATE NOT NULL,
            branch_id INTEGER NOT NULL,
            author TEXT NOT NULL,
            special_note TEXT,
            FOREIGN KEY (branch_id) REFERENCES branches(id)
        );
    """))
    # order_details 테이블 생성
    conn.execute(text("""
        CREATE TABLE IF NOT EXISTS order_details (
            id INTEGER PRIMARY KEY,
            order_id INTEGER NOT NULL,
            product_id INTEGER NOT NULL,
            quantity INTEGER NOT NULL,
            FOREIGN KEY (order_id) REFERENCES orders(id),
            FOREIGN KEY (product_id) REFERENCES products(id)
        );
    """))

print("Database and tables created successfully.")