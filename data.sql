CREATE TABLE users (
   id INT AUTO_INCREMENT PRIMARY KEY,
   username VARCHAR(255) UNIQUE NOT NULL,
   registration_number VARCHAR(255) UNIQUE NOT NULL,
   branch VARCHAR(255),
   year_of_study INT, -- Add column for year of study
   created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
