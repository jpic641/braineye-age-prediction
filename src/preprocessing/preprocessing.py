import torch
from torchvision import transforms
from PIL import Image

def preprocess_image(image_path):
    """
    Preprocessing pipeline for a single image 

    Args:
        image_path (str or os.path): Path for input image

    Returns:
        image_tensor (torch.Tensor): Tensor of preprocessed input image
    """
    # Define preprocessing steps
    preprocess = transforms.Compose([
        transforms.Resize(224),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
    ])
    
    # Load image
    image = Image.open(image_path).convert("RGB")
    
    # Preprocess and return tensor
    image_tensor = preprocess(image).unsqueeze(0)
    return image_tensor

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python input_preprocessing.py <image_path>")
        sys.exit(1)
    
    image_path = sys.argv[1]
    tensor = preprocess_image(image_path)
    torch.save(tensor, "preprocessed_image.pt")
    print("Image preprocessed and saved as preprocessed_image.pt")