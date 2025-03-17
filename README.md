# Jokes Explainer

This app explains jokes that the user inputs and explains the reasoning and understanding of the joke via Language Learning Model. Here, this app is using OpenAI's GPT-4o-Mini LLM.

## How It Works

1. **User Input**: The user enters a joke into the text box provided in the app.
2. **Submit Button**: The user clicks the "Submit" button to send the joke for explanation.
3. **API Call**: The app sends the joke to the OpenAI API, specifically to the GPT-4o-Mini model, asking it to explain the joke.
4. **Explanation**: The API returns an explanation of the joke, which is then displayed on the app.

## Technologies Used

- **Streamlit**: A framework used to create the web app interface.
- **OpenAI**: The service providing the language model used to explain the jokes.
- **Python**: The programming language used to build the app.

## Setup Instructions

1. **Clone the repository**:
    ```sh
    git clone <repository-url>
    cd jokes_explainer
    ```

2. **Install the required packages**:
    ```sh
    pip install -r requirements.txt
    ```

3. **Set up environment variables**:
    - Create a `.env` file in the root directory of the project.
    - Add your OpenAI API key to the `.env` file:
        ```
        GITHUB_TOKEN=your_openai_api_key
        ```

4. **Run the app**:
    ```sh
    streamlit run [jokes_explainer.py](http://_vscodecontentref_/1)
    ```

## Usage

- Open the app in your browser.
- Enter a joke in the text box.
- Click the "Submit" button.
- Read the explanation provided by the app.

## Example

1. **Input**: "Why don't scientists trust atoms? Because they make up everything!"
2. **Output**: The app will explain that the joke is a play on words, as "make up" can mean both "to form" and "to lie".

## Troubleshooting

- Ensure that your OpenAI API key is correctly set in the environment variables.
- Check your internet connection if the app is unable to reach the OpenAI API.

## Contributing

Feel free to submit issues or pull requests if you have suggestions for improvements or find any bugs.

## License

This project is licensed under the MIT License.

