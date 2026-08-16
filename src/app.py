import gradio as gr
from predict import predict_spam

# Safety guidelines mapped by platform
SAFETY_TIPS = {
    "Email": ["📧 Check sender domain", "📧 Avoid links", "📧 Beware urgent language"],
    "SMS": ["📱 Do not reply unknown numbers", "📱 Avoid short links", "📱 Banks don't ask info via SMS"],
    "YouTube": ["🎥 Beware giveaway links", "🎥 Verify channel badge", "🎥 Report scam links"]
}

def analyze_message(text, platform):
    if not text.strip():
        return "<b>Please enter a message.</b>", ""
    
    # Get model prediction and metrics
    is_spam, confidence, ham_prob, spam_prob, highlighted_text = predict_spam(text)
    bg_card = "#fee2e2" if is_spam else "#dcfce7"
    status_label = "🚨 Spam Alert" if is_spam else "✅ Safe Message"
    
    # Generate UI HTML components
    result_html = f"<div style='background-color: {bg_card}; padding: 15px;'><h2>{status_label}</h2><p>Confidence: {confidence:.1f}%</p><div>{highlighted_text}</div></div>"
    tips = SAFETY_TIPS.get(platform, [])
    tips_html = "<ul>" + "".join([f"<li>{t}</li>" for t in tips]) + "</ul>"
    return result_html, tips_html

# Build Gradio Web Interface
with gr.Blocks(title="AI Spam Detector") as demo:
    gr.Markdown("# 🛡️ Spam Detector")
    platform = gr.Dropdown(choices=["Email", "SMS", "YouTube"], value="Email")
    text = gr.Textbox(lines=5)
    btn = gr.Button("Analyze")
    out1 = gr.HTML()
    out2 = gr.HTML()
    btn.click(fn=analyze_message, inputs=[text, platform], outputs=[out1, out2])

if __name__ == "__main__":
    demo.launch()
