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

- **Contract Address:** `[Deploy and provide address]`
- **Explorer Link:** [Will be generated after deployment]
- **Source Code:** [bnb_price_oracle.py](https://github.com/Dark-Brain07/genlayer--intelligent/blob/main/contracts/bnb_price_oracle.py)

#### 3. Country Info Oracle

**Title:** Real-World Country Data Oracle for Quest Generation
**Description:**
An intelligent contract that fetches real country information (name, population, region) from the RestCountries API using `gl.nondet.web.get()`. The data is parsed from JSON and pipe-delimited for clean consensus via `gl.eq_principle.strict_eq`. Used in Chain Quest to dynamically generate quest locations based on real geography.

- **Contract Address:** `[Deploy and provide address]`
- **Explorer Link:** [Will be generated after deployment]
- **Source Code:** [country_info_oracle.py](https://github.com/Dark-Brain07/genlayer--intelligent/blob/main/contracts/country_info_oracle.py)

#### 4. Crypto Price Oracle

**Title:** Live BTC/USDT Price Feed Oracle for GenLayer
**Description:**
An intelligent contract that fetches the real-time Bitcoin price from the Binance public API using `gl.nondet.web.get()`. The price string is parsed from JSON, converted to an integer for byte-identical consensus, and wrapped in `gl.eq_principle.strict_eq`. Used in Chain Quest to set the in-game gold exchange rate.

- **Contract Address:** `[Deploy and provide address]`
- **Explorer Link:** [Will be generated after deployment]
- **Source Code:** [crypto_price_oracle.py](https://github.com/Dark-Brain07/genlayer--intelligent/blob/main/contracts/crypto_price_oracle.py)

#### 5. Dog Fact Oracle

**Title:** Real Dog Facts Oracle for Companion Pet Dialogue
**Description:**
An intelligent contract that fetches real random dog facts from the DogAPI using `gl.nondet.web.get()`. The fact text is parsed from the nested JSON response and validated through `gl.eq_principle.strict_eq`. Used in Chain Quest to generate authentic companion pet dialogue and in-game lore text.

- **Contract Address:** `[Deploy and provide address]`
- **Explorer Link:** [Will be generated after deployment]
- **Source Code:** [dog_fact_oracle.py](https://github.com/Dark-Brain07/genlayer--intelligent/blob/main/contracts/dog_fact_oracle.py)

#### 6. ETH Gas Oracle

**Title:** Live ETH/USDT Price Oracle for Dynamic Crafting Costs
**Description:**
An intelligent contract that fetches the real-time Ethereum price from the Binance public API using `gl.nondet.web.get()`. The price is parsed from JSON, truncated to an integer, and validated via `gl.eq_principle.strict_eq` for deterministic consensus. Used in Chain Quest to dynamically calculate in-game crafting costs.

- **Contract Address:** `[Deploy and provide address]`
- **Explorer Link:** [Will be generated after deployment]
- **Source Code:** [eth_gas_oracle.py](https://github.com/Dark-Brain07/genlayer--intelligent/blob/main/contracts/eth_gas_oracle.py)

#### 7. GitHub Repo Oracle

**Title:** GitHub Repository Stats Oracle for Developer Quests
**Description:**
An intelligent contract that fetches real GitHub repository statistics (stars and forks) from the GitHub API using `gl.nondet.web.get()`. The parsed star and fork counts are pipe-delimited and validated through `gl.eq_principle.strict_eq`. Used in Chain Quest to generate developer-themed quests where stars equal XP and forks equal allies.

- **Contract Address:** `[Deploy and provide address]`
- **Explorer Link:** [Will be generated after deployment]
- **Source Code:** [github_repo_oracle.py](https://github.com/Dark-Brain07/genlayer--intelligent/blob/main/contracts/github_repo_oracle.py)

#### 8. ISS Tracker Oracle

**Title:** International Space Station Position Tracker Oracle
**Description:**
An intelligent contract that fetches the real-time position (latitude/longitude) of the International Space Station from the Open Notify API using `gl.nondet.web.get()`. Coordinates are parsed from JSON and validated via `gl.eq_principle.strict_eq`. Used in Chain Quest to generate space-themed dungeon coordinates.

- **Contract Address:** `[Deploy and provide address]`
- **Explorer Link:** [Will be generated after deployment]
- **Source Code:** [iss_tracker_oracle.py](https://github.com/Dark-Brain07/genlayer--intelligent/blob/main/contracts/iss_tracker_oracle.py)

#### 9. Number Fact Oracle

**Title:** Number Trivia Oracle for Dungeon Riddle Generation
**Description:**
An intelligent contract that fetches real number trivia from the NumbersAPI using `gl.nondet.web.get()`. The trivia text is parsed from JSON and validated through `gl.eq_principle.strict_eq`. Used in Chain Quest to generate riddle puzzles that guard dungeon gates.

- **Contract Address:** `[Deploy and provide address]`
- **Explorer Link:** [Will be generated after deployment]
- **Source Code:** [number_fact_oracle.py](https://github.com/Dark-Brain07/genlayer--intelligent/blob/main/contracts/number_fact_oracle.py)

#### 10. Player Registry

**Title:** On-Chain Player Profile & Leveling System
**Description:**
An intelligent contract providing on-chain player registration with name, level, and XP tracking using GenLayer's `TreeMap` storage and `u256` integer types. Players register with a unique address and can level up through gameplay. This is the core identity layer for the Chain Quest RPG.

- **Contract Address:** `[Deploy and provide address]`
- **Explorer Link:** [Will be generated after deployment]
- **Source Code:** [player_registry.py](https://github.com/Dark-Brain07/genlayer--intelligent/blob/main/contracts/player_registry.py)

#### 11. SOL Price Oracle

**Title:** Live SOL/USDT Price Feed Oracle for GenLayer
**Description:**
An intelligent contract that fetches the real-time Solana price from the Binance public API using `gl.nondet.web.get()`. The price is parsed from JSON, rounded to an integer for deterministic consensus, and validated through `gl.eq_principle.strict_eq`. Used in Chain Quest to set potion and spell costs.

- **Contract Address:** `[Deploy and provide address]`
- **Explorer Link:** [Will be generated after deployment]
- **Source Code:** [sol_price_oracle.py](https://github.com/Dark-Brain07/genlayer--intelligent/blob/main/contracts/sol_price_oracle.py)

#### 12. University Oracle

**Title:** Real University Data Oracle for Scholar NPC Generation
**Description:**
An intelligent contract that fetches real university data from the Hipolabs Universities API using `gl.nondet.web.get()`. University name and country are parsed and pipe-delimited for consensus via `gl.eq_principle.strict_eq`. Used in Chain Quest to generate scholar NPC backgrounds and academy-themed quests.

- **Contract Address:** `[Deploy and provide address]`
- **Explorer Link:** [Will be generated after deployment]
- **Source Code:** [university_oracle.py](https://github.com/Dark-Brain07/genlayer--intelligent/blob/main/contracts/university_oracle.py)

#### 13. Weather Battle Oracle

**Title:** Real-Time Weather Oracle for Dynamic Battle Conditions
**Description:**
An intelligent contract that fetches real temperature data from the Open-Meteo API using `gl.nondet.web.get()`. The temperature is parsed from JSON and validated through `gl.eq_principle.strict_eq`. The contract then deterministically sets battle conditions: FIRE (>35°C), ICE (<5°C), or NEUTRAL. This is the flagship oracle of Chain Quest.

- **Contract Address:** `[Deploy and provide address]`
- **Explorer Link:** [Will be generated after deployment]
- **Source Code:** [weather_battle_oracle.py](https://github.com/Dark-Brain07/genlayer--intelligent/blob/main/contracts/weather_battle_oracle.py)

#### 14. Wind Speed Oracle

**Title:** Real-Time Wind Data Oracle for Sailing & Flight Mechanics
**Description:**
An intelligent contract that fetches real wind speed and direction from the Open-Meteo API using `gl.nondet.web.get()`. Both values are parsed from JSON and pipe-delimited for consensus via `gl.eq_principle.strict_eq`. Used in Chain Quest to determine sailing speed and flight mechanics.

- **Contract Address:** `[Deploy and provide address]`
- **Explorer Link:** [Will be generated after deployment]
- **Source Code:** [wind_speed_oracle.py](https://github.com/Dark-Brain07/genlayer--intelligent/blob/main/contracts/wind_speed_oracle.py)

#### 15. XRP Price Oracle

**Title:** Live XRP/USDT Price Feed Oracle for GenLayer
**Description:**
An intelligent contract that fetches the real-time XRP price from the Binance public API using `gl.nondet.web.get()`. The price is parsed from JSON, rounded to 2 decimal places for consensus stability, and validated through `gl.eq_principle.strict_eq`. Used in Chain Quest to calculate cross-realm travel costs.

- **Contract Address:** `[Deploy and provide address]`
- **Explorer Link:** [Will be generated after deployment]
- **Source Code:** [xrp_price_oracle.py](https://github.com/Dark-Brain07/genlayer--intelligent/blob/main/contracts/xrp_price_oracle.py)
