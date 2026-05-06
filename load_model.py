from PIL import Image
from transformers import BlipProcessor, BlipForConditionalGeneration

# Path to the fine-tuned model
model_path = "./blip-finetuned-epoch-5"

# Load the fine-tuned model and processor
model = BlipForConditionalGeneration.from_pretrained(model_path)
processor = BlipProcessor.from_pretrained(model_path)

# Load an image for prediction
image_path = "download.png"
image = Image.open(image_path).convert("RGB")

# Prepare the inputs
inputs = processor(images=image, return_tensors="pt")
            
# Generate a caption with randomness
outputs = model.generate(
    inputs["pixel_values"],
    min_length=2,               # Set minimum length of the caption
    max_length=50,              # Set maximum length of the caption
    temperature=0.9,            # Set the temperature for sampling
    top_k=50,                    # Consider the top 5 probable tokens
    do_sample=True              # Enable sampling to add randomness
)

# Decode the generated caption
caption = processor.batch_decode(outputs, skip_special_tokens=True)[0]

print(f"Generated Caption: {caption}")
