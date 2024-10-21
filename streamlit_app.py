
import streamlit as st
import pandas as pd

# Title of the web app
st.title("Anime Recommendation System")

# Load default dataset
default_anime = pd.read_csv("anime.csv")

# File uploader for the anime dataset (or load the default dataset)
uploaded_file = st.file_uploader("Choose an Anime Dataset (CSV)", type="csv")

if uploaded_file is not None:
    # Load the user's dataset
    anime = pd.read_csv(uploaded_file)
else:
    # Use default dataset if no file is uploaded
    st.write("No file uploaded. Using default anime dataset.")
    anime = default_anime

# Show dataset overview
st.subheader("Dataset Overview")
st.write("Shape of the dataset:", anime.shape)
st.write(anime.head())

# Allow the user to explore the data
if st.checkbox("Show dataset info"):
    st.write(anime.info())

# Filters for user input
st.subheader("Find Anime Recommendations")
selected_genre = st.text_input("Enter Genre (e.g., Action, Comedy):")
selected_type = st.selectbox("Select Type:", anime["type"].unique())

# Filter dataset based on user input
if selected_genre and selected_type:
    filtered_anime = anime[anime["genre"].str.contains(selected_genre, na=False) & (anime["type"] == selected_type)]
    if not filtered_anime.empty:
        st.subheader("Recommended Anime:")
        st.write(filtered_anime[["name", "genre", "type", "rating"]].head(10))  # Show top 10 recommendations
    else:
        st.write("No recommendations found for the selected genre and type.")
else:
    st.write("Please enter a genre and select a type to get recommendations.")
