Title: Pelican - 設定客製化網域並顯示在 Github Page 上 
Date: 2019-07-15
Tags: Pelican, Github, Domain
Slug: add-custom-domain-on-github-page-and-pelican
Authors: kokokuo
Summary: 使用 Github Page 架設個人的靜態網誌並寫了一些教學文有一些時間了，但是 Github Page 所架設的網誌，所使用的網域都是 `<username>.github.io` 格式，難道不能設定自己的買的網域嗎？ 那接著我們就來看看這篇吧！


# 一、設置化網域設定

## 1. 購買想要的域名
購買網域名稱這部分，在網路上有諸多的服務可以購買，如國產中華電信，全球較知名的網路註冊商[Godaddy](https://tw.godaddy.com),、[NameCheap](https://www.namecheap.com/)、[Gandi.net](https://www.gandi.net)，或是熟知的幾大雲端服務也會提供，如 [AWS Route53](https://docs.aws.amazon.com/zh_cn/Route53/latest/DeveloperGuide/registrar.html)、[Google Domain](https://domains.google/#/)、Azure，甚至一些比較小眾或是特別網域才買得到註冊商，像是本人用過 [Registr.TO](https://register.to/) ... 等等，都能購買。

不過因為網路上有太多的相關文章介紹與分享，所以這邊就直接跳過此段。且由於我本人比較常用也熟悉 GoDaddy 的服務，所以接下來的設定為以 GoDaddy 為例，如果有想要了解的部分也可以在聯繫我，我會嘗試為你解答。

我從 GoDaddy 購買了 `koko.guru` 這個網域，接下來我將要設定子網域 `note.koko.guru` 來作為我 Github Page 的客製化網域。

## 2. 在 Github Page 填上想要的客製化網域
接著打開我們的 Github Page Repository，點擊右上角的 **Settings**，找到 **GitHub Pages** 區塊的 **Custom Domain**，並輸入要加入的客製化網域，如我在這裡輸入 `note.koko.guru` 並按下 **Save**。

<img src="../images/20190715-add-custom-domain-on-github-page-and-pelican/github-page-setting-add-custom-domain.png" alt="github-page-setting-add-custom-domain" width="480px"/>

接著當你再次回到 Repository 下的時候就會看到 `CNAME` 出現在 `master` 分支中：

<img src="../images/20190715-add-custom-domain-on-github-page-and-pelican/cname-file-in-master.png" alt="cname-file-in-master" width="640px"/>

點擊 `CNAME` 檔案觀看時會發現該檔案其實很單純，只是打上的我們在 **GitHub Pages** 區塊的 **Custom Domain** 所填寫的 `note.koko.guru` 內容而已。

<img src="../images/20190715-add-custom-domain-on-github-page-and-pelican/cname-file-content.png" alt="cname-file-content" width="640px"/>

上述這種方式雖然很簡單，但是透過 Github 的 **Custom Domain** Settings 是只有一次性的建立 CNAME 而已。

若未來我們的網誌更新，再次藉由 Pelican 提供的 `make github` 推版上去 `master` 的 Repository 時，就會被整個覆蓋掉，所以這並不是長久之計。

因此我們最好的方式是在 Pelican 的靜態網站每次更新並推版到 `master` 時把這個 `CNAME` 也放在裡面部署上去，以下來介紹如何透過 Pelican 產生。


## 3. 透過 Pelican 產生 CNAME 檔案
在 Pelican 中，我們一樣要先建立這個 `CNAME` 的檔案，並且藉由先前在 [Pelican - 常用參數設定介紹與功能設定]({filename}/posts/20190315-pelican-setting-introduction.md) 與 [Pelican - 如何客製化 Pelican Theme 的 Flex 樣式]({filename}/posts/20190318-pelican-flex-theme-custom-css.md) 文中提到的 `EXTRA_PATH_METADATA` 與 `STATIC_PATHS` ，讓檔案可以在輸出成 HTML 到 `output` 時也被放 `output` 根目錄下。

```python
# 設定哪些目錄或檔案，要被視為靜態文件，並且放置到輸出目錄下
STATIC_PATHS = [
  "images", 
  "extra"
]
# 用來設定複製到輸出目錄時，該 extra/CNAME 會被投放對應的位置，這邊設定在 根目錄
EXTRA_PATH_METADATA = {
    "extra/CNAME": {"path": "CNAME"},
    "extra/README": {"path": "README.md"},
    "extra/favicon.ico": {"path": "static/favicon.ico"},
    "extra/custom.css": {"path": "static/custom.css"},
    "extra/koko-logo.png": {"path": "static/koko-logo.png"},
}
```


接著我們就可以開始到網域所購買的網域提供商，讓域名指向 Github Page 路徑了。

## 4. 只指向 Github Page


所以「網域提供商」指的也就是所購買的網域的來源服務商，像我就是 GoDaddy。並且網註冊商

# 二、設定 HTTPS

# 參考資料
1. [Quick start: Setting up a custom domain](https://help.github.com/en/articles/quick-start-setting-up-a-custom-domain)
2. [Adding or removing a custom domain for your GitHub Pages site](https://help.github.com/en/articles/adding-or-removing-a-custom-domain-for-your-github-pages-site)
3. [Github Pages 自訂域名 - 輕鬆擁有 https 綠鎖頭 (1)](https://blog.dmoon.tw/github-pages-custom-domain/index.html)