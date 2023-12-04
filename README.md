# Containerized App Exercise
# Image Recognition

[![Build Status](https://github.com/software-students-fall2023/4-containerized-app-exercise-team111/actions/workflows/web-app.yml/badge.svg?event=pull_request)](https://github.com/software-students-fall2023/4-containerized-app-exercise-team111/actions/workflows/web-app.yml/badge.svg?event=pull_request)
[![Build Status](https://github.com/software-students-fall2023/4-containerized-app-exercise-team111/actions/workflows/machine-learning-client.yml/badge.svg)](https://github.com/software-students-fall2023/4-containerized-app-exercise-team111/actions/workflows/machine-learning-client.yml/badge.svg)

## Description

Our project introduces a machine learning client implemented image recognition feature, enabling the identification of objects within an image with a percentage match to
indicate the plausibility of matching object in the image. The web app connects to the machine client, allowing users to upload image to utilize the aforementioned picture. The user-friendly design ensures a smooth experience for all users to make the most out of the powerful image recognition services. All data will be stored with pymongo and delievered to the users by it. 

## Team Members

- [Merlin Li](https://github.com/wwxihan2)
- [Steven](https://github.com/stevenkhl446)
- [Harley](https://github.com/harley-bulbasaur)
- [Zhiyi (Valery)](https://github.com/Val001z)

## Stand up meetings
```
Standup Report - 30 November 2023
--------------------------------

Steven Liu @stevenkhl446
- Done: implemented machine learning client
- Doing: test functions for mlc
- Blocking: none

Merlin @wwxihan2
- Done: setting up web app
- Doing: client side javascript for connecting to database(setting up pymongo) 
- Blocking: none

Standup Report - 2 December 2023
--------------------------------
Steven Liu @stevenkhl446
- Done: redirect machine client learning to Merlin
- Doing: test functions for updated machine client learning by Merlin
- Blocking: none

Merlin @wwxihan2
- Done: finished web app routers structure and pymongo
- Doing: client side javascript, and machine learning client 
- Blocking: none

Standup Report - 4 December 2023
--------------------------------
Steven Liu @stevenkhl446
- Done: finsihed test functions for both web-app and machine client learning
- Doing: retesting, and mongodb test functions on machine learning, other documentations 
- Blocking: none

Merlin @wwxihan2
- Done: machine learning client, webcam.js(client side javascript), web app, mongodb.
- Doing: review all documentations
- Blocking: none
```


## Task boards

- [Link to task board 1](https://github.com/orgs/software-students-fall2023/projects/99)
- [Link to task board 2](https://github.com/orgs/software-students-fall2023/projects/100)


## Running the Application

- step 1: Clone the repository
- step 2: In the main directory, run `docker-compose up --build`.
- step 3: Open your browser and go to `http://localhost:8001`. 
- step 4: Engjoy using the application!

## Test Coverage
![](coverage.png)



