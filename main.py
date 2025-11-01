import streamlit as st
from openai import OpenAI

OPENROUTER_API_KEY = "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"

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=OPENROUTER_API_KEY
)

st.set_page_config(page_title="Multi-Purpose LLM Tool", page_icon="🤖", layout="centered")

st.markdown(
    """
    <style>
        .main {
            background-color: #f9fafc;
        }
        .stButton > button {
            border-radius: 12px;
            height: 3em;
            width: 100%;
            font-weight: 600;
            font-size: 15px;
            background-color: #2e7df6;
            color: white;
            transition: all 0.2s ease-in-out;
        }
        .stButton > button:hover {
            background-color: #1e5dcc;
            transform: scale(1.02);
        }
        .stTextArea textarea {
            border-radius: 10px;
            border: 1.5px solid #ccc;
        }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("🤖 Multi-Purpose LLM Tool")
st.write("Nhập nội dung cần xử lý và chọn hành động bên dưới:")

# -----------------------------
# 📝 Nhập văn bản
# -----------------------------
user_input = st.text_area("✍️ Nhập văn bản:", height=200, placeholder="Nhập nội dung bạn muốn xử lý...")

st.markdown("---")

# -----------------------------
# 🎛️ Các nút chức năng
# -----------------------------
col1, col2, col3, col4, col5 = st.columns(5)

action = None
with col1:
    if st.button("📝 Tóm tắt"):
        action = "Tóm tắt nội dung sau đây:"
with col2:
    if st.button("🇫🇷 Dịch sang tiếng Pháp"):
        action = "Dịch sang tiếng Pháp nội dung sau đây:"
with col3:
    if st.button("🧒 Giải thích"):
        action = "Giải thích nội dung sau đây một cách đơn giản dễ hiểu cho trẻ em 5 tuổi:"
with col4:
    if st.button("🔑 Từ khóa"):
        action = "Trích xuất các từ khóa chính từ nội dung sau đây:"
with col5:
    if st.button("🐍 Tạo mã Python"):
        action = "Sinh mã Python cho yêu cầu sau đây:"

st.markdown("---")

# -----------------------------
# 🚀 Gửi yêu cầu đến OpenRouter
# -----------------------------
if action and user_input.strip():
    with st.spinner("⏳ Đang xử lý yêu cầu..."):
        try:
            response = client.chat.completions.create(
                model="meta-llama/llama-3.3-8b-instruct:free",
                messages=[
                    {"role": "system", "content": "Bạn là một trợ lý AI hữu ích, chính xác và nói tiếng Việt."},
                    {"role": "user", "content": f"{action}\n\n{user_input}"}
                ]
            )

            st.success("✅ Hoàn thành!")
            st.subheader("📘 Kết quả:")
            st.write(response.choices[0].message.content)

        except Exception as e:
            st.error(f"❌ Lỗi khi gọi API: {e}")
elif action and not user_input.strip():
    st.warning("⚠️ Vui lòng nhập nội dung trước khi chọn hành động.")

# -----------------------------
# 👣 Footer
# -----------------------------
st.markdown("---")
st.markdown(
    "<p style='text-align:center; color:gray;'>🚀 Xây dựng bởi OpenRouter API + Streamlit | Mô hình Meta: Llama 3.3 8B Instruct</p>",
    unsafe_allow_html=True

)

