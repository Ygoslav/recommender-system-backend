CREATE TABLE
    IF NOT EXISTS users (
        id SERIAL PRIMARY KEY,
        username VARCHAR(50) NOT NULL UNIQUE,
        password VARCHAR(50) NOT NULL
    );

CREATE TABLE
    IF NOT EXISTS products (
        id SERIAL PRIMARY KEY,
        product_name VARCHAR(200) NOT NULL,
        website VARCHAR(50),
        country VARCHAR(50),
        category VARCHAR(50),
        subcategory VARCHAR(50),
        title_href TEXT,
        price DECIMAL(10, 2),
        brand VARCHAR(100),
        ingredients TEXT,
        form VARCHAR(50),
        type VARCHAR(100),
        color VARCHAR(100),
        size DECIMAL(10, 2),
        rating DECIMAL(5, 2),
        noofratings INTEGER,
        has_allergen BOOLEAN,
        has_fragrance BOOLEAN,
        has_parfum BOOLEAN,
        has_limonene BOOLEAN,
        has_linalool BOOLEAN,
        has_citral BOOLEAN,
        has_citronellol BOOLEAN,
        has_eugenol BOOLEAN,
        has_hexyl_cinnamal BOOLEAN,
        has_benzyl_alcohol BOOLEAN,
        has_benzyl_salicylate BOOLEAN,
        has_coumarin BOOLEAN,
        has_alpha_isomethyl_ionone BOOLEAN,
        has_cinnamal BOOLEAN,
        has_isoeugenol BOOLEAN,
        has_farnesol BOOLEAN,
        has_geraniol BOOLEAN,
        has_hydroxycitronellal BOOLEAN,
        has_butylphenyl_methylpropional BOOLEAN,
        has_methylisothiazolinone BOOLEAN,
        has_methylchloroisothiazolinone BOOLEAN,
        has_dmdm_hydantoin BOOLEAN,
        has_formaldehyde BOOLEAN,
        has_propylene_glycol BOOLEAN
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
