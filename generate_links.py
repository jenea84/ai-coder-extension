#!/usr/bin/env python3
import os
import pathlib
import shutil
import subprocess
import tempfile
from datetime import datetime

# ==================== КОНФИГУРАЦИЯ ====================
REPO_BASE = "https://raw.githubusercontent.com/jenea84/ai-coder-extension/main"  # Базовый URL для raw-ссылок
REPO_URL = "https://github.com/jenea84/ai-coder-extension.git"  # URL репозитория для клонирования
BRANCH = "main"  # Ветка для синхронизации
SCAN_DIR = "."  # Корень локального проекта
OUTPUT_FILE = "INDEX.md"  # Имя индексного файла
# Папки, которые будут исключены из индекса и синхронизации
IGNORE_DIRS = {
    '__pycache__', '.git', 'node_modules', 'out', 'dist', '.vscode', 'tmp',
}
# Файлы, которые будут исключены из индекса и синхронизации
IGNORE_FILES = {
    '.DS_Store', 'Thumbs.db', '.env', '*.vsix',
}
# Разрешённые расширения файлов для индексации
ALLOWED_EXTENSIONS = {
    '.ts', '.js', '.json', '.md', '.html', '.css', '.py',
}

def should_ignore(path: pathlib.Path) -> bool:
    """
    Проверяет, нужно ли игнорировать файл/папку на основе настроек исключений.
    Используется при обходе локального проекта и при очистке временного клона.
    """
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

def collect_tree_and_files(startpath: str):
    """
    Обходит локальный проект и формирует:
    - tree_lines: структуру для markdown-дерева
    - file_links: список raw-ссылок на файлы
    Только для файлов и папок, не попавших под фильтры should_ignore.
    """
    tree_lines = []
    file_links = []
    startpath = pathlib.Path(startpath)
    for root, dirs, files in os.walk(startpath):
        # Фильтруем папки (исключаем ненужные)
        dirs[:] = [d for d in dirs if not should_ignore(pathlib.Path(root) / d)]
        level = pathlib.Path(root).relative_to(startpath).parts
        indent = '    ' * len(level)
        if level:
            tree_lines.append(f"{indent}├── {level[-1]}/")
        else:
            tree_lines.append("├── ./")
        file_indent = '    ' * (len(level) + 1)
        for f in sorted(files):
            file_path = pathlib.Path(root) / f
            if not should_ignore(file_path):
                tree_lines.append(f"{file_indent}├── {f}")
                rel_file_path = file_path.relative_to(startpath).as_posix()
                raw_url = f"{REPO_BASE}/{rel_file_path}"
                file_links.append(f"- [{f}]({raw_url})")
    return tree_lines, file_links

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

def parse_index_md(index_md_path):
    """
    Парсит структуру из INDEX.md (markdown-дерево) и возвращает:
    - files: список файлов
    - dirs: список папок
    Используется для точного копирования только нужных файлов/папок в репозиторий.
    """
    files = set()
    dirs = set()
    stack = ['.']
    with open(index_md_path, encoding='utf-8') as f:
        for line in f:
            line = line.rstrip()
            if not line.strip().startswith('├──'):
                continue
            indent_level = (len(line) - len(line.lstrip(' '))) // 4
            name = line.strip().replace('├── ', '')
            while len(stack) > indent_level + 1:
                stack.pop()
            parent = '/'.join(stack[1:]) if len(stack) > 1 else '.'
            if name.endswith('/'):
                dir_path = os.path.join(parent, name[:-1]) if parent != '.' else name[:-1]
                dirs.add(dir_path)
                stack.append(name[:-1])
            else:
                file_path = os.path.join(parent, name) if parent != '.' else name
                files.add(file_path)
    return files, dirs

def generate_index_md(target_dir: str = "."):
    """
    Генерирует файл INDEX.md с:
    - Деревом структуры проекта
    - Raw-ссылками на файлы
    - Ссылкой на raw INDEX.md и на сам INDEX.md
    """
    tree_lines, file_links = collect_tree_and_files(target_dir)
    # Ссылки на сам INDEX.md
    index_raw_url = f"{REPO_BASE}/{OUTPUT_FILE}"
    index_github_url = f"https://github.com/jenea84/ai-coder-extension/blob/main/{OUTPUT_FILE}"
    content = (
        f"## 🌳 Структура проекта\n"
        "```markdown\n"
        f"{chr(10).join(tree_lines)}\n"
        "```\n\n"
        f"**[Raw INDEX.md]({index_raw_url})** | **[INDEX.md на GitHub]({index_github_url})**\n\n"
        + '\n'.join(file_links) + '\n'
    )
    with open(os.path.join(target_dir, OUTPUT_FILE), 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"✅ Файл {OUTPUT_FILE} успешно сгенерирован в {target_dir}")

def sync_to_github_safe():
    """
    Клонирует репозиторий во временную папку, полностью очищает его (кроме .git),
    затем копирует только те файлы и папки, которые есть в дереве INDEX.md.
    Пустые папки добавляются с .gitkeep. После этого делает git add/commit/push.
    """
    with tempfile.TemporaryDirectory() as tmpdir:
        print(f"Клонирую репозиторий во временную папку: {tmpdir}")
        orig_dir = os.getcwd()
        subprocess.run(['git', 'clone', REPO_URL, tmpdir], check=True)
        os.chdir(tmpdir)
        subprocess.run(['git', 'checkout', BRANCH], check=True)

        # Удаляем всё кроме .git (репозиторий будет содержать только нужные файлы/папки)
        for item in os.listdir('.'):
            if item == '.git':
                continue
            if os.path.isdir(item):
                shutil.rmtree(item)
            else:
                os.remove(item)

        # Получаем список файлов и папок из локального INDEX.md
        files, dirs = parse_index_md(os.path.join(orig_dir, OUTPUT_FILE))
        # Создаём папки (и .gitkeep для пустых)
        for d in sorted(dirs):
            if d == '.' or d == '':
                continue
            os.makedirs(d, exist_ok=True)
            full_path = os.path.join(d)
            if not any(os.scandir(full_path)):
                open(os.path.join(full_path, ".gitkeep"), "w").close()
        # Копируем файлы
        for f in files:
            src = os.path.join(orig_dir, f)
            dst = f
            dst_dir = os.path.dirname(dst)
            if dst_dir and not os.path.exists(dst_dir):
                os.makedirs(dst_dir, exist_ok=True)
            shutil.copy2(src, dst)
        # Копируем сам INDEX.md
        shutil.copy2(os.path.join(orig_dir, OUTPUT_FILE), OUTPUT_FILE)

        # git add, commit, push
        subprocess.run(['git', 'add', '.'], check=True)
        try:
            subprocess.run(['git', 'commit', '-m', 'sync: full sync from local project'], check=True)
        except subprocess.CalledProcessError:
            print("Нет изменений для коммита, пропускаю git commit.")
        subprocess.run(['git', 'push'], check=True)
        print("✅ Репозиторий успешно синхронизирован!")

        os.chdir(orig_dir)

if __name__ == "__main__":
    generate_index_md()
    sync_to_github_safe()