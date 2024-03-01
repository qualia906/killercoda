import sys

def check_images_removed():
    allowed_image = "registry:2"
    all_removed = True

    for line in sys.stdin:
        image = line.strip()
        if image and image != allowed_image:
            print(f"Image is not allowed: {image}")
            all_removed = False

    return all_removed

if __name__ == "__main__":
    if check_images_removed():
        print("registry:2 is the only image left")
        sys.exit(0)
    else:
        sys.exit(1)
