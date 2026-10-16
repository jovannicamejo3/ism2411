# ISM2411 — Python for Business

## About Me

- Name: Jovanni Camejo
- Semester: Fall 2026
- School: University of South Florida

## About This Repo

This repository holds my coursework for ISM 2411, Introduction to Python for Business. It's organized by week, with each folder containing the code I wrote for that module.

## Modules

- `week05/` — Conditionals: tiered discount calculator
- `week06/` — Loops: sales report with sum, average, max
- `week07/` — Functions: calculate_tax, apply_discount
- `week08/` — Git: first GitHub submission

## How to Run

Each script is standalone. Open a terminal and run:
```
python week07/functions.py
``` 

## Reflection

### 1. Commit history

```
a588f7d add README with module listing and run instructions
663ccef add module 7 functions: calculate_tax, apply_discount, final_price
6e7bc12 add .gitignore for Python and OS files
5867a9f Update project name in README
f7b1720 Initial commit
```

If I were hiring someone and saw this history, it would tell me they work in small, organized steps instead of dumping everything in at once. Each commit does one thing and the message says exactly what changed, so someone else could follow the project without asking questions. It also shows they set up the project properly first (the .gitignore) before adding code.

### 2. How Git changes how I edit scripts

Before this module, if I had a working script I would just edit it directly and hope I didn't break anything. Now I would commit the working version first, then make my changes, so if something breaks I can always return to the last version that worked. I would also commit more often with clear messages so I can see what changed and when.

### 3. Something I would add to my .gitignore

I would add `.venv/`, which is the folder for a Python virtual environment. It holds installed packages specific to my computer, it can get really large, and anyone can recreate it from the project's requirements, so there's no reason to upload it to GitHub.