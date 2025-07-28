import streamlit as st
from google import genai
from google.genai import types
from apikeys import gemini_api_key, openai_api_key
import openai

st.set_page_config(page_title="ThinkType", page_icon="🤖", layout="wide")
st.title("🤖 ThinkType: Your Personalized AI Blog Companion")
st.subheader("Generate engaging, high-quality blogs with relevant images using AI.")

st.sidebar.title("ThinkType Settings")
st.sidebar.markdown("Provide the inputs below:")

blog_title = st.sidebar.text_input("📝 Blog Title", placeholder="Enter your blog title")
keywords = st.sidebar.text_area("🔑 Keywords", placeholder="Enter comma-separated keywords")
num_words = st.sidebar.slider("✍️ Blog Length (in words)", min_value=100, max_value=1000, value=300, step=100)
num_images = st.sidebar.number_input("🖼️ Number of Images", min_value=0, max_value=3, value=1, step=1)
submit_button = st.sidebar.button("🚀 Generate Blog")

def generate_blog_content(title, keywords, word_count):
    client = genai.Client(api_key=gemini_api_key)
    model = "gemini-2.5-pro"
    prompt = f"""
    Write a high-quality blog article on the topic '{title}' using the keywords: {keywords}.
    The article should be approximately {word_count} words long, original, informative, and engaging.
    Maintain a professional tone throughout.
    """

    contents = [types.Content(role="user", parts=[types.Part.from_text(text=prompt)])]
    tools = [types.Tool(googleSearch=types.GoogleSearch())]

    config = types.GenerateContentConfig(
        thinking_config=types.ThinkingConfig(thinking_budget=-1),
        tools=tools
    )

    blog_text = ""
    for chunk in client.models.generate_content_stream(
        model=model, contents=contents, config=config
    ):
        blog_text += chunk.text
    return blog_text

def generate_images(prompt, n):
    openai_client = openai.OpenAI(api_key=openai_api_key)
    image_urls = []
    for i in range(n):
        response = openai_client.images.generate(
            model="dall-e-3",
            prompt=prompt,
            n=1,
            size="1024x1024",
            quality="standard"
        )
        image_urls.append(response.data[0].url)
    return image_urls

if submit_button:
    if not blog_title or not keywords:
        st.warning("⚠️ Please enter both blog title and keywords.")
    else:
        st.info(f"Generating blog for **{blog_title}** using keywords: `{keywords}`")
        with st.spinner("🧠 Generating blog content using Gemini..."):
            blog_output = generate_blog_content(blog_title, keywords, num_words)
        
        st.success("✅ Blog content generated!")

        st.markdown("### 📄 Generated Blog:")
        st.markdown(blog_output)

        if num_images > 0:
            with st.spinner("🎨 Generating image(s) using DALL·E 3..."):
                try:
                    image_prompt = f"Blog titled '{blog_title}' with keywords: {keywords}"
                    image_urls = generate_images(image_prompt, num_images)
                    for i, url in enumerate(image_urls):
                        st.image(url, caption=f"Generated Image {i+1}", use_column_width=True)
                except Exception as e:
                    st.error(f"⚠️ Image generation failed: {e}")
