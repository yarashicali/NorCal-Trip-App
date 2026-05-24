import streamlit as st
from supabase import create_client, Client

# Streamlit automatically fetches these from the cloud settings you just saved
url: str = st.secrets["SUPABASE_URL"]
key: str = st.secrets["SUPABASE_KEY"]

# intialize your Supabase connection
supabase: Client = create_client(url, key)

st.sucess("Successfully connected to Supabase using Cloud Secrets")

st.set_page_config(page_title="Vacation Planner", page_icon="✈️", layout="wide")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700;900&family=Lato:wght@300;400;700&display=swap');
html, body, [class*="css"] { font-family: 'Lato', sans-serif; }
.stApp {
    background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
    background-size: 400% 400%;
    animation: gradientShift 12s ease infinite;
    color: #f0ece2;
}
@keyframes gradientShift {
    0%   { background-position: 0% 50%; }
    50%  { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}
.travel-scene { display:flex; justify-content:center; padding:2.5rem 1rem 0; animation:fadeDown 1s ease both; }
.travel-scene svg { max-width:820px; width:100%; }
.hero { text-align:center; padding:1.2rem 1rem 2rem; animation:fadeDown 1s ease both; }
@keyframes fadeDown {
    from { opacity:0; transform:translateY(-30px); }
    to   { opacity:1; transform:translateY(0); }
}
.hero-tag { font-family:'Lato',sans-serif; font-weight:300; font-size:0.85rem; letter-spacing:0.35em; text-transform:uppercase; color:#f4a261; margin-bottom:0.6rem; }
.hero h1  { font-family:'Playfair Display',serif; font-size:clamp(2.4rem,6vw,4.2rem); font-weight:900; line-height:1.1; color:#fff; margin:0 0 1rem; }
.hero h1 span { color:#f4a261; }
.hero-sub { 
    font-size:1.15rem; 
    font-weight:300; 
    color:#cdd9e1; 
    max-width:620px; 
    margin:0 auto 2rem; 
    line-height:1.7;
    text-align:center;
    display:block;
}
.divider  { width:60px; height:3px; background:#f4a261; margin:0 auto 2.5rem; border-radius:2px; }
.cards-row { display:flex; gap:1.2rem; flex-wrap:wrap; justify-content:center; padding:0 1rem 2.5rem; animation:fadeUp 1s ease 0.3s both; }
@keyframes fadeUp {
    from { opacity:0; transform:translateY(30px); }
    to   { opacity:1; transform:translateY(0); }
}
.card { background:rgba(255,255,255,0.06); border:1px solid rgba(255,255,255,0.12); border-radius:16px; padding:1.8rem 1.5rem; width:220px; text-align:center; backdrop-filter:blur(8px); transition:transform 0.25s,border-color 0.25s; }
.card:hover { transform:translateY(-6px); border-color:#f4a261; }
.card-icon  { font-size:2.4rem; margin-bottom:0.7rem; }
.card-title { font-family:'Playfair Display',serif; font-size:1.05rem; font-weight:700; color:#fff; margin-bottom:0.5rem; }
.card-desc  { font-size:0.85rem; color:#b0bec5; line-height:1.6; }
.body-section { max-width:800px; margin:0 auto 3rem; padding:0 1.5rem; animation:fadeUp 1s ease 0.5s both; }
.body-section h2 { font-family:'Playfair Display',serif; font-size:1.9rem; color:#fff; margin-bottom:1rem; }
.body-section p  { font-size:1rem; font-weight:300; color:#cdd9e1; line-height:1.85; margin-bottom:1rem; }
.highlight { color:#f4a261; font-weight:700; }
.stats-strip { display:flex; justify-content:center; gap:3rem; flex-wrap:wrap; padding:2rem 1rem; border-top:1px solid rgba(255,255,255,0.1); border-bottom:1px solid rgba(255,255,255,0.1); margin-bottom:3rem; animation:fadeUp 1s ease 0.6s both; }
.stat { text-align:center; }
.stat-number { font-family:'Playfair Display',serif; font-size:2.2rem; font-weight:900; color:#f4a261; }
.stat-label  { font-size:0.78rem; letter-spacing:0.2em; text-transform:uppercase; color:#90a4ae; }
.footer { text-align:center; padding:1.5rem; font-size:0.78rem; color:#546e7a; letter-spacing:0.1em; }
</style>
""", unsafe_allow_html=True)

# Travel illustration
st.markdown("""
<div class="travel-scene">
<svg viewBox="0 0 820 200" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="sky" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#1a3a5c"/>
      <stop offset="100%" stop-color="#2c6e8a"/>
    </linearGradient>
    <linearGradient id="ground_g" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#1e4d3b"/>
      <stop offset="100%" stop-color="#163628"/>
    </linearGradient>
    <linearGradient id="road_g" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#3a3a4a"/>
      <stop offset="100%" stop-color="#2a2a38"/>
    </linearGradient>
  </defs>
  <!-- Sky -->
  <rect x="0" y="0" width="820" height="155" fill="url(#sky)" rx="16"/>
  <!-- Clouds -->
  <ellipse cx="120" cy="38" rx="38" ry="14" fill="#e8f4f8" opacity="0.18"/>
  <ellipse cx="145" cy="32" rx="28" ry="12" fill="#e8f4f8" opacity="0.22"/>
  <ellipse cx="95"  cy="40" rx="22" ry="10" fill="#e8f4f8" opacity="0.15"/>
  <ellipse cx="670" cy="45" rx="42" ry="14" fill="#e8f4f8" opacity="0.16"/>
  <ellipse cx="698" cy="38" rx="30" ry="12" fill="#e8f4f8" opacity="0.20"/>
  <ellipse cx="645" cy="47" rx="24" ry="10" fill="#e8f4f8" opacity="0.13"/>
  <!-- Stars -->
  <circle cx="300" cy="22" r="1.5" fill="#fff" opacity="0.6"/>
  <circle cx="380" cy="14" r="1.2" fill="#fff" opacity="0.5"/>
  <circle cx="460" cy="28" r="1.5" fill="#fff" opacity="0.55"/>
  <circle cx="540" cy="16" r="1.0" fill="#fff" opacity="0.45"/>
  <circle cx="200" cy="18" r="1.2" fill="#fff" opacity="0.5"/>
  <circle cx="620" cy="22" r="1.4" fill="#fff" opacity="0.6"/>
  <!-- Moon -->
  <circle cx="740" cy="35" r="16" fill="#f9e8b0" opacity="0.85"/>
  <circle cx="748" cy="30" r="13" fill="#2c6e8a" opacity="0.75"/>
  <!-- Ground -->
  <rect x="0" y="148" width="820" height="52" fill="url(#ground_g)"/>
  <rect x="0" y="193" width="820" height="7"  fill="#163628"/>
  <!-- Road -->
  <rect x="0" y="158" width="820" height="35" fill="url(#road_g)"/>
  <rect x="30"  y="173" width="55" height="5" fill="#f4a261" opacity="0.55" rx="2"/>
  <rect x="120" y="173" width="55" height="5" fill="#f4a261" opacity="0.55" rx="2"/>
  <rect x="210" y="173" width="55" height="5" fill="#f4a261" opacity="0.55" rx="2"/>
  <rect x="300" y="173" width="55" height="5" fill="#f4a261" opacity="0.55" rx="2"/>
  <rect x="390" y="173" width="55" height="5" fill="#f4a261" opacity="0.55" rx="2"/>
  <rect x="480" y="173" width="55" height="5" fill="#f4a261" opacity="0.55" rx="2"/>
  <rect x="570" y="173" width="55" height="5" fill="#f4a261" opacity="0.55" rx="2"/>
  <rect x="660" y="173" width="55" height="5" fill="#f4a261" opacity="0.55" rx="2"/>
  <rect x="750" y="173" width="55" height="5" fill="#f4a261" opacity="0.55" rx="2"/>
  <!-- Trees left (park) -->
  <rect x="42" y="118" width="7" height="32" fill="#5a3e28"/>
  <ellipse cx="45" cy="108" rx="20" ry="22" fill="#2d7a3a"/>
  <ellipse cx="45" cy="100" rx="14" ry="16" fill="#37a348"/>
  <rect x="76" y="122" width="6" height="28" fill="#5a3e28"/>
  <ellipse cx="79" cy="112" rx="17" ry="19" fill="#2d7a3a"/>
  <ellipse cx="79" cy="104" rx="12" ry="14" fill="#37a348"/>
  <rect x="54"  y="142" width="32" height="4" fill="#8b6640" rx="2"/>
  <rect x="56"  y="138" width="4"  height="8" fill="#7a5530" rx="1"/>
  <rect x="80"  y="138" width="4"  height="8" fill="#7a5530" rx="1"/>
  <circle cx="35"  cy="148" r="3" fill="#f4a261"/>
  <circle cx="32"  cy="145" r="2" fill="#f9c784"/>
  <circle cx="100" cy="147" r="3" fill="#e07070"/>
  <circle cx="103" cy="144" r="2" fill="#f4a261"/>
  <!-- BUS -->
  <rect x="185" y="125" width="130" height="48" fill="#f4a261" rx="6"/>
  <rect x="190" y="118" width="120" height="12" fill="#e07a30" rx="4"/>
  <rect x="196" y="128" width="22" height="16" fill="#bfe8f5" rx="3" opacity="0.9"/>
  <rect x="224" y="128" width="22" height="16" fill="#bfe8f5" rx="3" opacity="0.9"/>
  <rect x="252" y="128" width="22" height="16" fill="#bfe8f5" rx="3" opacity="0.9"/>
  <rect x="280" y="128" width="22" height="16" fill="#bfe8f5" rx="3" opacity="0.9"/>
  <rect x="296" y="140" width="16" height="33" fill="#d4863a" rx="2"/>
  <rect x="186" y="140" width="9"  height="22" fill="#e07a30" rx="2"/>
  <circle cx="190" cy="164" r="4" fill="#fff9c4" opacity="0.9"/>
  <circle cx="215" cy="175" r="13" fill="#2a2a38"/>
  <circle cx="215" cy="175" r="7"  fill="#555"/>
  <circle cx="215" cy="175" r="3"  fill="#888"/>
  <circle cx="285" cy="175" r="13" fill="#2a2a38"/>
  <circle cx="285" cy="175" r="7"  fill="#555"/>
  <circle cx="285" cy="175" r="3"  fill="#888"/>
  <rect x="196" y="119" width="80" height="8" fill="#1a1a2e" rx="2"/>
  <text x="236" y="126" text-anchor="middle" fill="#f4a261" font-size="6" font-family="Lato,sans-serif" font-weight="700">VACATION EXPRESS</text>
  <!-- PLANE -->
  <ellipse cx="420" cy="68" rx="72" ry="18" fill="#e8f0f8"/>
  <ellipse cx="488" cy="68" rx="14" ry="12" fill="#d0dce8"/>
  <polygon points="352,68 340,44 365,60" fill="#c8d8e8"/>
  <polygon points="395,70 450,70 470,95 340,88" fill="#d0dce8"/>
  <polygon points="360,68 340,60 340,76" fill="#c0ccd8"/>
  <circle cx="430" cy="64" r="5" fill="#bfe8f5" opacity="0.85"/>
  <circle cx="445" cy="64" r="5" fill="#bfe8f5" opacity="0.85"/>
  <circle cx="460" cy="64" r="5" fill="#bfe8f5" opacity="0.85"/>
  <circle cx="475" cy="64" r="5" fill="#bfe8f5" opacity="0.85"/>
  <rect x="355" y="66" width="130" height="5" fill="#f4a261" opacity="0.7" rx="2"/>
  <ellipse cx="420" cy="88" rx="18" ry="7" fill="#b0bcc8"/>
  <ellipse cx="440" cy="88" rx="18" ry="7" fill="#b0bcc8"/>
  <line x1="350" y1="68" x2="290" y2="62" stroke="#fff" stroke-width="2.5" opacity="0.25" stroke-linecap="round"/>
  <line x1="350" y1="72" x2="285" y2="68" stroke="#fff" stroke-width="1.5" opacity="0.18" stroke-linecap="round"/>
  <!-- CAR -->
  <rect x="530" y="148" width="130" height="28" fill="#4e8ecb" rx="5"/>
  <rect x="548" y="130" width="90"  height="22" fill="#5a9ed8" rx="8"/>
  <rect x="554" y="133" width="30" height="16" fill="#bfe8f5" rx="3" opacity="0.9"/>
  <rect x="590" y="133" width="30" height="16" fill="#bfe8f5" rx="3" opacity="0.9"/>
  <rect x="627" y="133" width="8"  height="16" fill="#3a7ab8" rx="2"/>
  <rect x="546" y="133" width="8"  height="16" fill="#3a7ab8" rx="2"/>
  <circle cx="658" cy="162" r="5" fill="#fff9c4" opacity="0.9"/>
  <rect x="532" y="156" width="8" height="8" fill="#e07070" rx="1" opacity="0.85"/>
  <rect x="654" y="154" width="8" height="14" fill="#2c5e9a" rx="2"/>
  <circle cx="560" cy="177" r="13" fill="#1e1e2e"/>
  <circle cx="560" cy="177" r="7"  fill="#444"/>
  <circle cx="560" cy="177" r="3"  fill="#777"/>
  <circle cx="635" cy="177" r="13" fill="#1e1e2e"/>
  <circle cx="635" cy="177" r="7"  fill="#444"/>
  <circle cx="635" cy="177" r="3"  fill="#777"/>
  <!-- Trees right -->
  <rect x="736" y="120" width="7" height="30" fill="#5a3e28"/>
  <ellipse cx="739" cy="110" rx="20" ry="22" fill="#2d7a3a"/>
  <ellipse cx="739" cy="102" rx="14" ry="16" fill="#37a348"/>
  <rect x="768" y="124" width="6" height="26" fill="#5a3e28"/>
  <ellipse cx="771" cy="114" rx="17" ry="19" fill="#2d7a3a"/>
  <ellipse cx="771" cy="106" rx="12" ry="14" fill="#37a348"/>
  <circle cx="722" cy="148" r="3" fill="#e07070"/>
  <circle cx="719" cy="145" r="2" fill="#f4a261"/>
  <circle cx="784" cy="147" r="3" fill="#f4a261"/>
  <circle cx="787" cy="144" r="2" fill="#f9c784"/>
</svg>
</div>
""", unsafe_allow_html=True)

# Hero
st.markdown("""
<div class="hero">
    <div class="hero-tag">Your AI-Powered Group Travel Hub</div>
    <h1>Hello, Welcome to the<br><span>Vacation Planner</span></h1>
    <p class="hero-sub">
        Stop scrolling & drowning in group chats and tangled spreadsheets.
        Plan smarter, travel together, and let AI do the heavy lifting.
    </p>
    <div class="divider"></div>
</div>
""", unsafe_allow_html=True)

# Feature cards
st.markdown("""
<div class="cards-row">
    <div class="card">
        <div class="card-icon">💡</div>
        <div class="card-title">Brainstorm Together</div>
        <div class="card-desc">Drop ideas, links, and recommendations into one shared live feed.</div>
    </div>
    <div class="card">
        <div class="card-icon">🎯</div>
        <div class="card-title">Vibe Matching</div>
        <div class="card-desc">Answer 3 quick questions and let the AI balance every traveller's style.</div>
    </div>
    <div class="card">
        <div class="card-icon">🗺️</div>
        <div class="card-title">AI Itinerary</div>
        <div class="card-desc">One click generates a geo-optimised daily plan your whole crew will love.</div>
    </div>
    <div class="card">
        <div class="card-icon">🧾</div>
        <div class="card-title">Receipt Scanner</div>
        <div class="card-desc">Snap a receipt and let AI split expenses instantly — no awkward maths.</div>
    </div>
</div>
""", unsafe_allow_html=True)

# Stats
st.markdown("""
<div class="stats-strip">
    <div class="stat"><div class="stat-number">4</div><div class="stat-label">Smart Features</div></div>
    <div class="stat"><div class="stat-number">&#8734;</div><div class="stat-label">Trip Ideas</div></div>
    <div class="stat"><div class="stat-number">0</div><div class="stat-label">Spreadsheets Needed</div></div>
    <div class="stat"><div class="stat-number">100%</div><div class="stat-label">Group Harmony</div></div>
</div>
""", unsafe_allow_html=True)

# Body copy
st.markdown("""
<div class="body-section">
    <h2>Why this planner is different</h2>
    <p>Group travel should be exciting, not exhausting. Yet most trips start the same way — a flurry of
    messages across three different apps, a half-finished Google Doc nobody can find, and a spreadsheet
    that is out of date before the plane even lands. <span class="highlight">We built this app to fix that.</span></p>
    <p>At its core, the Vacation Planner is a <span class="highlight">real-time collaborative workspace</span>
    powered by cutting-edge AI. Every idea your group drops into the Brainstorming Feed is instantly
    visible to everyone. The Vibe Checker profiles each traveller's preferences — pace, interests,
    sleep schedule — and feeds those insights directly to the AI Itinerary Generator, which produces
    a day-by-day plan that genuinely balances conflicting wishes.</p>
    <p>Worried about splitting the bill? The <span class="highlight">Vision-Based Receipt Scanner</span>
    uses GPT-4o to read any photo of a receipt, extract the totals, and instantly update a shared
    ledger showing exactly who owes what. No more IOUs written on napkins.</p>
    <p>Everything runs on a secure, real-time database so changes made on a phone in the airport
    show up immediately on a laptop back home. Your API keys and credentials are never exposed —
    they live in encrypted environment variables, just the way they should.</p>
</div>
""", unsafe_allow_html=True)

# FAQ header
st.markdown("""
<div style="max-width:750px; margin:0 auto 1rem; padding:0 1.5rem; text-align:center;">
    <h2 style="font-family:'Playfair Display',serif; font-size:1.9rem; color:#fff; margin-bottom:0.3rem;">
        Frequently Asked Questions
    </h2>
    <div style="width:60px; height:3px; background:#f4a261; margin:0.5rem auto 1.8rem; border-radius:2px;"></div>
</div>
""", unsafe_allow_html=True)

faq_items = [
    ("🤔 Do I need a technical background to use this app?",
     "Not at all! The app is built with a simple, intuitive interface. "
     "If you can send a text message, you can use every feature here."),
    ("🔐 Is my data private and secure?",
     "Yes. The app uses encrypted environment variables for all API keys and credentials. "
     "Your trip data is stored in a private Supabase database accessible only to your group."),
    ("📱 Does it work on my phone?",
     "Absolutely. The layout is optimised for mobile viewports so you can add ideas, "
     "check the itinerary, and scan receipts right from your phone while you are on the go."),
    ("🤖 Which AI model powers the itinerary and receipt scanner?",
     "Itinerary generation uses OpenAI's GPT-4o-mini or GPT-4o for text synthesis, "
     "while the receipt scanner leverages GPT-4o's multimodal vision capabilities to read and interpret images."),
    ("👥 How many people can use the app at once?",
     "There is no hard limit. The real-time database syncs updates across all connected "
     "users instantly, making it great for groups of any size — from a couple to a large family reunion."),
    ("💸 Is the app free to use?",
     "The app itself is free and can be hosted at no cost on Streamlit Community Cloud. "
     "You will need your own OpenAI API key, which is billed per use — typical trip planning costs only a few cents."),
]

col1, col2, col3 = st.columns([1, 4, 1])
with col2:
    for question, answer in faq_items:
        with st.expander(question):
            st.write(answer)

# Footer
st.markdown("""
<div class="footer">
    &#9992;&#65039; Vacation Planner &nbsp;&middot;&nbsp; Built with Streamlit &amp; OpenAI &nbsp;&middot;&nbsp; Happy travels!
</div>
""", unsafe_allow_html=True)
