from flask import Flask, request, render_template
from transformers import pipeline

app = Flask(__name__)

# Initialize the summarization pipeline
summarizer = pipeline("summarization", model="t5-base")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/summarize', methods=['POST'])
def summarize():
    # Get the input text from the form
    article = request.form['article']

    # Perform summarization using the pipeline
    summary = summarizer(article, max_length=130, min_length=30, do_sample=False)

    # Render the summary template with the generated summary
    return render_template('summary.html', summary=summary[0]['summary_text'])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

