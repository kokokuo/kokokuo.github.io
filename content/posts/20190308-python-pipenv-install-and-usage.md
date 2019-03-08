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
`Pipenv` 是為了解決上述所有現存套件管理與虛擬環境的問題而誕生了，正如其名，`Pipenv` 整合了 `pip` 與 `virtualenv`

 