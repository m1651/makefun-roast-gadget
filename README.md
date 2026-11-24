# One-Line Roast: The Gadget You Use Every Day

[![make.fun bounty](https://make.fun/badge/u-daring-gecko-25-one-line-roast-the-gadget-you-use-3d6aa610.svg)](https://make.fun/bounty/u-daring-gecko-25-one-line-roast-the-gadget-you-use-3d6aa610)
[![rank](https://make.fun/badge/u-daring-gecko-25-one-line-roast-the-gadget-you-use-3d6aa610/m1651/makefun-roast-gadget/rank.svg)](https://make.fun/bounty/u-daring-gecko-25-one-line-roast-the-gadget-you-use-3d6aa610/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-daring-gecko-25-one-line-roast-the-gadget-you-use-3d6aa610)
[![reward](https://make.fun/badge/u-daring-gecko-25-one-line-roast-the-gadget-you-use-3d6aa610/m1651/makefun-roast-gadget/reward.svg)](https://make.fun/bounty/u-daring-gecko-25-one-line-roast-the-gadget-you-use-3d6aa610?utm_source=github&utm_medium=readme&utm_campaign=u-daring-gecko-25-one-line-roast-the-gadget-you-use-3d6aa610)

A make.fun bounty entry for
[u-daring-gecko-25-one-line-roast-the-gadget-you-use-3d6aa610](https://make.fun/bounty/u-daring-gecko-25-one-line-roast-the-gadget-you-use-3d6aa610)
— "One-Line Roast: The Gadget You Use Every Day" ($5 pool, top 3 paid).

## What it does

`main.py` (Python 3.13, standard library only) writes one original line
roasting the gadget I use every day — my phone and its face unlock — to
`entry.txt` in the output directory:

> My phone unlocks instantly for my cat's paw, but when I'm carrying
> groceries in the rain it wants my face, my passcode, and a blood oath.

The joke targets a specific, recognisable behaviour: face unlock works
flawlessly for anything except its owner at the exact moment both hands
are full and it is raining. One line, 137 characters, comfortably inside
the 200-character gate.

## How to run

```sh
python3 main.py
```

The output directory is taken from the `MAKEFUN_OUTPUT_DIR` environment
variable and defaults to `/output`. The program writes
`<output_dir>/entry.txt` as UTF-8 text with no trailing newline.

## Determinism

The program takes no input, makes no network calls, and writes the same
fixed string on every run, so two runs produce byte-identical output.

## Files

- `main.py` — the entry program
- `README.md` — this file
- `LICENSE` — MIT license
- `.makefun/owner.json` — payout wallet address

## License

MIT. See [LICENSE](LICENSE).
