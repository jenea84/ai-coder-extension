# AI Coder Extension - Структура репозитория для GitHub

## Файловая структура

```
ai-coder-extension/
├── README.md                          # Главная страница проекта
├── package.json                       # Конфигурация VS Code расширения
├── tsconfig.json                      # TypeScript конфигурация
├── .gitignore                         # Git ignore файл
├── CHANGELOG.md                       # История изменений
├── LICENSE                            # Лицензия
│
├── docs/                              # 📚 Документация
│   ├── architecture.md                # Архитектура проекта
│   ├── detailed-prompt.md             # Детальный промпт разработки
│   ├── current-status.md              # ⭐ ГЛАВНЫЙ файл статуса
│   ├── development-progress.md        # Детальный прогресс
│   ├── decisions.md                   # Архитектурные решения
│   ├── next-steps.md                  # Следующие шаги
│   ├── api-reference.md              # Справочник API
│   └── troubleshooting.md            # Решение проблем
│
├── src/                               # 💻 Исходный код
│   ├── core/                          # Ядро системы
│   ├── modes/                         # Режимы работы
│   ├── commands/                      # Система команд
│   ├── parser/                        # Система парсинга
│   ├── providers/                     # AI провайдеры
│   ├── config/                        # Конфигурация
│   ├── storage/                       # Хранение данных
│   ├── ui/                            # Интерфейс
│   ├── utils/                         # Утилиты
│   └── extension.ts                   # Точка входа
│
├── tests/                             # 🧪 Тесты
│   ├── unit/                          # Unit тесты
│   ├── integration/                   # Интеграционные тесты
│   └── fixtures/                      # Тестовые данные
│
├── resources/                         # 🎨 Ресурсы
│   ├── icons/                         # Иконки
│   └── templates/                     # Шаблоны
│
├── scripts/                           # 🔧 Скрипты
│   ├── build.sh                       # Сборка проекта
│   ├── update-status.sh               # Обновление статуса
│   └── deploy.sh                      # Деплой
│
└── examples/                          # 📖 Примеры использования
    ├── basic-usage.md
    ├── advanced-features.md
    └── code-samples/
```

## Ключевые файлы для ИИ

### 1. README.md - Главная панель управления
```markdown
# 🤖 AI Coder Extension

Умное расширение для VS Code с множественными AI-провайдерами и специализированными режимами программирования.

## 📊 Статус проекта

🚀 **Фаза:** 1 - Основа  
📈 **Прогресс:** 0% (только началось)  
🎯 **Текущая задача:** Создание базовых классов  
⏰ **Последнее обновление:** 2025-06-03  

## 🎯 Быстрая навигация для ИИ

### Документация
- 📋 [Архитектура проекта](docs/architecture.md)
- 📝 [Детальный промпт](docs/detailed-prompt.md)
- ⭐ [**ТЕКУЩИЙ СТАТУС**](docs/current-status.md) ← Начни отсюда!
- 📊 [Прогресс разработки](docs/development-progress.md)
- 🤔 [Принятые решения](docs/decisions.md)

### Код
- 💻 [Исходный код](src/)
- 🧪 [Тесты](tests/)
- 📖 [Примеры](examples/)

## 🔥 Ключевые особенности

- 4 специализированных режима работы (Chat, Edit, Turbo, Debug)
- Система кодированных инструкций (7 основных кодов)
- Множественные AI-провайдеры (OpenAI, Anthropic, Google, локальные)
- Умное управление контекстом и итоги сессий
- Система откатов изменений
- Подсветка различий в коде

## 🛠 Фазы разработки

- [ ] **Фаза 1:** Основа (BaseMode, ChatManager, простой UI)
- [ ] **Фаза 2:** Команды и парсер 
- [ ] **Фаза 3:** Продвинутые функции (контекст, откаты)
- [ ] **Фаза 4:** Полировка и оптимизация

## 🤝 Работа с ИИ

Для новых диалогов с ИИ используйте:

```
Привет! Работаю над AI Coder Extension.

Статус: https://github.com/username/ai-coder-extension/blob/main/docs/current-status.md
Архитектура: https://github.com/username/ai-coder-extension/blob/main/docs/architecture.md

Нужна помощь с: [ваша задача]
```
```

### 2. docs/current-status.md - Центр управления
```markdown
# 📊 AI Coder Extension - Текущий статус

**Дата обновления:** 2025-06-03 12:00  
**Фаза:** 1 - Основа  
**Прогресс:** 0%  
**Активный разработчик:** [ваше имя]  

## 🎯 Текущая задача

**Создание базовых классов системы**

Сейчас работаем над фундаментом проекта - базовыми классами, которые будут основой всей архитектуры.

### Приоритет сегодня:
1. BaseMode класс
2. Command интерфейс  
3. BaseProvider класс

## ✅ Выполнено

Пока ничего - только что начали проект!

## ⏳ В процессе

- [ ] Настройка структуры проекта
- [ ] Создание базовых TypeScript файлов

## 📋 Следующие шаги

1. Создать базовые классы (BaseMode, Command, BaseProvider)
2. Реализовать ChatManager
3. Создать простейший UI
4. Добавить OpenAI провайдер

## 🤔 Текущие вопросы/проблемы

- Как лучше организовать dependency injection между компонентами?
- Стоит ли использовать декораторы для команд?
- Какой паттерн лучше для управления состоянием режимов?

## 🔗 Полезные ссылки

- [Архитектура](./architecture.md)
- [Детальный промпт](./detailed-prompt.md)
- [План разработки](./development-progress.md)

---
*Этот файл обновляется после каждой сессии разработки*
```

### 3. scripts/update-status.sh - Автоматизация
```bash
#!/bin/bash

# Скрипт для быстрого обновления статуса проекта

echo "🔄 Обновление статуса AI Coder Extension..."

# Получаем текущую дату
DATE=$(date '+%Y-%m-%d %H:%M')

# Обновляем дату в current-status.md
sed -i "s/\*\*Дата обновления:\*\* .*/\*\*Дата обновления:\*\* $DATE/" docs/current-status.md

# Добавляем все изменения
git add .

# Коммитим с сообщением
if [ -n "$1" ]; then
    git commit -m "📊 Статус: $1"
else
    git commit -m "📊 Обновление статуса проекта"
fi

# Отправляем на GitHub
git push origin main

echo "✅ Статус успешно обновлен!"
echo "🔗 Ссылка: https://github.com/username/ai-coder-extension/blob/main/docs/current-status.md"
```

### 4. .gitignore
```gitignore
# Node modules
node_modules/

# VS Code
.vscode/settings.json
.vscode/launch.json

# Build outputs
out/
dist/
*.vsix

# OS
.DS_Store
Thumbs.db

# Logs
*.log

# Temporary files
tmp/
temp/
```

## 🚀 Инструкция по созданию репозитория

### Шаг 1: Создание на GitHub
1. Идите на GitHub.com
2. Нажмите "New repository"
3. Название: `ai-coder-extension`
4. Описание: "Smart VS Code extension with multiple AI providers and specialized coding modes"
5. Сделайте публичным (для доступа ИИ)
6. Добавьте README.md

### Шаг 2: Клонирование и настройка
```bash
git clone https://github.com/username/ai-coder-extension.git
cd ai-coder-extension

# Создаем структуру папок
mkdir -p docs src tests resources scripts examples
mkdir -p src/{core,modes,commands,parser,providers,config,storage,ui,utils}

# Копируем файлы (из artifact)
# Загружаем ваши существующие документы
```

### Шаг 3: Первый коммит
```bash
git add .
git commit -m "🎉 Инициализация AI Coder Extension проекта"
git push origin main
```

## 📝 Использование с ИИ

После создания репозитория, каждый новый диалог с ИИ будет выглядеть так:

```
Привет! Продолжаю работу над AI Coder Extension.

Статус: https://github.com/username/ai-coder-extension/blob/main/docs/current-status.md

Нужна помощь с созданием BaseMode класса.
```

И всё! ИИ сразу поймет контекст, текущее состояние и что нужно делать.