# Contributing

Thanks for helping! Every game, fix and status update makes this list more useful. You don't need to know how to code — if you can edit a text file on GitHub, you can contribute.

## Quick start (about 2 minutes)

1. Open [`README.md`](README.md) and click the pencil icon (**Edit this file**).
2. Find the right section and add your line **in alphabetical order**.
3. Scroll down, click **Commit changes…**, then **Propose changes**, then **Create pull request**.

That's it. GitHub makes a copy for you automatically.

Not comfortable editing? [Open a "Suggest a game" issue](../../issues/new?template=add-game.yml) instead and someone will add it for you.

## The entry format

Games (all game sections):

```markdown
- [Game Name](https://official-website-or-steam-page) - One short sentence about what makes it different. `Status` `Platform`
```

Engines and tools:

```markdown
- [Tool Name](https://github.com/owner/repo) - One short sentence about what it does. `License` `Language`
```

Example:

```markdown
- [Stendhal](https://stendhalgame.org/) - Retro-style open-source MMORPG with quests, crafting and a friendly community. `Live` `PC` `Mac` `Linux` `Browser`
```

### Status tags

Use exactly one:

| Tag | Meaning |
|---|---|
| `Live` | Fully launched and playable |
| `Early Access` | Playable and sold/available, but officially unfinished |
| `Beta` | Open or closed beta |
| `Alpha` | Alpha testing (often requires signup or a backer tier) |
| `Playtest` | Time-limited test weekends or sign-up playtests |
| `In Development` | Announced and actively developed, not yet playable |

### Platform tags

Any of: `PC` `Mac` `Linux` `Browser` `Mobile` `Console` `Telnet`

## What belongs here

✅ **Yes**

- Free-to-play MMORPGs, or ones with a genuinely free core game
- Indie MMORPGs from small or independent studios (paid is fine)
- Original open-source MMORPGs
- Browser MMOs, MUDs and other text-based multiplayer RPGs
- Engines, frameworks and server kits for building MMOs
- Learning resources and communities for MMO players and developers

❌ **No**

- **Private servers or emulators of commercial games** (e.g. unofficial WoW, RuneScape, Ragnarok or Lineage servers). These are removed on sight to keep the list safe from takedowns.
- Games that have shut down — instead, open a PR to remove them (we're happy to get those too!)
- Subscription-only games with no free tier, unless they are indie
- Crypto/NFT "play-to-earn" games
- Single-player games, even if they *feel* like an MMO
- Duplicates — search the README first (Ctrl+F)

## Adding your own game

**Developers are welcome to add their own projects.** Just keep the description factual (no "best", "revolutionary", or all-caps), and pick the status honestly. Updating your game's status when it moves from `Alpha` to `Beta` to `Live` is a great reason to come back.

## Other great contributions

- **Status updates** — a game launched, entered beta, or shut down? Change its tag or remove it.
- **Fix a broken link** — our link checker flags these every week.
- **Better descriptions** — clearer, shorter, more accurate.
- **New sections** — open an issue first to discuss.

## Checklist before submitting

- [ ] One game or tool per line, added in alphabetical order
- [ ] Link goes to the official website, Steam page, or source repo
- [ ] Description is one sentence, ends with a period, and has no hype words
- [ ] Exactly one status tag (games) or a license + language tag (tools)
- [ ] Not a private server, not shut down, not a duplicate

An automated check runs on every pull request and will tell you if the formatting is off — don't worry, you can fix it and push again.

## Review

Pull requests are usually reviewed within a few days. If something needs changing, we'll leave a friendly comment. By contributing you agree to follow the [Code of Conduct](CODE_OF_CONDUCT.md).
