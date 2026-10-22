DROP TABLE IF EXISTS entries;
DROP TABLE IF EXISTS projects;


CREATE TABLE entries (
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    posted TEXT NOT NULL, 
    content TEXT NOT NULL, 
    archived BOOLEAN NOT NULL
); 

CREATE TABLE projects (
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    title TEXT NOT NULL,
    created TEXT,
    technologies TEXT,
    img_path TEXT, 
    github TEXT,
    award TEXT,
    content TEXT NOT NULL, 
    completed BOOLEAN NOT NULL,
    archived BOOLEAN NOT NULL 
);

INSERT INTO projects (title, created, technologies, img_path, github, award, content, completed, archived)
VALUES
(
    "The Vibe Check",
    "February 2026",
    "Static HTML pages (with Javascript), Gemini API, Google Translate API",
    "SWICS_Hackathon.png",
    "https://github.com/el124-choi/swics_hackathon",
    "Hack With SWICS #1 - People's Choice Award",
    "There reviews for spaces in the real world, but no equivalent for digital spaces. This project aims to fill that gap - users can create reviews for websites; they can rate sites based on a number of factors such as how inclusive and accessible they are. This was the first time I used an API in a website - I found both the Gemini API and Google Translate API difficult to implement at the time, but now I use APIs in most of my projects. If we had more time, I would have liked to implement this using a javascript framework such as Node.js or Next.js and add a proper backend instead of having an application consisting solely of static html pages",
    1, 
    0
),
(
    "Automated plant watering system",
    "July 2026",
    "C++, Arduino",
    "Plant_Watering.jpg",
    "https://github.com/el124-choi/automatedPlantWateringSystem",
    NULL,
    "This program was for controlling an automated watering system that would independently water 3 plants over the course of a month. The system ended up lasting 2 weeks before it failed due to a wiring error (in my defence, it was my first arduino project - something was bound to happen!). In the future, I plan on adapting the wiring and the code to use an ESP32 to autonomously control a small-scale hydroponic basil garden and explore other ways to incorporate other custom IOT systems in my everyday life",
    1,
    0
), 
(
    "Badly Brewed Coffee (University Coursework)",
    "February - May 2026",
    "Ruby - Sinatra",
    "Badly_Brewed.png",
    NULL,
    NULL,
    "As part of our coursework for the first-year module 'Introduction to Software Engineering', we had to make a full stack CRUD website (complete with tests, a report and a video demonstration) for a client actor with Sinatra and SQL. Through this project, I gained first-hand experience with working in an Agile Scrum environment; we elected a scrum leader and, at the start of every week, we would have a planning session where we would select and delegate tasks and state what we had accomplished in the previous week",
    1, 
    0
),
(
    "Wakeup Streak",
    "August 2026",
    "Expo, React Native, Typescript",
    "Wakeup_Streak.png",
    "https://github.com/el124-choi/WakeupStreak",
    NULL,
    "A simple cross-platform alarm app. The user can set a time for the app to wake them up with a notification. Waking up on time increases their streak, with the aim being to get their 'Wakeup Streak' as high as possible. Creating this app allowed me to kill two birds with one stone over the summer: I could give myself the motivation to wake up earlier and learn how to use the Expo and React frameworks at the same time",
    1, 
    0
),
(
    "Cairn",
    "October 2026",
    "Html, JavaScript, Gemini API, Codex",
    "Cairn.png",
    "https://github.com/el124-choi/Cairn",
    "HuddleHive WIT hackathon #7 (HuddleHive Track)",
    "A gamified roadmap generator that utilises the Gemini API to generate timestamped roadmaps based on plaintext user input. As the user progresses through the roadmap, their progress is displayed in a progress bar, where their 'avatar' leaves a stone to mark the milestones they have achieved, inspired by how travellers leave cairns to mark points on their travels. My team was a team of 5, where I predominantly worked with OpenAI's Codex to create the roadmap generation code.Part of our hackathon submission was a pitch to the judges, which I thought was a great opportunity for me to explain the decisions I made in the development process (and also a chance to show off my public speaking skills) instead of just demonstrating the features like a regular hackathon",
    1, 
    0
);

INSERT INTO projects (title, github, content, completed, archived)
VALUES
(
    "Musecoll",
    "https://github.com/el124-choi/musecoll",
    "An app that allows users to collate snippets of audio, images, text and music videos in a free collage format - aimed at songwriters and creatives. I came up with the idea for this app when I was writing my own songs and found that I was saving songs and videos to playlists, images to Pinterest Boards and had no way to conveniently bring them together when producing",
    0, 
    0
), 
(
    "Portfolio", 
    "https://github.com/el124-choi/ec-portfolio", 
    "All of the projects and blog entries are stored on a database so that I could get some SQL practice. I am currently working on a weekly blog section for the website.",
    0, 
    0
);
