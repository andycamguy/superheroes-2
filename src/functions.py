from connection import execute_query

def get_all_heroes():
    query = """
        SELECT * FROM heroes;
    """
    returned_items = execute_query(query).fetchall()
    return returned_items

def add_hero(name, about_me, biography):
    query = """
        INSERT INTO heroes (name, about_me, biography)
        VALUES (%s, %s, %s)
    """
    params = (name, about_me, biography)
    execute_query(query, params)

def update_hero_biography(hero_id, new_biography):
    query = """
        UPDATE heroes
        SET biography = %s
        WHERE id = %s
    """
    params = (new_biography, hero_id)
    execute_query(query, params)

def delete_hero_by_name(hero_name):
    query = """
        DELETE FROM heroes
        WHERE name = %s;
    """
    params = (hero_name,)
    execute_query(query, params)
