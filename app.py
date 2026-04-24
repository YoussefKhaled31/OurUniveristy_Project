from flask import Flask, render_template, request
from textblob import TextBlob

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    sentiment_result = None
    emoji = None
    user_text = ""

    if request.method == 'POST':
        user_text = request.form.get('user_text', '')
        
        if user_text.strip():
            analysis = TextBlob(user_text)
            polarity = analysis.sentiment.polarity
            
            if polarity > 0.1:
                sentiment_result = "Positive"
                emoji = "✨ 🟢"
            elif polarity < -0.1:
                sentiment_result = "Negative"
                emoji = "🌧️ 🔴"
            else:
                sentiment_result = "Neutral"
                emoji = "⚖️ ⚪"

    return render_template('index.html', sentiment=sentiment_result, emoji=emoji, text=user_text)

if __name__ == '__main__':
    app.run(debug=True)
