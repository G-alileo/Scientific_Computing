# Weekly Temperature Plotter

This Python script uses `matplotlib` to visualize temperature readings recorded over a week. It generates a simple line chart with custom styling, plotting daily temperatures against corresponding weekdays.

## 📌 Overview

The script helps you understand temperature trends across a week using a visual line plot. It utilizes the `matplotlib` library to generate the chart and customizes the appearance for better readability and presentation.

### Example Output

The output is a line graph with:
- Days on the X-axis (`Mon` through `Sun`)
- Temperature values on the Y-axis
- A green dotted line connecting star-shaped markers


<p align="center">
  <img src="https://raw.githubusercontent.com/G-alileo/Scientific_Computing/main/Assets/temperature_graph.png" alt="Backend Binary Rain" width="100%" height="300" />
</p>

## 🧠 How It Works

1. **Data Initialization**:
   - `temperatures`: A list of temperature values for each day.
   - `days`: A list of day labels representing each day of the week.

2. **Plot Customization**:
   - Uses `marker='*'` for each point.
   - Applies a `dotted` line style with green color.
   - Sets marker size and line width for clarity.
   - Adds grid lines and axis labels.
   - Displays the chart using `plt.show()`.