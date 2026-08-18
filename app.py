import streamlit as st

# Page Config
st.set_page_config(
    page_title="Neo AI Studio",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom Cyberpunk / Modern Dark UI Styling
st.markdown("""
    <style>
    .stApp {
        background-color: #090a0f;
        color: #f3f4f6;
    }
    .login-container {
        max-width: 420px;
        margin: 0 auto;
        padding: 40px;
        background: #111318;
        border: 1px solid #1f293d;
        border-radius: 16px;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.5);
    }
    .brand-title {
        font-size: 32px;
        font-weight: 800;
        text-align: center;
        background: linear-gradient(90deg, #06b6d4, #3b82f6);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 5px;
    }
    .brand-subtitle {
        text-align: center;
        color: #9ca3af;
        font-size: 14px;
        margin-bottom: 30px;
    }
    .stButton button {
        width: 100%;
        border-radius: 8px;
        font-weight: 600;
        padding: 10px;
        transition: all 0.2s ease;
    }
    </style>
""", unsafe_allow_html=True)

# Initialize Session State
if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False
if "username" not in st.session_state:
    st.session_state["username"] = ""

# --- AUTHENTICATION SCREEN ---
if not st.session_state["authenticated"]:
    col1, col2, col3 = st.columns([1, 1.2, 1])
    
    with col2:
        st.markdown("<br><br>", unsafe_allow_html=True)
        st.markdown('<div class="login-container">', unsafe_allow_html=True)
        st.markdown('<div class="brand-title">⚡ Neo AI</div>', unsafe_allow_html=True)
        st.markdown('<div class="brand-subtitle">Access your all-in-one AI workspace</div>', unsafe_allow_html=True)
        
        tab_login, tab_signup = st.tabs(["Sign In", "Register"])
        
        with tab_login:
            with st.form("login_form"):
                email = st.text_input("Email Address", placeholder="name@example.com")
                password = st.text_input("Password", type="password", placeholder="••••••••")
                submit_login = st.form_submit_button("Sign In", type="primary")
                
                if submit_login:
                    if email and password:
                        st.session_state["authenticated"] = True
                        st.session_state["username"] = email.split("@")[0]
                        st.rerun()
                    else:
                        st.error("Please fill in all fields.")

        with tab_signup:
            with st.form("signup_form"):
                new_email = st.text_input("Email Address", placeholder="name@example.com")
                new_password = st.text_input("Create Password", type="password", placeholder="••••••••")
                submit_signup = st.form_submit_button("Create Account", type="primary")
                
                if submit_signup:
                    if new_email and new_password:
                        st.success("Account created successfully! Please sign in.")
                    else:
                        st.error("Please fill in all fields.")

        st.markdown("<div style='text-align: center; margin: 15px 0; color: #6b7280; font-size: 12px;'>OR CONNECT WITH</div>", unsafe_allow_html=True)
        
        # Google Sign-In Simulation / OAuth Button
        if st.button("🌐 Continue with Google", use_container_width=True):
            st.session_state["authenticated"] = True
            st.session_state["username"] = "GoogleUser"
            st.rerun()
            
        st.markdown('</div>', unsafe_allow_html=True)
    st.stop()

# --- MAIN APP INTERFACE (Logged In) ---

# Sleek Sidebar UI
with st.sidebar:
    st.markdown("### ⚡ Neo AI Workspace")
    st.write(f"Logged in as: **{st.session_state['username']}**")
    
    if st.button("🚪 Log Out", type="secondary"):
        st.session_state["authenticated"] = False
        st.rerun()

    st.divider()
    st.subheader("⚙️ Settings & Configuration")
    ai_model = st.selectbox("AI Model Engine", ["Neo-Llama-3 (Fast)", "Neo-Vision (Image Gen)", "Neo-Codex (Code Engine)"])
    theme_mode = st.radio("Interface Theme", ["Cyber Dark", "Neon Synthwave"])

    st.divider()
    st.markdown("### 🔑 API Access")
    st.code("neo_live_8f9yxBx1aJKuAMfBTa", language="text")
    st.caption("Keep your live API key private.")

# Main Workspace Chat Interface
st.title("⚡ Neo AI Studio")
st.caption("Your all-in-one generative suite: Code, Images, PDFs, and Video synthesis.")

# Chat history initialization
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display past messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Prompt input
if prompt := st.chat_input("Message Neo AI or request code, images, video assets..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Response generation mockup
    response = f"Neo AI processed your prompt using **{ai_model}**: *'{prompt}'*. (API Key verified & active)"
    
    with st.chat_message("assistant"):
        st.markdown(response)
    st.session_state.messages.append({"role": "assistant", "content": response})
