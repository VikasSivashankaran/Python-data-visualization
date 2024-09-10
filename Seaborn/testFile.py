import seaborn as sns
import streamlit as st
import matplotlib.pyplot as plt

data = sns.load_dataset("iris")

# draw lineplot
sns.lineplot(x="sepal_length", y="sepal_width", data=data)
plt.title('Title using Matplotlib Function')
st.pyplot(plt)