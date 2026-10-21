CREATE TABLE entries (
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    posted TEXT NOT NULL, 
    content TEXT NOT NULL, 
    archived BOOLEAN NOT NULL
); 

CREATE TABLE projects (
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    title TEXT NOT NULL,
    created TEXT NOT NULL,
    technologies TEXT NOT NULL,
    img_path TEXT, 
    github TEXT,
    content TEXT NOT NULL, 
    completed BOOLEAN NOT NULL,
    archived BOOLEAN NOT NULL 
);