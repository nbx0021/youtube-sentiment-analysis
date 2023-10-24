from flask import Flask, render_template, request
from textblob import TextBlob
import googleapiclient.discovery
import matplotlib.pyplot as plt

app = Flask(__name__)

# Load the YouTube API client secrets
# Replace 'YOUR_API_KEY.json' with the path to your API credentials JSON file
api_key_file = 'use your api key'

# Create a YouTube API client
youtube = googleapiclient.discovery.build("youtube", "v3", developerKey=api_key_file)



def get_video_comments(video_id):
    comments = []
    next_page_token = None

    while True:
        results = youtube.commentThreads().list(
            part="snippet",
            videoId=video_id,
            textFormat="plainText",
            pageToken=next_page_token if next_page_token else ""
        ).execute()

        for item in results["items"]:
            comment = item["snippet"]["topLevelComment"]["snippet"]["textDisplay"]
            comments.append(comment)

        # Check if there is a next page token
        if 'nextPageToken' in results:
            next_page_token = results["nextPageToken"]
        else:
            break  # No more pages to fetch

    return comments


def analyze_comments(comments):
    good_comments = 0
    bad_comments = 0
    neutral_comments = 0

    for comment in comments:
        analysis = TextBlob(comment)
        polarity = analysis.sentiment.polarity

        if polarity > 0.1:
            good_comments += 1
        elif polarity < -0.1:
            bad_comments += 1
        else:
            neutral_comments += 1

    analysis_results = {
        'Good Comments': good_comments,
        'Bad Comments': bad_comments,
        'Neutral Comments': neutral_comments
    }

    return analysis_results

def plot_results(analysis_results):
    categories = list(analysis_results.keys())
    counts = list(analysis_results.values())

    plt.figure(figsize=(8, 6))
    plt.bar(categories, counts, color=['green', 'red', 'blue'])
    plt.xlabel('Categories')
    plt.ylabel('Counts')
    plt.title('Comment Analysis')

    plt.tight_layout()
    plt.savefig('static/analysis.png')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    video_url = request.form.get('video_url')
    video_id = video_url.split('v=')[1]

    comments = get_video_comments(video_id)
    analysis_results = analyze_comments(comments)
    plot_results(analysis_results)

    return render_template('results.html', analysis=analysis_results)

if __name__ == '__main__':
    app.run(debug=True)
