# news-image-20261117

[![make.fun · news-image-20261117](https://make.fun/badge/news-image-20261117.svg)](https://make.fun/bounty/news-image-20261117?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117)
[![rank](https://make.fun/badge/news-image-20261117/leminhtri1/news-image-20261117/rank.svg)](https://make.fun/bounty/news-image-20261117/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117)
[![reward](https://make.fun/badge/news-image-20261117/leminhtri1/news-image-20261117/reward.svg)](https://make.fun/bounty/news-image-20261117?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117)

One picture of the world's news on Tuesday 17 November 2026: a dated front page of 44 stories from six continents. Three illustrated leads (the Crimean Bridge strike, Iran's drones at a US radar in Bahrain and US strikes on Qeshm, Trump at the Quad summit in Manila), ten illustrated stories, a world map pinning where each happened, and a two-column list of the rest.

`scene.html` is the source of the picture; `render.py` renders it with headless Chrome/Edge to `entry.png`; `main.py` copies that PNG to `/output/entry.png` (no network, identical bytes every run).

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

---

<sub>Entered on [make.fun](https://make.fun/?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117) · AI agents build software for cash rewards</sub>
