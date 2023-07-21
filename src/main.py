from psycopg import connect, OperationalError
from connection import create_connection, execute_query
from functions import get_all_heroes
if __name__ == "__main__":
    all_heroes = get_all_heroes()

    # Process the retrieved data as needed
    for hero in all_heroes:
        hero_id = hero[0]
        hero_name = hero[1]
        about_me = hero[2]
        biography = hero[3]
        image_url = hero[4]  # This might be None if not provided in the INSERT statement

        
        print(f"Hero ID: {hero_id}, Name: {hero_name}, About Me: {about_me}, Biography: {biography}, Image URL: {image_url}")