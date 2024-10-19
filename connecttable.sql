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

-- Insert sample data into the rating table
INSERT INTO rating (movie_name, rating) VALUES
('Inception', 8.8),
('The Matrix', 8.7),
('Interstellar', 8.6);


-- Insert a new movie only if it has a corresponding rating
INSERT INTO movie (name, year, rating)
SELECT 'Avatar', 2009, rating
FROM rating
WHERE movie_name = 'Avatar';
