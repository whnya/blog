---
title: Arch installation broken?
date: '2022-05-13'
tags: ['linux', 'tutorial']
draft: false
summary: Arch installation broken? Reinstall it, and get back to tracks with this tutorial.
---

## Introduction

As a stupid, newbie Arch Linux user, I often break my system. And such, I want a way to easily reinstall Arch Linux.

Alas, most popular solution fail to meet some of my needs.

So here I am, presenting to you, the definitive way to reinstall Arch Linux. Well, at the very least, according to whi_ne.

### Warning

This is a highly personalized tutorial, and thus will obviously not cater to all Arch Linux users.

I just wrote an article to go to whenever I want to reinstall Arch Linux.

## Installation

You will install Arch Linux using the Anarchy installer.

## Setup

### Preparation

I know that you are using your phone to view this tutorial.

We first need to install `dmenu`, `kitty`, and `firefox-developer-edition` so you can copy and paste commands from your machine easily.

- Press `$MOD` + `Enter` (Press `$MOD` and `Enter` keys simultaneously), then type the following:

  ```zsh
  su root -c "pacman -S --noconfirm dmenu kitty firefox-developer-edition"
  ```

  Press `Enter` afterwards. Wait for the command to finish.

- Press `$MOD` + `D` (Press `$MOD` and `D` keys simultaneously), type `firefox-developer-edition` and press `Enter`. A window with a title `Firefox Developer Edition` should appear.

- Hover to the address bar, right-click, type `blog.whinyaan.xyz/arch-install`, and press `Enter`. You should now be able to copy and paste commands on your machine.

- Press `$MOD` + `D` (Press `$MOD` and `D` keys simultaneously), type `kitty` and press `Enter`. A window with a title `~` should appear. You will now use this terminal to run the rest of the commands.

### Sudo permissions

Since Anarchy installer, for some reason, does not grant sudo permissions to the user, we have to do it manually.

Switch to the terminal window, and run the following command:

```zsh
su root -c "usermod -aG wheel $USER && echo '$USER All=(ALL:ALL) NOPASSWD: ALL' >> /etc/sudoers && sed -e 's/%wheel ALL=(ALL:ALL) ALL/# %wheel ALL=(ALL:ALL) ALL/' -i /etc/sudoers"
```

### DNS

We will be using Cloudflare's DNS server for our machine.

Run the following command:

```zsh
sudo touch /etc/resolvconf.conf
sudo chown -R "$USER:" /etc/resolvconf.conf
echo "\nnameserver 1.1.1.1\nnameserver 1.0.0.1" >> /etc/resolvconf.conf
```

### Pacman

We will be setting up pacman at this step.

Run the following command:

```zsh
sudo sed -e 's/CheckSpace/#CheckSpace/' -e 's/#ParallelDownloads\ =\ 5/ParallelDownloads = 30\nILoveCandy/' -e 's/#Color/Color/' -e 's/#VerbosePkgLists/VerbosePkgLists/' -i /etc/pacman.conf
sudo pacman-key --recv-key FBA220DFC880C036 --keyserver keyserver.ubuntu.com
sudo pacman-key --lsign-key FBA220DFC880C036
sudo pacman -Syyu --noconfirm base-devel git rust
git config --global user.email "mail@whinyaan.xyz"
git config --global user.name "whi~nyaan\!"
```

## Program Installation

### Build from source

#### snapd

Run the following command:

```zsh
cd /tmp
git clone https://aur.archlinux.org/snapd.git
cd snapd/
makepkg -si --noconfirm
systemctl enable --now snapd.socket
ln -s /var/lib/snapd/snap /snap
modprobe loop
cd .. && rm -rf snapd/
cd ~/
```

#### paru

Run the following command:

```zsh
cd /tmp
git clone https://aur.archlinux.org/paru.git
cd paru/
yes y | makepkg -si
cd .. && rm -rf paru/
cd ~/
```

### Install using paru

Run the following command:

```zsh
paru -Syyu --noconfirm bleachbit clipit dnsutils drive-bin feh flameshot flatpak fuse gcolor3 gimp imagemagick insomnia keepassxc kitty lxappearance mpv nano nitrogen nodejs-lts-gallium noto-fonts-emoji obs-studio ocs-url optipng p7zip potrace scrcpy squashfuse sublime-text ttf-hanazono tumbler visual-studio-code-bin xbindkeys yarn zathura zathura-pdf-mupdf
```

### Install using scripts

#### npm

Run the following command:

```zsh
su root -c "curl -L https://www.npmjs.com/install.sh|sh"
setcap cap_net_bind_service=+ep `readlink -f \`which node\``
```

## Miscellaneous

### Fonts

Run the following command:

```zsh
touch /etc/fonts/local.conf
chown -R "$USER:" /etc/fonts/local.conf
echo '<?xml version="1.0"?><!DOCTYPE fontconfig SYSTEM "fonts.dtd"><fontconfig><alias><family>sans-serif</family><prefer><family>Noto Sans</family><family>Noto Color Emoji</family><family>Noto Emoji</family><family>DejaVu Sans</family></prefer></alias><alias><family>serif</family><prefer><family>Noto Serif</family><family>Noto Color Emoji</family><family>Noto Emoji</family><family>DejaVu Serif</family></prefer></alias><alias><family>monospace</family><prefer><family>Noto Mono</family><family>Noto Color Emoji</family><family>Noto Emoji</family><family>DejaVu Sans Mono</family></prefer></alias></fontconfig>' | tee -a /etc/fonts/local.conf
fc-cache
```

## Theming

### Firefox Developer Edition

- Copy the following command:

  ```zsh
  echo '#!/bin/bash\nmkdir "$1/chrome" && echo "#tabbrowser-tabs { visibility: collapse !important; }" >> "$1/chrome/userChrome.css"' > tmp.sh && chmod +x tmp.sh && ./tmp.sh "
  ```

- Switch to the terminal window, and press `Ctrl` + `Shift` + `V` (Press `Ctrl`, `Shift`, and `V` keys simultaneously)

- Press `$MOD` + `D` (Press `$MOD` and `D` keys simultaneously), type `firefox-developer-edition` and press `Enter`. A window with a title `Firefox Developer Edition` should appear.

- Press the hamburger icon on the top-right corner of the window, then press `Sign In`. Sign in with your Firefox account. Wait for all the extensions to install.

- Hover to the address bar, right-click, type `about:config`, and press `Enter`. You should be greeted by the following prompt:

  ![about:config prompt](/static/images/screenshots/about:config prompt.png)

  Toggle the check box, then press the button with the text `Accept the Risk and Continue`.

- Focus to the text field and type `toolkit.legacyUserProfileCustomizations.stylesheets`. You should see the following:

  ![toolkit.legacyUserProfileCustomizations.stylesheets](/static/images/screenshots/toolkit.legacyUserProfileCustomizations.stylesheets.png)

  Press the `toggle` button once.

- Hover to the address bar, right-click, type `about:support`, and press `Enter`. Under the heading `Application Basics`, go to `Profile Directory` and copy the path.

- Switch to the terminal window, press `Ctrl` + `Shift` + `V` (Press `Ctrl`, `Shift`, and `V` keys simultaneously), type `"`, then press `Enter`.

### Visual Studio Code

Sign-in with your GitHub account, and the extensions, and thus, also the theme, will be automatically installed.

### GTK

- Switch to the terminal window and run the following command:

  ```zsh
  cd /tmp && wget -O "dracula pink.tar.xz" `wget -qSO - "https://api.github.com/repos/dracula/gtk/releases/latest" 2>&1 | grep -E "browser_download_url.*Dracula-pink-accent.tar.xz" | cut -d '"' -f4 | tail -1` && mkdir "dracula pink" && tar -xf "dracula pink.tar.xz" -C "dracula pink" && sudo rm -rf "dracula pink.tar.xz" "/home/$USER/.themes/dracula pink" && sudo mv -f "dracula pink/Dracula-pink-accent" "/home/$USER/.themes/dracula pink" && sudo rm -rf "dracula pink" && cd ~
  ```

- Press `$MOD` + `D` (Press `$MOD` and `D` keys simultaneously), type `lxappearance` and press `Enter`. A window with a title `Customize Look and Feel` should appear, as shown below:

  ![lxappearance](/static/images/screenshots/lxappearance.png)

  In the left side, pick `dracula pink` by hovering the cursor to text displaying the said name of the theme and left-clicking the mouse. In the lower-right corner, there is a button called `Apply`. hover towards it and right-click it to apply the theme.

- Close the window by pressing `$MOD` + `Shift` + `Q` (Press `$MOD`, `Shift`, and `Q` keys simultaneously).
