def get_all_heroes():
    query = """
        SELECT * FROM heroes;
    """
    returned_items = execute_query(query).fetchall()
    return returned_items