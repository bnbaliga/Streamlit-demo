import streamlit as st

conditions = {
    "More than 10 characters": lambda pwd: len(pwd) > 10,
    "At least 1 digit": lambda pwd: any(char.isdigit() for char in pwd),
    "At least 1 upper char": lambda pwd: any(char.isupper() for char in pwd),
    "At least 1 lower char": lambda pwd: any(char in "!@#$%^&*()-_=+[]{}|;:'\",.<>?/`~" for char in pwd),
}

st.title("Password Strength Checker")
password = st.text_input("Enter your password:", type="password")


#def check_password(password):
 #   results = {}
  #  for condition, func in conditions.items():
   #     results[condition] = func(password)
   # return results

#st.button("Check Password", on_click=check_password(password))
def get_password_properties(password):
    return {cond: check(password) for cond, check in conditions.items()}

if st.button("Check password"):
    if password:
        properties = get_password_properties(password)

        # Loop through password conditions and show the status for each
        for condition, passes in properties.items():
            if passes:
                st.success(f'✔ Pass: {condition}')
            else:
                st.error(f'✖ Fail: {condition}')
    else:
        st.error("Please enter a password.")



