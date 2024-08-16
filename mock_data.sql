INSERT INTO products (id, name, price) VALUES
(1, 'Product A', 100),
(2, 'Product B', 150),
(3, 'Product C', 200);

INSERT INTO roles(role_name)VALUES
('Admin'),
('User');

INSERT INTO customers (id, name, email, phone, username, password, role_id) VALUES
(1, 'John Doe', 'john@example.com', '1234567890', 'johndoe', 'password123', 2),
(2, 'Jane Smith', 'jane@example.com', '0987654321', 'janesmith', 'password456', 2),
(3, 'Nicolas Rodriguez', 'nr115935@gmail.com', '7866728316', 'nicolasrod', 'password789', 1);

INSERT INTO orders (id, date, customer_id) VALUES
(1, '2023-10-01', 1),
(2, '2023-10-02', 2),
(3, '2023-10-01', 3);

INSERT INTO order_product (order_id, product_id, quantity) VALUES
(1, 1, 1),
(1, 2, 1),
(2, 2, 5),
(2, 3, 9),
(3,1,1);

INSERT INTO Employees (name, email, phone) VALUES
('Alice Johnson', 'alice.johnson@example.com', '123-456-7890'),
('Bob Smith', 'bob.smith@example.com', '234-567-8901'),
('Charlie Brown', 'charlie.brown@example.com', '345-678-9012');

INSERT INTO employee_Product (employee_id, product_id) VALUES
(1, 1),
(2, 2),
(2, 3);