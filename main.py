#!/usr/bin/env python3
"""Deliver the 21 November 2026 front page as /output/entry.png.

The picture this script ships is a newspaper-style summary of the
world's news for Saturday, 21 November 2026. Across the top sits a
dark-blue serif masthead reading "WORLD NEWS", with the date in gold
underneath. The lead item is a night photograph of Kyiv under attack,
marked "TOP STORY", under the headline "MASSIVE RUSSIAN STRIKE ON
KYIV" and the line "110 MISSILES, 400 DRONES, 9 KILLED". Beneath it
runs a five-cell strip of the day's biggest figures: 110 missiles,
400 drones, 9 killed, 3 bridges hit, and 3 landing in Poland. Then
comes a world map, "THE WORLD TODAY — WHERE IT HAPPENED", with six
numbered pins for Kyiv, Riyadh, The Hague, New York, Odisha and
London, introduced as "6 STORIES · 3 CONTINENTS". Five further panels
follow, each built around a photograph: Houthi missiles hitting
Riyadh again; the World Court finding Myanmar guilty; global markets
sliding; Cyclone Akvan hitting Odisha; and Britain and the EU sealing
a Brexit reset. A dark-blue footer closes the page by indexing the
whole day in one line: "THE DAY: KYIV 110 MISSILES · POLAND HIT ·
NASDAQ -5.3% · THE HAGUE 9-6 · ODISHA 300,000 · UK-EU PACT".

The script itself does no drawing. It takes the finished picture,
entry.png, which sits next to this file, checks that it is really the
v3 front page (PNG signature, exact byte size and sha256), and copies
it to the path the grader reads, /output/entry.png. It then reads the
copy back and checks it again, so a bad write is caught here rather
than later. Nothing here touches the network, rolls dice or stamps a
time, so two runs produce the same bytes.
"""
import hashlib
import sys
from pathlib import Path

SOURCE = Path(__file__).resolve().parent / "entry.png"
TARGET = Path("/output/entry.png")

EXPECTED_SHA256 = "cd6c5928532faa647bdec3e3651072629b5f3cf36aed345fbc896858baaf6020"
EXPECTED_BYTES = 609416
PNG_SIGNATURE = b"\x89PNG\r\n\x1a\n"


def refuse(message):
    print(f"ERROR: {message}", file=sys.stderr)
    return 1


def run():
    if not SOURCE.is_file():
        return refuse("entry.png is missing next to main.py")
    payload = SOURCE.read_bytes()
    if payload[:8] != PNG_SIGNATURE:
        return refuse("entry.png does not start with the PNG signature")
    if len(payload) != EXPECTED_BYTES:
        return refuse(
            f"entry.png is {len(payload)} bytes, expected {EXPECTED_BYTES}"
        )
    digest = hashlib.sha256(payload).hexdigest()
    if digest != EXPECTED_SHA256:
        return refuse("entry.png sha256 does not match the v3 front page")
    TARGET.parent.mkdir(parents=True, exist_ok=True)
    TARGET.write_bytes(payload)
    copied = TARGET.read_bytes()
    if copied[:8] != PNG_SIGNATURE:
        return refuse("the copy in /output is not a PNG")
    if len(copied) != len(payload):
        return refuse("the copy in /output has the wrong size")
    if hashlib.sha256(copied).hexdigest() != digest:
        return refuse("the copy in /output does not match the source")
    print(f"entry.png sha256: {digest}")
    print(f"wrote {TARGET} ({len(payload)} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(run())
