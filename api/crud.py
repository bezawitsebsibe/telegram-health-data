from api.database import get_connection

def get_top_products(limit=10):
    conn = get_connection()
    cur = conn.cursor()
    query = """
    SELECT product_name, COUNT(*) as mention_count
    FROM fct_messages
    GROUP BY product_name
    ORDER BY mention_count DESC
    LIMIT %s;
    """
    cur.execute(query, (limit,))
    results = cur.fetchall()
    cur.close()
    conn.close()
    return [{"product_name": r[0], "mention_count": r[1]} for r in results]

def get_channel_activity(channel_name):
    conn = get_connection()
    cur = conn.cursor()
    query = """
    SELECT channel_name, post_date, COUNT(*) as message_count
    FROM fct_messages
    WHERE channel_name = %s
    GROUP BY channel_name, post_date
    ORDER BY post_date;
    """
    cur.execute(query, (channel_name,))
    results = cur.fetchall()
    cur.close()
    conn.close()
    return [{"channel_name": r[0], "post_date": r[1].strftime("%Y-%m-%d"), "message_count": r[2]} for r in results]

def search_messages(query):
    conn = get_connection()
    cur = conn.cursor()
    query_sql = """
    SELECT message_id, channel_name, message_text
    FROM fct_messages
    WHERE message_text ILIKE %s
    LIMIT 50;
    """
    cur.execute(query_sql, ('%' + query + '%',))
    results = cur.fetchall()
    cur.close()
    conn.close()
    return [{"message_id": r[0], "channel_name": r[1], "message_text": r[2]} for r in results]
