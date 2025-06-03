import os
import pathlib
import shutil
import subprocess
import tempfile

# --- НАСТРОЙКИ ---
REPO_URL = "git@github.com:jenea84/ai-coder-extension.git"  # или https://...
BRANCH = "main"
LOCAL_PROJECT = "."  # путь к вашему локальному проекту (обычно ".")
IGNORE_DIRS = {
    '__pycache__', '.git', 'node_modules', 'out', 'dist', '.vscode', 'tmp',
}
IGNORE_FILES = {
    '.DS_Store', 'Thumbs.db', '.env', '*.vsix',
}
ALLOWED_EXTENSIONS = {
    '.ts', '.js', '.json', '.md', '.html', '.css', '.py',
}

def should_ignore(path: pathlib.Path) -> bool:
    if path.name.startswith('.'):
        return True
    if path.is_dir() and path.name in IGNORE_DIRS:
        return True
    if not path.is_dir():
        if path.name in IGNORE_FILES:
            return True
        for pattern in IGNORE_FILES:
            if pattern.startswith('*') and path.name.endswith(pattern[1:]):
                return True
        if path.suffix.lower() not in ALLOWED_EXTENSIONS:
            return True
    return False

def get_synced_paths(startpath: str):
    synced_files = set()
    synced_dirs = set()
    startpath = pathlib.Path(startpath)
    for root, dirs, files in os.walk(startpath):
        dirs[:] = [d for d in dirs if not should_ignore(pathlib.Path(root) / d)]
        rel_root = pathlib.Path(root).relative_to(startpath)
        if rel_root != pathlib.Path('.'):
            synced_dirs.add(rel_root.as_posix())
        for f in files:
            file_path = pathlib.Path(root) / f
            if not should_ignore(file_path):
                synced_files.add(file_path.relative_to(startpath).as_posix())
    return synced_files, synced_dirs

def sync_to_github_safe():
    with tempfile.TemporaryDirectory() as tmpdir:
        print(f"Клонирую репозиторий во временную папку: {tmpdir}")
        subprocess.run(['git', 'clone', REPO_URL, tmpdir], check=True)
        os.chdir(tmpdir)
        subprocess.run(['git', 'checkout', BRANCH], check=True)

        # Удаляем всё кроме .git и исключённых
        for item in os.listdir('.'):
            if item == '.git' or should_ignore(pathlib.Path(item)):
                continue
            if os.path.isdir(item):
                shutil.rmtree(item)
            else:
                os.remove(item)

        # Копируем только нужные файлы и папки из локального проекта
        synced_files, synced_dirs = get_synced_paths(LOCAL_PROJECT)
        for d in sorted(synced_dirs):
            os.makedirs(d, exist_ok=True)
        for f in synced_files:
            src = os.path.join(LOCAL_PROJECT, f)
            dst = f
            dst_dir = os.path.dirname(dst)
            if dst_dir and not os.path.exists(dst_dir):
                os.makedirs(dst_dir, exist_ok=True)
            shutil.copy2(src, dst)

        # git add, commit, push
        subprocess.run(['git', 'add', '.'], check=True)
        subprocess.run(['git', 'commit', '-m', 'sync: full sync from local project'], check=True)
        subprocess.run(['git', 'push'], check=True)
        print("✅ Репозиторий успешно синхронизирован!")

if __name__ == "__main__":
    sync_to_github_safe()