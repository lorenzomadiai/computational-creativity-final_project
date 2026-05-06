# Research-Project-COCONUT
# AI Meme Generator — Co-Creative Meme Generation with GPT-2 and BLIP

Artificial Intelligence project focused on automated meme generation using pre-trained language and vision-language models.  
The project explores co-creative AI systems capable of generating humorous, context-aware memes from images through the integration of GPT-2, BLIP, prompt engineering, and multimodal learning. :contentReference[oaicite:0]{index=0}

## Team

- Jerry Poovakkottu
- Luca Girotti
- Lorenzo Madiai
- Virginia Samez

---

# Project Overview

The project investigates how AI systems can act as co-creative partners in meme creation by combining:
- image understanding,
- natural language generation,
- humor generation,
- human-guided interaction.

Two different approaches were developed and compared:
1. GPT-2 based meme generation with prompt engineering
2. Fine-tuned BLIP model for context-aware meme captioning

The objective was to evaluate the effectiveness, creativity, and humor quality of both approaches while analyzing the trade-offs between automation and human-AI collaboration.

---

# Approach 1 — GPT-2 Meme Generation

The first system combines:
- image captioning,
- prompt engineering,
- GPT-2 text generation.

## Workflow

1. The user uploads an image through a Streamlit interface
2. BLIP generates an image description
3. A custom prompt is constructed
4. GPT-2 generates a humorous meme caption
5. The caption is overlaid on the image

The prompts were designed to encourage:
- sarcastic humor,
- concise captions,
- dark-humor meme generation,
- contextual creativity.

This approach offers strong user interaction since users can directly influence meme generation through prompt customization. :contentReference[oaicite:1]{index=1}

---

# Approach 2 — Fine-Tuned BLIP Model

The second approach focuses on fine-tuning a pre-trained BLIP model using a meme dataset containing:
- 6992 labeled meme images,
- emotional labels,
- meme categories,
- humorous annotations. :contentReference[oaicite:2]{index=2}

## Pipeline

- Dataset preprocessing
- Image-text tokenization
- BLIP fine-tuning
- Caption generation on unseen meme templates

The fine-tuned model demonstrated improved:
- contextual understanding,
- humor quality,
- visual relevance,
- meme consistency.

Compared to GPT-2, this approach produced captions more strongly aligned with image content.

---

# Evaluation

The systems were evaluated through:
- qualitative analysis,
- user feedback,
- Instagram-based surveys,
- engagement metrics.

An Instagram page was created to publish generated memes and collect:
- likes,
- comments,
- poll preferences,
- audience reactions.

Results showed that the fine-tuned BLIP model achieved:
- higher engagement,
- more positive comments,
- better humor perception,
- stronger contextual relevance. :contentReference[oaicite:3]{index=3}

---

# Technologies

- Python
- GPT-2
- BLIP (Bootstrapped Language-Image Pretraining)
- Hugging Face Transformers
- Streamlit
- PyTorch
- Image Captioning
- Multimodal AI
