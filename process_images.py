import argparse
from pathlib import Path
from PIL import Image, ImageOps


def process_image(input_path: Path, output_dir: Path):
    """Load an image, rotate based on EXIF orientation, strip EXIF, and save."""
    img = Image.open(input_path)
    img = ImageOps.exif_transpose(img)
    output_path = output_dir / input_path.name
    # Save without EXIF metadata
    img.save(output_path)
    print(f"Processed {input_path} -> {output_path}")


def main():
    parser = argparse.ArgumentParser(description="Rotate images based on EXIF and strip metadata")
    parser.add_argument("images", nargs="+", help="Input image files")
    parser.add_argument("-o", "--output", default="processed", help="Output directory")
    args = parser.parse_args()

    out_dir = Path(args.output)
    out_dir.mkdir(parents=True, exist_ok=True)

    for img_path in args.images:
        process_image(Path(img_path), out_dir)


if __name__ == "__main__":
    main()

