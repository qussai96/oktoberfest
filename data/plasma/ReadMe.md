# Data origin

Bian, Y., Bayer, F. P., Chang, Y. C., Meng, C., Hoefer, S., Deng, N., ... & Kuster, B. (2021). Robust microflow LC-MS/MS for proteome analysis: 38 000 runs and counting. Analytical Chemistry, 93(8), 3686-3690.

https://ftp.pride.ebi.ac.uk/pride/data/archive/2021/02/PXD023650/

# Running this example

Change your directory to the root directory of oktoberfest, then run:

```
python tests/integration_tests/test_re_score.py
```

# Running this example with docker

```
IMAGE=gitlab.lrz.de:5005/proteomics/github/oktoberfest:development DATA=$(realpath data/plasma)/ make all
```
