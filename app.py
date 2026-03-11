import streamlit as st

st.logo(
    "https://img.freepik.com/premium-vector/black-white-picture-woman-playing-guitar_1281446-9574.jpg",
    icon_image= "https://img.freepik.com/premium-vector/black-white-picture-woman-playing-guitar_1281446-9574.jpg"
)

st.title ("Instruments Hub", width="stretch", text_alignment= "center")
st.markdown ("Learn About The Instruments", width="stretch", text_alignment= "center")

def landing_page():
    st.header("🎶 !Welcome to Instruments Hub! 🎶", text_alignment= "center")
    st.markdown("Your guide to finding the perfect instrument", text_alignment= "center")
    st.divider()
    
    col1, col2, col3 = st.columns([1, 2, 1])

    with col2:
        st.image("https://robbreport.com/wp-content/uploads/2022/09/378WE_MusicRoom.jpg?w=1000", caption="Explore the world of music", width= 350)
    
    st.markdown("Click on the sidebar to explore different types of instruments like Guitars, Pianos, and Drums", text_alignment="center")

def page_1():
    st.title("Guitars 🎸")
    st.write("Two Different Types of Guitar")

    col1, col2 = st.columns(2, gap="large")

    with col1:
        st.header("Electric Guitar", text_alignment= "center")
        st.image("https://cdn.mos.cms.futurecdn.net/BVsGJgu75JdwdQTGqSCGHa.jpg", width=300)
        
        st.markdown ("An electric guitar is a guitar that uses pickups and an amplifier to turn string vibrations into louder sound.", text_alignment= "justify")
        
        with st.popover("**Learn More**"):
            st.markdown(""" 
                        **ADVANTAGES** ✅
                        1. **Versatile Sound** – Electric guitars can produce a wide range of tones using pickups, amplifiers, and effects pedals, from clean melodies to heavy distortion.
                        2. **Easier to Play** - The strings are usually lighter and closer to the fretboard, making bending and fast playing easier.
                        3. **Effects and Modulation** – You can use effects like reverb, delay, distortion, chorus, and more to create unique sounds.

                        **DISADVANTAGES** ❌
                        1. **Requires Equipment** – To be heard properly, you need an amplifier and cables, which makes it less portable than acoustic guitars.
                        2. **Cost** – High-quality electric guitars and amplifiers can be expensive.
                        3. **Dependent on Power** - Amplifiers need electricity or batteries, so you can’t always play at full volume anywhere.
                        """)
        
    with col2:
        st.header("Acoustic Guitar", text_alignment= "center")
        st.image("https://cdn.mos.cms.futurecdn.net/TBeuyAaEtUjcfwmT2YMmZW.jpg", width=300)

        st.markdown ("An acoustic guitar produces sound naturally through its vibrating strings and hollow body, without electricity, offering a warm, natural tone.", text_alignment="justify")
        
        with st.popover("**Learn More**"):
            st.markdown("""
                         **ADVANTAGES** ✅
                        1. **Portability** – You can play an acoustic guitar anywhere without an amplifier or extra equipment.
                        2. **Simple Setup** – No complex electronics or cables are needed, making it beginner-friendly.
                        3. **Natural Sound** – Acoustic guitars produce sound through the vibration of strings and their hollow body, without the need for electricity.
                        
                        **DISADVANTAGES** ❌
                        1. **Limited Volume** – Acoustic guitars are quieter and may not be heard well in large groups or noisy environments.
                        2. **Harder Playability for Some** – Strings are often thicker and harder to press, which can be challenging for beginners.
                        3. **Susceptible to Weather** – Wooden bodies can be affected by humidity and temperature, potentially altering tone or causing damage.
                        """)
            
    st.link_button("Watch A Video", "https://www.youtube.com/watch?v=E3vjSbzyYjM", icon_position="right")
    st.subheader("Was this guitar guide helpful?")
    
    feedback = st.feedback("stars")
    
    if feedback is not None:
        st.write(f"Thank you for your rating!")
        st.balloons()

    comment = st.text_area("Your Thoughts?")
    if comment:
        st.write("Your comment:", comment)
        
    st.divider()
    if st.button("⬅️ Back to Home", use_container_width=True):
        st.switch_page(home)

def page_2():
    st.title("Pianos 🎹")
    st.write("Two Different Types of Piano")

    col1, col2 = st.columns(2, gap = "large")
    
    with col1:
        st.subheader("Keyboard (Electric)", text_alignment= "center")
        st.image("https://theonemusic.com/cdn/shop/files/preview_images/TheONE-Smart-Piano-TON-White-keyboard_U-Stand-Indoor.png?v=1714034195&width=1946", width=280)

        st.markdown ("An electric keyboard produces sound electronically when keys are pressed, offering various instrument tones, rhythms, and effects for versatile music use.", text_alignment="justify")
        
        with st.popover("**Learn More**"):
            st.markdown(""" 
                        **ADVANTAGES** ✅
                        1. **Versatile Sound** – Can imitate many instruments and produce different effects.
                        2. **Portable** – Lighter and easier to move than a piano.
                        3. **Beginner-Friendly** – Often includes learning modes and built-in rhythms.

                        **DISADVANTAGES** ❌
                        1. **Limited Acoustic Resonance** – Lacks the natural tone of a traditional piano..
                        2. **Requires Power** – Needs electricity or batteries to work.
                        3. **Dependent on Electronics** – Malfunctions in circuits can affect performance.
                        """)
    
    with col2:
        st.subheader("Grand Piano (Acoustic)", text_alignment= "center")
        st.image("https://www.cunninghampiano.com/cdn/shop/products/yamaha-c7x-76-grand-piano-in-polished-ebony-1604900.jpg?v=1752345750", width= 300)
        
        st.markdown ("A grand piano is an acoustic keyboard where hammers strike strings to produce rich, resonant sound, commonly used in classical and concert music.", text_alignment="justify")
        
        with st.popover("**Learn More**"):
            st.markdown(""" 
                        **ADVANTAGES** ✅
                        1. **Rich Sound** – Produces full, resonant tones with wide dynamic range.
                        2. **Durable Build** – High-quality construction lasts for decades.
                        3. **Prestige and Aesthetics** – Often used in concerts and formal settings.

                        **DISADVANTAGES** ❌
                        1. **Large Size** – Takes up a lot of space and is heavy.
                        2. **Expensive** – High purchase and maintenance costs.
                        3. **Regular Maintenance Needed** – Requires tuning and care to keep sound quality.
                        """)
    
    st.link_button("Watch A Video", "https://www.youtube.com/watch?v=pXG8_W7ZFjc")
    st.subheader("Was this piano guide helpful?")
    
    feedback = st.feedback("stars")
    
    if feedback is not None:
        st.write(f"Thank you for your rating!")
        st.balloons()


    comment = st.text_area("Your Thoughts?")
    if comment:
        st.write("Your comment:", comment)

    st.divider()
    if st.button("⬅️ Back to Home", use_container_width=True):
        st.switch_page(home)
        
def page_3():
    st.title("Drums 🥁")
    st.write("Two Different Types of Drums")

    col1, col2 = st.columns(2, gap = "large")
    
    with col1:
        st.subheader("Electric Drums", text_alignment= "center")
        st.image("https://www.carlsbro.com/wp-content/uploads/2017/10/CSD35M-cat.jpg", width=283)

        st.markdown ("Electric drums are electronic drum sets that produce sound through sensors and a sound module, offering versatile tones and quieter play than acoustic drums.", text_alignment="justify")
        
        with st.popover("**Learn More**"):
            st.markdown(""" 
                        **ADVANTAGES** ✅
                        1. **Versatile Sounds** – Offer multiple drum kits, effects, and sounds.
                        2. **Beginner-Friendly** – Often include built-in practice modes and metronomes.
                        3. **Quiet Practice** – Can be played with headphones without disturbing others.

                        **DISADVANTAGES** ❌
                        1. **Less Natural Feel** – Pads don’t fully replicate the rebound and feel of acoustic drums.
                        2. **Limited Acoustic Resonance** – Lack the full sound and dynamics of traditional drums.
                        3. **Sensitive Electronics** – Can malfunction if dropped or damaged.
                        """)
    
    with col2:
        st.subheader("Acoustic Drums", text_alignment= "center")
        st.image("https://www.premier-percussion.com/wp-content/uploads/2022/10/category.jpg", width= 300)
        
        st.markdown ("Acoustic drums are traditional drum sets that produce sound when the drummer strikes the drumheads and cymbals, relying on natural resonance of the drum shells. " \
        "They are widely used in rock, jazz, and live performances for their full, dynamic sound.", text_alignment="justify")
        
        with st.popover("**Learn More**"):
            st.markdown(""" 
                        **ADVANTAGES** ✅
                        1. **Natural Sound** – Produces full, resonant tones with authentic dynamics.
                        2. **No power needed** – play anywhere without electricity.
                        3. **Authentic feel** — realistic stick rebound and playing response.

                        **DISADVANTAGES** ❌
                        1. **Loud** – Can be too noisy for home practice.
                        2. **Limited Sound Variety** – Cannot easily change drum tones without swapping drums or heads.
                        3. **Space & portability** – take up room and are heavy to move.
                        """)
    
    st.link_button("Watch A Video", "https://www.youtube.com/watch?v=dLWjZ_PZ0m4")
    st.subheader("Was this Drum guide helpful?")
    
    feedback = st.feedback("stars")
    
    if feedback is not None:
        st.write(f"Thank you for your rating!")
        st.balloons()

    comment = st.text_area("Your Thoughts?")
    if comment:
        st.write("Your comment:", comment)
            
    st.divider()
    if st.button("⬅️ Back to Home", use_container_width=True):
        st.switch_page(home)
        
def about_page():
    st.title("About Instruments Hub")
    st.caption(""" Instruments Hub is an application that could help aspiring musicians to identify different musical instruments and choose their desired instrument.
    """)
    st.divider()

    st.title("Target Users")
    st.caption(""" Our target users are people who has zero to little knowledge about instruments for them to have a reference before buying their first instrument.
             """)

    st.title("What inputs does the app collect, and what output does it shows")
    st.caption("""
            INPUTS 
               - We only collect user comments and their feedback while using the app.
            OUTPUTS
               - This is an intrument guide app that help people to choose their first instrument. 
    """)

    VIDEO_URL = "https://www.youtube.com/watch?v=0eEkWvekQiE"
    st.video(VIDEO_URL)

    st.divider() 
    if st.button("⬅️ Back to Home", use_container_width=True):
        st.switch_page(home)

home = st.Page(landing_page, title="Home", icon="🏠")
p1 = st.Page(page_1, title="Guitars", icon="🎸")
p2 = st.Page(page_2, title="Pianos", icon="🎹")
p3 = st.Page(page_3, title="Drum", icon="🥁")
about = st.Page(about_page, title="About Us", icon="ℹ️")

pg = st.navigation({

    "Main": [home],
    "Type of Instruments"  :[p1, p2, p3,],
    "Info" :[about]

})
pg.run()
