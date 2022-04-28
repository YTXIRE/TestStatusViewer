CREATE TABLE IF NOT EXISTS project (
    name VARCHAR
);

INSERT INTO project (name) VALUES ("Project 1");
INSERT INTO project (name) VALUES ("Project 2");
INSERT INTO project (name) VALUES ("Project 3");
INSERT INTO project (name) VALUES ("Project 4");

CREATE TABLE IF NOT EXISTS reports (
	id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	message TEXT,
	status VARCHAR,
	test_name TEXT,
	created_at INTEGER,
	project VARCHAR
);
