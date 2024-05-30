CREATE TABLE ProductPrices (
    ProductID INT PRIMARY KEY,
    ProductName VARCHAR(50),
    Category VARCHAR(30),
    Price DECIMAL(10, 2),
    DateAdded DATE
);

INSERT INTO ProductPrices (ProductID, ProductName, Category, Price, DateAdded) VALUES
(1, 'Laptop', 'Electronics', 999.99, '2024-01-15'),
(2, 'Smartphone', 'Electronics', 699.99, '2024-01-20'),
(3, 'Tablet', 'Electronics', 399.99, '2024-01-25'),
(4, 'Headphones', 'Electronics', 199.99, '2024-02-01'),
(5, 'Smartwatch', 'Electronics', 249.99, '2024-02-05'),
(6, 'Camera', 'Photography', 499.99, '2024-02-10'),
(7, 'Printer', 'Office Supplies', 149.99, '2024-02-15'),
(8, 'Desk Chair', 'Furniture', 89.99, '2024-02-20'),
(9, 'Desk Lamp', 'Furniture', 39.99, '2024-02-25'),
(10, 'Monitor', 'Electronics', 199.99, '2024-03-01'),
(11, 'Keyboard', 'Electronics', 49.99, '2024-03-05'),
(12, 'Mouse', 'Electronics', 29.99, '2024-03-10'),
(13, 'Router', 'Electronics', 99.99, '2024-03-15'),
(14, 'External Hard Drive', 'Electronics', 129.99, '2024-03-20'),
(15, 'USB Flash Drive', 'Electronics', 19.99, '2024-03-25'),
(16, 'Webcam', 'Electronics', 59.99, '2024-04-01'),
(17, 'Microphone', 'Electronics', 79.99, '2024-04-05'),
(18, 'Graphic Tablet', 'Electronics', 249.99, '2024-04-10'),
(19, 'Fitness Tracker', 'Electronics', 149.99, '2024-04-15'),
(20, 'Bluetooth Speaker', 'Electronics', 89.99, '2024-04-20');
