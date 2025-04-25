import streamlit as st

def check_password(password):
    score = 0
    tips = []

    if len(password) >= 8:
        score += 1
    else:
        tips.append("😡 Use at least 8 characters.")

    if any(c.isupper() for c in password):
        score += 1
    else:
        tips.append("😠 Include at least one uppercase letter.")

    if any(c.islower() for c in password):
        score += 1
    else:
        tips.append("☹️ Include at least one lowercase letter.")

    if any(c.isdigit() for c in password):
        score += 1
    else:
        tips.append("🙂 Include at least one digit (0-9).")

    if any(c in "@!#$&*" for c in password):
        score += 1
    else:
        tips.append("🤩 Include a special character (@!#$&*).")

    return score, tips

def main():
    st.title("🔐 Password Strength Meter")
    password = st.text_input("🗝 Enter password", type="password")

    if password:
        score, tips = check_password(password)

        if score == 5:
            st.success("✅ Strong Password! Secure and Safe.")
        elif score in [3, 4]:
            st.warning("🚫 Moderate Password! Improve it.")
        else:
            st.error("❌ Weak Password! Follow these steps:")
            for tip in tips:
                st.write(tip)

if __name__ == "__main__":
    main()
