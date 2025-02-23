
import streamlit as st
import pandas as pd
# Titre de l'application centré avec une couleur blanche
st.markdown("<h1 style='text-align: center; color: #007BFF';font-size:2.5em;font-weight:bold;>My Data SCRAPPER APP</h1>", unsafe_allow_html=True)

# Description de l'application
st.markdown("""
            <style>
                div.stMarkdown {
                background-color: #f5faff;
                padding: 15px;
                border-radius: 10px;
                border-left: 5px solid #007BFF;
                box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.1);
            </style>
            
            
This app allows you to download scraped data on shoeses and clothes from coinafrica 
* **Python libraries:** base64, pandas, streamlit,Beautifulsoup
* **Data source:** [Coinafrica](https://sn.coinafrique.com/ )
""",unsafe_allow_html=True)



# Style personnalisé de l'application
st.markdown("""
<style>
    /* Style général du rapport */

    body {

        background-color: #f5faff; /* bleu clair */

        color: #333333; /* text principal en gris fonce */

        font-family: 'Poppins', sans-serif;

    }

    /* Style du titre principal */

    h1 {

        text-align: center;

        color: #007BFF; /* Bleu vibrant */

        font-size: 2.5em;

        font-weight: bold;

    }

    /* Sidebar customisation */

    .stSidebar {

        background-color: #ffffff;

        border-right: 3px solid #007BFF;

        padding: 20px; /*distance entre text et box

    }

    /* Styles of widgets  Selectbox sliders etc.*/

        .stSelectbox,.stTextInput,.stNumberInput {

        border-radius: 10px;

        border: 2px solid #007BFF;

        padding: 10px;

    }

    /* buttons */

    .stButton>button{

        background: linear-gradient(135deg, #007BFF, #00BFFF); /* Blue gradient */

        color: white;

        border: none;

        border-radius: 25px;

        padding: 12px 30px;

        font-size: 16px;
        font-weight:bold;
        transition:all 0.3s ease-in-out;
        box-shadow:3px 3px 10px rgba(0,123,255,0.3)
        cursor: pointer;
    }  

    .stButton>button:hover{
        background:linear-gradient(135deg,#00BFFF,#007BFF);
        transform:scale(1.05);
        box-shadow:4px 4px 15px rgba(0,123,255,0.5);
    }

     .stButton>button:active{
        
        transform:scale(0.95);
        background:#0056b3;
    }


    
    /* Effet pour les sections */
    .stMarkdown{
         background-color: #ffffff;
         border-right: 5px solid #007BFF; 
         padding:10px.
         border-radius:5px;
    }
    /*style des dataframes*/
    .stDataFrame{
          background-color: #ffffff;
          border-radius:12px;
          padding:15px;
          box-shadow:2px 2px 10px rgba(0,0,0,0.1)
    
    }
</style>
""",unsafe_allow_html=True)# Permet d'inclure du HTML et CSS dans l'application
    



# Barre latérale pour la sélection des options

st.sidebar.title("User Input")
# Sélection du nombre de pages
pages=st.sidebar.selectbox("pages ",options=list(range(1,101)),index=1)
# Sélection de la méthode de scraping
options=st.sidebar.selectbox("Options",["Webscraper","Beautifulsoup","Fill the form"])


# Fonction pour charger et afficher les données
def load_(dataframe, title, key):
    

  #creation button
    if st.button(title,key):
    
        st.subheader('Display data dimension')
        st.write('Data dimension: ' + str(dataframe.shape[0]) + ' rows and ' + str(dataframe.shape[1]) + ' columns.')
        st.dataframe(dataframe)  # Affichage des données dans un tableau
        
        # Bouton pour télécharger les données au format CSV
        st.download_button( 
            label="Download csv",
            data=dataframe.to_csv(index=False).encode('utf-8'),# Converssion en CSV avec encodage UTF-8
            file_name=title, # Nom du fichier téléchargé
            mime="text/csv" )#sert a indiquer le type de fichier que l'on telecharge)

# Chargement des données en fonction de l'option sélectionnée

if options=="Beautifulsoup":
    load_(pd.read_csv('data/vetments_enfants_url1.csv'), 'vetements enfants data', '1')
    load_(pd.read_csv('data/chaussures_enfants_url2.csv'), 'chaussures enfants', '2')

elif options=="Webscraper":
    load_(pd.read_csv('data/WebS_vetementsenfants_URL1.csv'), 'vetements enfants data', '1')
    load_(pd.read_csv('data/WebS_chaussuresenfants_url2.csv'), 'chaussures enfants', '2')

elif options=="Fill the form":
    # Sélection d'un formulaire à remplir
    commentaires=st.selectbox("FORM",["kobotoolbox","google form"])
      # Affichage d'un formulaire en fonction de la sélection
    if commentaires== "kobotoolbox":
        st.markdown("""<iframe src=https://ee.kobotoolbox.org/i/JuArXef9 width="800" height="600"></iframe>""",unsafe_allow_html=True)

    elif commentaires=="google form":
        st.markdown("""<iframe src=https://docs.google.com/forms/d/e/1FAIpQLSeFFvAc6hBhyfPsCX6P8EBN8vMRVfm0Lt3aAOeBGZl0CMvnVA/viewform?usp=dialog width="800" height="600"></iframe>""",unsafe_allow_html=True)