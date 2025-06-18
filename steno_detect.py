from PIL import Image, ExifTags

# def extract_metadata(image_path):
#     print("📌 Extracting Metadata...")
#     try:
#         image = Image.open(image_path)
#         exif_data = image._getexif()

#         if exif_data:
#             print("\n🗂️ Metadata Found:")
#             for tag_id, value in exif_data.items():
#                 tag = ExifTags.TAGS.get(tag_id, tag_id)
#                 print(f"  {tag}: {value}")
#         else:
#             print("⚠️ No metadata found.")
#     except Exception as e:
#         print(f"❌ Error reading metadata: {e}")


def decode_lsb(image_path):
    print("\n🔍 Checking for Steganography...")
    try:
        img = Image.open(image_path)
        binary_data = ""
        img = img.convert('RGB')
        pixels = list(img.getdata())

        for pixel in pixels:
            for color in pixel:
                binary_data += bin(color)[-1]

        chars = [binary_data[i:i+8] for i in range(0, len(binary_data), 8)]
        decoded = ""
        for ch in chars:
            decoded_char = chr(int(ch, 2))
            if decoded_char == "$":
                break
            decoded += decoded_char

        if decoded.strip():
            print("🚨 Hidden Message Found:")
            print(f"\n📨 \"{decoded.strip()}\"")
            return True, decoded.strip()
        else:
            print("✅ No hidden message detected.")
            return False, ""
    except Exception as e:
        print(f"❌ Error decoding image: {e}")
        return False, ""
