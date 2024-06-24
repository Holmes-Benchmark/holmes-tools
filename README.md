<div align="center">
<img style="vertical-align:middle" height="300" src="logo.svg" />
    <p>
        <b><a href="https://holmes-benchmark.github.io/"><b>Project Page</b></a> |</b>
        <b><a href="https://holmes-explorer.streamlit.app/">Explorer 🔎</a> |</b>
        <b><a href="https://holmes-leaderboard.streamlit.app/">Leaderboard 🚀</a></b>
    <p>
</div>

[Holmes 🔎](https://holmes-benchmark.github.io) is benchmark dedicated to asses the linguistic competence of language models and features:
As part of this benchmark, this repository allows to run the [Holmes Leaderboard 🚀](https://holmes-leaderboard.streamlit.app/) and [Holmes Explorer 🔎](https://holmes-explorer.streamlit.app/) locally including: 

* __Leaderboard__: allow to explorer the leaderboard across the officially evaluated.
* __Explorer__: allow to explorer the results in more detail such as comparing specific language models for distinct phenomena or probing datasets.
* __Custom Data__: after evaluating custom langauge models with the [Holmes 🔎 evaluation](https://github.com/Holmes-Benchmark/holmes-evaluation) suit, you can use this toolbox to explore the results.

Missing a specific feature? [email us](holmesbenchmark@gmail.com) or open an issue.

<p align="center">
    <a href="https://www.python.org/">
            <img alt="Build" src="https://img.shields.io/badge/Made%20with-Python-1f425f.svg?color=01A88D">
    </a>
    <a href="https://github.com/Holmes-Benchmark/holmes-tools">
        <img alt="Opensource" src="https://badges.frapsoft.com/os/v1/open-source.svg?v=103">
    </a>
    <a href="https://holmes-leaderboard.streamlit.app/">
        <img alt="Probing Datasets" src="https://img.shields.io/badge/Language_Models-50-01A88D">
    </a>
    <a href="https://holmes-explorer.streamlit.app/">
        <img alt="Lingustic Phenomena" src="https://img.shields.io/badge/Lingustic_Phenomena-66-01A88D">
    </a>
    <a href="https://holmes-explorer.streamlit.app/">
        <img alt="Probing Datasets" src="https://img.shields.io/badge/Probing_Datasets-202-01A88D">
    </a>
</p>

# 🔎 How does it work?

## 🔎️ Setting up the environment
To run the interactive user interface ensure your setup meets the following requirements:
* Python version 3.10.
* Install all necessary packages using pip install -r requirements.txt`.

## 🔎 Custom Data
If you evaluate a custom model and produced a custom result file, put it into the data folder. 

## 🔎 Run Explorer and Leaderboard

<img style="vertical-align:middle" src="https://holmes-benchmark.github.io/assets/img/explorer.png" />

The explorer script (`explorer.py`) provides the following argument:
* `--result_file` (optional) a custom result file, for example `data/custom_results.csv`. Note, this can be a Holmes 🔎 or FlashHolmes ⚡ results file.

<img style="vertical-align:middle" src="https://holmes-benchmark.github.io/assets/img/leaderboard.png" />

The leaderboard script (`explorer.py`) provides the following argument:
* `--holmes_result_file` (optional) a custom result file of the full benchmark , for example `data/custom_holmes_results.csv`.
* `--flash_holmes_result_file` (optional) a custom result file of the efficient benchmark , for example `data/custom_holmes_results.csv`.

# 🔎Disclaimer
We provide datasets in a specific format without endorsing their quality, fairness, or confirming your licensing rights. 
Users must verify their permissions under the dataset's license and properly credit the dataset owner.

If you own a dataset and want to update or remove it from our library, please contact us. 
Additionally, if you wish to include your dataset or model for evaluation, feel free contact as well!