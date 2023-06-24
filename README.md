# Sentiment Analysis App

This API provides sentiment analysis for text inputs using a pre-trained machine learning model.

## Requirements

- Python 3.x
- Django
- Django Rest Framework
- Transformers

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/ShahAman/sentiment-analysis-api.git
   ```

2. Change into the project directory:
   ```bash
   cd sentiment-analysis-api
   ```

3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Run the Django development server:
   ```bash
   python manage.py runserver
   ```

2. The API will be accessible at `http://localhost:8000/api/analyze/`.

3. Send a POST request to the `/analyze` endpoint with a JSON payload containing the `text` parameter:
   ```bash
   curl -X POST -H "Content-Type: application/json" -d '{"text": "I love this product!"}' http://localhost:8000/api/analyze/
   ```

4. The API will respond with a JSON object containing the sentiment analysis result:
   ```json
   {
     "sentiment": "positive"
   }
   ```

## Customization

- To change the port on which the API runs, modify the `runserver` command in the `manage.py` file.
- You can modify the sentiment analysis model by changing the `model_name` variable in `sentiment/views.py`.
- Additional customization options are available in Django and Django Rest Framework. Refer to their documentation for more details.

## License

This project is licensed under the MIT License. Feel free to use and modify it for your own purposes.

## Credits

- The sentiment analysis model used in this API is provided by [StatsGary](https://huggingface.co/StatsGary/setfit-ft-sentinent-eval).
- This project was developed by [Shahnewaz](https://github.com/ShahAman).

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.
