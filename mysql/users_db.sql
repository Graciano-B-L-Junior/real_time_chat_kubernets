-- Create the database
CREATE DATABASE IF NOT EXISTS speedchatdb;

-- Switch to the new database
USE speedchatdb;

-- Create a sample table
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    passphrase VARCHAR(100) NOT NULL
);

-- Insert sample data into the table
INSERT INTO users (username, passphrase) VALUES ('john_doe', 'john_123');
INSERT INTO users (username, passphrase) VALUES ('jane_doe', 'jane_123');