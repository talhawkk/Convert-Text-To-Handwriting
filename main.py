from PIL import Image, ImageDraw, ImageFont

img = Image.new('RGB', (600, 200), color='white')

draw = ImageDraw.Draw(img)
try:
    font_path = "path_to_your_font.ttf"  
    font = ImageFont.truetype("Caveat-VariableFont_wght.ttf", 40)

    text=input("Enter Test that you want to convert into hanwriting : ")

    draw.text((10, 50), text, font=font, fill=(0, 0, 0))
    img.save("handwritten_text.png")
except Exception as e:
    print(f"Error occured : {e}")
