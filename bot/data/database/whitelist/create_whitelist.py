def register_whitelist():
    """Создает белый список"""
    import sqlite3

    conn = sqlite3.connect('bot\data\database\whitelist\whitelist.db')
    cur = conn.cursor()

    cur.execute("""CREATE TABLE IF NOT EXISTS whitelist(
        number INT,
        userid INT PRIMARY KEY);
    """)
    conn.commit()
