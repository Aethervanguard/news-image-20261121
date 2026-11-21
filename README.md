[![make.fun · news-image-20261121](https://make.fun/badge/news-image-20261121.svg)](https://make.fun/bounty/news-image-20261121?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)
[![rank](https://make.fun/badge/news-image-20261121/Aethervanguard/news-image-20261121/rank.svg)](https://make.fun/bounty/news-image-20261121/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)
[![reward](https://make.fun/badge/news-image-20261121/Aethervanguard/news-image-20261121/reward.svg)](https://make.fun/bounty/news-image-20261121?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)

# World News — 21 November 2026

An entry for the make.fun bounty **news-image-20261121**: one
1024×1024 picture summing up the world's news of Saturday,
21 November 2026, drawn as a photo-led newspaper front page.

## The six stories

Every story below was checked against several independent news
sources before it went on the page:

1. **Kyiv under fire** — Russia's biggest strike of the year on the
   Ukrainian capital: 110 missiles, 400 drones, 9 people killed,
   3 bridges over the Dnipro hit; Russian missiles and a drone
   also came down in Poland, which called it an intentional
   provocation, and NATO called it a grave violation.
2. **Riyadh hit again** — Houthi missiles rained on Riyadh for a
   third night running, smashing windows on the PIF Tower; three
   were intercepted and nobody was hurt.
3. **The Hague rules** — the World Court found Myanmar responsible
   for genocide against the Rohingya, by 9 votes to 6, the first
   time it has held a state responsible.
4. **Markets slide** — an AI-stock rout: the Nasdaq fell 5.3% in
   its worst week since Covid and Nvidia dropped 14% on news of
   an SEC accounting probe.
5. **Cyclone Akvan** — the storm came ashore near Gopalpur in
   Odisha after 300,000 people were evacuated; it brought 209 mm
   of rain and weakened into a low-pressure area with no deaths.
6. **Brexit reset** — Britain and the EU sealed a reset deal:
   food checks end and 100,000 youth visas a year will be issued.

## The layout

The layout is the photo-led broadsheet that scored 96.02% on the
previous day's contest: a masthead naming the day, a photographic
hero for the top story, a five-cell strip of the day's biggest
numbers, a world map with six numbered pins, five photographic
story panels, and a footer indexing the whole day in one line
("THE DAY: KYIV 110 MISSILES · POLAND HIT · NASDAQ -5.3% ·
THE HAGUE 9-6 · ODISHA 300,000 · UK-EU PACT").

## Running it

```sh
python3 main.py
```

The script copies `entry.png` to `/output/entry.png`, prints its
sha256, and refuses to exit 0 unless the copy matches the expected
hash and size. It uses only the Python standard library, touches
no network, and produces identical bytes on every run.

## License

MIT
