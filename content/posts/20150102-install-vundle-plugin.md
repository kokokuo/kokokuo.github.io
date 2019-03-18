Title: Vundle 安裝與安裝 Plugin 時的注意事項
Date: 2015-01-02
Tags: Vim
Slug: install-vundle-and-notice
Authors: kokokuo
Summary: 剛開始學習使用 Vim，因為習慣了 GUI 的 IDE 特別是剛從號稱 Windows 的地表最強 IDE - Visual Studio 跳過來，整個好不容易，所以這裡記錄了一些剛使用 Vundle 時下載 Plugin 的小須知


# 前言
---
剛開始學習使用 Vim，因為習慣了 GUI 的 IDE 特別是剛從號稱 Windows 的地表最強 IDE - Visual Studio 跳過來，整個非常不容易，所以這裡記錄了一些剛使用 Vundle 時下載 Plugin 的小須知


# 安裝 Vundle
---
要安裝 Vundle 的方式便是透過 Git 下載來安裝：

```bash
git clone https://github.com/gmarik/vundle.git ~/.vim/bundle/vundle
```

下載好後，在 Home 目錄下修改 `.vimrc` (如果沒有就新建出來此檔案)，可以先參考[Github 上 Vundle 的介紹](https://github.com/gmarik/vundle)，使用它的 Configuration 範例完成安裝。


# [vim-script](http://vim-scripts.org/vim/scripts.html) 下載時要注意名稱含有 .vim
---
在 `vim-script` 上的有些 Repository 名稱會包含 `.vim`，如 `taglist.vim` 等
所以在編輯 .vimrc 時,要記得補上 `.vim`，如下：

```bash
Plugin 'taglist.vim'
```

# 使用 Vundle 提供的 `vimrc` 範例小注意
---
在 Github 中提供的 `.vimrc` 範例有兩行：

```bash
" Git plugin not hosted on GitHub
Plugin 'git://git.wincent.com/command-t.git'
" git repos on your local machine (i.e. when working on your own plugin)
Plugin 'file:///home/gmarik/path/to/plugin'
```

第二行則表示如果你是自己下載 Plugin Repository 到自己主機上，才需要去指定 local 端自己電腦的下載下來放置的 Repository 位置
所以預設如果有裝 Git，沒有下載下來 Plugin，此行是不需要的。

而第一行的 `git.wincent.com/command-t.git` 是一種套件，名叫 **CommandT**，詳細資訊可以參考[官方](github.com/wincent/Command-T)

# Plugin & Bundle 指令
---
目前 Vundle 已經把指令都改成 Plugin 開頭，但仍支援 Bundle 指令，以下用 `taglist.vim` 作為例子：

```bash
Plugin 'taglist.vim'
```

上述是新的 Plugin 語法，但是若要使用 Bundle 語法也沒問題，只是不建議，如下：

```bash
Bundle 'taglist.vim'
```

# 參考資料
---
1. [Vundle：Vim Plugin 自動下載、安裝、更新與管理工具（Vim Bundle）](http://www.gtwang.org/2014/04/vundle-vim-bundle-plugin-manager.html)
2. [Error in installing Bundle for Vim](http://stackoverflow.com/questions/20394142/error-in-installing-bundle-for-vim)