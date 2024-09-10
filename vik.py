import seaborn as sns
import streamlit as st
import matplotlib.pyplot as plt

st.title("hi")

# loading dataset
data = sns.load_dataset("iris")

# function to draw the graph
def graph():
    sns.lineplot(x="sepal_length", y="sepal_width", data=data)

# create a figure for the plot
fig, axs = plt.subplots(3, 1, figsize=(5, 15))

# draw each plot on a subplot
plt.subplot2grid((7, 1), (0, 0), rowspan=2, colspan=1)
graph()

plt.subplot2grid((7, 1), (2, 0), rowspan=2, colspan=1)
graph()

plt.subplot2grid((7, 1), (4, 0), rowspan=2, colspan=1)
graph()

# display the plots in Streamlit
st.pyplot(plt)

# clear the figure after plotting
plt.clf()

# # importing packages
# import seaborn as sns
# import matplotlib.pyplot as plt

# # loading dataset
# data = sns.load_dataset("iris")


# def graph():
#     sns.lineplot(x="sepal_length", y="sepal_width", data=data)
#     #plt.show()

# # adding the subplots
# axes1 = plt.subplot2grid(
#     (7, 1), (0, 0), rowspan=2, colspan=1)
# graph()

# axes2 = plt.subplot2grid(
#     (7, 1), (2, 0), rowspan=2, colspan=1)
# graph()

# axes3 = plt.subplot2grid(
#     (7, 1), (4, 0), rowspan=2, colspan=1)
# graph()


# plt.show()