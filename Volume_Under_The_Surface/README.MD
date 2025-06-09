# Volume Approximation Under Surface \( z = x^2 + y^2 \)

This Python script approximates the volume under the surface defined by \( z = x^2 + y^2 \) over 0 ≤ x, y ≤ 1 , using numerical integration via list comprehensions.

## 📌 Overview

The script divides the unit square into a grid of small rectangles and sums up the contributions from each rectangle using the value of the surface function at its lower-left corner.
This technique is a basic form of Riemann sum approximation.

### Example Output

<p align="center">
  <img src="https://raw.githubusercontent.com/G-alileo/Scientific_Computing/main/Assets/volume_under_the_surface.png" alt="Backend Binary Rain" />
</p>
