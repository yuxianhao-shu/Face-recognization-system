import sqlite3
def init_db():
    """初始化数据库，创建用户表"""
    conn = sqlite3.connect("face_db.sqlite")
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS faces (
        user_id TEXT PRIMARY KEY,
        image_path TEXT
    )
    """)
    conn.commit()
    conn.close()

def register_user(user_id, image_path):
    """注册用户"""
    conn = sqlite3.connect("face_db.sqlite")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO faces (user_id, image_path) VALUES (?, ?)", (user_id, image_path))
    conn.commit()
    conn.close()

def get_all_users():
    """获取所有用户数据"""
    conn = sqlite3.connect("face_db.sqlite")
    cursor = conn.cursor()
    cursor.execute("SELECT user_id, image_path FROM faces")
    users = cursor.fetchall()
    conn.close()
    return users
