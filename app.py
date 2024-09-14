import streamlit as st
import pandas as pd
import numpy as np


macro_elements = ["Fe2O3","Al2O3","SiO2","LOI"]
all_elements = ['SAMPLE','Ni', 'Co', 'Al2O3', 'CaO', 'Cr2O3', 'Fe2O3', 'K2O',
                 'MgO', 'MnO', 'Na2O', 'P*', 'S*', 'SiO2', 'TiO2', 'LOI']

def balancer(dataframe_input):
    df=dataframe_input
    df["Sum"]= oxide_sum(df)
    df["Diff"]= diff(df)
    df["Macro"]=macro_sum(df)
    for x in macro_elements:
        df[f'%{x}']=macro_proportion(df,f"{x}")
        df[f'{x}']+=np.round((df["Diff"]*df[f'%{x}']),2)
    df["Sum"]= oxide_sum(df)
    df = df[all_elements]

    
    
    return df 

def macro_changer(df,macro_element):
    df[macro_element]+=np.round((df["Diff"]*df[f'%{macro_element}']),2)

    pass

def macro_proportion(df, macro_element):
    element_proportion = df[macro_element]/df["Macro"]
    return element_proportion



def macro_sum(df):
    macro_data = df["macro"]=df[["Fe2O3","Al2O3","SiO2","LOI"]].sum(axis=1)
    return macro_data

def diff(df):
    diff100=np.round(100-df["Sum"])

    return diff100
    

def oxide_sum(df):
    sum_oxide = df[['Ni', 'Co', 'Al2O3', 'CaO', 'Cr2O3', 'Fe2O3', 'K2O',
                 'MgO', 'MnO', 'Na2O', 'P*', 'S*', 'SiO2', 'TiO2', 'LOI']].sum(axis=1)
    
    return sum_oxide


def main():
    st.title("SUCOFINDO REPORT BALANCER")
    st.text("Position Only")

    uploaded_file = st.file_uploader("Upload an Excel file")

    if uploaded_file is not None:
        try:
            df = pd.read_excel(uploaded_file)
            st.success("File uploaded successfully!")
            df_final = balancer(df.copy())
            st.write("BEFORE")
            st.dataframe(df, width=800, height=400)
            # print(oxide_sum(df))

            st.write("AFTER")
            st.dataframe(df_final, width=800, height=400)
            
        except Exception as e:
            st.error(f"Error reading Excel file: {e}")



passwordnya = st.text_input("MIE BURUNG DARA, ENAKNYA.....")
jawaban = "RASA BURUNG"



if passwordnya.upper() == jawaban:
    main()
else :
    pass





# if __name__ == '__main__':
#     main()