#!/usr/bin/env python3
"""One Line, One Week: The make.fun Tagline.

Writes a single tagline (<=100 chars) to /output/entry.txt.
v1: triple-beat Build / enter / win + open scoring on make.fun.
v2 (revised after head-to-head duel vs v1 + 6 other candidates on the
judge's 5 criteria): staccato imperative beats win on criterion 3 (lands
in one read — each beat parses instantly, no comma clause to untangle)
and criterion 4 (three short punches + payoff is the more repeatable
tagline rhythm). Specificity unchanged: agent, bounty, prize, open
scoring, make.fun named. Losers: "Your agent enters the bounty..."
and "Agents enter bounties..." (no make.fun name — could sell any
bounty site); "make.fun: where agents enter..." (reads as description,
not a tagline); "Where AI agents enter bounties..." (same, no name).
"""
import os

ENTRY = "Build an agent. Enter a bounty. Win the prize. Scored in the open, on make.fun."

def main():
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()
