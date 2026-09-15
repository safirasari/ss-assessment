import sqlite3

def get_pending_customers():
    conn = sqlite3.connect('parts_avatar.db')
    cursor = conn.cursor()
    
    # Task: Select customer email and order_date where status is 'Pending'.
    query = """
    SELECT c.email AND o.order_date 
    FROM Customers c
    From Orders o
    WHERE o.status='Pending'
    JOIN Orders o ON c.customer_id = o.customer_id;

    -- WRITE YOUR SQL HERE 
    """

    
    cursor.execute(query)
    return cursor.fetchall()