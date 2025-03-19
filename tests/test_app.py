import unittest
from fastapi.testclient import TestClient
from main import app
from io import BytesIO
from PIL import Image

# Create a test client
client = TestClient(app)

# Helper function to create a dummy image
def create_dummy_image():
    img = Image.new("RGB", (224, 224), color=(255, 255, 255))
    img_bytes = BytesIO()
    img.save(img_bytes, format="JPEG")
    img_bytes.seek(0)
    return img_bytes

class TestFastAPIApp(unittest.TestCase):

    def test_predict_valid_image(self):
        """Test if the /predict endpoint works with a valid image."""
        response = client.post("/predict/", files={"file": ("test.jpg", create_dummy_image(), "image/jpeg")})
        self.assertEqual(response.status_code, 200)
        self.assertIn("prediction", response.json())

    def test_predict_missing_file(self):
        """Test if the /predict endpoint returns 422 when no file is provided."""
        response = client.post("/predict/")
        self.assertEqual(response.status_code, 422)

if __name__ == "__main__":
    unittest.main()
