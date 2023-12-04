# Containerized App Exercise
# Image Recognition

[![Build Status](https://img.shields.io/badge/build-passing-brightgreen.svg)](URL-to-build-status)
[![Tests Status](https://img.shields.io/badge/tests-passing-brightgreen.svg)](URL-to-tests-status)

## Description

The machine learning client implemented image recognition feature, being able to identify objects within the image with a percentage match to
indicate the plausibility of matching object in the image. The web app connects to the machine client, allowing users to upload image to utilize the aforementioned picture. All data will be stored with pymongo and delievered to the users by it. 

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
-doing: test functions for mlc
-blockers none

Merlin @wwxihan2
- did: setting up web app
-doing: client side javascript for connecting to database(setting up pymongo) 
-blockers none


Standup Report - 2 December 2023
--------------------------------
Steven Liu @stevenkhl446
-did: redirect machine client learning to Merlin
-doing: test functions for updated machine client learning by Merlin
-blockers none

Merlin @wwxihan2
- did: finished web app routers structure and pymongo
-doing: client side javascript, and machine learning client 
-blockers none

Standup Report - 4 December 2023
--------------------------------
Steven Liu @stevenkhl446
- did: finsihed test functions for both web-app and machine client learning
-doing: retesting, and mongodb test functions on machine learning, other documentations 
-blockers none

Merlin @wwxihan2
- did: machine learning client, webcam.js(client side javascript), web app, mongodb.
-doing: review all documentations
-blockers none
```


## Configuration and Setup

step 1: clone the repository
step 2: run  docker-compose up --build in the main directory
step 3: go to http://localhost:8001 on your browser
step 4: enjoy!
.....
### Prerequisites
[Requirement.txt File](/4-containerized-app-exercise-team111/requirements.txt)

put requriements.txt here
### Setup and Installation

- Step-by-step guide on setting up the environment.
- How to install the necessary dependencies/packages.

### Running the Application

- Instructions on how to run the web app.
- Instructions on how to run the machine learning client.

## Importing Starter Data

If your system requires starter data to operate correctly, provide instructions on how to import this data into the database.

### Steps to Import Data

1. Step 1: Direct to app.py within web-app foler
2. Step 2: Run the program to the main page
3. Step 3: Upload preferred image(jpg or png) to see results
4. step 4: results will be stored in a database

## Additional Notes

Be aware of the version of dependencies downloaded. They must match the provided dependencies in requirements.txt.
---

Build a containerized app that uses machine learning. See [instructions](./instructions.md) for details.
