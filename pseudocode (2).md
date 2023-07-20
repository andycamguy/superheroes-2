# Where do I begin? What am I doing?

No idea, so ask lots of questions.

Create an interactive shell script with the help of python that helps superheroes stay in touch with their friends and keep track of supervillains through the terminal.
For this project, we will be using Python 3 and PostgreSQL and the PyPi package psycopg3.

I don't have docker and cannot install it due to hardware and software constraints

# Procedural
### user stories
 - As a superhero, I want to add new friends to my network so that I can keep in touch with them and strengthen our alliance against supervillains.

- As a superhero, I want to view a list of all my friends (superheroes) and foes (villains) in the database so that I can keep track of them and their current status.
- As a superhero, I want to update the type (hero/villain) of my friends in the database, so I can ensure accurate information about their alignment and activities.
- As a superhero, I want the interactive shell script to maintain data consistency in the database, ensuring that no duplicate entries or invalid data is allowed.
- As a superhero, I want the interactive shell script to provide a smooth and efficient user experience, minimizing delays in data retrieval and processing, so I can focus on protecting the world.


## Begin

Connect to the PostgreSQL Database: At the beginning, the program establishes a connection to the PostgreSQL database. This step ensures that the script can communicate with the database for data storage and retrieval.

## Init
Create a Table for Superheroes and Villains: Once connected to the database, the script initializes the project by creating a table named "heroes_villains." This table will store information about superheroes and villains, such as their names and types.

Questions:
Who are the superheroes? where will the data be drawn from?

## Render
- Provide an Interactive Shell Interface for Users: After setting up the database, the script presents an interactive shell interface to the users. This interface allows users to interact with the database through the terminal using various commands.
  *Note* there will only be interactivity in the terminal and no where else. queries will be made using sql

## Compute

## END

# Flowchart 
```
                      +-------------------------------+
                      |       Begin: Connect DB       |
                      +-------------------------------+
                                  |
                                  v
                      +-------------------------------+
                      | Initialize: Create Table     |
                      +-------------------------------+
                                  |
                                  v
                      +-------------------------------+
                      |         Render: Shell         |
                      |                               |
                      |  +-------------------------+  |
                      |  | Display Options         |  |
                      |  +-------------------------+  |
                      |             |                 |
                      |             v                 |
                      |  +-------------------------+  |
                      |  | User Input and Action   |  |
                      |  +-------------------------+  |
                      |             |                 |
                      v             v                 |
          +------------------+   +------------------+  |
          | Update Database |   | Show Data         |  |
          +------------------+   +------------------+
```

# Functional 

```
function create table
{
if table name doesn't exist, make the table with the name
}
function make a hero
{
add a hero and values with it

}
function add relationships
{
if a friend of a hero, build a link on grounds of being an ally

if an enemy of a hero, build a link on grounds of being an enemy
}

function add abilities
{
if a hero exists claiming of having an ability, connect it otherwise ignore
}


```

# Object Oriented
```
Class Hero:
    Attribute name
    Attribute hero_type
    Attribute friends: List of Hero
    Attribute enemies: List of Hero
    Attribute abilities: List of Ability

    Method add_friend(friend: Hero):
        Add friend to friends list

    Method add_enemy(enemy: villain):
        Add enemy to enemies list

    Method add_ability(ability: Ability):
        Add ability to abilities list


Class Ability:
    Attribute name
    Attribute description


Class Villain:
    Attribute name
    Attribute friends: List of Villain
    Attribute enemies: List of Hero
    Attribute abilities: List of Ability
```
# Chat GPT Advice Procedural
Begin:

Connect to the PostgreSQL Database: At the beginning, the program establishes a connection to the PostgreSQL database. This step ensures that the script can communicate with the database for data storage and retrieval.

Initialize:

Create a Table for Superheroes and Villains: Once connected to the database, the script initializes the project by creating a table named "heroes_villains." This table will store information about superheroes and villains, such as their names and types.

Render:

- Provide an Interactive Shell Interface for Users: After setting up the database, the script presents an interactive shell interface to the users. This interface allows users to interact with the database through the terminal using various commands.

X Options Display: In the interactive shell, the available options are displayed to the users. These options represent the CRUD operations (Create, Read, Update, Delete) that they can perform on the superhero and villain data.

User Input and Action: Users are prompted to enter their choice (1/2/3/4/5) based on the displayed options. The script takes the user's input and proceeds accordingly:

Option 1: Add Hero/Villain - Users can input the name and type (hero/villain) of a new superhero or villain, which will be added to the database.
Option 2: View All Heroes/Villains - The script retrieves all the superheroes and villains from the database and displays them in a formatted manner.
Option 3: Update Hero/Villain Type - Users can input the ID of a hero/villain and update its type (hero/villain) in the database.
Option 4: Delete Hero/Villain - Users can input the ID of a hero/villain to be deleted from the database.
Option 5: Exit - If users choose to exit, the script ends the interactive shell loop and the program terminates.

## superhero stories

- As a superhero, I want to add new friends to my network so that I can keep in touch with them and strengthen our alliance against supervillains.

 - As a superhero, I want to view a list of all my friends (superheroes) and foes (villains) in the database so that I can keep track of them and their current status.

- As a superhero, I want to update the type (hero/villain) of my friends in the database, so I can ensure accurate information about their alignment and activities.

X As a superhero, I want to delete supervillains from the database, so I can maintain an up-to-date list of threats and potential dangers to our world.

X As a superhero, I want to easily navigate through the interactive shell interface, so I can quickly perform various CRUD operations without any technical complexities.

X As a superhero, I want the interactive shell script to provide clear instructions and prompts, so I can easily understand the available options and make informed decisions.

X As a superhero, I want the interactive shell script to handle errors gracefully, so I can receive meaningful error messages and troubleshoot any issues encountered during database operations.

- As a superhero, I want the interactive shell script to maintain data consistency in the database, ensuring that no duplicate entries or invalid data is allowed.

X As a superhero, I want the interactive shell script to be secure and protect my superhero friends' data from unauthorized access or modifications.

- As a superhero, I want the interactive shell script to provide a smooth and efficient user experience, minimizing delays in data retrieval and processing, so I can focus on protecting the world.



# Gpt oop

When thinking in object-oriented programming (OOP) terms, you can represent the tables and their relationships as classes and objects. Each table can be thought of as a class, and the rows in the table can be seen as individual objects of that class.

Here's how you can approach it:

Heroes Table as a Class:

The "heroes" table can be represented as a Hero class in your OOP design.
Each row in the "heroes" table will be an instance (object) of the Hero class, representing a specific superhero.
Friends and Enemies as Relationships:

The "friends" and "enemies" tables can be thought of as relationships between superheroes.
To represent these relationships in OOP, you can use instance variables in the Hero class, such as a list of friends and a list of enemies, where each element in the list represents another Hero object.
Abilities Table as a Class:

The "abilities" table can be represented as an Ability class.
Each row in the "abilities" table will be an instance (object) of the Ability class, representing a specific superpower or ability.
Villains Table as a Class:

The "villains" table can be represented as a Villain class.
Each row in the "villains" table will be an instance (object) of the Villain class, representing a specific supervillain.
Relationships between Classes:

To represent relationships between classes, you can use attributes within the classes.
For example, the Hero class can have attributes like friends, enemies, and abilities, where each attribute holds instances of the corresponding classes (Hero and Ability).
Methods for CRUD Operations:

You can define methods within each class to handle CRUD operations, such as adding friends, updating abilities, etc.
These methods will interact with the database (tables) to perform the necessary operations.
Here's a simplified example to illustrate the concept in Python-like pseudo-code:


class Hero:
    def __init__(self, name, hero_type):
        self.name = name
        self.type = hero_type
        self.friends = []  # List of Hero objects representing friends
        self.enemies = []  # List of Hero objects representing enemies
        self.abilities = []  # List of Ability objects representing superpowers

    def add_friend(self, friend_hero):
        self.friends.append(friend_hero)

    def add_ability(self, ability):
        self.abilities.append(ability)


class Ability:
    def __init__(self, name, description):
        self.name = name
        self.description = description


class Villain:
    def __init__(self, name):
        self.name = name


### Usage Example:
hero1 = Hero("Superman", "hero")
hero2 = Hero("Batman", "hero")

ability1 = Ability("Super Strength", "Ability to lift heavy objects.")
ability2 = Ability("Flight", "Ability to fly.")

hero1.add_friend(hero2)
hero1.add_ability(ability1)
hero1.add_ability(ability2)
In this example, we have represented the Hero, Ability, and Villain entities as classes. Heroes can have friends and abilities, and abilities are represented as a separate class. You can extend this concept to your PostgreSQL database design and implement the necessary methods for CRUD operations and relationships between different entities.
