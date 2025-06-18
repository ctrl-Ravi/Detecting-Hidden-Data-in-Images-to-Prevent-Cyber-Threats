
from steno_detect import decode_lsb

def main():
    print("🔐 Welcome to Image Threat Scanner")
    image_path = input("🖼️ Enter image path to scan: ")



    found = decode_lsb(image_path)

    print("\n🧾 RESULT:")
    if found:
        print("⚠️ Status: Suspicious image (hidden content found)")
    else:
        print("✅ Status: Clean image (no hidden content)")

if __name__ == "__main__":
    main()

