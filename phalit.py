import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load your dataset (replace 'your_data.csv' with your actual dataset)
data = pd.read_csv('car details v4.csv')

# Sidebar with slicers
selected_make = st.sidebar.multiselect("Select Make", data['Make'].unique())

# Check if the 'Select Year' slider range is not empty
if not data.empty:
    selected_year = st.sidebar.slider("Select Year", min(data['Year']), max(data['Year']), (min(data['Year']), max(data['Year'])))
else:
    # Default values if the dataset is empty
    selected_year = (min(data['Year']), max(data['Year']))

# Filter data based on slicer values
filtered_data = data[(data['Make'].isin(selected_make)) & (data['Year'].between(selected_year[0], selected_year[1]))]


# Dashboard Title
st.title("Car Sales Dashboard")

st.write("Please select data to be applied to the visuals using the sidebar.")

# 1. Sales Performance by Make
st.header("Sales Performance by Make")
if not filtered_data.empty:
    fig1, ax1 = plt.subplots()
    sns.countplot(x='Make', data=filtered_data, order=filtered_data['Make'].value_counts().index, ax=ax1)

    # Rotate x-axis labels
    ax1.set_xticklabels(ax1.get_xticklabels(), rotation=75, horizontalalignment='right')  # Adjust the rotation angle as needed

    st.pyplot(fig1)
else:
    st.warning("No data available for the selected filters or the dataset is empty.")

# 2. Price Distribution
st.header("Price Distribution")
fig2, ax2 = plt.subplots()
sns.histplot(filtered_data['Price'], bins=30, kde=True, ax=ax2)  # Use the filtered dataset for this plot
ax2.axvline(filtered_data['Price'].median(), color='red', linestyle='dashed', linewidth=2, label='Median')
ax2.axvline(filtered_data['Price'].mean(), color='green', linestyle='dashed', linewidth=2, label='Mean')
ax2.legend()
st.pyplot(fig2)

st.write("1e6 = 10^6 = 10,00,000")

# 5. Popular Models
st.header("Popular Models")
if not filtered_data.empty:
    fig5, ax5 = plt.subplots()
    sns.barplot(x='Model', y='Price', data=filtered_data, order=filtered_data['Model'].value_counts().index[:10], ax=ax5)

    # Rotate x-axis labels
    ax5.set_xticklabels(ax5.get_xticklabels(), rotation=75, horizontalalignment='right')  # Adjust the rotation angle as needed

    st.pyplot(fig5)
else:
    st.warning("No data available for the selected filters or the dataset is empty.")

st.write("1e6 = 10^6 = 10,00,000")

# 6. Transmission Type
st.header("Transmission Type")
fig6, ax6 = plt.subplots()
data['Transmission'].value_counts().plot.pie(autopct='%1.1f%%', ax=ax6)  # Use the full dataset for this plot
ax6.set_ylabel('')
ax6.set_xlabel('')  # Clear x-axis label
ax6.tick_params(axis='x', rotation=90)  # Rotate x-axis labels
st.pyplot(fig6)

# 8. Color Preferences
st.header("Color Preferences")
if not filtered_data.empty:
    fig8, ax8 = plt.subplots()
    sns.countplot(x='Color', data=filtered_data, order=filtered_data['Color'].value_counts().index, ax=ax8)

    # Rotate x-axis labels
    ax8.set_xticklabels(ax8.get_xticklabels(), rotation=45, horizontalalignment='right')  # Adjust the rotation angle as needed

    st.pyplot(fig8)
else:
    st.warning("No data available for the selected filters or the dataset is empty.")

# 10. Drivetrain Comparison
st.header("Drivetrain Comparison")
if not filtered_data.empty:
    fig10, ax10 = plt.subplots()
    filtered_data['Drivetrain'].value_counts().plot.pie(autopct='%1.1f%%', ax=ax10)
    ax10.set_ylabel('')
    st.pyplot(fig10)
else:
    st.warning("No data available for the selected filters or the dataset is empty.")