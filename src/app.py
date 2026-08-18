import streamlit as st
from predict import predict_spam

# Safety guidelines mapped by platform
SAFETY_TIPS = {
    "Email": ["📧 Check sender domain", "📧 Avoid links", "📧 Beware urgent language"],
    "SMS": ["📱 Do not reply unknown numbers", "📱 Avoid short links", "📱 Banks don't ask info via SMS"],
    "YouTube": ["🎥 Beware giveaway links", "🎥 Verify channel badge", "🎥 Report scam links"]
}

st.set_page_config(page_title="AI Spam Detector", page_icon="🛡️")

st.title("🛡️ AI Spam Detector")

platform = st.selectbox("Select Platform", ["Email", "SMS", "YouTube"])
text = st.text_area("Enter Message", height=150)

if st.button("Analyze"):
    if not text.strip():
        st.warning("Please enter a message.")
    else:
        is_spam, confidence, ham_prob, spam_prob, highlighted_text = predict_spam(text)
        
        if is_spam:
            st.error(f"🚨 Spam Alert (Confidence: {confidence:.1f}%)")
        else:
            st.success(f"✅ Safe Message (Confidence: {confidence:.1f}%)")
            
        st.markdown(highlighted_text, unsafe_allow_html=True)
        
        st.subheader("💡 Safety Tips")
        tips = SAFETY_TIPS.get(platform, [])
        for tip in tips:
            st.write(f"- {tip}")
