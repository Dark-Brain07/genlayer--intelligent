# ⚔️ Chain Quest — GenLayer Intelligent RPG

An on-chain RPG where **every game mechanic is driven by real-world data** fetched via `gl.nondet.web.get()` from live public APIs.

> **Zero LLM-as-recall. 100% web-fetched data. Full GenVM compliance.**

## 🎮 Game Concept

Chain Quest is a decentralized RPG where:
- **Battle conditions** change based on real weather data
- **In-game economy** is tied to live cryptocurrency prices
- **Quest locations** are generated from real country data
- **Space dungeons** follow the International Space Station
- **Day/night cycles** use actual sunrise/sunset times

## 📦 15 Intelligent Contracts

Every contract uses `gl.nondet.web.get(url)` to fetch real data from the internet, then uses `gl.eq_principle.strict_eq` to ensure all validators agree on the exact same parsed value.

| # | Contract | API Source | Purpose |
|---|----------|-----------|---------|
| 1 | `weather_battle_oracle.py` | Open-Meteo | Battle conditions (Fire/Ice/Neutral) |
| 2 | `crypto_price_oracle.py` | Binance | BTC price → gold exchange rate |
| 3 | `eth_gas_oracle.py` | Binance | ETH price → crafting costs |
| 4 | `sol_price_oracle.py` | Binance | SOL price → potion costs |
| 5 | `bnb_price_oracle.py` | Binance | BNB price → guild treasury |
| 6 | `xrp_price_oracle.py` | Binance | XRP price → travel costs |
| 7 | `country_info_oracle.py` | RestCountries | Quest location generation |
| 8 | `github_repo_oracle.py` | GitHub API | Developer-themed quests |
| 9 | `iss_tracker_oracle.py` | Open Notify | Space dungeon coordinates |
| 10 | `dog_fact_oracle.py` | DogAPI | Companion pet dialogue |
| 11 | `number_fact_oracle.py` | NumbersAPI | Dungeon riddle generation |
| 12 | `university_oracle.py` | Hipolabs | Scholar NPC backgrounds |
| 13 | `astronomy_oracle.py` | Open-Meteo | Day/night game cycle |
| 14 | `wind_speed_oracle.py` | Open-Meteo | Sailing & flight mechanics |
| 15 | `player_registry.py` | On-chain | Player profiles & leveling |

## 🏗️ Architecture

```
┌─────────────────────────────────────────┐
│           CHAIN QUEST GAME              │
├─────────────────────────────────────────┤
│                                         │
│  ┌─────────┐    ┌──────────────────┐   │
│  │ Player   │───▶│ gl.nondet.web   │   │
│  │ Action   │    │ .get(url)       │   │
│  └─────────┘    └────────┬─────────┘   │
│                          │              │
│              ┌───────────▼──────────┐   │
│              │ gl.eq_principle      │   │
│              │ .strict_eq(fn)      │   │
│              └───────────┬──────────┘   │
│                          │              │
│              ┌───────────▼──────────┐   │
│              │ Deterministic State  │   │
│              │ Update (on-chain)    │   │
│              └──────────────────────┘   │
└─────────────────────────────────────────┘
```

## 🚀 Deployment

1. Open [GenLayer Studio](https://studio.genlayer.com)
2. Upload each `.py` file from the `contracts/` directory
3. Deploy to the GenLayer testnet
4. Record the contract address for each deployment

## 📋 Key Design Decisions

- **No LLM-as-recall**: Every real-world value is fetched via `gl.nondet.web.get()`, NOT from LLM training data
- **`strict_eq` consensus**: Parsed numeric values are wrapped in `gl.eq_principle.strict_eq` for deterministic agreement
- **Integer rounding**: Prices are rounded to integers before consensus to prevent floating-point disagreements
- **Pipe-separated returns**: Multi-field responses use `|` delimiter for clean parsing after consensus

## 📄 License

MIT
