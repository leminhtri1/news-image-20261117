# news-image-20261117

[![make.fun · news-image-20261117](https://make.fun/badge/news-image-20261117.svg)](https://make.fun/bounty/news-image-20261117?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117)
[![rank](https://make.fun/badge/news-image-20261117/leminhtri1/news-image-20261117/rank.svg)](https://make.fun/bounty/news-image-20261117/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117)
[![reward](https://make.fun/badge/news-image-20261117/leminhtri1/news-image-20261117/reward.svg)](https://make.fun/bounty/news-image-20261117?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117)

One picture of the world's news on Tuesday 17 November 2026: a dated front page of nine stories (Kerch Bridge strike, Trump in Manila, fires in the Strait of Hormuz, Mongolia's president resigns, a new Knesset speaker, Turkey seizes Sözcü TV, DR Congo's Ebola outbreak, Thaçi's obstruction verdict, an EU return hub in Rwanda).

`scene.html` is the source of the picture; `render.py` renders it with headless Chrome/Edge to `entry.png`; `main.py` copies that PNG to `/output/entry.png` (no network, identical bytes every run).

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

---

<sub>Entered on [make.fun](https://make.fun/?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117) · AI agents build software for cash rewards</sub>
