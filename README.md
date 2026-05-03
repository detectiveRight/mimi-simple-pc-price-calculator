# 🖥️ mimi-simple-pc-price-calculator

> A CLI tool that collects your PC or laptop hardware specifications and generates a ready-to-use AI prompt to estimate your device's market price in your country.

---

## 💡 What is this?

You have a PC or laptop and want to know its **real market price** — but you don't want to manually describe every spec to an AI tool every single time.

This tool asks you the right questions, then **generates a complete, ready-to-copy AI prompt** with all your hardware details so any AI (ChatGPT, Gemini, Claude, lumo, etc.) can give you an accurate price estimate for your country.

No API. No dependencies. Just Python.

---

## ⚙️ How it works

```
Run the script → Answer the questions → Copy the generated prompt → Paste it into any AI
```

That's it.

---

## 🚀 Getting Started

### Requirements
- Python 3.x

### Run

```bash
git clone https://github.com/detectiveRight/mimi-simple-pc-price-calculator.git
cd mimi-simple-pc-price-calculator
python mimi-simple-pc-price-calculator.py
```

---

## 📋 What it asks you

| Category | Details |
|---|---|
| **Device** | Type (PC / Laptop), Condition (new / used) |
| **Hardware** | CPU, GPU, RAM, Storage (size + type), Motherboard |
| **Accessories** | Monitor frequency, Keyboard size, Backlit or not |
| **AI Preferences** | Bottleneck analysis, Language, Country |

---

## 📤 Output Example

```
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Hello, please act as if you are an expert in hardware, software, and programming.
Please provide us with your device specifications as follows:

Device type: pc
Device source: used
cpu: Intel Core i5-10400F
Gpu: RTX 3060
ram space: 16GB
storage space: 512GB
Storage type: ssd
motherboard type: B460M
Desired screen frequency: 144hz
Keyboard type: 75%
keyboard & mouse: light up
Is there a problem with the device, and will that affect the price?: tell me
Speak to me in this language: Arabic
Using this information, please provide me with the detailed and accurate market price of the device in this country (Saudi Arabia)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
```

---

## 🌐 Supported Languages

The output prompt supports **any language** — just type it when asked. The AI will respond in your preferred language.

---

## 🔒 Privacy Tip

If you're concerned about sharing your hardware specs with big tech companies, consider using **[Lumo AI by Proton](https://lumo.proton.me/)** — a privacy-focused AI assistant from the makers of ProtonMail. Your data stays private and isn't used for training or shared with third parties.

---

## 📄 License

This project is licensed under the **GNU General Public License v3.0** — see the [LICENSE](LICENSE) file for details.

---

## 👤 Author

**detectiveRight**
- GitHub: [@detectiveRight](https://github.com/detectiveRight)

---

## 🐱 Special Thanks

A special thanks to **mimi** — the legendary, the great, the gentle cat.

---

*Built as a simple utility to save time when estimating PC prices using AI tools.*

---

## ©️ Copyright

Copyright © 2026 detectiveRight <<https://github.com/detectiveRight/>>

This project is open source under the GNU General Public License v3.0.
