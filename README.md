# 💣 AFU Nuker v1.5 — Discord Server Nuker Bot

> ⚠️ **Educational use only. This tool is intended for testing in your own servers or development sandboxes. Misuse of this tool can result in permanent Discord bans and legal consequences. You are responsible for your actions.**

---

## 🧩 About

**AFU Nuker v1** is a Discord nuker bot built using `discord.py`. It performs destructive actions on a server (with permission), such as:
- Renaming the server
- Deleting all channels and roles
- Banning all members
- Spamming new channels and roles
- Sending spam messages via **webhooks**

Originally made for educational and stress-testing purposes, this bot demonstrates how automation and webhooks can interact with Discord’s server structure.

---

## 🚀 Features

| Feature           | Description                                                                 |
|------------------|-----------------------------------------------------------------------------|
| `!afu` Command    | Launches full nuking process                                                |
| Server Rename     | Renames server to value from config                                         |
| Channel Wipe      | Deletes all existing text and voice channels                                |
| Role Wipe         | Deletes all roles except `@everyone`                                        |
| Member Ban        | Attempts to ban every member in the server                                  |
| Channel Spam      | Creates endless spam channels                                               |
| Role Spam         | Creates endless new roles                                                   |
| Webhook Spam      | Creates webhooks in each channel to send messages at high speed             |

---

## 🛠️ Setup Instructions

1. **Clone this repository**:
   ```bash
   git clone https://github.com/yourusername/afu-nuker.git
   cd afu-nuker
   
