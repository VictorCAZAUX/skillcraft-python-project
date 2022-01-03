# Skillcraft1 Dataset Analysis

## Starcraft II: Wings of Liberty

It is a multiplayer, strategy video game. It was released in 2010.
Online players are distributed into 7 leagues according to their level. 

## The Dataset

### Composition:
- 20 attributes
- 3 395 instances

### Collection of Data:
- Telemetry from 3 340 players of 7 leagues contacted through social media and online gaming communities
- Replays of 55 professional players found on gaming websites

## Problem: League Prediction
### Why?
- By analyzing games, we will be able to assess gamers' level and allocate them to a concording league so that the enjoyment maximum: no boredom nor frustration
- Better train game's AI so that players can feel the same challenge even offline

## Results
Our study of the SkillCraft1 dataset led to the implementation of a randomforest classifier. We managed 47% with some tuning and data tweaking


## Running the API

To run the API once you've downloaded the project,

```
$ py app.py
```

A web page on your default browser should open with the flask app. If not, go to this adress: localhost:5551/
