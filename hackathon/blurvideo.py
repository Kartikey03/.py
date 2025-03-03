import tkinter as tk
from PIL import Image, ImageTk, ImageFilter

# Function to update the background image
def update_background():
    global offset_x, offset_y, scale_factor
    
    # Apply blur effect to the image
    blurred_image = original_image.filter(ImageFilter.GaussianBlur(radius=10))
    
    # Calculate the scaled size of the background image
    scaled_size = (
        original_image.width + scale_factor,
        original_image.height + scale_factor
    )
    
    # Resize the blurred image
    blurred_image = blurred_image.resize(scaled_size)
    
    # Update the background image
    background_image = ImageTk.PhotoImage(blurred_image)
    canvas.itemconfig(background, image=background_image)
    canvas.image = background_image  # Keep a reference to prevent garbage collection
    
    # Update the position of the background image
    offset_x = (offset_x + 1) % original_image.width
    offset_y = (offset_y + 1) % original_image.height
    canvas.coords(background, -offset_x, -offset_y)
    
    # Increase the scale factor
    scale_factor += 1
    
    # Schedule the next update
    root.after(100, update_background)

# Create the Tkinter window
root = tk.Tk()
root.title("Zoom-In Blurred Background")

# Load the original background image
original_image = Image.open("D:\DOWNLOADS\8df20c28-c0c5-4d7f-8583-1e449740d69b.jpg")

# Create a canvas to display the background image
canvas = tk.Canvas(root, width=800, height=600)
canvas.pack()

# Initialize the offset values for movement and the scale factor
offset_x = 0
offset_y = 0
scale_factor = 0

# Display the original background image
background_image = ImageTk.PhotoImage(original_image)
background = canvas.create_image(0, 0, anchor=tk.NW, image=background_image)

# Start updating the background image
update_background()

# Start the Tkinter event loop
root.mainloop()
