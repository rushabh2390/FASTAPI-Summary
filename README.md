# FASTAPI summary
## generate file probable metadata and probable summary
---
## Required  npm(version: 8.1.2) and python(version >3.7)
---
### Run locally
1. Clone this repo.
2. Go to project in terminal   
``` cd FAVM tutorial ```
3. Go to backend   
``` cd backend ```
4. Create virtual environment by running following command ( Note: if pipenv is not there the install it using ```pip install pipenv```)   
``` pipenv shell ```   
5. Run the followiing command to active virtual environment   
``` pipenv install ```
6. Execute the following command to run uvicorn
``` uvicorn main:app --reload ```
7. Open another terminal and go to project directory
8. Go to frontend   
``` cd frontend ```   
9. Install package from package.json   
``` npm install ```
10. Run front end vue   
``` npm run dev ```
11. Open  frontend in browser from [frontend](http://127.0.0.1:8080)
12. You can visit fastapi docs from [backend](http://127.0.0.1:8000)  
---
### Run in Docker
1. clone this repo
2. Go to project in terminal   
``` cd FASTAPI-Summary ```
3. Run follwing command to start docker with application
``` docker-compose up ``` Or ``` docker-compose up -d ```
4. Open  frontend in browser from [frontend](http://127.0.0.1:8080)
5.  You can visit fastapi docs from [backend](http://127.0.0.1:8000)