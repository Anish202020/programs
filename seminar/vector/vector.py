import svgwrite

# Create an SVG drawing
dwg = svgwrite.Drawing('example.svg', profile='tiny')

# Add a circle
dwg.add(dwg.circle(center=(50, 50), r=40, stroke=svgwrite.rgb(10, 10, 16, '%'), fill='red'))

# Add a rectangle
dwg.add(dwg.rect(insert=(100, 50), size=(50, 100), stroke=svgwrite.rgb(10, 10, 16, '%'), fill='blue'))

# Add a line
dwg.add(dwg.line(start=(0, 0), end=(150, 150), stroke=svgwrite.rgb(10, 10, 16, '%')))

# Save the SVG file
dwg.save()

print("Vector image created and saved as 'example.svg'")
