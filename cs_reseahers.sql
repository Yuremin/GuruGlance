CREATE DATABASE cs_researchers;

USE cs_researchers;

CREATE TABLE researchers (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    domain VARCHAR(255) NOT NULL,
    homepage VARCHAR(255)
);
