from functions import get_all_heroes, add_hero, update_hero_biography, delete_hero_by_name 
from connection import execute_query
def print_heroes(heroes):
    for hero in heroes:
        hero_id, name, about_me, biography, _ = hero
        print(f"ID: {hero_id}, Name: {name}, About Me: {about_me}, Biography: {biography}")

def add_new_hero():
    name = input("Enter the hero's name: ")
    about_me = input("Enter a short description (about me): ")
    biography = input("Enter the hero's biography: ")

    # Add hero to the database
    add_hero(name, about_me, biography)

    # Get the newly added hero's ID
    all_heroes = get_all_heroes()
    hero_id = all_heroes[-1][0]

    # Add hero's abilities to the database
    abilities = []
    while True:
        ability = input("Enter an ability (or type 'done' to finish): ")
        if ability.lower() == 'done':
            break
        abilities.append(ability)

    # Add hero's abilities to the database
    for ability in abilities:
        add_ability(hero_id, ability)

def add_ability(hero_id, ability):
    # Check if the ability is valid and get its ID from the ability_types table
    query = """
        SELECT id FROM ability_types WHERE name = %s;
    """
    params = (ability,)
    result = execute_query(query, params).fetchone()

    if result:
        ability_id = result[0]

        # Insert the ability with the correct ability_type_id
        query = """
            INSERT INTO abilities (hero_id, ability_type_id)
            VALUES (%s, %s)
        """
        params = (hero_id, ability_id)
        execute_query(query, params)

    else:
        print(f"Ability '{ability}' not found in the database. Skipping...")

def update_hero_relationship():
    all_heroes = get_all_heroes()
    print_heroes(all_heroes)

    hero_id = int(input("Enter the hero's ID to update their biography: "))
    new_biography = input("Enter the new biography: ")

    # Update the hero's biography in the database
    update_hero_biography(hero_id, new_biography)
    print("Hero's biography updated successfully!")

def print_hero(hero_data):
    hero_id = hero_data[0]
    hero_name = hero_data[1]
    about_me = hero_data[2]
    biography = hero_data[3]
    is_friend = hero_data[5]

    print("--- HERO DETAILS ---")
    print(f"Hero ID: {hero_id}")
    print(f"Name: {hero_name}")
    print(f"About Me: {about_me}")
    print(f"Biography: {biography}")
    print(f"Is Friend: {'Yes' if is_friend else 'No'}")

def view_hero():
    hero_name = input("Enter the hero's name to view details: ")

    hero_data = get_hero_by_name(hero_name)

    if hero_data:
        print_hero(hero_data)
    else:
        print(f"Hero '{hero_name}' not found in the database.")

def delete_hero():
    all_heroes = get_all_heroes()
    print_heroes(all_heroes)

    hero_name = input("Enter the hero's name to delete: ")

    # Delete the hero from the database
    delete_hero_by_name(hero_name)
    print("Hero deleted successfully!")

if __name__ == "__main__":
    while True:
        print("\n--- HERO DATABASE MENU ---")
        print("1. View all heroes")
        print("2. View a specific hero")
        print("3. Add a new hero")
        print("4. Update a hero's biography")
        print("5. Delete a hero")
        print("6. Exit")

        choice = input("Enter your choice (1/2/3/4/5/6): ")

        if choice == '1':
            all_heroes = get_all_heroes()
            print_heroes(all_heroes)

        elif choice == '2':
            view_hero()

        elif choice == '3':
            add_new_hero()

        elif choice == '4':
            update_hero_relationship()

        elif choice == '5':
            delete_hero()

        elif choice == '6':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")
