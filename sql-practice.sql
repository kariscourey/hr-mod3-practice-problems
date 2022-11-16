CREATE TABLE users (
  id INTEGER NOT NULL UNIQUE,
  first TEXT NOT NULL,
  last TEXT NOT NULL,
  avatar TEXT NOT NULL,
  email TEXT NOT NULL,
  username TEXT NOT NULL
);

CREATE TABLE trucks (
  id INTEGER NOT NULL UNIQUE,
  name TEXT NOT NULL,
  website TEXT NOT NULL,
  category TEXT NOT NULL,
  vegetarian_friendly BOOLEAN NOT NULL,
  owner_id INTEGER NOT NULL REFERENCES users(id)
);

CREATE TABLE reviews (
  id INTEGER NOT NULL UNIQUE,
  title TEXT NOT NULL,
  content TEXT NOT NULL,
  reviewer_id INTEGER REFERENCES users("id"),
  rating INTEGER NOT NULL,
  truck_id INTEGER NOT NULL REFERENCES trucks("id")
);

CREATE TABLE truck_menu_items (
  truck_id INTEGER NOT NULL REFERENCES trucks("id"),
  menu_item_id INTEGER NOT NULL REFERENCES menu_items("id"),
  price INTEGER NOT NULL
);

CREATE TABLE menu_items (
    id INTEGER NOT NULL UNIQUE,
    name TEXT NOT NULL,
    calories INTEGER NOT NULL
);

-- Write you SELECT statement here
SELECT id, first, last, email
FROM users;

-- Write you SELECT statement here
SELECT id, first, last, email
FROM users
ORDER BY last;

-- Write you SELECT statement here
SELECT id, name, website
FROM trucks
WHERE vegetarian_friendly=true
ORDER BY name;

-- Write you SELECT statement here
SELECT users.email, trucks.name
FROM users
INNER JOIN trucks
  ON (users.id = trucks.owner_id)
ORDER BY trucks.name;

-- Write you SELECT statement here
-- SELECT trucks.name, COUNT(reviews.id)
-- FROM trucks
-- INNER JOIN reviews
--   ON (trucks.id = reviews.truck_id);
-- GROUP BY trucks.name

SELECT t.name as name,
       COUNT(r.*) AS num_reviews
FROM trucks AS t
LEFT OUTER JOIN reviews r
  ON (t.id = r.truck_id)
GROUP BY t.name;

-- Write you SELECT statement here
SELECT t.name as name,
    COUNT(r.*) AS num_reviews,
    AVG(r.rating) AS average_rating
FROM trucks AS t
LEFT OUTER JOIN reviews r
  ON (t.id = r.truck_id)
GROUP BY t.name;

-- Write you SELECT statement here
SELECT t.name as name,
    COUNT(r.*) AS num_reviews,
    ROUND(AVG(r.rating)) AS average_rating
FROM trucks AS t
LEFT OUTER JOIN reviews r
  ON (t.id = r.truck_id)
GROUP BY t.name;


-- Write you SELECT statement here
SELECT t.name as name,
    COUNT(tmi.*) AS num_items,
    ROUND(AVG(tmi.price),2) AS avg_price
FROM trucks AS t
LEFT OUTER JOIN truck_menu_items tmi
  ON (t.id = tmi.truck_id)
GROUP BY t.name
ORDER BY t.name DESC;

-- Write you SELECT statement here
SELECT t.name as name,
    SUM(mi.calories) AS total_calories
FROM trucks AS t
LEFT OUTER JOIN truck_menu_items tmi
  ON (t.id = tmi.truck_id)
LEFT OUTER JOIN menu_items mi
  ON (tmi.menu_item_id = mi.id)
GROUP BY t.name
ORDER BY t.name
