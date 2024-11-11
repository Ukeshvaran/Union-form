import streamlit as st
import psycopg2 as pg
import urllib.parse as urlparse
import time

game={1:"The best way to predict your future is to create it",
      2:"Every day may not be good, but there’s something good in every day",
      3:"Believe in yourself, and you’ll be unstoppable",
      4:"You are never too old to set another goal or to dream a new dream",
      5:"Your attitude determines your direction",
      6:"Success is not the key to happiness. Happiness is the key to success",
      7:"Don't wait for the perfect moment. Take the moment and make it perfect",
      8:"You are capable of amazing things",
      9:"The only limit to our realization of tomorrow is our doubts of today",
      10:"Be a voice, not an echo"}

st.markdown(
    """
    <style>
        /* Hide the Streamlit GitHub icon and top bar */
        .css-1d391kg {display: none;}  /* GitHub icon */
        
        /* Hide the "Streamlit" label in the top bar */
        header {visibility: hidden;}  /* Hide Streamlit branding on the header */
        
        /* Optionally, remove the footer */
        footer {visibility: hidden;}  /* Hide the footer (Streamlit's footer text) */
    </style>
    """,
    unsafe_allow_html=True
)


DATABASE_URL = "postgres://avnadmin:AVNS_Wlr66NJhJl_VBS7Xzz9@my-postgres-db-union-form.j.aivencloud.com:24887/defaultdb?sslmode=require"  
url = urlparse.urlparse(DATABASE_URL)
try:
    con = pg.connect(
        host=url.hostname,
        port=url.port,  
        database=url.path[1:],  
        user=url.username,
        password=url.password)

except Exception as e:
    st.error(f"Error connecting to Database: {e}")
try:
    st.markdown(''' # :red[Welcome] :balloon:''')
    st.columns(3)[1].image("https://occ-0-1723-1722.1.nflxso.net/dnm/api/v6/LmEnxtiAuzezXBjYXPuDgfZ4zZQ/AAAABePV7eWrtLkRVZOiqV4jEB8vJQK-lZ5yBySb3DaltJRXRqeOkZQ279u4XEz4B4RL_dJFVvQmQJyhyH0Osd9jzJXIIK0nSaHuduLCMjJP9EH0.png?r=797",width=250)
    st.divider()
    def info():
            name = st.text_input(" **Name** :",placeholder="Enter your name")
            st.write("")
    
            phone=st.text_input(" **Phone number** :",placeholder="Enter your contact number")
            st.write("")
    
            theme=st.text_input(" **Do you have any specific theme suggestion for the event** :",placeholder="Enter your text here")
            st.write("")
    
            event_avail= st.radio(" **Please confirm whether you will be available to join the event** :",["Yes","No","Not sure"],horizontal=True)
            st.write("")
    
            availability = st.radio(" **Are you comfortable with the event date** :", ["Yes", "No"],horizontal=True)
            st.write("")
            if availability == "No":
                availability = st.text_input(" **Kindly share us your availability** :",placeholder="DD/MM/YYYY")
    
            eve_plc=st.radio(" **Are you comfortable with event place** :",["Yes","No"],horizontal=True)
            st.write("")
            if eve_plc=="No":
                 eve_plc=st.text_area(" **Reason** :",placeholder="Enter your text here")
            
            
            food = st.radio(" **Food preference** :", ["Veg", "Non-veg"],horizontal=True)
            st.write("")
            if food=="Veg":
                st.write("selected : :green[veg]")
            else:
                st.write("selected : :red[non-veg]")
    
            suggestion = st.radio(" **Do you have any suggestion for the event** :", ["Yes", "No"], index=1, horizontal=True)
            st.write("")
            if suggestion == "Yes":
                suggestion = st.text_area("Suggestions :",placeholder="Enter your suggestion here")
    
            performance=st.radio(" **Are you willing to perform any art at the event** :",["Yes","No"],index=1,horizontal=True)
            st.write("")
            guess=st.text_input("Enter any number between 1 - 10 : ",placeholder="Enter your number here")
            btnn=st.button("Enter",type='primary')
            def result(game,guess):
                  for i in game:
                        if int(guess)==i:
                              return (game[i])
            if btnn:
                  st.write(result(game,guess))
            if performance=="Yes":
                 with st.chat_message('user'):
                      conn=st.container(border=True)
                      conn.write("if your going to perform any group activity. Kindly coordinate with your team and update here, what your going to perform along with your team-mates name")
                 performance=st.text_input(" **Please enter what you are going to perform** :",placeholder="Enter your input in a single line")
            st.divider()
            check_box=st.checkbox(":blue[Click here] ")
            st.markdown(":copyright: :red[yukesh's]  personal  web  deployment")
            st.write("")
            st.write("")
            st.write("")
            
            
            if check_box:
                 with st.chat_message('ai'):
                    container = st.container(border=True)
                    container.write("This information will be stored in a database that can be accessed whenever necessary. It will be fully encrypted from end to end, ensuring that only authorized personnel and the admin can access it, keeping it secure from unauthorized users.")
    
                 submit = st.columns(3)[1].button("Submit",type='primary')
             
                 if submit:
                     with st.spinner(text="Loading......"):
                         bar = st.progress(0)
                         time.sleep(3)
                         bar.progress(100)
                         time.sleep(2)
                         st.success("Thanks for your response!", icon=":material/thumb_up:")
                         st.error("You can now close your browser")
                     
                     sqlupdate(name, phone ,theme,event_avail,availability,eve_plc, food, suggestion,performance)
                     st.balloons()
            
            
            vid="https://youtu.be/c5_dMj0J08Y?si=Ijhuxj4xyQdwSZ9G"
            st.video(vid,loop=True,autoplay=True,muted=True,subtitles=None)
            st.markdown(" **Feedback** :")
            st.feedback(options="faces")

    
    def sqlupdate(a, b, c, d , e,f,g,h,i):
        cur = con.cursor()
        cur.execute("""CREATE TABLE IF NOT EXISTS "unitable" (
                            name VARCHAR(60),
                            phone VARCHAR(15),
                            Theme VARCHAR(500),
                            event_availability VARCHAR(10),
                            availability VARCHAR(500),
                            place VARCHAR(500),
                            food VARCHAR(30),
                            suggestion VARCHAR(500),
                            Performance VARCHAR(500)
                        )""")
        cur.execute("""INSERT INTO "unitable" (name, phone , theme,event_availability,availability,place ,food, suggestion,performance)
                        VALUES (%s, %s, %s, %s, %s,%s,%s,%s,%s)""", (a, b, c, d, e,f,g,h,i))
        con.commit()


except:
    st.warning("An error occurred")

    

info()

con.close()
