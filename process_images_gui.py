import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from pathlib import Path
from process_images import process_image


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("돌쇠 이미지 처리기")
        self.geometry("320x170")
        self.image_paths = []
        self.output_dir = Path("processed")

        tk.Button(self, text="이미지 선택", command=self.select_images).pack(fill="x", pady=2)
        tk.Button(self, text="출력 폴더 선택", command=self.select_output_dir).pack(fill="x", pady=2)
        tk.Button(self, text="처리 시작", command=self.process).pack(fill="x", pady=2)

        self.progress = ttk.Progressbar(self, maximum=100)
        self.progress.pack(fill="x", pady=2)
        self.progress_label = tk.Label(self, text="진행률: 0 / 0")
        self.progress_label.pack(pady=2)

    def select_images(self):
        paths = filedialog.askopenfilenames(filetypes=[("Images", "*.jpg *.jpeg *.png *.bmp *.gif")])
        if paths:
            self.image_paths = list(paths)
            messagebox.showinfo("선택 완료", f"{len(self.image_paths)}개 이미지 선택")
            self.progress_label.config(text=f"진행률: 0 / {len(self.image_paths)}")

    def select_output_dir(self):
        directory = filedialog.askdirectory()
        if directory:
            self.output_dir = Path(directory)

    def process(self):
        if not self.image_paths:
            messagebox.showwarning("오류", "이미지를 먼저 선택하세요")
            return
        self.output_dir.mkdir(parents=True, exist_ok=True)
        total = len(self.image_paths)
        self.progress.configure(maximum=total, value=0)
        for idx, path in enumerate(self.image_paths, 1):
            process_image(Path(path), self.output_dir)
            self.progress['value'] = idx
            self.progress_label.config(text=f"진행률: {idx} / {total}")
            self.update_idletasks()
        messagebox.showinfo("완료", "처리가 완료되었습니다.")


def main():
    app = App()
    app.mainloop()


if __name__ == "__main__":
    main()
