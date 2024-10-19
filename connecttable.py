import mysql.connector
from mysql.connector import Error

# Function to create a database connection
def create_connection(host_name, user_name, user_password, db_name=None):
    connection = None
    try:
        if db_name:
            connection = mysql.connector.connect(
                host=host_name,
                user=user_name,
                password=user_password,
                database=db_name
            )
        else:
            connection = mysql.connector.connect(
                host=host_name,
                user=user_name,
                password=user_password
            )
        print("Connection to MySQL DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")
    return connection

# Function to create the required tables
def create_tables(connection):
    cursor = connection.cursor()
    
    # Create the movie table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS movie (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255) NOT NULL UNIQUE,
        year INT NOT NULL
    )
    """)

    # Create the rating table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS rating (
        movie_name VARCHAR(255) NOT NULL,
        rating FLOAT NOT NULL,
        FOREIGN KEY (movie_name) REFERENCES movie(name)
        ON DELETE CASCADE
    )
    """)
    
    connection.commit()

# Function to add a movie with its rating
def add_movie_with_rating(db_connection, movie_name, movie_year):
    cursor = db_connection.cursor()
    
    # Check if the rating exists for the movie
    cursor.execute("SELECT rating FROM rating WHERE movie_name = %s", (movie_name,))
    result = cursor.fetchone()
    
    if result:
        rating = result[0]
        # Insert the movie
        cursor.execute("INSERT INTO movie (name, year) VALUES (%s, %s)", 
                       (movie_name, movie_year))
        db_connection.commit()
        print(f"Added movie: {movie_name} ({movie_year}) with rating {rating}")
    else:
        print("No rating found for movie:", movie_name)

# Function to insert sample ratings into the rating table
def insert_sample_ratings(connection):
    cursor = connection.cursor()
    sample_ratings = [
        ('Inception', 8.8),
        ('The Matrix', 8.7),
        ('Interstellar', 8.6),
        ('Avatar', 7.8)
    ]
    
    cursor.executemany("INSERT IGNORE INTO rating (movie_name, rating) VALUES (%s, %s)", sample_ratings)
    connection.commit()

# Main execution
if __name__ == "__main__":
    # Replace these with your actual database credentials
    host = "localhost"  # Your database host
    user = "your_username"  # Your database username
    password = "your_password"  # Your database password
    database = "your_database"  # Your database name

    # Create a connection to the database
    connection = create_connection(host, user, password, database)

    # Create tables if they do not exist
    create_tables(connection)

    # Insert sample ratings
    insert_sample_ratings(connection)

    # Add a movie with a rating
    add_movie_with_rating(connection, 'Inception', 2010)

    # Clean up the connection
    connection.close()





#pip install mysql-connector-python
