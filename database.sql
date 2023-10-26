CREATE TABLE user (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255) NOT NULL,
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    email VARCHAR(255) UNIQUE,
    password_hash VARCHAR(255) NOT NULL,
    date_joined DATETIME DEFAULT CURRENT_TIMESTAMP
);



CREATE TABLE transaction  (
    id INT AUTO_INCREMENT PRIMARY KEY,
    description VARCHAR(255),
    expense FLOAT,
    income FLOAT,
    total_income FLOAT,
    total_expenses FLOAT,
    balance FLOAT AS (total_income - total_expenses) VIRTUAL,
    date_recorded DATETIME DEFAULT CURRENT_TIMESTAMP,
    user_id INT NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(id)
);