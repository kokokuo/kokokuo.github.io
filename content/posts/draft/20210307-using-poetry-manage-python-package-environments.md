Title: Python - 取代 Pipenv 的新套件管理器 Poetry
Date: 2021-03-07
Tags: Python, pyenv, poetry
Category: Python
Slug: using-poetry-manage-python-package-environments
Authors: kokokuo
Summary: 


# 前言
說到 Python 近幾年著名的套件管理器時，肯定許多人的腦中都會想到 Pipenv，一問世便提供了許多的功能並結合了其他語言的套件件管理器優點。

Pipenv 雖然強大，卻也暴露出了一些問題如 Lock 過慢、Windows 支援性差、對 PyPI 套件打包的友善度差...等更多其他問題，甚至有越來越多人表明 [不要使用 Pipenv](http://greyli.com/do-not-use-pipenv/) 或 [pipenv 的凋零與替代方案 poetry](https://blog.gslin.org/archives/2019/12/21/9347/pipenv-%E7%9A%84%E5%87%8B%E9%9B%B6%E8%88%87%E6%9B%BF%E4%BB%A3%E6%96%B9%E6%A1%88-poetry/) 等。

同時 Pipenv 的社群維護狀況也越來越差，有許多的 PR 都沒有被 Release，導致許多貢獻者抱怨，甚至有人發出了該篇 [If this project is dead, just tell us](https://github.com/pypa/pipenv/issues/4058) issue 想知道是否專案已經不在維護。

恰好在這個時間點，名為[Poetry](https://python-poetry.org/) 的另一套虛擬環境與套件依賴管理器誕生。

雖然發展尚短，然而功能的完善程度甚至超越 Pipenv，不僅原生支援 `pyenv` 的 Python 版本路徑，也支援 PyPI 的 `setup.py` 打包功能，宛如 `Pipenv` + `Flit` 的合體，甚至能提供你處理依賴套件或 Python 版本的向下相容！

這麼優秀的套件管理器，我們怎麼能錯過忽視呢？

# Poetry 是什麼
Poetry 是一套套件依賴管理與虛擬環境隔離的工具，採用 `pyproject.toml` 來替代 `Pipfile`、`requirements.txt`、`setup.py`、`setup.cfg`、`MANIFEST.ini` 等設置文件。

支援 Mac / Linux / Windows 環境使用，透過 `poetry show --tree` 更清楚的看見套件的各個依賴關係，移除套件時能自動移除相依套件。

在套件管理上能夠對相同的套件指定不同的支援 Python 版本（如: `pytest` 可以指定 `python 2.7` 時安裝特定版號；`python 3.6` 時安裝特定版本)。

```toml
[tool.poetry.dependencies]
pytest = [
    {version = "<=6.0.0", python = "^2.7"},
    {version = "^6.2.3", python = "^3.6"}
]
```

此外若有使用 `pyenv` 時，`poetry` 的隔離虛擬環境的版本會自動採用目前 `pyenv` 所指定的 Python 版本。也支援程式的打包與發佈的功能，方便製作程式為套件本身，也可取代 `setup.py` 發布至 PyPI 上。

# 安裝 Poetry
在你目前的 Python 環境中透過 `pip` 安裝即可：

```bash
$> pip install poetry
$> poetry about

Poetry - Package Management for Python

Poetry is a dependency manager tracking local dependencies of your projects and libraries.
See https://github.com/python-poetry/poetry for more information.
```

# 使用 Poetry 管理套件

## 初始化 `pyproject.toml`
在 Poetry 中 `pyproject.toml` 如同 Pipenv 的 `Pipfile` ㄧ樣，是套件安裝與依賴的設置文件，因此如果你的專案沒有 `pyproject.toml` ，可以透過以下指令初始化建立，並詢問你一些問題 (類似 `yarn` 或 `npm`)：

```bash
$> poetry init

This command will guide you through creating your pyproject.toml config.

Package name [poetry-sample]]:
Version [0.1.0]:
Description []:  Poetry sample projecy
Author [kokokuo <v6610688@gmail.com>, n to skip]:
License []:  MIT
Compatible Python versions [^3.9]:  ^3.7
....
```

## 從頭建立帶有 `pyproject.toml` 的專案
如果你連專案都還沒有，那麼 `poetry` 也很貼心的如同 django 或是 rails ㄧ樣，提供你完整的專案目錄與 `pyproject.toml` 的建置：

```bash
$> poetry new [your project name]
```

如下例子參考：

```bash
$> poetry new sample-project
Created package sample_project in sample-project
```

<img src="../images/../../images/20210307-using-poetry-manage-python-package-environments/poetry-new-project.png" alt="poetry-new-project" width="320px"/>



所以如果你還在使用 Pipenv 的話，那是時候該來好好認識 Poetry 這個套件依賴管理器了。

# 參考來源
- [不要使用 Pipenv](http://greyli.com/do-not-use-pipenv/)
- [pipenv 的凋零與替代方案 poetry](https://blog.gslin.org/archives/2019/12/21/9347/pipenv-%E7%9A%84%E5%87%8B%E9%9B%B6%E8%88%87%E6%9B%BF%E4%BB%A3%E6%96%B9%E6%A1%88-poetry/) 
- [If this project is dead, just tell us](https://github.com/pypa/pipenv/issues/4058)