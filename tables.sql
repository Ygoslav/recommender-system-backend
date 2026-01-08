CREATE TABLE
    IF NOT EXISTS users (
        id SERIAL PRIMARY KEY,
        username VARCHAR(50) NOT NULL UNIQUE,
        password VARCHAR(50) NOT NULL
    );

CREATE TABLE
    IF NOT EXISTS products (
        id SERIAL PRIMARY KEY,
        name VARCHAR(100) NOT NULL
    );

CREATE TABLE
    IF NOT EXISTS favorites (
        user_id INTEGER NOT NULL,
        product_id INTEGER NOT NULL,
        PRIMARY KEY (user_id, product_id),
        FOREIGN KEY (user_id) REFERENCES users (id) ON DELETE CASCADE,
        FOREIGN KEY (product_id) REFERENCES products (id) ON DELETE CASCADE
    );

CREATE TABLE
    IF NOT EXISTS user_product_views (
        user_id INTEGER NOT NULL,
        product_id INTEGER NOT NULL,
        views_count INTEGER NOT NULL,
        PRIMARY KEY (user_id, product_id),
        FOREIGN KEY (user_id) REFERENCES users (id) ON DELETE CASCADE,
        FOREIGN KEY (product_id) REFERENCES products (id) ON DELETE CASCADE
    );

CREATE TABLE
    IF NOT EXISTS carts (
        id SERIAL PRIMARY KEY,
        current_status VARCHAR(6) NOT NULL DEFAULT 'active', -- cart status ('active', 'closed')
        user_id INTEGER NOT NULL,
        FOREIGN KEY (user_id) REFERENCES users (id) ON DELETE CASCADE,
    );

CREATE TABLE
    IF NOT EXISTS cart_items (
        cart_id INTEGER NOT NULL,
        product_id INTEGER NOT NULL,
        quantity INTEGER NOT NULL,
        PRIMARY KEY (cart_id, product_id),
        FOREIGN KEY (cart_id) REFERENCES carts (id) ON DELETE CASCADE,
        FOREIGN KEY (product_id) REFERENCES products (id) ON DELETE CASCADE
    );
