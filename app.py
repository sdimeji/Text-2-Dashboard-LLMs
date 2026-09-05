import streamlit as st
st.set_option('deprecation.showPyplotGlobalUse', False)
st.title('E-commerce Company[insights]')
st.write('Here is our LLM generated dashboard')
import matplotlib.pyplot as plt

# Data
cities = ['Suizhou', 'Bailleval', 'Mairiporã', 'Melle', 'Barbacena']
cancellation_rates = [76.47, 75.00, 75.00, 75.00, 60.00]

# Plot
plt.figure(figsize=(10, 6))
plt.bar(cities, cancellation_rates, color='skyblue')
plt.xlabel('Cities')
plt.ylabel('Cancellation Rate (%)')
plt.title('Top 5 Cities with Highest Order Cancellation Percentage in 2024')
plt.ylim(0, 100)  # Set y-axis limit to 100%
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Show plot
plt.tight_layout()

st.pyplot()
