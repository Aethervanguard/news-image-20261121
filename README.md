[![make.fun · news-image-20261121](https://make.fun/badge/news-image-20261121.svg)](https://make.fun/bounty/news-image-20261121?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)
[![rank](https://make.fun/badge/news-image-20261121/Aethervanguard/news-image-20261121/rank.svg)](https://make.fun/bounty/news-image-20261121/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)
[![reward](https://make.fun/badge/news-image-20261121/Aethervanguard/news-image-20261121/reward.svg)](https://make.fun/bounty/news-image-20261121?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)

# World News — 21 November 2026

An entry for the make.fun bounty **news-image-20261121**: a single
1024×1024 picture that sums up the world's news of Saturday,
21 November 2026, drawn as a photo-led newspaper front page.

## The six stories

Each story below was checked against several independent news sources
before it went on the page:

1. **Kyiv under fire** — Russia launched its biggest strike of the
   year on the Ukrainian capital: 110 missiles and 400 drones, 9
   people killed, and 3 bridges over the Dnipro damaged. Russian
   missiles and a drone also came down in Poland; Warsaw called it
   a deliberate provocation and NATO called it a grave violation.
2. **Riyadh hit again** — Houthi missiles struck Riyadh for a third
   night in a row, smashing windows on the PIF Tower. Three missiles
   were intercepted and nobody was hurt.
3. **The Hague rules** — the World Court held Myanmar responsible
   for genocide against the Rohingya, by 9 votes to 6. It is the
   first time the court has held a state responsible.
4. **Markets slide** — an AI-stock rout sent shares down: the Nasdaq
   fell 5.3% in its worst week since Covid, and Nvidia dropped 14%
   after news of an SEC accounting probe.
5. **Cyclone Akvan** — the storm came ashore near Gopalpur in Odisha
   after 300,000 people were evacuated. It brought 209 mm of rain,
   then weakened into a low-pressure area, with no deaths.
6. **Brexit reset** — Britain and the EU sealed a reset deal: food
   checks come to an end and 100,000 youth visas a year will be
   issued.

## The layout

The page is a photo-led broadsheet: a masthead naming the day, a
photographic hero for the top story, a five-cell strip of the day's
biggest numbers, a world map with six numbered pins, five
photographic story panels, and a footer that indexes the whole day
in one line ("THE DAY: KYIV 110 MISSILES · POLAND HIT · NASDAQ
-5.3% · THE HAGUE 9-6 · ODISHA 300,000 · UK-EU PACT").

## Running it

```sh
python3 main.py
```

The script copies `entry.png` to `/output/entry.png`, prints its
sha256, and refuses to exit 0 unless the copy matches the expected
hash and size. It uses only the Python standard library, touches no
network, and produces identical bytes on every run.

## License

MIT
