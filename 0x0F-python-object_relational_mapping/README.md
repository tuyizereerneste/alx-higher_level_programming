0x0F. Python - Object-relational mapping


TASKS:

Write a script that lists all states from the database hbtn_0e_0_usa:
	You must use the module MySQLdb (import MySQLdb)

2. Write a script that lists all states with a name starting with N (upper N) from the database hbtn_0e_0_usa:

	Your script should take 3 arguments: mysql username, mysql password and database name (no argument validation needed)
	You must use the module MySQLdb (import MySQLdb)

3. Write a script that takes in an argument and displays all values in the states table of hbtn_0e_0_usa where name matches the argument.

	Your script should take 4 arguments: mysql username, mysql password, database name and state name searched (no argument validation needed)
	You must use the module MySQLdb (import MySQLdb)

4. test "Arizona'; TRUNCATE TABLE states ; SELECT * FROM states WHERE name = '" as an input?

5. Write a script that lists all cities from the database hbtn_0e_4_usa

	Your script should take 3 arguments: mysql username, mysql password and database name
	You must use the module MySQLdb (import MySQLdb)

6. Write a script that takes in the name of a state as an argument and lists all cities of that state, using the database hbtn_0e_4_usa

Your script should take 4 arguments: mysql username, mysql password, database name and state name (SQL injection free!)
You must use the module MySQLdb (import MySQLdb)

7. Write a python file that contains the class definition of a State and an instance Base = declarative_base():

	State class:
		inherits from Base Tips
		links to the MySQL table states
	class attribute id that represents a column of an auto-generated, unique integer, can’t be null and is a primary key
	class attribute name that represents a column of a string with maximum 128 characters and can’t be null
You must use the module SQLAlchemy

8. Write a script that lists all State objects from the database hbtn_0e_6_usa

	Your script should take 3 arguments: mysql username, mysql password and database name
	You must use the module SQLAlchemy

9. Write a script that lists all State objects that contain the letter a from the database hbtn_0e_6_usa

	Your script should take 3 arguments: mysql username, mysql password and database name
	You must use the module SQLAlchemy

10. Write a script that prints the State object with the name passed as argument from the database hbtn_0e_6_usa

	Your script should take 4 arguments: mysql username, mysql password, database name and state name to search (SQL injection free)
	You must use the module SQLAlchemy

11. Write a script that adds the State object “Louisiana” to the database hbtn_0e_6_usa

	Your script should take 3 arguments: mysql username, mysql password and database name
	You must use the module SQLAlchemy

12. Write a script that changes the name of a State object from the database hbtn_0e_6_usa

	Your script should take 3 arguments: mysql username, mysql password and database name
	You must use the module SQLAlchemy

13. Write a script that deletes all State objects with a name containing the letter a from the database hbtn_0e_6_usa

14. Write a Python file similar to model_state.py named model_city.py that contains the class definition of a City.

	City class:
		inherits from Base (imported from model_state)
		links to the MySQL table cities
		class attribute id that represents a column of an auto-generated, unique integer, can’t be null and is a primary key
		class attribute name that represents a column of a string of 128 characters and can’t be null
		class attribute state_id that represents a column of an integer, can’t be null and is a foreign key to states.id
	You must use the module SQLAlchemy
