from flask import Flask, request, jsonify
from sentiment_analysis import predict_sentiment

app = Flask(__name__)


@app.route('/sentiment-analysis', methods=['POST'])
def predict():
    data = request.get_json()
    review = data.get('review', '')
    if not review:
        return jsonify({"error": "Review text is required"}), 400  
    sentiment = predict_sentiment(review) 
    if isinstance(sentiment, dict) and "Sentiment" in sentiment:
        return jsonify({"review": review, "sentiment": sentiment["Sentiment"]})
    else:
        return jsonify({"review": review, "sentiment": sentiment}), 500
    
if __name__ == '__main__':
    app.run(debug=True)

