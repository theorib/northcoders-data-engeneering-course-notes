# Day 1

## First Lecture
### What makes a good coder
1. Analythical problem solving
2. Technical communication
3. Good engineering practices
4. Non-technical communication

### A Day in the life
- 08:30 - 08:45 | Prep/notes reading
- 08:45 - 09:45 | Lecture
    - Introduction to new concepts
    - All lectures are on zoom
    - All in the calendar
- 09:45 - 17:00 | Sprint
    - Set challenges to practice new concepts
    - Not actually a race
    - some solo, some pair
- 12:30 - 13:30 | Lunch time
- 13:30 - 14:30 | Seminar / 2nd Lecture
    - Seminars are more discussions less new concepts more collaborative
    - Best places for questions and open discussions
- 16:00 - 17:00 | 1-1 mentor check-ins (not everyday for everyone)

### What if you are stuck in a sprint
1. discussion with your pairs
2. Scheduled checkins
3. documentation
4. Google
5. Mentor 1-2-1s
6. Helpdesk

### Course Structure
1. 1 week | Intro Week
2. 3 weeks | Python Fundamentals
    -  Assessment at the end
3. 4 weeks | DE Fundamentals
    - devops
    - cloud fundamentals
    -  Assessment at the end
4. 2 weeks | DE Toolkit
5. 3 weeks | Projects

### What is hardware
- The physical tangible parts of a computer

### What is software
- the code!
- set of instructions to carry out a task
- programs that run on your hardware

### What is an operating system
- software that manages computer resources for other software
- the bridge between hardware and software
- allows us to write nice code without having to deal with the complexity of interacting directly with hardware
- It abstracts away a lot of common tasks necessary to run most software allowing them to interact with the hardware and letting programmers focus on the problems they want to solve, not on lots of smaller hurdles along the way
- An OS abstracts away a lot of common tasks necessary to run most software allowing them to interact with the hardware and letting programmers focus on the problems they want to solve, not on lots of smaller hurdles along the way
- unix-based

## VS Code setup for `code` command
- open the command pallet with cmd+shift+p and look for `shell`
- select install `code` command in PATH
- restart the terminal
- save changes on focus change

## Git
### Guidelines
    - we write git commit messages imperativelly as if they were preceded by "this commit will..."
    - if we are about to write the word `and` to our commit, it should probably be done in multiple commits
    
### Look at
 - git revert
    -   Git rever brings us back in history to a previous commit by making a new commit. It is a much safer way to go back and fix mistakes than git reset

 - git reset
    - Git reset reverts the history to a specified commit and remove all commits that came after the specified commit, leaving changes in the staging area.
    - It is dangerous to modify the git history so use this with lots of care

Remove files in the stagint area
 ```shell
 git restore --staged filename
 ```

shows what remote is connected to our local repo or sets it up if additional arguments are passed
 ```shell
 git remote -v
 ```
 
Clone a github repo
```shell
git clone github://url
```

Push changes
```shell
git push origin main
```

Downloading changes to repository
```shell
git pull origin main
```

## Pair programming

### Navigator
- Focus
    The navigator's role is to review the code in real time ensuring it's accuracy and quality
- Task
    The navigator acts as a sounding board, asking questions, offering suggestions, and identifying potential problems or areas for improvement
- Communication
    The navigator should activelly participate in the conversation, explaining their reasoning and providing feedback to the driver

### Driver
- Focus
    The Driver's primary resposibility is to type the code and implement the solution.
- Task:
    Tge driver takes the lead in translating tthe problem into code, following the navigator's suggestions and guidance
- Communication:
    The driver needs to explain their thought process and the code they are writing to the navigator, fostering a collaborative environment

### Shared responsabilities
- Problem solving
- Code Quality
- Knowledge sharing
- Communication

Within a team the models inside a software developer's head are also part of the software development process

## Command Line Commands
- [100 Useful Command-Line Utilities](https://oliverelliott.org/post/commandlinereference/#Introduction)