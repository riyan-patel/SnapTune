# trans_download_heic.py
from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image
import pyheif
import os

def compute_caption(image_path):
    # Load the processor and model
    processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
    model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

    # Check if the path exists
    if os.path.exists(image_path):
        # Check the file extension and handle accordingly
        if image_path.lower().endswith('.heic'):
            # Read HEIC image
            heif_file = pyheif.read(image_path)
            # Convert to a PIL Image
            image = Image.frombytes(
                heif_file.mode, 
                heif_file.size, 
                heif_file.data,
                "raw",
                heif_file.mode,
                heif_file.stride,
            )
        else:
            # Open the image directly for other formats
            image = Image.open(image_path)

        # Preprocess the image
        inputs = processor(image, return_tensors="pt")

        # Generate a caption for the image
        output = model.generate(
            **inputs,
            do_sample=True, 
            max_length=50,  
            num_beams=10,     
            temperature=2.0    
        )

        # Decode the generated token IDs to a string
        caption = processor.decode(output[0], skip_special_tokens=True)
        
        # Ensure we return a valid caption
        return caption if caption else "No caption generated."  # Default message if caption is empty
    else:
        print(f"File does not exist at: {image_path}")
        return "No caption generated."
