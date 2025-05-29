import tkinter as tk
from tkinter import filedialog, messagebox
from pathlib import Path
from process_images import process_image


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("돌쇠 이미지 처리기")
        self.geometry("300x120")
        self.image_paths = []
        self.output_dir = Path("processed")

        tk.Button(self, text="이미지 선택", command=self.select_images).pack(fill="x", pady=2)
        tk.Button(self, text="출력 폴더 선택", command=self.select_output_dir).pack(fill="x", pady=2)
        tk.Button(self, text="처리 시작", command=self.process).pack(fill="x", pady=2)

    def select_images(self):
        paths = filedialog.askopenfilenames(filetypes=[("Images", "*.jpg *.jpeg *.png *.bmp *.gif")])
        if paths:
            self.image_paths = list(paths)
            messagebox.showinfo("선택 완료", f"{len(self.image_paths)}개 이미지 선택")

    def select_output_dir(self):
        directory = filedialog.askdirectory()
        if directory:
            self.output_dir = Path(directory)

    def process(self):
        if not self.image_paths:
            messagebox.showwarning("오류", "이미지를 먼저 선택하세요")
            return
        self.output_dir.mkdir(parents=True, exist_ok=True)
        for path in self.image_paths:
            process_image(Path(path), self.output_dir)
        messagebox.showinfo("완료", "처리가 완료되었습니다.")


def main():
    app = App()
    app.mainloop()


if __name__ == "__main__":
    main()
