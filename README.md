# Simple ChatGPT 
## Introduction
Welcome to the Python Flask Server with OpenAI API project! This project provides a simple web interface to interact with OpenAI API. You can send a prompt to OpenAI API and get the response as text.

## Requirements
- Flask
- Requests

## How to run
- Clone the repository:
```
git clone https://github.com/[YOUR_GITHUB_USERNAME]/python-flask-openai.git
```
- Install the required packages:
```
pip install -r requirements.txt
```
- Run the app:
```
python app.py
```
## Endpoints
- `GET /`: The default endpoint displays an input field and a submit button. You can enter your prompt in the input field and click the submit button to send a POST request to the server.
- `POST /prompt`: This endpoint takes a string as input (sent as a prompt) and sends it to OpenAI API. The response from the API is returned as text.

## Author
Ahmad Sofwan

## License
This project is licensed under the [LICENSE_NAME] license.

## Acknowledgements
- OpenAI API for providing the AI text generation service
- Flask for building the web server

## Conclusion
This project is just a starting point to demonstrate the capabilities of OpenAI API. You can enhance this project by adding more functionality and making the UI more user-friendly. Happy coding!
