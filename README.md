# youtube-sentiment-analysis
this program is about to gather comments sentiment for good, netural and bad


# YouTube Comment Sentiment Analyzer

An application that extracts comments from a YouTube video and performs sentiment analysis on them to categorize them as "Good," "Bad," or "Neutral."

## Table of Contents

- [Overview](#overview)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [How it Works](#how-it-works)
- [Screenshots](#screenshots)
- [Contributing](#contributing)
- [License](#license)

## Overview

The YouTube Comment Sentiment Analyzer is a web application built with Flask that allows you to analyze comments on a YouTube video. It retrieves comments using the YouTube API, performs sentiment analysis on each comment, and visualizes the results in a bar chart.

## Prerequisites

- Python 3.x
- Flask
- TextBlob
- Google API credentials
- Matplotlib

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/your-repo.git


Obtain Google API credentials and replace 'use your google api key' in the code with your API key file path.

Usage
Run the application:

bash
Copy code
python your_app_file.py
Open a web browser and access the application at http://localhost:5000.

Enter the URL of the YouTube video you want to analyze.

Click the "Analyze" button to perform sentiment analysis on the comments.

How it Works
The application retrieves comments from a YouTube video using the YouTube API.
It performs sentiment analysis on each comment to determine whether it's "Good," "Bad," or "Neutral."
The results are visualized in a bar chart using Matplotlib.

Contributing
If you'd like to contribute to this project, please follow the standard GitHub fork and pull request workflow.

License
This project is licensed under the MIT License. See the LICENSE file for details.
