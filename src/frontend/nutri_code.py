import streamlit as st
import matplotlib.pyplot as plt


def generate_nutri_score_image(letter):
    """Generates a Nutri-Score image based on the given score."""

    # Define color mappings for each letter grade
    color_map = {
        'A': '#008000',  # Dark green
        'B': '#90EE90',  # Light green
        'C': '#FFFF00',  # Yellow
        'D': '#FFA500',  # Orange
        'E': '#FF0000'  # Red
    }

    # Create a figure and axis
    fig, ax = plt.subplots(figsize=(4, 1))

    # Create a rectangle for the background
    rect = plt.Rectangle((0, 0), 5, 1, color='white')
    ax.add_patch(rect)

    # Create a border around the Nutri-Score image
    border_rect = plt.Rectangle((0, 0), 5, 1, color='black', linewidth=1)
    ax.add_patch(border_rect)

    # Create rectangles for only specified letters
    x_pos = 0
    for l in 'ABCDE':
        if l == letter:
            color = color_map.get(l, 'gray')  # Highlight the selected letter
            rect = plt.Rectangle((x_pos, 0), 3, 3, color=color, linewidth=5)
        else:
            color = color_map.get(l, 'gray')  # Use color map for other letters
            rect = plt.Rectangle((x_pos, 0), 1, 1, color='gray')
        ax.add_patch(rect)

        # Add the letter inside the rectangle
        ax.text(x_pos + 0.5, 0.5, l, ha='center', va='center', color='black', fontsize=12, fontweight='bold')
        x_pos += 1

    # Set axis limits and hide ticks
    ax.set_xlim(0, 5)
    ax.set_ylim(0, 1)
    ax.axis('off')

    # Add title
    ax.set_title('Nutri-Score', fontsize=14)

    # Display the image
    st.pyplot(fig)

# # # Example usage:
# score = st.text_input(label="Enter the score")  # Replace with the desired score

# if score:
#     generate_nutri_score_image(score)