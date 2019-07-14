Title: Golang - 安裝 Golang 在 Mac 上
Date: 2019-07-13
Tags: Golang, Mac
Slug: golang-install-on-mac
Authors: kokokuo
Summary: 最近開始摸 Golang ( 簡稱 Go )，而正所謂預先善其事必先利其器，當然要先把環境安裝好。在 Mac 上安裝 Golang 非常容易，可以直接透過 `hombrew` 或是從 Golang 官方下載安裝即可。但是這麼做會使電腦的 Golang 的版本被限縮在某一版，如果今天從 Github 上或是與其他團隊共同開發 Golang 專案時，可能會需要同時存在不同版本，因此本篇介紹如何安裝 Golang 以及使用 Golang 版本管理器 - GVM 來俐落的安裝不同的 Golang 版本。

# 前言
最近開始摸 Golang，而正所謂預先善其事必先利其器，當然要先把環境安裝好。在 Mac 上安裝 Golang 非常容易，可以直接透過 `hombrew` 或是從 Golang 官方下載安裝即可。但是這麼做會使電腦的 Golang 的版本被限縮在某一版，如果今天從 Github 上或是與其他團隊共同開發 Golang 專案時，可能會需要同時存在不同版本，因此本篇介紹如何安裝 Golang 以及使用 Golang 版本管理器 - GVM 來俐落的安裝不同的 Golang 版本。

# 一、透過 GVM 管理 Go 版本

## 1. 什麼是 GVM ( Go Version Management ) 
GVM 是一套由第三方的開源開發者們共同撰寫的 Go 語言版本管理器，能夠在系統上同時透過這套 GVM 的套件，為我們同時安裝多個不同版本的 Go ，並且可以切換要使用的版本。

這樣的管理器，如果有寫過其他語言的人一定不陌生，例如 Ruby 的 [RVM](https://github.com/rvm/rvm)，Python 的 [pyenv](https://github.com/pyenv/pyenv)，Node.js 的 [nvm](https://github.com/nvm-sh/nvm) ...等等。

而在 Go 語言上也有這樣方便好用的版本管理器，安裝非常簡單，以下我們來看一下。

## 2. 安裝 GVM

### 安裝到 Bash 中
輸入以下指令安裝：

```shell
$ bash < <(curl -s -S -L https://raw.githubusercontent.com/moovweb/gvm/master/binscripts/gvm-installer)
```

透過執行這段指令，GVM 會被安裝到 `~/.gvm` 目錄下，此外自動為我們寫入 bash 的用戶環境變數中：

```shell
 [[ -s "/Users/<username>/.gvm/scripts/gvm" ]] && source "/Users/<username>/.gvm/scripts/gvm"`
 ```

如下圖是 `~/.bash_profile`：

<img src="../images/20190713-install-golang-on-mac/bash-profile-gvm-settings.png" alt="bash-profile-gvm-settings" width="480px"/>


<br/>

### 安裝到 Zsh 中
然而若是使用 `zsh`，則可以改成下載套件並設定到 `zsh` 中：

```shell
$ zsh < <(curl -s -S -L https://raw.githubusercontent.com/moovweb/gvm/master/binscripts/gvm-installer)
```

<img src="../images/20190713-install-golang-on-mac/install-gvm-to-zsh.png" alt="install-gvm-to-zsh" width="480px"/>

打開 `~/.zshrc` 可以看到 `[[ -s "/Users/<username>/.gvm/scripts/gvm" ]] && source "/Users/<username>/.gvm/scripts/gvm"` 被設定進去。

<img src="../images/20190713-install-golang-on-mac/zshrc-show-gmv-env-settings.png" alt="zshrc-show-gmv-env-setting" width="480px"/>


## 3. 啟動 GVM 安裝 Golang
在上述安裝完並檢查環境變數有指向 GVM 後，接著可以透過重新啟動 Ternimal 或是手動以 `source` 指令來啟動 GVＭ：

```shell
$ source /Users/<username>/.gvm/scripts/gvm
```

接著輸入 `gvm` 便會看到可以開始使用 GVM 版本管理器。

<img src="../images/20190713-install-golang-on-mac/installed-gvm.png" alt="installed-gvm" width="480px"/>

接著我們要來安裝需要的 Go 版本