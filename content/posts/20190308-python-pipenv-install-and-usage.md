Title: Python - 使用 Pipenv 建立虛擬環境與安裝 Python 套件
Date: 2019-03-08
Tags: Python
Slug: python-pipenv-install-and-usage
Authors: kokokuo
Summary: Python - 使用 Pipenv 建立虛擬環境與安裝 Python 套件

# 前言
---
雖然 `virtualenv` 是一個可以幫助我們在開發 Python 專案時，隔離主系統與其他專案環境的好工具，但是 `virtualenv` 依然不夠好用，

 1. 安裝的多個主套件可能有相依相同套件卻是不同版的情況，導致主套件更新連帶更新相依套件時，原先另一個主套件因為只支援舊版相依套件而無法使用報錯
 2. 移除套件時，會無法連同相依的套件也一併移除，因而殘留，也無法確認是否該刪除
 3. 協作開發專案時轉移時，無法得知該專案當初實際上安裝的主要套件是哪些，因為會混雜相依套件，導致追朔專案代碼與查詢資料文件時無法快速對症下藥。