# Twitch Plays Program - Step-by-Step Plan

- [x] **Step 1: Environment Setup** ✅
  - [x] Finalize architecture plan
  - [x] Initialize project directory `c:\projecten\python-proj\chat-plays`
  - [x] Create virtual environment
  - [x] Install `twitchio` and `pydirectinput`

- [/] **Step 2: The Twitch Listener** 🔨
  - [x] Create `twitch_listener.py`
  - [x] Set up basic bot with `twitchio`
  - [ ] Test reading chat and printing to console ← **You need to do this!**

- [x] **Step 3: The Command Parser** ✅
  - [x] Create `command_parser.py`
  - [x] Filter raw chat messages for allowed commands
  - [x] Abstract out spam
  - [x] Integrate parser into `twitch_listener.py`

- [/] **Step 4: The Input Emulator** 🔨
  - [x] Create `input_emulator.py`
  - [x] Implement robust `pydirectinput` keystrokes
  - [ ] Test keystrokes in simple application (e.g., Notepad) ← **You need to do this!**

- [x] **Step 5: The Configuration System** ✅
  - [x] Create `config.json`
  - [x] Create logic to load mappings (e.g., `"up": "w"`) from JSON instead of hardcoded

- [ ] **Step 6: Integration (The Final Bot)**
  - [ ] Create `main.py`
  - [ ] Tie listener, parser, configuration, and emulator together
  - [ ] Test in a real game environment

- [ ] **Step 7: Personalization & Expansion**
  - [ ] Discuss and add custom features (Democracy mode, User whitelists, delays, etc.)
