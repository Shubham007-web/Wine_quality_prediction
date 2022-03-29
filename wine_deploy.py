import joblib
import numpy as np
import streamlit as st
import csv
# loading saved wine model named
model = joblib.load('/home/shubhm/Documents/python/machine_learning_projects/wine/wine_qaulity_RandomForest.dat')


# creating function for prediction

def wine_qaulity_prediction(input_data):
    input_data_as_numpy_array = np.asarray(input_data)

    # reshaping array in one dimensional vector
    reshaped_data = input_data_as_numpy_array.reshape(1,-1)


    # making prediction on the data

    prediction = model.predict(reshaped_data)
    if (prediction[0]== 3):
      return 'Very Poor Quality Wine and Quanlity Score : 3'
    elif (prediction[0]==4 ):
      return 'Poor Qaulity Wine and Quanlity Score : 4'

    elif (prediction[0]== 5):
        return 'Moderate Quality Wine and Quanlity Score : 5'

    elif (prediction[0]== 6):
        return 'Good Quality Wine and Quanlity Score : 6'

    elif (prediction[0]== 7):
        return 'Better Quality Wine and Quanlity Score : 7'

    else:
        return 'Best Quality Wine and Quanlity Score : 8'


# l = ['fixed acidity', 'volatile acidity', 'citric acid', 'residual sugar',
#        'chlorides', 'free sulfur dioxide', 'total sulfur dioxide', 'density',
#        'pH', 'sulphates', 'alcohol', 'quality']

# UI app function
def main():
    # title of the Page
    st.title('Wine Quality Prediction')

    im = '/home/shubhm/Documents/python/machine_learning_projects/wine/images.jpeg'
    st.image(im, caption='Red Wine', width=(600), use_column_width=None, clamp=False, channels="RGB", output_format="auto")

    # name =st.text_area('Text to translate')

    fixed_acidity, volatile_acidity, citric_acid, residual_sugar = st.columns(4)
    with fixed_acidity:
        fixed_acidity  =st.text_input('Fixed Acidity')
    with volatile_acidity:
        volatile_acidity = st.text_input('Residual Sugar')
    with citric_acid:
        citric_acid  = st.text_input('Citric Acid')
    with residual_sugar:
        residual_sugar = st.text_input('Residual_Sugar')
    # with residual_sugar:
    #     residual_sugar = st.text_input('Residual Sugar')
    chlorides, free_sulfur_dioxide, total_sulfur_dioxide, density = st.columns(4)

    with chlorides:
        chlorides = st.text_input('Chlorides')
    with free_sulfur_dioxide:
        free_sulfur_dioxide = st.text_input('Free Sulfur Dioxide')
    with total_sulfur_dioxide:
        total_sulfur_dioxide = st.text_input('Total Sulfur Dioxide')
    with density:
        density = st.text_input('Density')

    pH, sulphates, alcohol = st.columns(3)

    with pH:
        pH = st.text_input('PH')
    with sulphates:
        sulphates = st.text_input('Sulphates')
    with alcohol:
        alcohol = st.text_input('Alcohol')
    lst_data = [fixed_acidity, volatile_acidity, citric_acid, residual_sugar,
    chlorides, free_sulfur_dioxide, total_sulfur_dioxide, density
    ,pH, sulphates, alcohol]

    predicted = ''

    # creating button for Prediction
    if st.button('Quality of Wine'):
        lst_data = [fixed_acidity, volatile_acidity, citric_acid, residual_sugar,
        chlorides, free_sulfur_dioxide, total_sulfur_dioxide, density
        ,pH, sulphates, alcohol]
        predicted =  wine_qaulity_prediction(lst_data)
        st.header('Your Test Result')
    st.success(predicted)
    lst_data.append(predicted)
    with open('wine_Database.csv','a+', newline='') as f:
        # adding header
        writer = csv.writer(f)
        writer.writerow(lst_data)




if __name__ == '__main__':
    main()
