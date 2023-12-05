import streamlit as st
import lang_help
import pandas as pd

st.title("Restaurant Name Generator")

cuisine = st.sidebar.selectbox("Select a cuisine", ["Chinese", "Indian", "Italian", "Mexican", "Thai"])
price = st.sidebar.slider("Select a price range", 100, 1000)

if cuisine:
    response = lang_help.generate_name(cuisine, price)
    st.header(response["restaurant_name"].strip())
    menu_items = response["menu_items"].strip().split("|")
    
    # Remove empty strings from the list
    menu_items = [item.strip() for item in menu_items if item.strip()]
    print(menu_items)
    
    # Split the list into two: names and prices
    names = menu_items[::2]
    prices = menu_items[1::2]
    
    # Create a DataFrame for the menu items
    df = pd.DataFrame({"Thali Item": names, "Price": prices})
    
    # Reset the index of the DataFrame
    df.reset_index(drop=True, inplace=True)

    # Add 1 to the index of the DataFrame
    df.index = df.index + 1
    
    # Display the DataFrame as a table in Streamlit
    st.table(df)
