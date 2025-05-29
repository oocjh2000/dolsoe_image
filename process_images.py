import argparse
from pathlib import Path
from PIL import Image, ImageOps


def print_progress(idx: int, total: int) -> None:
    """Simple console progress bar."""
    percent = int(idx / total * 100)
    bar_len = 30
    filled = int(bar_len * percent / 100)
    bar = "█" * filled + "-" * (bar_len - filled)
    print(f"\r[{bar}] {percent}% ({idx}/{total})", end="", flush=True)


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

    total = len(args.images)
    for idx, img_path in enumerate(args.images, 1):
        process_image(Path(img_path), out_dir)
        print_progress(idx, total)
    print()


if __name__ == "__main__":
    main()

