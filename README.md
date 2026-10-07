# 🌿 TouchGrass AI

> Turn your free time into real-world experiences.

TouchGrass AI is an AI-powered outdoor activity planner built for the Hacktoberfest 2026 Week 1 challenge, **"Touch Grass"**.

The app uses a locally running open-weight AI model, **Gemma 3**, through **Ollama** to create personalized outdoor activity plans based on the user's time, mood, interests, group size, and location.

The goal is simple: use AI to help people spend **less time on screens and more time outdoors.** 🌱

---

## ✨ Features

- 🌳 Personalized outdoor activity recommendations
- ⏰ Time-based outdoor plans
- 👥 Supports individual and group activities
- 😊 Recommendations based on mood
- 🎯 Activity recommendations based on interests
- 🎒 Things-to-carry suggestions
- 📵 Screen-free challenge
- 🔄 Alternative outdoor activity
- ✅ Screen-free challenge completion tracker
- 🔒 AI runs locally through Ollama

---

## 🤖 How AI Is Used

TouchGrass AI uses **Gemma 3 (1B)** as the core AI model.

The user provides:

- Available time
- Number of people
- Mood
- Interest
- Location

These details are sent to the locally running Gemma model through Ollama.

Gemma then generates:

1. An outdoor activity
2. A time-based plan
3. Things to carry
4. A screen-free challenge
5. An alternative activity

This makes AI the core of the application rather than just an additional feature.

---

## 🛠️ Tech Stack

- **Python**
- **Streamlit**
- **Ollama**
- **Gemma 3 (1B)**
- **Git & GitHub**

---

## 🏗️ Project Flow

```text
User
  ↓
Streamlit Interface
  ↓
User Preferences
  ↓
Python Application
  ↓
Ollama
  ↓
Gemma 3
  ↓
Personalized Outdoor Plan
  ↓
Real-World Outdoor Activity 🌳