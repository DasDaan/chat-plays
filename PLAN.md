# Twitch Plays Architecture Plan

## Goal Description
Build a highly customizable, from-scratch Twitch Plays program in Python. The focus is on using the best available modern libraries for maximum game compatibility and organizing the code so it is easy to understand and expand step-by-step.

## User Review Required
> [!IMPORTANT]
> Please review this updated plan where I explain *why* we chose certain technologies. If everything makes sense, we will proceed to Step 1!

## Proposed Changes & Best Options

### 1. Technology Stack Selection (The "Why")

*   **Twitch Connection: `twitchio`**
    *   *Why it's the best*: Instead of writing raw socket connections (which is what DougDoug often does in his older videos), `twitchio` is a modern, asynchronous library explicitly built for Twitch. It automatically handles reconnects, easily parses chat messages, and deals with Twitch's rate limits. It is the most robust way to read chat in Python today.
*   **Keyboard/Mouse Emulation: `pydirectinput`**
    *   *Why it's the best*: The standard library for this is `pyautogui`, but it uses virtual keycodes that most modern 3D games (like Minecraft, GTA, etc.) ignore because they use "DirectInput". `pydirectinput` sends DirectX scancodes directly to the OS, closely mimicking a physical keyboard. This guarantees your program will work on almost any game.
*   **Controller Emulation (Optional Future Step): `vgamepad`**
    *   *Why it's the best*: Some modern games completely ignore simulated keyboards. `vgamepad` creates a virtual Xbox 360 controller on your PC. It’s the ultimate fallback if standard keyboard emulation fails.
*   **Configuration: JSON (`config.json`)**
    *   *Why it's the best*: JSON is built into Python natively. It allows you to create a simple text file mapping words like `"jump"` to the `"spacebar"` without touching the actual Python code.

### 2. Step-by-Step Architecture

We will build this in small, digestible steps, ensuring each piece works perfectly before moving to the next.

#### Step 1: The Environment
Set up the Python folder, verify the installation, and install our "best option" libraries (`twitchio`, `pydirectinput`).

#### Step 2: The Twitch Listener (`twitch_listener.py`)
A script that just connects to your Twitch channel and prints chat messages to your console. We test this to make sure we can actually "hear" the chat.

#### Step 3: The Command Parser (`command_parser.py`)
We add logic to filter the chat. If someone types "Hello", we ignore it. If someone types "jump", we recognize it as a valid command. 

#### Step 4: The Input Emulator (`input_emulator.py`)
A script that takes our valid commands ("jump") and actually presses the corresponding keys on your computer. We will test this outside of a game first (like in a Notepad file).

#### Step 5: The Configuration System (`config.json`)
We move the hardcoded commands out of the code and into a simple file so you can easily change controls for different games.

#### Step 6: Integration (`main.py`)
We link everything together: Chat comes in -> Parser checks it -> Emulator presses the key. 

## Verification Plan
For each step, we will run the individual script. For example, in Step 2, we will run the script, you type in your Twitch chat, and we verify it appears on your screen. We only move to Step 3 once Step 2 is perfectly understood and working.
