-- Create the movie table
CREATE TABLE movie (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    year INT NOT NULL,
    rating FLOAT
);

-- Create the rating table
CREATE TABLE rating (
    movie_name VARCHAR(255) NOT NULL,
    rating FLOAT NOT NULL
);



-- Insert a new movie only if it has a corresponding rating
INSERT INTO movie (name, year, rating)
SELECT 'Avatar', 2009, rating
FROM rating
WHERE movie_name = 'Avatar';
