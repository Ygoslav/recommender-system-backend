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
        id SERIAL PRIMARY KEY,
        user_id INTEGER NOT NULL,
        product_id INTEGER NOT NULL,
        UNIQUE (user_id, product_id),
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
