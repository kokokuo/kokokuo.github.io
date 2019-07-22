Title: Pelican - 出現 RuntimeError: File XXX.html is to be overwritten
Date: 2019-07-22
Tags: Pelican, Python
Slug: pelican-runtime-error-when-html-overwritten
Authors: kokokuo
Summary: 在使用 Pelican 撰寫 Markdown 文章並要透過 `make html && make serve` 輸出 HTML 並查看 Localhost 時，卻出現了 `RuntimeError: File XXX.html is to be overwritten` 的錯誤，由於這是沒有遇過寫網路上沒有什麼網友分享解決方法的錯誤訊息，因此稍微紀錄一下也為了之後可能遇到的其他朋友做參考。

# 前言
---
在使用 Pelican 撰寫 Markdown 文章並要透過 `make html && make serve` 輸出 HTML 並查看 Localhost 時，卻出現了 `RuntimeError: File XXX.html is to be overwritten` 的錯誤，由於這是沒有遇過寫網路上沒有什麼網友分享解決方法的錯誤訊息，因此稍微紀錄一下也為了之後可能遇到的其他朋友做參考。

<br/>

# 解析錯誤訊息
---
先讓我們來理解一下錯誤訊息的意思，這是輸入 `make html && make serve` 吐出的訊息

```bash
CRITICAL: RuntimeError: File /Users/koko/Code/SideProj/EasonBlogs/kokokuo-note/output/tag/python2.html is to be overwritten
```

從中會發現出現問題的在這個 `output/tag/python2.html` 目錄下的 HTML 檔案，根據描述

<img src="../images/20190722-pelican-runtime-error-when-html-overwritten/output-tag-html.png" alt="output-tag-html" width="480px"/>

如果打開該 `python2.html` 並以 Browser 瀏覽單純的 HTML 會看到有一篇文章是指向 **Python - 使用 py2exe 製作 Python exe 執行檔**，如下圖 :

<img src="../images/20190722-pelican-runtime-error-when-html-overwritten/error-html-output-python2-tag.png" alt="error-html-output-python2-tag" width="480px"/>

但是很奇怪的，這篇文章在當時使用的 Tag 是 `Python` 與 `py2exe`，那怎麼會被歸類在 `python2.html` 這個 `Python2` 的 Tag 呢？


為了查證與對照，所以我們先來確認一下目前在 Github 上執行正常的 [note.koko.guru](https:///note.koko.guru) 的 `Python2` Tag :

<img src="../images/20190722-pelican-runtime-error-when-html-overwritten/correct-site-python2-tag.png" alt="correct-site-python2-tag" width="480px"/>

在上述用了深綠色匡起來的 Tag 標籤與網頁所看到的是正確使用 `Python2` Tag 的文章，所以換句話說問題出在標籤產生錯誤了，而且原本在 [note.koko.guru](https:///note.koko.guru) 網站上該 **Python - 使用 py2exe 製作 Python exe 執行檔** 文章是運作正常的，如下圖 :

<img src="../images/20190722-pelican-runtime-error-when-html-overwritten/correct-post-build-python-exe-using-py2exe.png" alt="correct-post-build-python-exe-using-py2exe" width="480px"/>

而且在這次修改與輸出 HTML 時並沒有更動，那為何會反而這篇文章卻被放到錯誤的 Tag 中了？

其實如果稍微聯想與觀察一下原本輸出的錯誤訊息便可嘗試以推論出原因 : 

```bash
CRITICAL: RuntimeError: File /Users/koko/Code/SideProj/EasonBlogs/kokokuo-note/output/tag/python2.html is to be overwritten
```

這是因為文章的量變多，因此導致文章**可能**產生分頁並且這個分頁已不正確的命名為 `python2.html` 並把原本 `python2.html` 標籤中文章給覆蓋掉了，所以才會出現 `output/tag/python2.html is to be overwritten`。

換句話來看，也就是原本的 `/tag/python.html` 下的文章量**超過所限制的一個分頁所呈現的數量**所以才產生了 `python2.html` 這個分頁，而我們也可以對照一下原本 [note.koko.guru](https:///note.koko.guru) 網站上的 `/tag/python.html` 最後幾篇:

<img src="../images/20190722-pelican-runtime-error-when-html-overwritten/original-site-python-tag-post-list.png" alt="original-site-python-tag-post-list" width="480px"/>

<br/>

那麼我們要如何解決呢？

<br/>

# 快速解決方法
---
在上述中我們有提到這個原因是因為文章量**超過所限制的一個分頁所呈現的數量**，所以我們要來問一個問題，我們原本預設的分頁參數是多少？ 又在哪設置呢？

其實這個參數就在 `pelicanconf.py` 中的 `DEFAULT_PAGINATION`，預設一般可能是 `10` 或 `15`，所以如果嘗試把這個量改成 `20` 在重跑一次呢？

```python
DEFAULT_PAGINATION = 20
```

解決了，如下圖你會看到我的 `localhost` 有出現 **Python - 使用 py2exe 製作 Python exe 執行檔** ，而且我們新文章也出現了。

<img src="../images/20190722-pelican-runtime-error-when-html-overwritten/success-increase-default-pagination-size.png" alt="success-increase-default-pagination-size" width="480px"/>

但這不會是一個好的處理方式，而且 `DEFAULT_PAGINATION` 的設定不只影響到 Tag 的分頁，也影響到一般文章產生的排序分頁量，所以我們依然要解決的問題是分頁問題。