# Pokemon RPG Implementation in Pygame

A turn-based RPG game developed using Pygame, featuring monster battles and trainer encounters. This project implements core mechanics of monster-training games, including battle systems, character interactions, and world exploration. Note: This is a development version with known issues.

#Git link: https://github.com/kryyo1441/pygame-pokemon-rpg

## Project Documentation

Visual documentation of key game components:

![Title Screen](readme/title_screen.png)
Interface implementation demonstrating the game's entry point

![Battle Scene](readme/battle.png)
Battle system implementation with turn-based combat

![Overworld](readme/overworld.png)
World navigation and character interaction system

## Quick Start

Getting the game running is super simple:
1. Open your terminal/command prompt
2. Navigate to the project folder and install required dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Navigate to the code folder:
   ```
   cd code
   ```
4. Run the game:
   ```
   python main.py
   ```

## How It Works 🔄

Here's a flowchart of the game's main systems:

```
                                  [Title Screen]
                                       |
                                   [Play/Exit]
                                       |
                                 [Game World]
           ___________________________|___________________________
          |                |                    |                |
    [Player Movement]  [NPCs/Trainers]     [Transitions]   [Menu System]
          |                |                    |                |
    [Collisions]     [Dialogue]         [Battle System]   [Monster Index]
                          |                    |
                          |                    |
                          |        [Current Monster Actions]
                          |         ________|________
                          |        |       |        |
                          |   [Attack] [Defend] [Switch]
                          |        |
                          |    [Animate]
                          |        |
                          |   [Deal Damage]
                          |        |
                          |   [Battle End]
                          |   [Win/Lose]
                          |
                     [Return to World]
```

## The Squad Behind the Game 👥

Our awesome team of developers who brought this to life:

* **vedantgrd** (86 commits: +14,540 -2,529)
  - Overworld development
  - Core battle system and logic
  - Primary game mechanics

* **arctic** (58 commits: +765 -127)
  - Monster index implementation
  - Battle screen design
  - Battle logic enhancements
  - Animation systems

* **kryyo1441** (55 commits: +719 -233)
  - Overworld features
  - Battle animations
  - Bug fixes and polish
  - Final gameplay tweaks

* **vicharerushi2005** (27 commits: +310 -88)
  - Battle system setup
  - Battle completion mechanics

* **Apekshat69** (22 commits: +737 -70)
  - Dialogue system
  - Battle setup assistance

## Implemented Features

* World exploration system
* Trainer battle mechanics
* Monster progression system
* Turn-based combat implementation
* Battle animation framework
* Dialog interaction system
* Monster database interface

## Technical Challenges

* **Collision System**: Implementation of collision detection presents ongoing challenges due to the complexity of multiple collision layers (NPCs, objects, transitions). Current implementation requires optimization and bug fixes.

* **Battle Logic**: The battle system's complexity, involving extensive game data management (monsters, moves, stats), presents significant synchronization challenges. Current implementation requires additional error handling and state management improvements.

* **Game State Management**: Transition management between overworld, battles, and menu states presents substantial complexity in maintaining consistent game state. Current implementation requires enhanced state validation and error recovery systems.

## Known Issues 🐛

* Collision detection can be unreliable in certain areas
* Some battle transitions might get stuck (just restart if this happens!)
* Monster stats might not always update correctly after battles
* Occasional visual glitches in battle animations

## Future Features 🚀

* Wild monster encounters system
* Monster catching mechanics
* More diverse battle environments
* Improved collision system
* Save/Load game feature
* More trainer battles
* Extended monster roster
* Evolution system

## Want to Try It? 🎯

Just clone the repo, make sure you have Python and Pygame installed, and you're good to go! Jump into the code folder and start your adventure!

## Credits 🎨

* **Art Assets**: Huge thanks to [Scarloxy](https://scarloxy.itch.io/mpwsp01) for their amazing tileset, animations, and art assets that bring our game to life.

Have fun playing! 🎮✨