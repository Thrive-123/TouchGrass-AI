import streamlit as st
import ollama

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="TouchGrass AI",
    page_icon="🌿",
    layout="centered"
)

# ---------------- HEADER ----------------
st.title("🌿 TouchGrass AI")
st.subheader("Turn your free time into real-world experiences.")

st.write(
    "Tell us about your free time and preferences. "
    "Our local AI will create a personalized outdoor plan for you."
)

st.divider()

# ---------------- USER INPUTS ----------------
time_available = st.selectbox(
    "⏰ How much time do you have?",
    ["30 minutes", "1 hour", "2 hours", "3 hours", "Half a day"]
)

people = st.number_input(
    "👥 How many people are joining?",
    min_value=1,
    max_value=20,
    value=1
)

mood = st.selectbox(
    "😊 What's your mood?",
    ["Relaxed", "Energetic", "Social", "Adventurous", "Creative"]
)

interest = st.selectbox(
    "🌳 What are you interested in?",
    [
        "Nature",
        "Walking",
        "Sports",
        "Photography",
        "Gardening",
        "Bird watching",
        "Something new"
    ]
)

location = st.text_input(
    "📍 Where are you planning to go?",
    placeholder="Example: Near my college / local park"
)

# ---------------- GENERATE PLAN ----------------
if st.button("🌱 Generate My Outdoor Plan", use_container_width=True):

    if not location:
        st.warning("📍 Please enter a location.")
    else:

        prompt = f"""
You are TouchGrass AI, an outdoor activity planning assistant.

Create a practical outdoor activity plan using these details:

Available time: {time_available}
Number of people: {people}
Mood: {mood}
Interest: {interest}
Location: {location}

The goal is to help the user spend meaningful time outdoors
and reduce unnecessary screen time.

Return the answer using EXACTLY these sections:

ACTIVITY:
Give one suitable outdoor activity.

TIME PLAN:
Create a simple timeline for the available time.

THINGS TO CARRY:
Give 4 to 6 useful items.

SCREEN-FREE CHALLENGE:
Give one challenge that requires ZERO phone or screen usage.
The challenge should encourage observing nature, talking to people,
walking, breathing, listening, or noticing the surroundings.
Never suggest using, checking, scrolling, photographing, or timing
anything with a phone.

ALTERNATIVE:
Give one alternative outdoor activity that also does not require
a phone or screen.

Keep the answer practical, concise and encouraging.
Do not ask questions at the end.
Do not suggest activities that require a phone or screen.
"""

        with st.spinner("🌿 Creating your outdoor plan..."):

            response = ollama.chat(
                model="gemma3:1b",
                messages=[
                    {
                        "role": "user",
                        "content": prompt
                    }
                ]
            )

        result = response["message"]["content"]

        # ---------------- OUTPUT ----------------
        st.success("🎉 Your outdoor plan is ready!")

        st.markdown("## 🌳 Your TouchGrass Plan")

        st.write(result)

        st.divider()

        # ---------------- SCREEN-FREE CHALLENGE ----------------
        st.markdown("### 📵 TouchGrass Challenge")

        st.write(
            "Put your phone away and complete the screen-free "
            "challenge from your plan."
        )

        completed = st.checkbox(
            "✅ I completed my screen-free challenge!"
        )

        if completed:
            st.success(
                "🌱 Amazing! You touched grass today! "
                "Keep the streak going."
            )

        st.divider()

        # ---------------- FOOTER ----------------
        st.caption(
            "🤖 Powered by Gemma 3 running locally through Ollama. "
            "Your input is processed locally on your computer."
        )