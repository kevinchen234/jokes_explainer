import streamlit as st
import openai
import os
from openai import OpenAI

token = os.environ["GITHUB_TOKEN"]
endpoint = "https://models.inference.ai.azure.com"
model_name = "gpt-4o-mini"

client = OpenAI(
    base_url=endpoint,
    api_key=token,
)


# Streamlit app title
st.title("Joke Explainer")

# Text box for user to input a joke
joke_input = st.text_area("Enter your joke here:")

# Submit button
if st.button("Submit"):
    if joke_input:
        # Call the OpenAI API to get the explanation
        try:
            response = client.chat.completions.create(
                messages=[
                    {
                        "role": "user",
                        "content": f"Explain this joke: {joke_input}",
                    }
                ],
                model="gpt-4o-mini",
            )

            explanation = response.choices[0].message.content
            # Display the explanation
            st.subheader("Explanation")
            st.write(explanation)
        except Exception as e:
            st.error(f"An error occurred: {e}")
    else:
        st.warning("Please enter a joke before submitting.")
