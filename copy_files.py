import argparse
from pathlib import Path
import shutil

def parse_args():
    parser = argparse.ArgumentParser(description="Копіювання файлів з сортуванням за розширеннями.")
    parser.add_argument("--source", type=Path, required=True, help="Шлях до вихідної директорії")
    parser.add_argument("--dest", type=Path, default=Path("dist"), help="Шлях до директорії призначення")
    return parser.parse_args()

def copy_files(src, dst):
    try:
        for item in src.iterdir():
            if item.is_dir():
                copy_files(item, dst)  # Рекурсивний виклик для піддиректорії
            else:
                # Отримання розширення файлу
                ext = item.suffix[1:]  # Видаляємо крапку перед розширенням
                if not ext:  # Якщо у файлу немає розширення
                    ext = "no_extension"
                # Створюємо піддиректорію для розширення, якщо вона не існує
                target_dir = dst / ext
                target_dir.mkdir(parents=True, exist_ok=True)
                # Копіюємо файл у відповідну піддиректорію
                shutil.copy2(item, target_dir / item.name)
                print(f"Скопійовано {item} до {target_dir / item.name}")
    except Exception as e:
        print(f"Помилка при копіюванні файлів: {e}")

def main():
    args = parse_args()
    print(f"Копіювання з {args.source} до {args.dest}")
    args.dest.mkdir(parents=True, exist_ok=True)  # Створюємо директорію призначення, якщо вона не існує
    copy_files(args.source, args.dest)

if __name__ == "__main__":
    main()


    
   # python copy_files.py --source C:\Users\Nataliia\git\goit-algo-hw-03\test --dest C:\Users\Nataliia\git\goit-algo-hw-03\dist
