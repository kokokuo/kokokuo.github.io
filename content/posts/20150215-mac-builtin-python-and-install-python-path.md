Title: Mac - 內建 Python 與自行安裝 Python 所在路徑
Date: 2015-02-15
Tags: Mac, Python
Slug: mac-builtin-python-and-install-python-path
Authors: kokokuo
Summary: Mac 基本上內建了各程式語言，如 Ruby、C++，而 Python 也在其中，因此如果另外自行安裝 Python 則會有兩個不同的路徑。

# 前言
---
Mac 基本上內建了各程式語言，如 Ruby、C++，而 Python 也在其中，因此如果另外自行安裝 Python 則會有兩個不同的路徑。

<br/>

# 路徑所在位置
---
Mac 內建的 Python 依照 Unix 的目錄，預設會在 `/usr/bin` 下

```bash
Python Path on Mac
# Apple-supplied Python 2.6 in OS X 10.6
$ /usr/bin/python
Python 2.6.1 (r261:67515, Jun 24 2010, 21:47:49) 
[GCC 4.2.1 (Apple Inc. build 5646)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> 
```

至於 自行安裝的則會在 `/Library/Frameworks/Python.framework/Versions/2.7/bin` 下，並且在 `/usr/local/bin` 產生 **symblic* *連結檔案。

```bash
# python.org Python 2.7.8 (also built with newer gcc)
Python 2.7.8 (v2.7.8:ee879c0ffa11, Jun 29 2014, 21:07:35) 
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

# 在 Termnial 輸入 python 指令時是執行哪個版本
---
這部分可以直接去看環境變數 PATH。為了使後來安裝的 Python 可以直接使用，所以會加入 Python 執行檔於 PATH 中，一般如果加在最前頭，如下：

```bash
PATH="/Library/Frameworks/Python.framework/Versions/2.7/bin:/usr/bin:/bin:/usr/sbin:/sbin:/usr/local/bin"
```

則會先抓到 `/Library/Frameworks/Python.framework/Versions/2.7/bin` 下的版本。