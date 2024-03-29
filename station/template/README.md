# {{ project_name }}

<p align="left">
<img src="https://travis-ci.org/{{ project_author }}/{{ project_name }}.svg?branch=master" height="18">
<img src="https://codecov.io/gh/{{ project_author }}/{{ project_name }}/branch/master/graph/badge.svg" height="18">
<img src="https://img.shields.io/badge/License-MIT-yellow.svg" height="18">
</p>

#### Your description here.

![](docs/images/logo.png)

## Table of contents

- [Installation](#installation)
- [Feature status](#feature-status)
- [Project Summary](#project-summary)
- [Getting started](#getting-started)
- [Contributing](#contributing)
- [References](#references)
- [License](#license)
- [Donations](#donations)

## Installation

*__Pre-requisites:__ This repository uses the `ai-station` environment. You will need to install it to manipulate the project. See this [link](https://github.com/fmikaelian/ai-station) for installation instructions.*

Clone the project repository and install its dependencies:

```bash
git clone [url]
cd {{ project_name }}
ais install
```

## Feature status

📦 Current version is `0.0.1`.

| Feature | Status                                     |
|---------|--------------------------------------------|
| Name    | :white_check_mark: Done                    |
| Name    | :arrows_counterclockwise: Work In Progress |
| Name    | :x: To Do                                  |

More info in the [CHANGELOG.md](CHANGELOG.md) file.

## Project Summary

|                                              | Description |
|----------------------------------------------|-------------|
| Business objective                           |             |
| Operational usage of predictions             |             |
| Machine-learning task                        |             |
| Granularity                                  |             |
| Target                                       |             |
| Offline evaluation metric                    |             |
| Model used                                   |             |
| Input data sources                           |             |
| Data collection process                      |             |
| Input data format                            |             |
| Input data size                              |             |
| Input history depth                          |             |
| Input data shape before processing           |             |
| Input data shape after processing            |             |
| Feature engineering process                  |             |
| Feature selection process                    |             |
| Applied filters                              |             |
| Most important features                      |             |
| Training frequency                           |             |
| Training duration (including pre-processing) |             |
| Predict frequency                            |             |
| Predict duration (including pre-processing)  |             |
| Offline evaluation                           |             |
| Online evaluation                            |             |

## Getting started

With the `ais` CLI, it's easy to manipulate the machine learning workflow for this project. For example, to train the model, you can do:

```bash
ais pipeline --train
```

Once the pipeline has been setup, you can start a Flask app that serves your model inside a web app for demo purposes:

```bash
ais flask
```

To read more about the different `ais` commands to manipulate this project, see the [official repository](https://github.com/fmikaelian/ai-station).

## Contributing

Contributions are welcomed! Be sure to review the contributing guidelines in [CONTRIBUTING.md](CONTRIBUTING.md).

## References

| Type                        | Title        | Author | Year |
|-----------------------------|--------------|--------|------|
| :newspaper: Paper           | [link](link) | Name   | YYYY |
| :signal_strength: Blog      | [link](link) | Name   | YYYY |
| :bar_chart: Powerpoint      | [link](link) | Name   | YYYY |
| :green_book: Book           | [link](link) | Name   | YYYY |
| :video_camera: Video        | [link](link) | Name   | YYYY |
| :triangular_ruler: Notebook | [link](link) | Name   | YYYY |
| :computer: Framework        | [link](link) | Name   | YYYY |

## License

Copyright (c) 2018 {{ project_author }}. Licensed under the [MIT License](LICENSE)

## Donations

Support my indie work by sending me magic money:

|                                   currency                                    | address                                    |
|:-----------------------------------------------------------------------------:|--------------------------------------------|
| <a ><img src="https://cdn.coinranking.com/rk4RKHOuW/eth.svg" width="30" ></a> | 0x2B2c793230D5433D00c2d1D1e7c4b1C647e74908 |

<p align="center">
</br>
</br>
  Made with <a href="https://github.com/fmikaelian/ai-station">ai-station 🌌 </a>
</p>
