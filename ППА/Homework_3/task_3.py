from PIL import Image
import os

class JPEGCompressor:
    def __init__(self):
        self.image = None
        self.quality = 100

    def load(self, filepath):
        if not os.path.exists(filepath):
            raise FileNotFoundError()

        try:
            image = Image.open(filepath)
            if image.format != 'JPEG':
                raise TypeError()
            self.image = image
        except (OSError, TypeError):
            raise TypeError()

    def compress(self, quality):
        if self.image is None:
            raise FileNotFoundError()

        if not (0 <= quality <= 95):
            raise ValueError()
        self.quality = quality

    def save(self, file_path):
        if self.image is None:
            raise FileNotFoundError()
        self.image.save(file_path, format='JPEG', quality=self.quality, optimize=True)

# код ниже должен работать, если вы сделали всё верно
compressor = JPEGCompressor()
compressor.load("wallpapers.jpeg")
compressor.compress(10)
compressor.save("wallpapers_compressed.jpeg")

