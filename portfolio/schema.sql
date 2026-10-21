DROP TABLE IF EXISTS entries; 
DROP TABLE IF EXISTS projects; 
DROP TABLE IF EXISTS in_progress;

CREATE TABLE entries (
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    posted DATETIME NOT NULL, 
    content TEXT NOT NULL, 
    archived BOOLEAN NOT NULL
); 

CREATE TABLE projects (
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    title TEXT NOT NULL,
    created TEXT NOT NULL,
    img_path TEXT NOT NULL, 
    content TEXT NOT NULL, 
    completed BOOLEAN NOT NULL,
    archived BOOLEAN NOT NULL 
);