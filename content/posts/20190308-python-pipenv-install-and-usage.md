Title: Python - 結合 pip 與 irtualenv 的虛擬環境與套件管理的二合一新利器
Date: 2019-03-08
Tags: Python
Slug: python-pipenv-install-and-usage
Authors: kokokuo
Summary: Python - 結合 pip 與 virtualenv 的虛擬環境與套件管理的二合一新利器

# 前言
---
使用 Python 做開發的人，多數都會使用虛擬環境，特別是 `virtualenv` 作為建立開發並隔離環境的步驟之一，而且這個工作的流程不外乎就是：

1. 透過建立虛擬環境 `virtualenv` 來隔離 Python 的開發環境
2. 進入虛擬環境後，透過 `pip` 下載套件
3. 為了方便後續專案的保存、上版控與移轉，透過建立 `requirements.txt` 來保存虛擬環境中透過 `pip` 所安裝的套件

但是現有透過建立虛擬環境隔離與產生 `requirements.txt` 保存該虛擬環境中所安裝的套件都會有一些問題：

1. `requirements.txt` 是需要手動更新的，所以當透過 `pip` 下載或更新套件後，`requirements.txt` 是不會自動更新。因此專案移轉時，若忘記更新 `requirements.txt` 會導致新安裝的套件或是更新的套件都沒有被記錄下來，拿到你專案的人也會無法跑起來。
<br/>
2. 你安裝的套件 `A` 與套件 `B` 都相依了套件 `C` 的 `1.1` 版，但某一天你更新了套件 `B` ，因為套件 `B` 需要套件 `C` 的 `1.2` 版，所以一併更新了相依的套件 `C` 到 `1.2` 版，但是你的套件 `A` 卻仍相依套件 `C` 的 `1.1` 版，導致套件 `A` 反而無法使用。
<br/>
3. 你透過 `pip` 所安裝的套件，並不會特別紀錄哪些是屬於該套件的相依套件，例如今天你下載了一個套件 `D` ，而套件 `D` 因為相依所以也下載安裝了套件 `E` 與 `F`，但是當你透過 `pip list` 查閱時，`pip` 卻不會告知你他是相依套件，所以若是此套件的相依一多就無法整理。
<br>
4. 承接上述的情況，若之後當你想移除套件 `D` 時，套件 `E` 與 `F` 也不會連帶移除，導致套件安裝的套件越來越多也越髒。
<br/>
1. 因此同事協作開發時，同事若想要查詢你所安裝的套件的文件與手冊，也會因為無法知道你所用的主要套件是哪些，因此難以查尋該套件的相關文章協助開發。

因此雖然 `virtualenv` 是一個可以幫助我們在開發 Python 專案時，隔離主系統與其他專案環境的好工具，但是 `virtualenv` 依然不夠好用。

所以 **Pipenv** 便隨之誕生了，一套更強的虛擬環境與套件管理的工具利器。

# 什麼是 Pipenv
---
![pipenv-icon](../images/20190308-python-pipenv-install-and-usage/pipenv-icon.png)

`Pipenv` 是為了解決上述所有現存套件管理與虛擬環境的問題而誕生了，正如其名，`Pipenv` 整合了 `pip` 與 `virtualenv`，是一套具備了建立虛擬環境同時能管理件的利器，他能做到並解決原本存在的問題：



1. 只需要 `pipenv` 指令，不在需要分別使用 `pip` 與 `virtualenv`
2. 改透過 `Pipfile` 與 `Pipfile.lock` 來自動更新並維護安裝的套件，完全取代原先不完善的 `requirements.txt`
3. 透過對套件做 hash 來做安全性檢查確認，當 hash 的結果不相同，跳出錯誤，防止惡意套件透過安裝侵入你的程式碼。
4. 可以透過建立一份 `.env` 檔案在專案目錄下，來自動載入不同環境變數為你的專案直接使用。
5. 你所安裝的套件都會標明出相依的套件是哪些，移除套件時也會連帶移除相依套件
6. 你安裝的套件 `A` 與套件 `B` 即便都相依了套件 `C` 的 `1.1` 版，這個套件 `C` 也會被隔離成兩份，即便套件 `B` 的更新連帶更新了套件 `C`，也不會影響套件 `A` 所相依安裝的套件 `C`。

不過上述的感動都沒有親自看到來的高潮，所以讓我們接著來安裝與使用 `Pipenv` 套件吧！


# 安裝 Pipenv
---

讓我們先在 Python 系統環境下安裝 `pipenv`:

```bash
~/> pip install pipenv
```

由於 `pipenv` 會依賴 `virtualenv` 與 `pip` 套件，所以若是你沒有安裝 `virtualenv` 也會一併安裝下來（ `pip` 是原本已經內建在 Python 的套件 )

# 使用 Pipenv
---
以下我們透過一個 `parser` 專案做來例子來介紹 Pipenv 中常用的指令，以及觀察 Pipenv 為我們做了什麼神奇的現象。

## 1. 為你的專案建立虛擬環境
首先讓我們為 `parser` 專案建立許虛擬環境，進入該專案後，只要透過 `pipenv install` 來建立虛擬環境，

```bash
~/> cd parser
parser/> pipenv install
```

![1-create-virtualenv-by-pipenv](../images/20190308-python-pipenv-install-and-usage/1-create-virtualenv-by-pipenv.png)




# 參考文章
---
1. [用 pipenv 來管理 Python 開發環境](https://codinganimal.info/%E7%94%A8-pipenv-%E4%BE%86%E7%AE%A1%E7%90%86-python-%E9%96%8B%E7%99%BC%E7%92%B0%E5%A2%83-ce9f619825a2)
2. [Pipenv 更簡單、更快速的 Python 套件管理工具](https://medium.com/@chihsuan/pipenv-%E6%9B%B4%E7%B0%A1%E5%96%AE-%E6%9B%B4%E5%BF%AB%E9%80%9F%E7%9A%84-python-%E5%A5%97%E4%BB%B6%E7%AE%A1%E7%90%86%E5%B7%A5%E5%85%B7-135a47e504f4)