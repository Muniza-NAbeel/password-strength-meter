import streamlit as st
import re
import random
import string


# Set the title of the app
st.set_page_config(page_title="Password Strength Meter by Muniza Nabeel", page_icon="🔐")
st.title("🔐 Password Strength Meter")
st.markdown("🔑 Check your password strength and get suggestions to improve it. 📈")

# ✅ Common weak passwords ki expanded blacklist
common_passwords = {
    "password", "password123", "123456", "12345678", "abcdefg",
    "password1", "1234567890", "123456789", "abc123", "12345678",
    "qwerty", "qwerty123", "passw0rd", "iloveyou", "monkey",
    "54321", "654321", "qwertyui", "asdfghjkl", "zxcvbnm",
}

# Precompile regex patterns for performance
upper_lower_pattern = re.compile(r"(?=.*[A-Z])(?=.*[a-z])")   # Check for at least one uppercase and one lowercase letter
digit_pattern = re.compile(r"\d")        # Check for at least one digit
special_pattern = re.compile(r"[!@#$%^&*]")   # Check for at least one special character

# Function to generate a strong password
def generate_strong_password():    
    """Random strong password generate karega"""
    characters = string.ascii_letters + string.digits + "!@#$%^&*"
    return ''.join(random.choice(characters) for _ in range(12))

# Function to check password strength
def check_password_strength(password):
    """Password ki strength check karne ka function"""
    if password.lower() in common_passwords:
        return "❌ This password is too common! Please choose a stronger one.", "very weak", [], 0, None

    score = 0
    feedback = []

    # Length Check
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("🔴 Password should be at least 8 characters long.")
    
    # Upper & Lowercase Check
    if upper_lower_pattern.search(password):
        score += 1
    else:
        feedback.append("🟠 Include both uppercase and lowercase letters.")
    
    # Digit Check
    if digit_pattern.search(password):
        score += 1
    else:
        feedback.append("🟡 Add at least one number (0-9).")
    
    # Special Character Check
    if special_pattern.search(password):
        score += 1
    else:
        feedback.append("🟢 Include at least one special character (!@#$%^&*).")
    
    strength_percentage = (score / 4) * 100
    
    if score == 4:
        return "✅ Strong Password! 🎉 Your password is highly secure.", "strong", ["🔹 Great job! Your password meets all security criteria.", "🔹 Keep using unique and complex passwords for better safety.", "🔹 Consider using a password manager to store it securely."], strength_percentage, password
    elif score == 3:
        return "⚠️ Moderate Password - Consider adding more security features.", "moderate", feedback, strength_percentage, None
    else:
        return "❌ Weak Password - Improve it using the suggestions below.", "weak", feedback, strength_percentage, None

password = st.text_input("Enter your password:", type="password")

# Check password strength when button is pressed
if st.button("🛡️ Check Strength"):
    if password:
        result, strength, feedback, strength_percentage, show_password = check_password_strength(password)
        
        # Display password strength result
        st.subheader(result)
        
        # **⚡ If password is very weak (common passwords), show alert**
        if strength == "very weak":
            st.error("🚨 This password is in the common weak password list! Please choose a stronger one.")

        # **Custom Progress Bar Colors based on strength**
        bar_color = "red" if strength_percentage < 50 else "yellow" if strength_percentage < 75 else "green"
        st.markdown(
            f"""
            <style>
            .stProgress > div > div > div > div {{
                background-color: {bar_color};
            }}
            </style>
            """,
            unsafe_allow_html=True,
        )
        st.progress(strength_percentage / 100)
        
        # Display feedback for improvement
        if feedback:
            st.warning("💡 Suggestions to improve your password:")
            for index, tip in enumerate(feedback, start=1):
                st.write(f"{index}. {tip}")
        
        # Generate Strong Password if weak or moderate
        if strength in ["weak", "moderate"]:
            if st.button("Generate Strong Password"):
                strong_password = generate_strong_password()
                st.success(f"🔑 Suggested Strong Password: `{strong_password}`")
        
        # If password is strong, show the success message and password
        elif strength == "strong":
            st.success("✨ Your password is strong! Keep it safe and avoid sharing it with anyone.")
            st.info(f"🔑 Your Strong Password: `{show_password}`")
    else:
        st.error("Please enter a password to check strength.")
