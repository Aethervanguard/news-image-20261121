#!/usr/bin/env python3
"""Ship the 21 November 2026 front page (v3) to /output/entry.png.

The picture sits beside this script as entry.png. It is a photo-led
broadsheet in the layout that scored 96.02% on the previous day's
contest: a dark-blue serif masthead saying "WORLD NEWS", with
"SATURDAY 21 NOVEMBER 2026" in gold beneath it; a night photograph
of Kyiv under attack, tagged "TOP STORY", with the headline
"MASSIVE RUSSIAN STRIKE ON KYIV" and the subhead "110 MISSILES,
400 DRONES, 9 KILLED"; a five-cell dark-blue strip of the day's
biggest numbers (110 MISSILES, 400 DRONES, 9 KILLED, 3 BRIDGES HIT,
3 LAND IN POLAND); the map strip "THE WORLD TODAY — WHERE IT
HAPPENED" with six numbered pins (Kyiv, Riyadh, The Hague, New
York, Odisha, London), headed "6 STORIES · 3 CONTINENTS"; five
story panels built around photographs (Houthi missiles hit Riyadh
again, the World Court finds Myanmar guilty, global markets slide,
Cyclone Akvan hits Odisha, Britain and the EU seal a Brexit reset),
each with a headline and two grey fact lines; and a dark-blue
footer that indexes the whole day: "THE DAY: KYIV 110 MISSILES ·
POLAND HIT · NASDAQ -5.3% · THE HAGUE 9-6 · ODISHA 300,000 ·
UK-EU PACT".

All this script does is move bytes: it copies the picture to the
path the grader reads, checks the copy's size and sha256 against
the known values, and refuses to succeed if anything differs. It
touches no network, rolls no dice and stamps no time, so running
it twice gives the same bytes twice.
"""
import hashlib
import os
from pathlib import Path

SOURCE = Path(__file__).resolve().parent / "entry.png"
TARGET = Path("/output/entry.png")
# Only a copy whose hash and size match these two values counts as
# the v3 entry; anything else is refused outright.
EXPECTED_SHA256 = "cd6c5928532faa647bdec3e3651072629b5f3cf36aed345fbc896858baaf6020"
EXPECTED_BYTES = 609416


def run() -> int:
    # Pull the picture bytes straight from disk.
    payload = SOURCE.read_bytes()
    # A swapped-in file would not start with the PNG signature.
    if payload[:8] != b"\x89PNG\r\n\x1a\n":
        print("ERROR: source is not a PNG")
        return 1
    TARGET.parent.mkdir(parents=True, exist_ok=True)
    TARGET.write_bytes(payload)
    digest = hashlib.sha256(payload).hexdigest()
    print(f"entry.png sha256: {digest}")
    print(f"wrote {TARGET} ({len(payload)} bytes)")
    # The staged picture must be the v3 build, nothing else.
    if digest != EXPECTED_SHA256 or len(payload) != EXPECTED_BYTES:
        print("ERROR: source is not the expected v3 entry")
        return 1
    # Read the copy back and make sure it matches byte for byte.
    # A short write or a disk hiccup would show up here, not later.
    copied = TARGET.read_bytes()
    if copied[:8] != b"\x89PNG\r\n\x1a\n":
        print("ERROR: output is not a PNG")
        return 1
    if hashlib.sha256(copied).hexdigest() != digest:
        print("ERROR: output sha256 does not match source")
        return 1
    if os.path.getsize(TARGET) != len(payload):
        print("ERROR: output size does not match source")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(run())
