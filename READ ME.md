<p align="center"><img src="Imagenes%20del%20READ%20ME/uc3m_logo.png" alt="uc3m" width="480"></p>

**Programming 2026 - 2027**

# Final Project: *Service Rush*

---

## Table of contents

1. [Introduction](#1-introduction)
2. [Project Objectives](#2-project-objectives)
3. [Game Description](#3-game-description)
   - [Game Objective](#game-objective)
   - [Setting and Characters](#setting-and-characters)
   - [Game Mechanics](#game-mechanics)
   - [Recipes](#recipes)
   - [Cooking](#cooking)
   - [Orders](#orders)
   - [Score and end of service](#score-and-end-of-service)
4. [Project Requirements](#4-project-requirements)
5. [Project Deliverables](#5-project-deliverables)
6. [Evaluation](#6-evaluation)
7. [Submission Rules](#7-submission-rules)

---

## 1. Introduction

This document describes the final project for the Programming course, focused on the development of a cooking game inspired by *Overcooked*. Students will apply the programming concepts and techniques learned throughout the course to create a fully functional and engaging game.

## 2. Project Objectives

The main objectives of this project are:

- Design and implement a cooperative cooking game using Python with Pyxel.
- Demonstrate mastery of fundamental programming concepts such as loops, conditional statements, data structures, and **object-oriented programming**.
- Gain experience in game development concepts such as character movement or collision detection.
- Develop problem-solving and critical thinking skills in a creative and engaging context.

## 3. Game Description

![Overcooked gameplay screenshot](Imagenes%20del%20READ%20ME/cover_overcooked.png)

Students will develop a cooking game inspired by Overcooked. Two chefs work together in a traditional Spanish restaurant to prepare and serve the customers' orders before they run out of patience. A counter divides the kitchen into two zones, one for each chef, so they have to work together. Each service is a level with a time limit. The game goes on level after level, with one more order each time, until the team makes 3 failures, and the score keeps growing according to how well the team serves the orders.

This is how an order goes from the board to the customer:

1. An order appears on the service board with a time that starts running down.
2. Each chef uses a dish to take from their drawers the ingredients of their zone and chops those that need it.
3. Anything that changes zone (a dish, empty or with food) is left on a hand-over surface in the middle of the kitchen for the other chef.
4. The ingredients go into the right piece of equipment. When the preparation is ready, it is taken out with a dish; only Chef 2 can take dishes from the stack.
5. Chef 1, the only one who serves, hands the dish in at the delivery counter before its time runs out, and the team scores the points of the recipe.

Meanwhile new orders keep arriving, so the chefs have to share the work and keep several orders going at once.

<p align="center">
  <img src="Imagenes%20del%20READ%20ME/figure1_kitchen_layout.png" alt="Figure 1: The kitchen layout" width="600">
</p>
<p align="center"><em><strong>Figure 1:</strong> The kitchen. Every group uses this layout (see Setting and Characters, below).</em></p>

### Game Objective

The objective is to serve as many orders as possible, reach the highest possible level and get the highest possible score before the game ends with 3 failures.

### Setting and Characters

The game is played on a single screen of **192 × 176 pixels**: the service board is at the top and the kitchen is below it. Each chef starts in the middle of their zone and can carry only one object at a time.[^1]

The kitchen is shown in Figure 1, with every element always in the same place. Tiles with no station are free worktop (on the worktops) or solid wall (on the dividing counter).

- **Chef 1:** works in the upper zone and cannot reach anything in the lower one. She has her own drawers, a chopping board and the blender. She is the only one who serves at the delivery counter.
- **Chef 2:** works in the lower zone and cannot reach anything in the upper one. He has his own drawers, a chopping board, the pan and the stack of dishes. He is the only one who takes dishes from the stack.
- **Zones:** each zone has three rows of floor and a worktop along its outer edge. Chefs can only stand on the floor. The dividing counter runs between the two zones and belongs to both.
- **Worktops:** hold the stations of each zone. Any empty tile can hold one dish.
- **Stations:** the fixed elements on the worktops and the dividing counter. Each holds one element at a time.
- **Ingredients:** some must be chopped first; others go straight into the equipment. Each unit is used up when it joins a preparation, so two orders that need the same ingredient need two units. Each ingredient can be whole, chopped or blended, and raw or cooked.
- **Drawers:** each is an unlimited source of one raw ingredient. No ingredient is available in both zones, so no recipe can be finished by one chef alone.
  - *Lower zone:* tomato and potato, which must be chopped.
  - *Upper zone:* onion and chorizo, which must be chopped, and egg, which goes straight in.
- **Chopping boards:** one in each zone. They turn raw ingredients into chopped ones.
- **Blender and pan:** turn a set of ingredients into a preparation. The blender is in the upper zone and the pan in the lower one, so a preparation often has to change zones.
- **Dishes:** a preparation is served on a dish, and a dish is the only way to take anything out of a piece of equipment. A dish is either empty or full, and only a full dish completes an order. Each chef works with a single dish: the ingredients are added to it, taken to the equipment and taken out again in the same dish. A chef who needs to pick up another dish leaves their own on a free surface first.
- **Stack of dishes:** in the lower zone, it is an unlimited source of empty dishes. Only Chef 2 can take them, so he passes Chef 1 every dish she needs through the dividing counter.
- **Delivery counter:** in the upper zone. A full dish handed in here completes an order and disappears.
- **Bin:** shared by both chefs. The content of a dish thrown in is lost. The dish is never destroyed: it is emptied and stays in the chef's hands.
- **Dividing counter:** runs across the kitchen from wall to wall. It is the only point of contact between the chefs, who cannot cross it or walk on it. Each of its tiles is one of these:
  - *Hand-over surface:* holds a dish and both chefs can reach it. Everything that changes zones must be left here.
  - *Solid wall:* holds nothing; it only separates the zones.
  - *The Bin*, described above, or *the sink*, which is only used in the optional dish cycle (Sprint 5).

  There are always four hand-over surfaces (Figure 1).
- **Service board:** the band at the top of the screen, outside the kitchen. It shows:
  - *Left side — Orders:* one ticket per order, each with its time counter. When the time runs out, the order is lost and a failure is added.
  - *Right side — Score, failures and timer:* the score grows with each order delivered correctly and drops when an order is lost, the failure counter adds each mistake, and the timer shows the time left.

[^1]: If the game window looks small, maximise it or press <kbd>Alt</kbd>+<kbd>Enter</kbd> for full screen, and the game scales to fit. To open it directly at a comfortable size, pass `display_scale=4` to `pyxel.init`, so that each game pixel is shown as a 4 × 4 block.

### Game Mechanics

Both chefs are controlled at the same time:

| Chef | Movement | Action |
|------|----------|--------|
| Chef 1 | <kbd>W</kbd> <kbd>A</kbd> <kbd>S</kbd> <kbd>D</kbd> | Left <kbd>Shift</kbd> |
| Chef 2 | Arrow keys | Right <kbd>Shift</kbd> |

Each moves in four directions across the floor of their zone.

The action key affects the tile the chef is facing. What it does depends on what the chef is facing and what they are carrying, for example chopping, blending, leaving the dish or picking it up:

**Empty-handed**

- Facing the dish stack → takes out one empty dish
- Facing a station holding a dish → picks it up

**Carrying a dish**

- Empty or full, facing a free surface → leaves it there
- Empty or full, facing a drawer → the ingredient is added to the dish
- Empty, facing a piece of equipment or a chopping board → takes out whatever is inside
- Full, facing a piece of equipment → leaves everything in the dish to be processed
- Full, facing a chopping board → leaves the ingredients to be chopped; if there are several, all those that can be chopped are chopped
- Full, facing a station holding a dish → leaves the contents of the held dish into the other dish
- Full, facing the delivery counter → hands it in: it completes the matching order, or adds a failure if there is none
- Full, facing the bin → throws away the food

In any other case, the action key does nothing.

### Recipes

> The steps described below for each recipe are only one way of preparing it: any order and any split of the work between the chefs is valid, as long as the rules of the game are followed.

A recipe is an exact set of ingredients plus the equipment it is made in. The order of the ingredients does not matter, but nothing can be missing or extra:

| Recipe | Ingredients | Equipment | Points | Time limit | If lost |
|--------|-------------|-----------|:------:|:----------:|:-------:|
| Gazpacho | chopped tomato + chopped onion | Blender (upper zone) | 10 | 48 s | −5 |
| Spanish omelette | chopped potato + chopped onion + egg | Pan (lower zone) | 12 | 60 s | −6 |
| Broken eggs with chorizo | chopped potato + egg + chopped chorizo | Pan (lower zone) | 12 | 60 s | −6 |

- **Gazpacho** — *chopped tomato + chopped onion → blender, upper zone.* 10 points, time limit 48 s, −5 if lost. Chef 2 passes Chef 1 an empty dish. She adds an onion, chops it and leaves the dish on a hand-over surface. Chef 2 adds a tomato to his dish, chops it and empties it into Chef 1's dish. Chef 1 picks up her dish, empties it into the blender, takes the gazpacho out with that dish and serves it.
- **Spanish omelette** — *chopped potato + chopped onion + egg → pan, lower zone.* 12 points, time limit 60 s, −6 if lost. Chef 1 adds an onion to a dish passed by Chef 2, chops it, adds an egg and leaves the dish on a hand-over surface. Chef 2 adds a potato to his dish, chops it and empties it into Chef 1's dish. Then he picks up that dish, empties it into the pan, takes the omelette out with it and leaves it on a hand-over surface for Chef 1, who serves it.
- **Broken eggs with chorizo** — *chopped potato + egg + chopped chorizo → pan, lower zone.* 12 points, time limit 60 s, −6 if lost. Chef 1 adds a chorizo to a dish passed by Chef 2, chops it, adds an egg and leaves the dish on a hand-over surface. Chef 2 adds a potato to his dish, chops it and empties it into Chef 1's dish. Then he picks up that dish, empties it into the pan, takes the broken eggs out with it and leaves it on a hand-over surface for Chef 1, who serves it.

### Cooking

All the ingredients in the dish go into the equipment together. If they form a recipe of that equipment, they become that preparation. If not, the equipment still does its job: the blender blends them and the pan cooks them. They are then no good for any recipe and can be thrown in the bin. Everything is taken out together with a dish.

### Orders

The first order appears **3 seconds** after the service starts, giving the players time to find their way around the kitchen.

There will be **at most 3 orders** waiting at once. Each order is a gazpacho, a Spanish omelette or broken eggs with chorizo, randomly selected.

The first level has **4 orders** and each new level has one more. They arrive spread evenly over the service. If there are already 3 orders waiting, the next one appears when there is room. Orders still waiting when the service ends are not failures.

Each ticket shows the icon of the finished dish, the ingredients and its time counter.

### Score and end of service

The service lasts **3 minutes** and ends when the timer runs out or after **3 failures**. A failure is added when an order runs out of time or when something that completes no order is handed in. Binning is never a failure. The score never goes below zero.

When the timer runs out, the game stops and the score stays on the service board. Then everything is cleaned up and a new service starts at the next level. The score and the failures remain from one level to the next. After 3 failures the game stops and shows **"Game over"**.

Time is measured by counting frames. Pyxel runs at 30 frames per second by default, so 30 frames are one second. We recommend it so you do not need another library, but each group can use the method they prefer.

## 4. Project Requirements

The project must meet the following requirements:

- **Functionality:** The game must be fully functional, allowing the players to control both chefs and take an order from the drawers to the delivery counter.
- **Code quality:** The code must be well written, organized, and commented, and must use object-oriented programming.
- **User interface:** The game must have a clear and intuitive user interface, showing the kitchen with its two zones and every station described above, both chefs with whatever they are carrying, and the service board with the waiting orders, the score, the failure counter and the timer.
- **Game design:** The game design must be attractive and challenging, keeping a consistent retro aesthetic.
- **Graphics:** The graphic design will be a collaborative task in which the entire class will create the graphics as pyxres or png files using the Pyxel graphics editor, at 16 × 16 pixels as described in Sprint 1, and creating a common repository in Aula Global. Each group of students can change these images for their own. It is recommended not to spend too much time on this, as what will be marked is the correct implementation of the game using the object-oriented programming paradigm, and not its visual appearance. The first 3 groups that upload their pyxres graphics with the game images to Aula Global will receive an extra 0.1 points, provided that the final score of the work does not exceed the maximum of 2.5 points.
- **Music and sound effects:** sound effects can be included as extra (when chopping, when a preparation is ready, when a dish is served, when an order is lost, etc.).

## 5. Project Deliverables

Students must submit the following final products:

- **Source code:** the complete and well-commented source code of the game. The `.py` files and the `.pyxres` file the game uses must be submitted.
- **Report:** a PDF report with the contents described in Submission Rules, at the end of this document.

It is recommended to follow the steps below, although each group of students can choose their own implementation strategy, there will not be weekly control or monitoring.

### Sprint 1: Objects and graphical interface

- Create a class for each main game element: `Chef`, `Station`, `Ingredient`, `Dish`, `Order`, etc.
- All the behaviour logic of each entity must be contained in its corresponding class. Avoid including game logic in the main program (penalty if it occurs).
- The structure of the scenario must be the one in Figure 1. The images can be different.
- Keep the layout as data, in a list or a table the kitchen reads when the game starts.
- All the values in this document (the position of each element of the kitchen, times, points, penalties and the duration of the service) are fixed. Define them as constants in the code.
- Implement a score counter, a failure counter and a service timer visible during the game.
- Define the basic data structures that will manage the recipes, the waiting orders and the state of each station.

For this first sprint, it is enough to visually represent the elements, even if they do not move.

It is recommended to design 16 × 16 pixel graphics in the Pyxel editor and draw them at their real size, so that each tile is 16 × 16. To make the game look bigger, scale the whole screen with `display_scale` in `pyxel.init` instead of scaling each image.

The service board takes the top 192 × 32 pixels. Each group decides how to lay out the tickets, the score, the failure counter and the timer, as long as all the orders fit at once.

Each element should be drawn according to its state. For example ingredients may have a sprite when raw, another when chopped and another when blended. Dishes should have a sprite when empty and one for each finished recipe.

### Sprint 2: Chef movement

- Implement the movement of both chefs in the four directions:
  - Chef 1: <kbd>W</kbd> / <kbd>A</kbd> / <kbd>S</kbd> / <kbd>D</kbd> keys.
  - Chef 2: arrow keys.
- Each chef must move only across the floor of their own zone, without crossing the worktops or the dividing counter.
- Implement collision detection.

The objective of this sprint is to have fully controllable characters within the environment.

### Sprint 3: Ingredients, stations and recipes

- Implement the contextual action key (what it does depends on what the chef is facing and carrying, see [Game Mechanics](#game-mechanics)) and the flow of ingredients: drawers, chopping boards, cooking equipment, the stack of dishes and the dividing counter in both directions.
- Implement carrying: one dish per chef, a dish to take anything out of a piece of equipment, one element per station, and nothing dropped on the floor.
- Implement the visual states of the ingredients and of the content of each dish and each piece of equipment.
- Implement recipe validation.

At the end of this sprint, a complete dish can be prepared and plated, with no orders or scoring yet.

### Sprint 4: Orders, scoring and end of service

- Implement order generation, with a random recipe and the time counter.
- Implement the delivery counter: a full dish completes the matching order, or adds a failure if there is none, and disappears.
- Implement scoring, the penalties and the failure counter.
- Implement the bin to empty dishes.
- Implement the service timer and stop the game when the service ends, keeping the score visible, and show "Game over" after 3 failures.
- Implement the new level after each service. Each new level will increase the recipes to be prepared by 1 (see [Orders](#orders)).

From this sprint on, the game should be playable from start to finish.

### Sprint 5: Additional features (optional)

Up to **0.5 additional points** can be obtained, never exceeding the maximum of 2.5 for the project.

| Feature | Points | Description |
|---------|:------:|-------------|
| Sound effects | 0.10 | For example when chopping, when a preparation is ready, when a dish is served or when an order is lost. |
| Stars, start screen and end-of-service screen | 0.10 | At the end the team gets one, two or three stars according to the points scored in the level (never zero, even if the service ends through failures). The start screen shows the controls. At the end of each level, the end-of-service screen shows the score and the stars, and lets continue to the next level or quit; after "Game over", it lets play again or quit. |
| Dish cycle | 0.20 | Dishes become limited. A served dish comes back dirty to the return counter sometime later; Chef 2 washes it at the sink and it stays clean in the hands of whoever washed it. Without a clean dish nothing can be plated, and a dish emptied in the bin becomes dirty. |
| Times | 0.20 | Actions are not instantaneous. Chopping blocks the chef for a time. Cooking takes time but does not block the chef, who can do other things. |

## 6. Evaluation

The final project will be graded between **0 and 2.5 points**. Each sprint from 1 to 4 will be graded with 0.5 points. The report will represent the remaining 0.5 points. The optional part will be graded with an additional 0.5 points, distributed according to the difficulty of each functionality as detailed in Sprint 5, although the maximum score of 2.5 points will never be exceeded.

| Part | Points |
|------|:------:|
| Sprint 1 | 0.5 |
| Sprint 2 | 0.5 |
| Sprint 3 | 0.5 |
| Sprint 4 | 0.5 |
| Report | 0.5 |
| **Total** | **2.5** |
| Optional (Sprint 5) | up to +0.5 (max. 2.5 overall) |

The following aspects will be taken into account when evaluating the final project:

- Appropriate class design.
- Correct game execution and adequate adherence to the rules established in this document.
- Quality of the implemented code.
- Exclusive use of the content and principles taught during the course.
- Inclusion of comments in the code.
- General description of the implemented code in the report, according to the rules specified in the following section.

The following penalties will apply, if applicable:

| Penalty | Reason |
|:-------:|--------|
| −0.25 | Insufficient comments are included. All methods and classes must be correctly commented and annotated. Comments must also be included within the code of the different methods. |
| −0.5 | Methods are not used, repetitive code is included instead of loops, good programming practices taught during the course are not followed, poor class design, lists are not used to represent orders and ingredients, etc. |
| −0.5 | Unnecessary attributes are included, public attributes that should be private, attributes created outside the `__init__` method, or properties are not used where they should be. |
| −0.5 | Code outside the classes (with the exception of the main program), or methods that are too long (as a general rule, a method should occupy a single screen without the need to scroll). |

> [!WARNING]
> **Plagiarism will be strictly penalized:** both those who copy and those who are copied will be automatically excluded from continuous evaluation, in addition to any administrative measures that the University may apply. Two projects can be considered copied even if their degree of similarity is restricted to the code of a single method. Automatic plagiarism detection tools will be used.
>
> **The use of Generative AI is forbidden:** any use of AI to create any part of the code will be considered as plagiarism.

## 7. Submission Rules

The following rules are mandatory. Failure to comply with them may result in the task not being evaluated.

The final project must be carried out in **groups of 2 students**. Each group must upload a zip file containing the report, the source code and the `.pyxres` file to Aula Global before the deadline. The name of the zip file must follow the following format: `initials1-initials2.zip` (for example, if the students are Lucía Pérez Gómez and Juan García Jiménez, the file name must be `lpg-jgj.zip`).

The report (PDF format) must be **no more than 10 pages long**, and must include at least:

- Cover page, index, and a brief summary of the document.
- Class diagram and description of the designed classes, including the main attributes and methods.
- General description of the main algorithms used.
- Description of the work carried out, functionalities included, unimplemented parts, and additional functionalities performed.
- Game user manual with a description of how to play.
- Conclusions:
  - Final summary of the work carried out.
  - Main problems encountered.
  - Personal comments, evaluation, and aspects to improve the final project.
