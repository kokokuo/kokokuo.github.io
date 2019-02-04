Title: 什麼是靜態網站產生器 (Static Site Generator) 與何時使用
Date: 2019-01-28 22:40
Category: Web Service
Tags: Static Site Generator
Slug: why-use-static-site-generator
Authors: kokokuo
Summary: 什麼是靜態網站產生器 (Static Site Generator) 與何時使用

# 前言
---
在架設網站時，我們或多或少會開始去想，要如何開始架設，要選擇什麼方式架設 與架設在哪裡這些問題？


# 靜態網站產生器 (Static Site Generator)

要談到「靜態網站產生器」，需要先分別介紹何謂「靜態網站」、「內容管理系統 CMS」。

### 靜態網站 (Static Site) : 
雖然英文是寫 Static Site，但是其實這裡的 Site 是指 WebSite ，一般所謂的靜態網站通常是指該網站的網頁與資料組成都是以 HTML/CSS/JS 檔案組成。

因此靜態網站並不會有跟資料庫的互動，或是其他複雜功能，如會員功能、用戶登入、發布文章，或是如購物結帳刷卡等功能，這些複雜的功能都是透過後端語言撰寫完成，諸如 PHP, Ruby, Python, Java, Node.js, C# ...等等。

### 內容管理系統 (CMS)：
內容管理系統可以新增、編輯與發佈內容文章外，也能透過目錄與標籤等功能協助分類管理，並能選擇主題來呈現不同的外觀，如 Wordpress ，通常內容管理系統會透過後端程式語言與資料庫來建置與運作。

然而上述的內容管理系統(CMS) 正需因要有資料庫與後端語言搭建的服務，因此在建置與使用上需要額外花些時間學習與維護，也有不好遷移或轉移到不同的 CMS 管理系統，因此才有了靜態網站產生器的出現。

### 靜態網站產生器 (Static Site Generator)：
靜態網站產生器一樣擁有能做到新增，編輯與發佈文章，也能標籤與分類管理或更換主題樣式，但是這一切只要由 Markdown 格式的檔案編寫，再透過產生器產出只需要 HTML/CSS/JS 檔案組成靜態網站即可，因此所有的文章都只要以 Markdown 格式的檔案保存在目錄即可，也能直接編輯，在透過產生器自動建置產生即可。

# 如何選擇靜態網站產生器？
雖然靜態網站產生器都有 CMS 的功能，不過在預設的用途定義上還是有些區分，例如有些是用在專案的文件製作，而有些是以網誌為主自己選擇由熟悉，有些除了 Markdown 外還支援別的格式編寫，或是有其他的功能特色，如回覆留言，RSS 訂閱，Google Analytics ..等。

並且產生器所使用的程式語言都不太相同 (e.g: Ruby, Node.js, Python, PHP ....)，詳細可以參考可以參考 [StaticGen](https://www.staticgen.com/) 。