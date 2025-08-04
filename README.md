# ThinkType: Your Personalized AI Blog Companion
ThinkType is a user-friendly Streamlit web application that enables users to generate **high-quality, SEO-friendly blog content along with relevant AI-generated images**. It leverages **Google Gemini 2.5 Pro** for content generation and **OpenAI's DALL·E 3** for visual imagery creation.

##  Features
* Generate personalized blog content using Google Gemini Pro.
* Input your blog title, keywords, and desired word count.
* Add AI-generated images based on blog context using DALL·E 3.
* Simple, interactive sidebar for custom inputs.
* Clean and responsive UI built with Streamlit.

##  Tech Stack
* **Frontend/UI:** Streamlit
* **Text Generation:** Google Gemini 2.5 Pro (via google.genai)
* **Image Generation:** OpenAI DALL·E 3
* **API Integration:** Google Generative AI, OpenAI

## Create a virtual environment (optional but recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```
Install the required packages: 
```bash
pip install -r requirements.txt
```

## Set up API Keys
Edit a file named apikeys.py in the root directory and add your API keys:
```bash
# apikeys.py
gemini_api_key = "your_gemini_api_key"
openai_api_key = "your_openai_api_key"
```

## Usage
Run the Streamlit app locally:
```bash
streamlit run app.py
```

## Example Inputs
* Blog Title: The Future of Renewable Energy
* Keywords: solar power, wind energy, sustainability
* Word Count: 300–1000 words
* Images: Up to 3 images

## Important Notes
* Ensure you have valid API keys for both Gemini and OpenAI.
* Internet access is required for both content and image generation.
* API usage may incur costs based on your provider’s pricing.

## Sample Input and Output:
<img width="1906" height="976" alt="image" src="https://github.com/user-attachments/assets/1ae3f43c-58f8-4d83-abea-fa935729e432" />
<img width="1911" height="983" alt="image" src="https://github.com/user-attachments/assets/8abf9ded-49af-4acf-8e63-225ade7b1309" />
<img width="1914" height="982" alt="image" src="https://github.com/user-attachments/assets/adbc9976-0abc-4d64-8952-c1d74cfb5360" />





