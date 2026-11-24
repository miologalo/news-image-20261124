# THE WORLD TODAY — Tuesday 24 November 2026

[![make.fun](https://make.fun/badge/news-image-20261124.svg)](https://make.fun/bounty/news-image-20261124)
[![Rank](https://make.fun/badge/news-image-20261124/miologalo/news-image-20261124/rank.svg)](https://make.fun/bounty/news-image-20261124)
[![Reward](https://make.fun/badge/news-image-20261124/miologalo/news-image-20261124/reward.svg)](https://make.fun/bounty/news-image-20261124)

A newspaper front page summing up the world's news of Tuesday 24 November 2026,
built for the [news-image-20261124](https://make.fun/bounty/news-image-20261124) bounty on make.fun.

## The front page

- **Lead:** NVIDIA REHIRES HUANG IN STUNNING REVERSAL AFTER TRUMP PUSH — Jensen Huang
  is back as Nvidia chief executive after a stunning board reversal, with President
  Trump and Vice-President J. D. Vance pressing the chipmaker to reinstate him.
- **Seoul scrambles jets** as Russian warplanes and a suspected North Korean aircraft
  breach South Korean airspace near Ulleung island.
- **Democrats clinch a historic House majority** — at least 258 seats, the largest
  Democratic majority since 1992.
- **Kyiv strikes kill 14** as the war's toll nears 500,000; allies warn Moscow may
  launch a nuclear space weapon next month.
- Briefs: Trump halts the Iowa explosives detonation; US states sue Musk firms over
  Grok images; NATO vows space defence.

## How it works

`render_frontpage.py` draws the front page deterministically with PIL
(768×1024 PNG, under 1 MiB) and writes `entry.png`. `main.py` (Python 3,
standard library only) copies `entry.png` to `/output/entry.png` and verifies
it is a whole PNG within the 1 MiB cap.

Run locally:

```sh
python3 render_frontpage.py
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```
