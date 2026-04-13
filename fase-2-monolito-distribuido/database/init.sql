CREATE TABLE orders (
    id SERIAL PRIMARY KEY,
    product TEXT,
    quantity INT,
    status TEXT,
    created_at TIMESTAMP DEFAULT NOW()
);