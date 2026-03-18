# Twitch Plays Program - Step-by-Step Plan

- [x] **Step 1: Environment Setup** ✅
  - [x] Finalize architecture plan
  - [x] Initialize project directory `c:\projecten\python-proj\chat-plays`
  - [x] Create virtual environment
  - [x] Install `twitchio` and `pydirectinput`

- [ ] **Step 2: The Twitch Listener**
  - [ ] Create `twitch_listener.py`
  - [ ] Set up basic bot with `twitchio`
  - [ ] Test reading chat and printing to console

- [ ] **Step 3: The Command Parser**
  - [ ] Create `command_parser.py`
  - [ ] Filter raw chat messages for allowed commands
  - [ ] Abstract out spam

- [ ] **Step 4: The Input Emulator**
  - [ ] Create `input_emulator.py`
  - [ ] Implement robust `pydirectinput` keystrokes
  - [ ] Test keystrokes in simple application (e.g., Notepad)

- [ ] **Step 5: The Configuration System**
  - [ ] Create `config.json`
  - [ ] Create logic to load mappings (e.g., `"up": "w"`) from JSON instead of hardcoded

- [ ] **Step 6: Integration (The Final Bot)**
  - [ ] Create `main.py`
  - [ ] Tie listener, parser, configuration, and emulator together
  - [ ] Test in a real game environment

- [ ] **Step 7: Personalization & Expansion**
  - [ ] Discuss and add custom features (Democracy mode, User whitelists, delays, etc.)
