import cv2
import easyocr
from google import genai

# Pass your API key directly as a string into the Client initialization
client = genai.Client(api_key="___")

# Setting up Variables
coordinates = (50, 250)      # (X, Y) position of the bottom-left corner of the text
font = cv2.FONT_HERSHEY_SIMPLEX
font_scale = 0.5
color = (0, 255, 0)          # Green color in BGR format
thickness = 2
line_type = cv2.LINE_AA      # Anti-aliased line for smoother text curves
imagepath = r'StreetSigns\newtest.jpg'
myimage = cv2.imread(imagepath)

# Setting up English and Chinese Text Detection
reader = easyocr.Reader(['en'])
results = reader.readtext(myimage)

cantoneseReader = easyocr.Reader(['ch_tra', 'en'])
newresults = reader.readtext(myimage)

#print(newresults)
extracted_lines = []
for (points, text, confidence) in newresults:
    p1 = (int(points[0][0]), int(points[0][1]))
    p2 = (int(points[2][0]), int(points[2][1]))
    rectangles = cv2.rectangle(myimage, p1,p2, (100,200,100), 3)
    # Add text to the image
    cv2.putText(myimage, text, p1, font, font_scale, color, thickness, line_type)
    print(text)
    extracted_lines.append(text)

# For Chinese, joining with an empty string or a space works best to form continuous text
full_chinese_text = "\n".join(extracted_lines)
interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input=f"Translate this from Traditional Chinese to English {full_chinese_text}"
)
cv2.imshow("screen", myimage)
print(results)
cv2.waitKey(0)
