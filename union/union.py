import streamlit as st
import psycopg2 as pg
st.columns(3)[1].title("Welcome")
con = pg.connect(host='localhost', port='5432', database='jack', user='postgres', password='137700')
cur = con.cursor()
page_bg=f"""<style>
[data-testid="stAppViewContainer"]{{
background-image:url("data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wCEAAkGBw8PDQ0PDw8PDw8NDQ0NDQ0PEA8PDw0NFREWFhURFRMYHSggGBolHRUVITEhJSkrLi4uFx8zODMsNygtLisBCgoKDg0NFQ8PFS0dFR0rKy0tKy0tKystKystKysrKy0rKzctKysrLTcrKysrLS0rKy0uKy0rLSsrKysrLSs3K//AABEIAKsBJgMBIgACEQEDEQH/xAAYAAEBAQEBAAAAAAAAAAAAAAAAAQIDB//EACQQAQEAAgECBgMBAAAAAAAAAAABAhGBMfASIUFRYZGhscED/8QAFgEBAQEAAAAAAAAAAAAAAAAAAAEC/8QAGhEBAQEAAwEAAAAAAAAAAAAAABEBAjFREv/aAAwDAQACEQMRAD8A9w8xF4EA4/QKgvfkgi7VkBoSVRQAAAAAAAAAAAAAAAAAAAAAAAAAAAEAoAHAAAIKggsqANDKyiqAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAcAAAgoIiKAsqsNSgoAoAAAAAAAAAAAAAAAAAAAAACAAAAHIAcgAAAgoIiKAStMEqjYkqooAAAAAAAAAAAAAAAAAAACAAAAAAcgAcgAACIKAiKig1KyA2JKqKAAAAAAAAAAAAAAAAAAgAgAKAaAF0AgoCcigIGgBF0giCooLMkBGxmVpGgAAAAAAAAAAAAAAZyyk6gm8sxdKAoAAAAAAAAAAAAACaTTQDA2zcRIhKllTas11gxK1KjWaoAoAAAAAACbBUtTaaErOXn/AAaFZ+WwEbAAAAAAAAAAAAAAAAAAEslUBzuF9LxWfFw7JZtazvHxmZtbc7/n7fVMc/SiWdumxBGlNnfQFNgCIKAgoCBoBoAUAAAAAAAAAAAAAAAAAAAAAATLGXqoDl4bPmflqZbbZyw38X3VmToVjdnX79GkXNXvoIoAAoACCgigCgAAAAAAAAAAAAAAAAAAAAAAAAADFx10+mwSMSqtjOrAa79RJQFAAAFUAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAEuKNAkZUsQFE2A//Z");
opacity:1.5;
}}
[data-testid="stHeader"]
{{background-color:rgba(0,0,0,0);}}
</style>"""
st.markdown(page_bg,unsafe_allow_html=True)

def info():
        name = st.text_input("Name :",placeholder="Enter your name")

        phone=st.text_input("Phone number :",placeholder="Enter your contact number")

        theme=st.text_input("Do you have any specific theme suggestion for the event :")

        availability = st.radio("Are you comfortable with the event date :", ["yes", "No"],horizontal=True)
        if availability == "No":
            availability = st.text_input("Kindly share us your availability :",placeholder="DD/MM/YYYY")

        eve_plc=st.radio("Are you comfortable with event place :",["Yes","No"],horizontal=True)
        if eve_plc=="No":
             eve_plc=st.text_area("Reason :",placeholder="Enter your text here")
        
        
        food = st.radio("Food preference :", ["Veg", "Non-veg"],horizontal=True)

        st.write(f"selected : :green[{food}]")

        suggestion = st.radio("Do you have any suggestions for the event :", ["Yes", "No"], index=1, horizontal=True)
        if suggestion == "Yes":
            suggestion = st.text_area("Suggestions :")

        performance=st.radio("Are you willing to perform any art at the event :",["Yes","No"],index=1,horizontal=True)
        if performance=="Yes":
             with st.chat_message('user'):
                  conn=st.container(border=True)
                  conn.write("if your going to perform any group activity. Kindly coordinate with your team and update here, what your going to perform along with your team-mates name")
             performance=st.text_input("Please enter what you are going to perform :",placeholder="Enter your input in a single line")

        check_box=st.checkbox("click & submit")
        if check_box:
             with st.chat_message('ai'):
                container = st.container(border=True)
                container.write("This information will be stored in a database that can be accessed whenever necessary. It will be fully encrypted from end to end, ensuring that only authorized personnel and the admin can access it, keeping it secure from unauthorized users.")

             submit = st.columns(4)[2].button("Submit",type='primary')
             if submit:
                 st.success("Thanks for your response!", icon=":material/thumb_up:")
                 sqlupdate(name, phone ,theme,availability,eve_plc, food, suggestion,performance)
                 st.balloons()
        st.markdown(":copyright: Jack's Personal deployment")
def sqlupdate(a, b, c, d , e,f,g,h):
    cur.execute("""CREATE TABLE IF NOT EXISTS "unitable" (
                        name VARCHAR(60),
                        phone VARCHAR(15),
                        Theme VARCHAR(500),
                        availability VARCHAR(500),
                        place VARCHAR(500),
                        food VARCHAR(30),
                        suggestion VARCHAR(500),
                        Performance VARCHAR(500)
                    )""")
    cur.execute("""INSERT INTO "unitable" (name, phone , theme,availability,place ,food, suggestion,performance)
                    VALUES (%s, %s, %s, %s, %s,%s,%s,%s)""", (a, b, c, d, e,f,g,h))
    con.commit()

info()

con.close()
