# AI Agents Learning

This repository contains various projects and examples for learning AI agents using different frameworks and APIs, including OpenAI, Gemini, Hugging Face, LangGraph, Ollama, and more.

## Projects

### agent_sdk
Examples of building agents using the Agent SDK, including agents as tools for translation tasks.

### hello_world
Basic "Hello World" examples interacting with AI models:
- Using Google's Gemini API directly
- Using OpenAI client with Gemini models

### hugging_face
Integration with Hugging Face transformers for image-text-to-text tasks.

### image
Image captioning using OpenAI's vision-compatible models.

### langgraph
Building conversational chatbots using LangGraph for state management and graph-based workflows.

### ollama_fastapi
FastAPI server that uses Ollama for running local AI models, with a chat endpoint.

### prompt
Various prompting techniques for AI models:
- Automating Chain of Thought (CoT) prompting
- Few-shot prompting
- Persona prompting
- Zero-shot prompting
- Other prompt formatting styles

### rag
Retrieval-Augmented Generation (RAG) implementation using OpenAI embeddings and Qdrant vector database for document-based Q&A.

### rag_queues
RAG system with a queue-based architecture using RQ (Redis Queue) for handling requests asynchronously, including client, server, and worker components.

### voice_agent
Voice-based AI agent with speech recognition (using speech_recognition) and text-to-speech (TTS) capabilities.

### weather_agent
Weather information agent that fetches weather data and uses AI for responses.

## Setup

1. Clone the repository.
2. Install dependencies: `pip install -r requirements.txt`
3. Set up environment variables (e.g., API keys) as needed for each project.
4. Run individual projects by executing their main files (e.g., `python main.py` in each folder).

Note: Some projects require additional setup like Docker containers (e.g., Ollama, Qdrant) or API keys.