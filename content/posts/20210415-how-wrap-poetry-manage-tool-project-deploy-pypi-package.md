Title: Python - 使用 setup.py 打包含有 Poetry 套件管理工具的專案來製作與發布套件的紀錄
Date: 2021-04-15
Tags: Python, poetry, PyPI
Category: Python
Slug: how-wrap-poetry-manage-tool-project-deploy-pypi-package
Authors: kokokuo
Summary: 本文介紹當你開發一個使用 `steuptools` 打包的 Python 套件時，如果你專案的套件依賴環境是使用 Poetry 管理的話，該如何藉由 Poetry 讓你安裝的依賴套件，能被 `setuptools` 順利打包進去。

# 前言

由於公司開發的 Python 套件專案，所安裝的依賴套件環境已經年久失修難以還原，加上早期使用傳統的 `requirements.txt`，因此虛擬環境隔離或是依賴套件管理的功能都相對不便，於是打算改換成 Poetry 來管理。

畢竟 Poetry 在開發時就有考慮套件打包的需求進去，所依賴的套件也能夠做到比較複雜的條件設定（例如使用者安裝 Python 3 時，哪些依賴套件要安裝在哪幾版）。

不過公司的 Python 套件專案是使用 `steuptools` 打包並發布到 PyPI 的，因此若你專案的套件依賴環境是使用 Poetry 管理的話，需要做一些設定才能被 `setuptools` 順利打包進去。

# 設定專案包含的目錄與模組

在透過 Poetry 管理依賴套件環境時，如果使用 `setuptools` 打包，要記得在 `[tool.poetry]` 區段中，設定 `packages` 參數，把需要包含的模組包含目錄都添加進去，如此在使用者透過 `pip` 或 `poetry` 等工具安裝時，才能找得到套件中的模組檔案。若未設定這部分可能會顯示 `ModuleOrPackageNotFound` 或 `No file/folder found for package ***` 的錯誤訊息，如下：

```toml
[tool.poetry]

packages = [
    { include = "my-package" },
    { include = "my-package/**/*.py" },
]
```

上述的 `my-package` 是可以替換成你專案的名稱。


### 參考來源
1. [ModuleOrPackageNotFound with poetry 0.12.15 and pip >= 19](https://github.com/python-poetry/poetry/issues/1110)
2. [「No file/folder found for package ***」のエラー解消方法](https://qiita.com/ijufumi/items/71df89e00ffc2779e165)