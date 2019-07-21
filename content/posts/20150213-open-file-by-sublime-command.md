Title: Mac - 使用指令以 Sublime 開啟檔案
Date: 2015-02-13
Tags: Mac, Sublime
Slug: open-file-by-sublime-command
Authors: kokokuo
Summary: 最近使用 Sublime 開發，但是因為本身習慣用 Command 做事情，所以懶得用 UI 點擊軟體開啟的方式，因此決定尋找 Sublime 是否有指令可以做，以下紀錄設定過程。

# 前言
最近使用 Sublime 開發，但是因為本身習慣用 Command 做事情，所以懶得用 UI 點擊軟體開啟的方式，因此決定尋找 Sublime 是否有指令可以做，以下紀錄設定過程。

<br/>

# 設定步驟

## 1.把 Sublime 的指令放到 `usr/local/bin` 目錄下

一般預設而言，下載 Sublime 並安裝在 Mac 後，如果是 Text2 預設路徑會在：

```bash
/Applications/Sublime\ Text\ 2.app/Contents/SharedSupport/bin/
```

如果是 Text3 則是：

```bash
/Applications/Sublime\ Text.app/Contents/SharedSupport/bin/
```

而不管是 Text2 或 Text3 的 `bin` 目錄底下，都會有一個 `subl` 執行檔案。
因此我們要把此執行檔加至環境變數，如果才能讓 Terminal 在輸入 `subl` 時找到該程式，並以此程式開啟檔案。

而為了方便檔案的管理，接著採用 symlink 捷徑的方式放到 `/usr/local/bin` 目錄下管理（ 系統管理員在本機自行安裝自己下載的軟體( 非 distribution 預設提供者 )）。

所以若是 Text2 請在 Terminal 中輸入此行執行：

```bash
ln -s /Applications/Sublime\ Text\ 2.app/Contents/SharedSupport/bin/subl /usr/local/bin/subl
```

若是版本是 Text3 則在 Terminal 中輸入此行執行：

```bash
ln -s /Applications/Sublime\ Text.app/Contents/SharedSupport/bin/subl /usr/local/bin/subl
```

## 2. 把 `usr/local/bin` 路徑加入致環境變數

若是 `/usr/local/bin/` 不存在於環境變數 PATH 中，請把此路徑加入至用戶的環境變數設定檔中，如 `.bash_profile` ( 如果沒有請在 Home 目錄建置 )。

完成後，重啟 Terminal 後 sublime 便會被系統環境偵測到，如果要查看指令，因為我們的 symlink 是改成 sublime，所以下 `sublime -h` 即可。

<br/>

# 參考資料
1. [Launch Sublime Text 2 from the Mac OS X Terminal](https://gist.github.com/artero/1236170)