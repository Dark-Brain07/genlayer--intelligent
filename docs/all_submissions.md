# Chain Quest — GenLayer Submission Templates

Use these templates to submit your project to the **GenLayer Points Portal**. Submit the main project under **Projects & Milestones**, then submit each of the 15 contracts individually under **Tools & Infrastructure** for maximum points.

---

## MAIN SUBMISSION → Category: Projects & Milestones (20-4000 pts)

### Chain Quest: On-Chain RPG Powered by Real-World Data

**Title:** Chain Quest — GenLayer Intelligent RPG with 15 Web-Fetched Oracles
**Description:**
Built an on-chain RPG game consisting of 15 intelligent contracts on GenLayer where every game mechanic is driven by real-world data fetched via `gl.nondet.web.get()` from live public APIs (Binance, Open-Meteo, GitHub, RestCountries, ISS Tracker, and more). Every oracle uses `gl.eq_principle.strict_eq` for deterministic validator consensus on parsed values. Includes a pixel-art retro landing page with starfield animation.

- **GitHub Repository:** [https://github.com/Dark-Brain07/genlayer--intelligent](https://github.com/Dark-Brain07/genlayer--intelligent)
- **Landing Page:** [View Landing Page](https://github.com/Dark-Brain07/genlayer--intelligent/blob/main/landing/index.html)

---

## INDIVIDUAL CONTRACT SUBMISSIONS → Category: Tools & Infrastructure (50-2500 pts)

_Deploy each contract in GenLayer Studio. Once deployed, provide the contract address and I will auto-generate the Explorer Link._

#### 1. Astronomy Oracle

**Title:** Sunrise/Sunset Day-Night Cycle Oracle for GenLayer
**Description:**
An intelligent contract that fetches real sunrise and sunset times from the Open-Meteo API using `gl.nondet.web.get()`. The fetched timestamps are parsed from JSON and validated through `gl.eq_principle.strict_eq` to ensure all validators reach identical consensus on the day/night cycle data. Used in Chain Quest to drive time-based game events.

- **Contract Address:** `0x004DAA7BEcC8Ebf7A0829420e0F807376C6D9C33`
- **Explorer Link:** [View on GenLayer Studio](https://explorer-studio.genlayer.com/address/0x004DAA7BEcC8Ebf7A0829420e0F807376C6D9C33)
- **Source Code:** [astronomy_oracle.py](https://github.com/Dark-Brain07/genlayer--intelligent/blob/main/contracts/astronomy_oracle.py)

#### 2. BNB Price Oracle

**Title:** Live BNB/USDT Price Feed Oracle for GenLayer
**Description:**
An intelligent contract that fetches the real-time BNB/USDT price from the Binance public API using `gl.nondet.web.get()`. The price is parsed from JSON, rounded to an integer for deterministic consensus, and validated through `gl.eq_principle.strict_eq`. Used in Chain Quest to determine guild treasury value.

- **Contract Address:** `0x6a0e4e049E03db0C07Cd049CC36Dd4737E3434a5`
- **Explorer Link:** [View on GenLayer Studio](https://explorer-studio.genlayer.com/address/0x6a0e4e049E03db0C07Cd049CC36Dd4737E3434a5)
- **Source Code:** [bnb_price_oracle.py](https://github.com/Dark-Brain07/genlayer--intelligent/blob/main/contracts/bnb_price_oracle.py)

#### 3. Country Info Oracle

**Title:** Real-World Country Data Oracle for Quest Generation
**Description:**
An intelligent contract that fetches real country information (name, population, region) from the RestCountries API using `gl.nondet.web.get()`. The data is parsed from JSON and pipe-delimited for clean consensus via `gl.eq_principle.strict_eq`. Used in Chain Quest to dynamically generate quest locations based on real geography.

- **Contract Address:** `0x2a6A5Ae66F5530028C714C1Ef3A2FdcEf4C9b0Ca`
- **Explorer Link:** [View on GenLayer Studio](https://explorer-studio.genlayer.com/address/0x2a6A5Ae66F5530028C714C1Ef3A2FdcEf4C9b0Ca)
- **Source Code:** [country_info_oracle.py](https://github.com/Dark-Brain07/genlayer--intelligent/blob/main/contracts/country_info_oracle.py)

#### 4. Crypto Price Oracle

**Title:** Live BTC/USDT Price Feed Oracle for GenLayer
**Description:**
An intelligent contract that fetches the real-time Bitcoin price from the Binance public API using `gl.nondet.web.get()`. The price string is parsed from JSON, converted to an integer for byte-identical consensus, and wrapped in `gl.eq_principle.strict_eq`. Used in Chain Quest to set the in-game gold exchange rate.

- **Contract Address:** `0xD40098A712cbFd701A6634DA54e2445cd9637051`
- **Explorer Link:** [View on GenLayer Studio](https://explorer-studio.genlayer.com/address/0xD40098A712cbFd701A6634DA54e2445cd9637051)
- **Source Code:** [crypto_price_oracle.py](https://github.com/Dark-Brain07/genlayer--intelligent/blob/main/contracts/crypto_price_oracle.py)

#### 5. Dog Fact Oracle

**Title:** Real Dog Facts Oracle for Companion Pet Dialogue
**Description:**
An intelligent contract that fetches real random dog facts from the DogAPI using `gl.nondet.web.get()`. The fact text is parsed from the nested JSON response and validated through `gl.eq_principle.strict_eq`. Used in Chain Quest to generate authentic companion pet dialogue and in-game lore text.

- **Contract Address:** `0xF61D5d595893F4e3369B0dCC15125555eF6c8489`
- **Explorer Link:** [View on GenLayer Studio](https://explorer-studio.genlayer.com/address/0xF61D5d595893F4e3369B0dCC15125555eF6c8489)
- **Source Code:** [dog_fact_oracle.py](https://github.com/Dark-Brain07/genlayer--intelligent/blob/main/contracts/dog_fact_oracle.py)

#### 6. ETH Gas Oracle

**Title:** Live ETH/USDT Price Oracle for Dynamic Crafting Costs
**Description:**
An intelligent contract that fetches the real-time Ethereum price from the Binance public API using `gl.nondet.web.get()`. The price is parsed from JSON, truncated to an integer, and validated via `gl.eq_principle.strict_eq` for deterministic consensus. Used in Chain Quest to dynamically calculate in-game crafting costs.

- **Contract Address:** `0xA07D2648171c93754Ce1Cf5cf9F6eAA5e52448e0`
- **Explorer Link:** [View on GenLayer Studio](https://explorer-studio.genlayer.com/address/0xA07D2648171c93754Ce1Cf5cf9F6eAA5e52448e0)
- **Source Code:** [eth_gas_oracle.py](https://github.com/Dark-Brain07/genlayer--intelligent/blob/main/contracts/eth_gas_oracle.py)

#### 7. GitHub Repo Oracle

**Title:** GitHub Repository Stats Oracle for Developer Quests
**Description:**
An intelligent contract that fetches real GitHub repository statistics (stars and forks) from the GitHub API using `gl.nondet.web.get()`. The parsed star and fork counts are pipe-delimited and validated through `gl.eq_principle.strict_eq`. Used in Chain Quest to generate developer-themed quests where stars equal XP and forks equal allies.

- **Contract Address:** `0xFDa8103792751eC370A9bfca881Bb97281cF5D84`
- **Explorer Link:** [View on GenLayer Studio](https://explorer-studio.genlayer.com/address/0xFDa8103792751eC370A9bfca881Bb97281cF5D84)
- **Source Code:** [github_repo_oracle.py](https://github.com/Dark-Brain07/genlayer--intelligent/blob/main/contracts/github_repo_oracle.py)

#### 8. ISS Tracker Oracle

**Title:** International Space Station Position Tracker Oracle
**Description:**
An intelligent contract that fetches the real-time position (latitude/longitude) of the International Space Station from the Open Notify API using `gl.nondet.web.get()`. Coordinates are parsed from JSON and validated via `gl.eq_principle.strict_eq`. Used in Chain Quest to generate space-themed dungeon coordinates.

- **Contract Address:** `0xd432f74fe6F9BEA47f019191556e66a4fAA78CBA`
- **Explorer Link:** [View on GenLayer Studio](https://explorer-studio.genlayer.com/address/0xd432f74fe6F9BEA47f019191556e66a4fAA78CBA)
- **Source Code:** [iss_tracker_oracle.py](https://github.com/Dark-Brain07/genlayer--intelligent/blob/main/contracts/iss_tracker_oracle.py)

#### 9. Number Fact Oracle

**Title:** Number Trivia Oracle for Dungeon Riddle Generation
**Description:**
An intelligent contract that fetches real number trivia from the NumbersAPI using `gl.nondet.web.get()`. The trivia text is parsed from JSON and validated through `gl.eq_principle.strict_eq`. Used in Chain Quest to generate riddle puzzles that guard dungeon gates.

- **Contract Address:** `0x5328088D1C5eB19eC1a8cc2AcaB525a0f71ADb48`
- **Explorer Link:** [View on GenLayer Studio](https://explorer-studio.genlayer.com/address/0x5328088D1C5eB19eC1a8cc2AcaB525a0f71ADb48)
- **Source Code:** [number_fact_oracle.py](https://github.com/Dark-Brain07/genlayer--intelligent/blob/main/contracts/number_fact_oracle.py)

#### 10. Player Registry

**Title:** On-Chain Player Profile & Leveling System
**Description:**
An intelligent contract providing on-chain player registration with name, level, and XP tracking using GenLayer's `TreeMap` storage and `u256` integer types. Players register with a unique address and can level up through gameplay. This is the core identity layer for the Chain Quest RPG.

- **Contract Address:** `0xC5F491350B19878044DEfc4549B72d59CA2AA455`
- **Explorer Link:** [View on GenLayer Studio](https://explorer-studio.genlayer.com/address/0xC5F491350B19878044DEfc4549B72d59CA2AA455)
- **Source Code:** [player_registry.py](https://github.com/Dark-Brain07/genlayer--intelligent/blob/main/contracts/player_registry.py)

#### 11. SOL Price Oracle

**Title:** Live SOL/USDT Price Feed Oracle for GenLayer
**Description:**
An intelligent contract that fetches the real-time Solana price from the Binance public API using `gl.nondet.web.get()`. The price is parsed from JSON, rounded to an integer for deterministic consensus, and validated through `gl.eq_principle.strict_eq`. Used in Chain Quest to set potion and spell costs.

- **Contract Address:** `0x8aD72aEDa266Dc5be20F6eC26e6B52774fAfb23a`
- **Explorer Link:** [View on GenLayer Studio](https://explorer-studio.genlayer.com/address/0x8aD72aEDa266Dc5be20F6eC26e6B52774fAfb23a)
- **Source Code:** [sol_price_oracle.py](https://github.com/Dark-Brain07/genlayer--intelligent/blob/main/contracts/sol_price_oracle.py)

#### 12. University Oracle

**Title:** Real University Data Oracle for Scholar NPC Generation
**Description:**
An intelligent contract that fetches real university data from the Hipolabs Universities API using `gl.nondet.web.get()`. University name and country are parsed and pipe-delimited for consensus via `gl.eq_principle.strict_eq`. Used in Chain Quest to generate scholar NPC backgrounds and academy-themed quests.

- **Contract Address:** `0x7702821e11743EE9dE0B4944F722Ed8E0bF24f1f`
- **Explorer Link:** [View on GenLayer Studio](https://explorer-studio.genlayer.com/address/0x7702821e11743EE9dE0B4944F722Ed8E0bF24f1f)
- **Source Code:** [university_oracle.py](https://github.com/Dark-Brain07/genlayer--intelligent/blob/main/contracts/university_oracle.py)

#### 13. Weather Battle Oracle

**Title:** Real-Time Weather Oracle for Dynamic Battle Conditions
**Description:**
An intelligent contract that fetches real temperature data from the Open-Meteo API using `gl.nondet.web.get()`. The temperature is parsed from JSON and validated through `gl.eq_principle.strict_eq`. The contract then deterministically sets battle conditions: FIRE (>35°C), ICE (<5°C), or NEUTRAL. This is the flagship oracle of Chain Quest.

- **Contract Address:** `0x8107A929f1b7F9b2c549bc5645C942c9D1F006aE`
- **Explorer Link:** [View on GenLayer Studio](https://explorer-studio.genlayer.com/address/0x8107A929f1b7F9b2c549bc5645C942c9D1F006aE)
- **Source Code:** [weather_battle_oracle.py](https://github.com/Dark-Brain07/genlayer--intelligent/blob/main/contracts/weather_battle_oracle.py)

#### 14. Wind Speed Oracle

**Title:** Real-Time Wind Data Oracle for Sailing & Flight Mechanics
**Description:**
An intelligent contract that fetches real wind speed and direction from the Open-Meteo API using `gl.nondet.web.get()`. Both values are parsed from JSON and pipe-delimited for consensus via `gl.eq_principle.strict_eq`. Used in Chain Quest to determine sailing speed and flight mechanics.

- **Contract Address:** `0x1045869F7DE3A264a169bB6572F4BBc619826C00`
- **Explorer Link:** [View on GenLayer Studio](https://explorer-studio.genlayer.com/address/0x1045869F7DE3A264a169bB6572F4BBc619826C00)
- **Source Code:** [wind_speed_oracle.py](https://github.com/Dark-Brain07/genlayer--intelligent/blob/main/contracts/wind_speed_oracle.py)

#### 15. XRP Price Oracle

**Title:** Live XRP/USDT Price Feed Oracle for GenLayer
**Description:**
An intelligent contract that fetches the real-time XRP price from the Binance public API using `gl.nondet.web.get()`. The price is parsed from JSON, rounded to 2 decimal places for consensus stability, and validated through `gl.eq_principle.strict_eq`. Used in Chain Quest to calculate cross-realm travel costs.

- **Contract Address:** `0x3160849592D43C3c2dC76199e9Fe7411cE34102c`
- **Explorer Link:** [View on GenLayer Studio](https://explorer-studio.genlayer.com/address/0x3160849592D43C3c2dC76199e9Fe7411cE34102c)
- **Source Code:** [xrp_price_oracle.py](https://github.com/Dark-Brain07/genlayer--intelligent/blob/main/contracts/xrp_price_oracle.py)
