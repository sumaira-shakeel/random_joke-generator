# import streamlit as st
# import requests

# def get_random_joke():
#     """Fatch a random  joke from the API"""
#     try:
#         response = requests.get("https://official-joke-appspot.com/random_joke")
#         if response.status_code == 200:
#             joke_data = response.json()
#             return f"{joke_data['setup']}\n\n {joke_data['punchline']}"
#         else:
#             return "Failed to fetch a joke.please try again later!"
#     except Exception as e:
#         return "why did the programmer quite his job \n because he didn't get arrays"
# def main():
#     st.title("Random Joke Generator")
#     st.write("Click the button below to generate a random joke")
#     if st.button("Generate  a joke!"):
#         joke = get_random_joke()
#         st.success(joke)

# if __name__ == "__main__":
#     main()






import streamlit as st
import requests

def get_random_joke():
    """Fetch a random joke from the API"""
    try:
        response = requests.get("https://official-joke-api.appspot.com/random_joke")
        if response.status_code == 200:
            joke_data = response.json()
            return f"{joke_data['setup']}\n\n{joke_data['punchline']}"
        else:
            return "Failed to fetch a joke. Please try again later!"
    except Exception:
        return "Why did the programmer quit his job?\nBecause he didn't get arrays."

def main():
    st.title("Random Joke Generator")
    st.write("Click the button below to generate a random joke.")

    if st.button("Generate a Joke!"):
        joke = get_random_joke()
        st.success(joke)
    st.divider()
    st.markdown(
        """
    <div style='text-align:center;'>
        <p>Joke from official Joke Api</P>
        <p>Build with   ❤️  by  <a href='https://github.com/sumaira-shakeel'> Sumaira Shakeel</a> using streamlit</P>
    </div>
""",
unsafe_allow_html=True
    )    

if __name__ == "__main__":
    main()

    
