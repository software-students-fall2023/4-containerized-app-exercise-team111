# Containerized App Exercise
# Image Recognition

[![Build Status](https://github.com/software-students-fall2023/4-containerized-app-exercise-team111/actions/workflows/web-app.yml/badge.svg?event=push)](https://github.com/software-students-fall2023/4-containerized-app-exercise-team111/actions/workflows/web-app.yml/badge.svg?event=push)
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
- did: implemented machine learning client
- doing: test functions for mlc
- blockers: none

Merlin @wwxihan2
- did: setting up web app
- doing: client side javascript for connecting to database(setting up pymongo) 
- blockers: none

Zhiyi @Val001z
- did: review project specifications/instructions
- doing: try to develop functions according to instructions
- blockers: none

Standup Report - 2 December 2023
--------------------------------
Steven Liu @stevenkhl446
- did: redirect machine client learning to Merlin
- doing: test functions for updated machine client learning by Merlin
- blockers: none

Merlin @wwxihan2
- did: finished web app routers structure and pymongo
- doing: client side javascript, and machine learning client 
- blockers: none

Zhiyi @Val001z
- did: review the updated functions and limitations
- doing: test functions
- blockers: none

Standup Report - 4 December 2023
--------------------------------
Steven Liu @stevenkhl446
- did: finsihed test functions for both web-app and machine client learning
- doing: retesting, and mongodb test functions on machine learning, other documentations 
- blockers: none

Merlin @wwxihan2
- did: machine learning client, webcam.js(client side javascript), web app, mongodb.
-doing: review all documentations
-blockers none 
- doing: review all documentations
- blockers: none

Zhiyi @Val001z
- did: write the documentations.
- doing: review and revise the documentations
- blockers: none
```


## Task boards

- [Link to task board 1](https://github.com/orgs/software-students-fall2023/projects/99)
- [Link to task board 2](https://github.com/orgs/software-students-fall2023/projects/100)


## Running the Application

- step 1: Clone the repository
- step 2: In the main directory, run `docker-compose up --build`.
- step 3: Open your browser and go to `http://localhost:8001`. 
- step 4: Enjoy using the application!
Or
- Or access http://159.203.68.77:8001(However, it is extremely slow, so local sever is recommended)
If using Google Chrome, follow these steps to activate your camera:

1. **Open Chrome Flags**:
   - Type `chrome://flags/#unsafely-treat-insecure-origin-as-secure` in the address bar and press Enter.

2. **Enable Insecure Origins**:
   - Add `http://159.203.68.77:8001` in the "Insecure origins treated as secure" section.
   - Change dropdown to 'Enabled'.

3. **Relaunch Chrome**:
   - Click 'Relaunch' to apply changes.

## Test Coverage
![](coverage.png)



