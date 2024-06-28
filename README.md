# YouTube Transcript to Detailed Notes Converter

This Streamlit application takes a YouTube video URL, extracts its transcript, and uses Google's generative AI model, Gemini Pro, to summarize the transcript into detailed notes.

## Features

- **Load Environment Variables**: Uses `python-dotenv` to load necessary API keys and configurations from an `.env` file.
- **Transcript Extraction**: Utilizes `youtube_transcript_api` to fetch and compile the transcript of the given YouTube video.
- **Content Generation**: Leverages Google's generative AI, Gemini Pro, to summarize the transcript into a concise format.

## Prerequisites

Before you run this application, you need to have the following installed:
- Python 3.8 or later
- Streamlit
- python-dotenv
- `youtube_transcript_api` package
- Google's generativeai package
