import streamlit as st
from helpers import * #importing each function from helpers.py

def main(): 
    st.title("Auto Feature Selector Tool")
    # file uploader
    uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
    if uploaded_file is not None: 
        analyze_csv_file(uploaded_file)
        
        df = st.session_state.get('df')
        
        if df is not None: 
            if st.button('Transform Object Columns'): 
                df, label_encoders = transform_object_columns(df)
                st.session_state['df'] = df
                st.success("Objects columns transformed successfully")
                st.write("Transformed Data")
                st.write(df)
                
            select_target_column(df)
            feature_selection_options()
            
            if st.session_state.get('feature_selection_method') == 'Correlation Coefficient': 
                correlation_coefficient_selection()
                
            if st.session_state.get('feature_selection_method') == "Chi-Square Test":
                chi_square_selection()
                
            if st.session_state.get('feature_selection_method') == "Anova":
                anova_selection()
                
            if st.session_state.get('feature_selection_method') == "Mutual Information":
                mutual_info_selection()
                
            if st.session_state.get('feature_selection_method') == "Variance Threshold":
                variance_threshold_selection()
                
if __name__ == "__main__": 
    main()