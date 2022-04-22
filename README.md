# Wine_quality_prediction
Wine quality prediction
The two datasets are related to red and white variants of the Portuguese "Vinho Verde" wine. 
These datasets can be viewed as classification or regression tasks. The classes are ordered and not balanced. Here In this project, I have used classification algorithm for making prediction from 1 to 8.
- **The data table have following features and  target classes**
1. Fixed acidity
2. Volatile acidity
3. citric acid
4. residual sugar
5. chlorides
6. free sulfur dioxide
7. total sulfur dioxide
8. density
9. pH
10. sulphates
11.  alcohol

**Output variable (based on sensory data):**

12 - quality (score between 1 to 8)

- Here quality score of wine 3 represent very poor quality and 8 excellent quality of wine, and remaining classes in between. pyth
- In this predictive model, I saved model weights with help of joblib library with the extentsion **.dat** (binary file).
- Which is used to deploy model without data training again and again.
- I deploied this model with streamlit python library.
