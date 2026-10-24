
import streamlit as st
from pathlib import Path
from urllib.parse import quote
import base64
import html

st.set_page_config(
    page_title="Chaatwala | Indian Street Food",
    page_icon="🍛",
    layout="wide",
)

# ---------------- CONFIGURATION ----------------

BASE_DIR = Path(__file__).parent
IMAGE_DIR = BASE_DIR / "images"


def get_image(name):
    """Return a local image as a data URI, or None if missing."""
    path = IMAGE_DIR / name

    if not path.exists():
        return None

    mime = "image/png" if path.suffix.lower() == ".png" else "image/jpeg"
    encoded = base64.b64encode(path.read_bytes()).decode("utf-8")
    return f"data:{mime};base64,{encoded}"


# ---------------- STYLING ----------------

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Playfair+Display:wght@600;700;800&display=swap');

.stApp {
    background: #fff8ee;
    color: #352116;
    font-family: 'DM Sans', sans-serif;
}

.block-container {
    max-width: 1180px;
    padding-top: 1.5rem;
    padding-bottom: 2rem;
}

header[data-testid="stHeader"] {
    background: transparent;
}

h1, h2, h3 {
    font-family: 'Playfair Display', serif !important;
    color: #382117;
}

.hero {
    background: linear-gradient(
        90deg,
        rgba(38, 22, 13, 0.96) 0%,
        rgba(38, 22, 13, 0.78) 45%,
        rgba(38, 22, 13, 0.12) 100%
    );
    border-radius: 22px;
    min-height: 350px;
    padding: 48px 42px;
    display: flex;
    flex-direction: column;
    justify-content: center;
    color: #fff;
    overflow: hidden;
    background-position: center;
    background-size: cover;
}

.hero h1 {
    color: white !important;
    font-size: clamp(2.6rem, 5vw, 4.5rem);
    line-height: 1.1;
    margin: 12px 0;
}

.hero p {
    color: #f8e8d5;
    max-width: 490px;
    font-size: 1.05rem;
    line-height: 1.8;
}

.eyebrow {
    color: #ffbf69 !important;
    font-weight: 700;
    letter-spacing: 3px;
    font-size: 0.78rem;
}

.accent {
    color: #ffb44d;
}

.section-heading {
    font-family: 'Playfair Display', serif;
    font-size: 2.2rem;
    font-weight: 700;
    margin-bottom: 2px;
}

.section-subtitle {
    color: #826b5b;
    margin-bottom: 22px;
}

.feature {
    background: #fff;
    border: 1px solid #f0dfcd;
    padding: 19px;
    border-radius: 15px;
    min-height: 110px;
}

.feature-title {
    font-size: 1.05rem;
    font-weight: 700;
    margin-bottom: 5px;
}

.feature-desc {
    color: #826b5b;
    font-size: 0.9rem;
}

.menu-panel {
    background: rgba(255, 255, 255, 0.96);
    border: 1px solid #ead9c7;
    border-radius: 16px;
    padding: 18px;
    height: auto;
    min-height: 0;
    box-sizing: border-box;
    margin-bottom: 20px;
}

.menu-category {
    color: #b45b24;
    font-size: 12px;
    font-weight: 700;
    letter-spacing: 1px;
    margin-bottom: 6px;
}

.menu-name {
    font-family: 'Playfair Display', serif;
    font-size: 21px;
    font-weight: 700;
    margin-bottom: 12px;
    line-height: 1.3;
}

.dish-list {
    display: grid;
    grid-template-columns: 1fr;
    gap: 8px;
    color: #6c5748;
    font-size: 14px;
    line-height: 1.5;
}

.dish-item {
    overflow-wrap: anywhere;
    padding-bottom: 6px;
    border-bottom: 1px solid #f0e7dd;
}

.dish-item:last-child {
    border-bottom: none;
    padding-bottom: 0;
}

@media (min-width: 900px) {
    .dish-list {
        grid-template-columns: 1fr 1fr;
    }
}

@media (max-width: 700px) {
    .menu-panel {
        padding: 15px;
    }

    .menu-name {
        font-size: 19px;
    }
}

.contact-box {
    background: #382117;
    color: #fff;
    text-align: center;
    padding: 35px 20px;
    border-radius: 20px;
}

.contact-box h2 {
    color: white !important;
}

.contact-box p {
    color: #f4dfcc;
}

.contact-number {
    color: #ffbf69;
    font-size: 1.8rem;
    font-weight: 700;
}

.stButton > button,
.stLinkButton > a {
    border-radius: 10px;
    font-weight: 600;
}

div[data-testid="stImage"] img {
    border-radius: 14px;
}

hr {
    border-color: #ead9c7;
}

@media (max-width: 700px) {
    .hero {
        min-height: 300px;
        padding: 25px 20px;
    }

    .section-heading {
        font-size: 1.8rem;
    }

    .block-container {
        padding-left: 1rem;
        padding-right: 1rem;
    }
}
.stApp {
    background-color: #fff8ee;
    background-image:
        linear-gradient(
            rgba(255, 248, 238, 0.91),
            rgba(255, 248, 238, 0.94)
        ),
        url("images/website_background.png");
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
}


</style>
""", unsafe_allow_html=True)


# ---------------- WEBSITE BACKGROUND ----------------

website_background = get_image("website_background.png")

if website_background:
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image:
                linear-gradient(
                    rgba(255, 248, 238, 0.86),
                    rgba(255, 248, 238, 0.90)
                ),
                url("{website_background}");

            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}
        </style>
        """,
        unsafe_allow_html=True,
    )
else:
    st.warning(
        "Background image not found. Check images/website_background.jpg"
    )

# ---------------- MENU ----------------

MENU = {
    "Chaat": [
        "Pani Puri", "Sev Batata Puri", "Dahi Batata Puri",
        "Bhel Puri Sukha / Geela", "Aloo Bomb", "Cucumber Bomb",
        "Ragda Pattice", "Samosa Chaat", "Green Chana Masala",
        "Dabeli", "Dahi Vada"
    ],
    "Dosa": [
        "Sada Dosa", "Masala Dosa",
        "Mysore Masala Dosa", "Cheese Dosa"
    ],
    "Sandwich": [
        "Cheese Sandwich", "Chutney Sandwich",
        "Tomato Sandwich", "Cucumber Sandwich",
        "Mix Veg Sandwich", "Vegetable Toast (Grilled)",
        "Vegetable Cheese Toast (Grilled)",
        "Samosa Toast (Grilled)",
        "Samosa Cheese Toast (Grilled)"
    ],
    "Pizza": [
        "Cheese Pizza",
        "Cheese/Tomato/Onion Pizza",
        "Paneer Pizza"
    ],
    "Frankie": ["Veg Frankie"],
    "Pav Bhaji": ["Pav Bhaji"],
    "Rice & Combos": [
        "Veg Biryani", "Tawa Pulao", "Chhole Kulche"
    ],
}

CATEGORY_IMAGES = {
    "Chaat": "chaat.png",
    "Dosa": "dosa.png",
    "Sandwich": "sandwich.png",
    "Pizza": "pizza.png",
    "Frankie": "frankie.png",
    "Pav Bhaji": "pav_bhaji.png",
    "Rice & Combos": "rice.png",
}


# ---------------- HERO ----------------

hero_image = get_image("snacks_background.png")

if hero_image:
    hero_style = (
        "background-image: linear-gradient("
        "90deg, rgba(38,22,13,.96), "
        "rgba(38,22,13,.75) 48%, "
        "rgba(38,22,13,.15)), "
        f"url('{hero_image}');"
    )
else:
    hero_style = (
        "background: linear-gradient("
        "120deg, #382117, #75401f, #a65d2b);"
    )

st.markdown(
    f"""
    <div class="hero" style="{hero_style}">
        <p class="eyebrow">FRESH • FLAVOURFUL • DESI</p>
        <h1>Your cravings.<br>
        <span class="accent">Our Chaatwala.</span></h1>
        <p>
            From chatpati street-style chaat to crispy dosas,
            cheesy sandwiches and comforting Indian favourites.
            There is something delicious for everyone.
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

st.write("")

# ---------------- HIGHLIGHTS ----------------

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="feature">
        <div class="feature-title">🌶️ Chatpata Bites</div>
        <div class="feature-desc">
            Tangy chaat and street-food favourites.
        </div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="feature">
        <div class="feature-title">🥪 Desi Comfort</div>
        <div class="feature-desc">
            Sandwiches, pizza and delicious frankie.
        </div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="feature">
        <div class="feature-title">🍛 Filling Favourites</div>
        <div class="feature-desc">
            Dosa, biryani, pulao and more.
        </div>
    </div>
    """, unsafe_allow_html=True)

st.write("")
st.divider()

# ---------------- MENU SECTION ----------------

st.markdown(
    '<div class="section-heading">Explore Our Menu</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="section-subtitle">'
    'Your favourite flavours, all in one place.'
    '</div>',
    unsafe_allow_html=True
)

search_col, category_col = st.columns([1.4, 1])

with search_col:
    search = st.text_input(
        "Search dishes",
        placeholder="Try pani puri, dosa, biryani..."
    )

with category_col:
    category = st.selectbox(
        "Choose a category",
        ["All"] + list(MENU.keys())
    )

# Filter menu
shown = []

for cat, dishes in MENU.items():
    if category != "All" and cat != category:
        continue

    for dish in dishes:
        if (
            not search.strip()
            or search.strip().casefold() in dish.casefold()
            or search.strip().casefold() in cat.casefold()
        ):
            shown.append((cat, dish))

if not shown:
    st.info("No dishes found. Try a different search.")

else:
    # Display a small number of category photos,
    # rather than repeating an image for every dish.
    displayed_categories = []

    for cat, dish in shown:
        if cat not in displayed_categories:
            displayed_categories.append(cat)

    for start in range(0, len(displayed_categories), 2):
        category_row = displayed_categories[start:start + 2]
        cols = st.columns(len(category_row), gap="medium")

        for col, cat in zip(cols, category_row):
            with col:
                image_name = CATEGORY_IMAGES[cat]
                local_image = get_image(image_name)

                if local_image:
                    st.image(local_image, use_container_width=True)

                st.markdown(
                    f'<div class="menu-panel">'
                    f'<div class="menu-category">'
                    f'{html.escape(cat)}</div>'
                    f'<div class="menu-name">'
                    f'What We Serve</div>'
                    f'<div class="dish-list">'
                    + "".join(
                        f'• {html.escape(d)}<br>'
                        for c, d in shown if c == cat
                    )
                    + '</div></div>',
                    unsafe_allow_html=True
                )

st.write("")
st.divider()

# ---------------- CONTACT ----------------

st.markdown("""
<div class="contact-box">
    <p class="eyebrow">COME SAY HELLO</p>
    <h2>Good food. Great mood.</h2>
    <p>For enquiries, contact Paresh</p>
    <div class="contact-number">90292 19176</div>
    <p>We look forward to serving you!</p>
</div>
""", unsafe_allow_html=True)

st.write("")

call_col, whatsapp_col = st.columns(2)

with call_col:
    st.link_button(
        "☎️ Call Paresh",
        "tel:+919029219176",
        use_container_width=True
    )

with whatsapp_col:
    message = quote(
        "Hi Chaatwala! I'd like to know more about your menu."
    )
    st.link_button(
        "💬 WhatsApp Us",
        f"https://wa.me/919029219176?text={message}",
        use_container_width=True
    )

st.write("")
st.divider()

st.markdown(
    "<p style='text-align:center;color:#826b5b;'>"
    "Chaatwala · Made with a little extra masala ❤️"
    "</p>",
    unsafe_allow_html=True
)
