import PIL.Image as Image
import pytesseract
from gtts import gTTS

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Function for converting an image to sound
def image_to_sound(path_to_image):
  """
  Converts an image to sound using OCR and speech synthesis.

  Args:
    path_to_image: The path to the image file.

  Returns:
    True if the image was converted to sound successfully, False otherwise.
  """

  try:
    # Load the image
    loaded_image = Image.open(path_to_image)

    # Extract the text from the image
    decoded_text = pytesseract.image_to_string(loaded_image)

    # Clean up the extracted text
    cleaned_text = " ".join(decoded_text.split("\n"))

    # Convert the text to speech
    sound = gTTS(cleaned_text, lang="en")

    # Save the sound to an MP3 file
    sound.save("sound.mp3")

    return True
  except Exception as bug:
    print("The bug thrown while executing the code\n", bug)
    return False

# If the script is run directly, convert the first image in the current directory to sound
if __name__ == "__main__":
  image_to_sound("Capture_1.jpg")
