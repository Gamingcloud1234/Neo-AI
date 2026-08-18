import streamlit as st
from st_login_form import login_form

# Page Config
st.set_page_config(
    page_title="Neo AI",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 1. Authentication Check using st-login-form
if "authenticated" not in st.session_state or not st.session_state["authenticated"]:
    st.markdown("<h1 style='text-align: center;'>⚡ Neo AI Portal</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: gray;'>Sign in or create an account to access your workspace</p>", unsafe_allow_html=True)
    
    # Corrected function call (reads from secrets.toml automatically)
    supabase = login_form(title="Authentication")
    st.stop()

# --- MAIN APP (Only visible if logged in) ---

# User Info & Logout Sidebar
st.sidebar.title("⚡ Neo AI Workspace")
st.sidebar.write(f"Logged in as: **{st.session_state.get('username', 'User')}**")

if st.sidebar.button("Log Out"):
    st.session_state["authenticated"] = False
    st.rerun()

st.sidebar.divider()

# 2. Settings Panel in Sidebar
st.sidebar.subheader("⚙️ Settings")
ai_model = st.sidebar.selectbox("Select AI Model", ["Neo-Llama-3 (Fast)", "Neo-Vision (Images)", "Neo-Codex (Code)"])
theme_mode = st.sidebar.radio("Interface Theme", ["Cyber Dark", "Neon Synthwave"])

st.sidebar.divider()
st.sidebar.markdown("### 🔑 API Keys")
st.sidebar.code("neo_live_abc123xyz789...", language="text")

# 3. Main Chat & Multi-modal Interface
st.title("⚡ Neo AI Studio")
st.caption("Your all-in-one AI assistant: Code generation, image creation, PDF processing, and video tooling.")

# Chat history initialization
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display prior chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User prompt input
if prompt := st.chat_input("Ask Neo AI anything or request code/images..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Simulated AI response
    response = f"Neo AI received your request for: *'{prompt}'*. (Model: {ai_model})"
    
    with st.chat_message("assistant"):
        st.markdown(response)
    st.session_state.messages.append({"role": "assistant", "content": response})
