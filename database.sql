-- PROGRESQL DATABASE

-- Users Table
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(255),
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    email VARCHAR(255) UNIQUE,
    password VARCHAR(255),
    date_joined TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP
);

-- Transactions Table
CREATE TABLE transactions (
    transaction_id SERIAL PRIMARY KEY,
    user_id INT NOT NULL,
    transaction_type VARCHAR(50),
    amount NUMERIC(15, 2),
    date CURRENT_TIMESTAMP
    transaction_date TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP,
    description VARCHAR(255),
    total_income NUMERIC(15, 2) DEFAULT 0,
    total_expense NUMERIC(15, 2) DEFAULT 0,
    balance NUMERIC(15, 2) DEFAULT 0,
    FOREIGN KEY (user_id) REFERENCES users(id)
);

-- Trigger for income transactions
CREATE OR REPLACE FUNCTION income_transaction_trigger() RETURNS TRIGGER AS $$
BEGIN
    IF NEW.transaction_type = 'income' THEN
        NEW.total_income = COALESCE((SELECT SUM(amount) FROM transactions WHERE user_id = NEW.user_id AND transaction_type = 'income'), 0) + NEW.amount;
        NEW.total_expense = COALESCE((SELECT SUM(amount) FROM transactions WHERE user_id = NEW.user_id AND transaction_type = 'expense'), 0);
    END IF;

    NEW.balance = NEW.total_income - NEW.total_expense;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER income_transaction_trigger
BEFORE INSERT ON transactions
FOR EACH ROW
EXECUTE FUNCTION income_transaction_trigger();

-- Trigger for expense transactions
CREATE OR REPLACE FUNCTION expense_transaction_trigger() RETURNS TRIGGER AS $$
BEGIN
    IF NEW.transaction_type = 'expense' THEN
        NEW.total_income = COALESCE((SELECT SUM(amount) FROM transactions WHERE user_id = NEW.user_id AND transaction_type = 'income'), 0);
        NEW.total_expense = COALESCE((SELECT SUM(amount) FROM transactions WHERE user_id = NEW.user_id AND transaction_type = 'expense'), 0) + NEW.amount;
    END IF;

    NEW.balance = NEW.total_income - NEW.total_expense;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER expense_transaction_trigger
BEFORE INSERT ON transactions
FOR EACH ROW
EXECUTE FUNCTION expense_transaction_trigger();


-- MYSQL DATABASE
-- -- Create a new database
-- CREATE DATABASE YourDatabaseName;
-- USE YourDatabaseName;

-- -- Users Table
-- CREATE TABLE users (
--     id INT AUTO_INCREMENT PRIMARY KEY,
--     username VARCHAR(255),
--     first_name VARCHAR(255),
--     last_name VARCHAR(255),
--     email VARCHAR(255) UNIQUE,
--     password VARCHAR(255),
--     date_joined DATETIME DEFAULT CURRENT_TIMESTAMP
-- );

-- -- Transactions Table
-- CREATE TABLE Transactions (
--     transaction_id INT AUTO_INCREMENT PRIMARY KEY,
--     user_id INT NOT NULL,
--     transaction_type VARCHAR(50),
--     amount DECIMAL(15, 2),
--     transaction_date DATETIME DEFAULT CURRENT_TIMESTAMP,
--     description VARCHAR(255),
--     balance DECIMAL(15, 2),
--     FOREIGN KEY (user_id) REFERENCES users(id)
-- );


-- -- Trigger for income transactions
-- DELIMITER $$
-- CREATE TRIGGER income_transaction_trigger
-- BEFORE INSERT ON Transactions
-- FOR EACH ROW
-- BEGIN
--     IF NEW.transaction_type = 'income' THEN
--         SET NEW.total_income = (SELECT IFNULL(SUM(amount), 0) FROM Transactions WHERE user_id = NEW.user_id AND transaction_type = 'income') + NEW.amount;
--         SET NEW.total_expense = (SELECT IFNULL(SUM(amount), 0) FROM Transactions WHERE user_id = NEW.user_id AND transaction_type = 'expense');
--     END IF;
    
--     SET NEW.balance = NEW.total_income - NEW.total_expense;
-- END;
-- $$
-- DELIMITER ;

-- -- Trigger for expense transactions
-- DELIMITER $$
-- CREATE TRIGGER expense_transaction_trigger
-- BEFORE INSERT ON Transactions
-- FOR EACH ROW
-- BEGIN
--     IF NEW.transaction_type = 'expense' THEN
--         SET NEW.total_income = (SELECT IFNULL(SUM(amount), 0) FROM Transactions WHERE user_id = NEW.user_id AND transaction_type = 'income');
--         SET NEW.total_expense = (SELECT IFNULL(SUM(amount), 0) FROM Transactions WHERE user_id = NEW.user_id AND transaction_type = 'expense') + NEW.amount;
--     END IF;
    
--     SET NEW.balance = NEW.total_income - NEW.total_expense;
-- END;
-- $$
-- DELIMITER ;
