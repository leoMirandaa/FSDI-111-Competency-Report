-- Create a database table calle "user":
-- primary key = not null (implicit)
CREATE TABLE user (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  first_name VARCHAR(45) NOT NULL,
  last_name VARCHAR(45) NOT NULL,
  hobbies TEXT,
  active BOOLEAN NOT NULL DEFAULT 1
);

-- Dummy data to play with:
INSERT INTO user (
  first_name,
  last_name,
  hobbies
) VALUES (
  "Leopoldo",
  "MIranda",
  "Play the guitar"
);

INSERT INTO user (
  first_name,
  last_name,
  hobbies
) VALUES (
  "Josh",
  "Gilbert",
  "Go to movies"
);

INSERT INTO user (
  first_name,
  last_name,
  hobbies
) VALUES (
  "Michale",
  "Jordan",
  "Play basketball"
);

CREATE TABLE user2 (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  first_name VARCHAR(45) NOT NULL,
  last_name VARCHAR(45) NOT NULL,
  hobbies TEXT,
  active BOOLEAN NOT NULL DEFAULT 1
);
