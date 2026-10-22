from portfolio import create_app
from portfolio.db import get_db


PROJECTS = [
    (
        "The Vibe Check",
        "February 2026",
        "Static HTML pages (with Javascript), Gemini API, Google Translate API",
        "SWICS_Hackathon.png",
        "https://github.com/el124-choi/swics_hackathon",
        "Hack With SWICS #1 - People's Choice Award"
        "There reviews for spaces in the real world, but no equivalent for digital spaces. This project aims to fill that gap - users can create reviews for websites; they can rate sites based on a number of factors such as how inclusive and accessible they are. This was the first time I used an API in a website - I found both the Gemini API and Google Translate API difficult to implement at the time, but now I use APIs in most of my projects. \nIf we had more time, I would have liked to implement this using a javascript framework such as Node.js or Next.js and add a proper backend instead of having an application consisting solely of static html pages.",
    ),
    (
        "Automated plant watering system",
        "July 2026",
        "C++, Arduino",
        "Plant_Watering.jpg",
        None,
        "https://github.com/el124-choi/automatedPlantWateringSystem",
        "This program was for controlling an automated watering system that would independently water 3 plants over the course of a month. The system ended up lasting 2 weeks before it failed due to a wiring error (in my defence, it was my first arduino project - something was bound to happen!). \nIn the future, I plan on adapting the wiring and the code to use an ESP32 to autonomously control a small-scale hydroponic basil garden and explore other ways to incorporate other custom IOT systems in my everyday life.",
    ),
    (
        "Badly Brewed Coffee (University Coursework)",
        "February - May 2026",
        "Ruby - Sinatra",
        "Badly_Brewed.png",
        None,
        None,
        "As part of our coursework, we had to make a full stack CRUD website (complete with tests, a report and a video demonstration) for a client actor with Sinatra and SQL. \nThrough this project, I gained first-hand experience with working in an Agile Scrum environment; we elected a scrum leader and, at the start of every week, we would have a planning session where we would select and delegate tasks and state what we had accomplished in the previous week.",
    ),
    (
        "Wakeup Streak",
        "August 2026",
        "Expo, React Native, Typescript",
        "Wakeup_Streak.png",
        "https://github.com/el124-choi/WakeupStreak",
        None,
        "A simple cross-platform alarm app. \nThe user can set a time for the app to wake them up with a notification. Waking up on time increases their streak, with the aim being to get their 'Wakeup Streak' as high as possible. Creating this app allowed me to kill two birds with one stone over the summer: I could give myself the motivation to wake up earlier and learn how to use the Expo and React frameworks at the same time. ",
    ),
    (
        "Cairn",
        "October 2026",
        "Html, JavaScript, Gemini API, Codex",
        "Cairn.png",
        "https://github.com/el124-choi/Cairn",
        "HuddleHive WIT hackathon #7 (HuddleHive Track)"
        "A gamified roadmap generator that utilises the Gemini API to generate timestamped roadmaps based on plaintext user input. As the user progresses through the roadmap, their progress is displayed in a progress bar, where their 'avatar' leaves a stone to mark the milestones they have achieved, inspired by how travellers leave cairns to mark points on their travels. My team was a team of 5, where I predominantly worked with OpenAI's Codex to create the roadmap generation code.Part of our hackathon submission was a pitch to the judges, which I thought was a great opportunity for me to explain the decisions I made in the development process (and also a chance to show off my public speaking skills) instead of just demonstrating the features like a regular hackathon.",
    ),
]


def insert_projects():
    app = create_app()
    with app.app_context():
        db = get_db()
        inserted = 0

        for title, created, technologies, img_path, github, content in PROJECTS:
            exists = db.execute(
                "SELECT 1 FROM projects WHERE title = ?",
                (title,),
            ).fetchone()
            if exists:
                print(f"Skipped existing project: {title}")
                continue

            db.execute(
                """INSERT INTO projects
                   (title, created, technologies, img_path, github, content, completed, archived)
                   VALUES (?, ?, ?, ?, ?, ?, ?, ?)""",
                (
                    title,
                    created,
                    technologies,
                    img_path,
                    github,
                    content,
                    1,
                    0,
                ),
            )
            inserted += 1

        db.commit()
        print(f"Inserted {inserted} project(s).")


if __name__ == "__main__":
    insert_projects()
