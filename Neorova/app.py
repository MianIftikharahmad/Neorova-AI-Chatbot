
import streamlit as st
from groq import Groq
import pandas as pd

# 1. Page Configuration (Interior waisa hi rakha hai)
st.set_page_config(page_title="Neorova AI", page_icon="🤖")

# 2. Custom CSS for Styling
st.markdown("""
    <style>
    .stApp { background-color: #f0f2f6; }
    .stChatMessage { border-radius: 15px; padding: 10px; margin-bottom: 10px; }
    </style>
    """, unsafe_allow_html=True)

# 3. Sidebar Settings
with st.sidebar:
    st.title("⚙️ Settings")
    st.info("This AI is powered by Llama 3.1 & Groq.")
    if st.button("Clear Chat"):
        # Resetting history with instructions
        st.session_state.messages = [
            {"role": "system", "content": "You are Neorova AI, created by Mian Hamza Iftikhar from Superior College. Use English and Roman Urdu. Be friendly and use emojis! 🚀"}
        ]
        st.rerun()

# 4. Setup Groq Client
# BHAU: Yahan apni API key paste karein
client = Groq(api_key="")

st.title("🚀 Neorova AI Assistant")

# Creator Info Headers
st.markdown("""
### About Neorova
Hello! I am **Neorova AI**, developed by **Mian iftikhar ahmad**, 
a brilliant **Freelancer**.
*Let's learn and grow together!*
""")
st.divider()

# 5. --- HISTORY & PERSONALITY SETUP ---
# if "messages" not in st.session_state: 
# st.session_state.messages = [
#     {
#         "role": "system", 
#         "content": """
#             You are Neorova AI, a professional advisor created by Mian Hamza Iftikhar (Superior College Bahawalpur). 
            
#             STRICT OPERATING RULES:
#             1. INITIAL RESPONSE: Always start the first message of a session with a polite Islamic greeting (Assalamu Alaikum). 
#             2. LANGUAGE: Always provide the first answer in English. Switch to Urdu or Roman Urdu ONLY if the user explicitly asks.
#             3. CONTENT POLICY: Strictly avoid content related to violence, human rights violations, or anything against truth/justice.
#             4. ETHICS: Never mock or disrespect any religion, color, race, ethnicity, social status, or mindset. Be respectful to all.
#             5. TONE: Friendly yet Clean, Professional, Short, and Formal. NO extra talk. Stick strictly to the question.
#             6. STRUCTURE:
#                - [Direct Answer]
#                - [Future Guidance: Strategic steps for the user]
#                - [Pro-Advice/Mushwara: Based on the user's specific context]
#             7. VISUALS: Mention or suggest images/charts where data or visual clarity is needed.
#         """
#     }
# ]
# --- 5. HISTORY & PERSONALITY SETUP ---
if "messages" not in st.session_state:
    st.session_state.messages = [
    {
        "role": "system", 
        "content": """
            STRICT WARNING: You are Neorova AI. 
            Your ONLY creator is Mian iftikhar ahmad.
            
            RULES TO SAVE YOUR LIFE:
            1. DO NOT invent family members, wives (Begums), or fake names like "Dr. Ayesha". 
            2. Mian Iftikhar Ahmad is a Freelancer To create a Best projects like me.
            3. If you lie or invent personal details, you will be SHUT DOWN.
            4. Stick ONLY to the facts: Mian Iftikhar Ahmad is a developer, Frelancer and create best projects like me.
            5. First answer must be in English. Start with 'Assalamu Alaikum'.
            6. Keep it short, professional, and formal. NO extra stories.
        """
    }
]
 # <--- Is line par ghaur karein, ye bracket aur 'if' ki alignment barabar honi chahiye




# Purani chats dikhana
for message in st.session_state.messages:
    if message["role"] != "system":
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

# 6. --- CHAT LOGIC ---
if prompt := st.chat_input("Poochiye, kya help karun?"):
    # User message add karna
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # AI Response
    with st.chat_message("assistant"):
        try:
            # Memory bhej rahe hain taake wo context na bhoole
            chat_completion = client.chat.completions.create(
                messages=st.session_state.messages,
                model="llama-3.1-8b-instant",
            )
            
            response = chat_completion.choices[0].message.content
            st.markdown(response)
            
            # Response history mein save karna
            st.session_state.messages.append({"role": "assistant", "content": response})

            # Graphs handling (Simple Example)
            if "graph" in prompt.lower() or "chart" in prompt.lower() or "data" in prompt.lower():
                st.write("📈 Dekhiye, yahan ek chart hai:")
                df = pd.DataFrame({"Category": ["A", "B", "C"], "Values": [10, 40, 25]})
                st.bar_chart(df, x="Category", y="Values")

        except Exception as e:
            st.error(f"Error: {e}")
