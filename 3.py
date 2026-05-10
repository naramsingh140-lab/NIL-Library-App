from PIL import Image, ImageDraw
import os

# Create Icon (Aqua N on Black)
icon = Image.new('RGB', (1024, 1024), color=(0, 0, 0))
draw = ImageDraw.Draw(icon)
draw.line([(300, 800), (300, 200), (700, 800), (700, 200)], fill=(0, 255, 255), width=80)
icon.save('icon.png')

# Create Splash (Minimal Branding)
splash = Image.new('RGB', (1080, 1920), color=(0, 0, 0))
draw = ImageDraw.Draw(splash)
draw.line([(450, 1000), (450, 920), (630, 1000), (630, 920)], fill=(0, 255, 255), width=20)
splash.save('splash.png')

print("Assets Generated: icon.png and splash.png")