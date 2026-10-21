DROP TABLE IF EXISTS entries; 
DROP TABLE IF EXISTS projects; 
DROP TABLE IF EXISTS in_progress;

CREATE TABLE entries (
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    created DATETIME NOT NULL, 
    content TEXT NOT NULL, 
    archived BOOLEAN NOT NULL
); 

CREATE TABLE projects (
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    title TEXT NOT NULL,
    img_path TEXT NOT NULL, 
    content TEXT NOT NULL, 
    archived BOOLEAN NOT NULL 
); 

CREATE TABLE in_progress (
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    project_id INTEGER NOT NULL,
    title TEXT NOT NULL,
    content TEXT NOT NULL,
    FOREIGN KEY (project_id) REFERENCES projects (id) 

)