from pathlib import Path
from tempfile import TemporaryDirectory

from nicegui import ui

from process_images import process_image


image_files: list[ui.UploadedFile] = []


def select_images(event: ui.UploadEvent) -> None:
    """Store uploaded image files and show a notification."""
    image_files.extend(event.files)
    ui.notify(f"{len(image_files)}개 이미지 선택")
    progress_label.text = f"진행률: 0 / {len(image_files)}"


def start_process() -> None:
    """Process selected images with progress feedback."""
    if not image_files:
        ui.notify("이미지를 먼저 선택하세요", color="negative")
        return

    out_dir = Path(output_input.value or "processed")
    out_dir.mkdir(parents=True, exist_ok=True)

    with TemporaryDirectory() as temp_dir:
        total = len(image_files)
        for idx, file in enumerate(image_files, 1):
            temp_path = Path(temp_dir) / file.name
            file.save(temp_path)
            process_image(temp_path, out_dir)
            progress.value = idx / total
            progress_label.text = f"진행률: {idx} / {total}"

    ui.notify("처리가 완료되었습니다.")
    image_files.clear()
    progress.value = 0
    progress_label.text = "진행률: 0 / 0"


with ui.column().classes("w-80 m-auto p-4"):
    ui.label("돌쇠 이미지 처리기").classes("text-2xl")
    ui.upload(on_upload=select_images, multiple=True).props("accept='image/*'")
    output_input = ui.input(label="출력 폴더", value="processed")
    ui.button("처리 시작", on_click=start_process)
    progress = ui.linear_progress(value=0)
    progress_label = ui.label("진행률: 0 / 0")


ui.run()

