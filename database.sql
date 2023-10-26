-- Users Table
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255),
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    email VARCHAR(255) UNIQUE,
    password VARCHAR(255),
    date_joined DATETIME DEFAULT CURRENT_TIMESTAMP,
    balance DECIMAL(15, 2)
);

-- Transactions Table
CREATE TABLE Transactions (
    transaction_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL, FOREIGNKEY
    transaction_type VARCHAR(50),
    amount DECIMAL(15, 2),
    transaction_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    description VARCHAR(255),
    FOREIGN KEY (user_id) REFERENCES Users(id)
);


-- Initial
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

-- Demo

-- -- Customers Table
-- CREATE TABLE Customers (
--     customer_id INT AUTO_INCREMENT PRIMARY KEY,
--     first_name VARCHAR(255),
--     last_name VARCHAR(255),
--     date_of_birth DATE,
--     address VARCHAR(255),
--     phone_number VARCHAR(15),
--     email VARCHAR(255)
-- );

-- -- Accounts Table
-- CREATE TABLE Accounts (
--     account_id INT AUTO_INCREMENT PRIMARY KEY,
--     customer_id INT,
--     account_number VARCHAR(20),
--     account_type VARCHAR(50),
--     balance DECIMAL(15, 2),
--     date_opened DATE,
--     FOREIGN KEY (customer_id) REFERENCES Customers(customer_id)
-- );

-- -- Transactions Table
-- CREATE TABLE Transactions (
--     transaction_id INT AUTO_INCREMENT PRIMARY KEY,
--     account_id INT,
--     transaction_type VARCHAR(50),
--     amount DECIMAL(15, 2),
--     transaction_date DATETIME,
--     description VARCHAR(255),
--     FOREIGN KEY (account_id) REFERENCES Accounts(account_id)
-- );
