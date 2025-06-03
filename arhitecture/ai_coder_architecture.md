# AI Coder - Финальная архитектура проекта

## Структура проекта

```
ai-coder/
├── src/
│   ├── core/                          # Ядро системы
│   │   ├── ChatManager.ts             # Управление режимами чата и переключением
│   │   ├── MessageManager.ts          # Обработка сообщений (ввод/вывод, история)
│   │   ├── HistoryManager.ts          # Управление историей чатов
│   │   ├── ContextManager.ts          # Управление контекстом для ИИ
│   │   └── ExtensionContext.ts        # Контекст расширения VS Code
│   │
│   ├── modes/                         # Режимы работы с ИИ
│   │   ├── base/
│   │   │   ├── BaseMode.ts            # Базовый класс для всех режимов
│   │   │   └── ModeRegistry.ts        # Реестр режимов
│   │   ├── ChatMode.ts                # Режим "Чат" (только базовые команды)
│   │   ├── EditMode.ts                # Режим "Редактирование" + специальные команды
│   │   ├── TurboMode.ts               # Режим "Турбо" + быстрые команды
│   │   └── DebugMode.ts               # Режим "Отладка" + команды отладки
│   │
│   ├── commands/                      # Система команд по режимам
│   │   ├── base/
│   │   │   ├── Command.ts             # Интерфейс команды
│   │   │   ├── CommandRegistry.ts     # Реестр команд
│   │   │   └── CommandExecutor.ts     # Выполнитель команд
│   │   │
│   │   ├── chat/                      # Команды для режима "Чат"
│   │   │   └── ChatCommands.ts        # Базовые команды общения
│   │   │
│   │   ├── edit/                      # Команды для "Редактирования"
│   │   │   ├── EditCommands.ts        # Редактирование, Анализ проекта
│   │   │   ├── RefactorCommands.ts    # Рефакторинг, Оптимизация
│   │   │   ├── FileCommands.ts        # Работа с файлами
│   │   │   └── CompareCommands.ts     # Сравнить файлы
│   │   │
│   │   ├── turbo/                     # Команды для "Турбо"
│   │   │   ├── TurboCommands.ts       # Турбо режим
│   │   │   ├── QuickCommands.ts       # Быстрый анализ
│   │   │   └── ExpressCommands.ts     # Экспресс-правки
│   │   │
│   │   └── debug/                     # Команды для "Отладки"
│   │       ├── DebugCommands.ts       # Отладка, Анализ проекта
│   │       ├── BugCommands.ts         # Найти баги, Найти баги в файле
│   │       ├── TestCommands.ts        # Создать тесты, Тестирование парсера
│   │       └── AnalysisCommands.ts    # Анализировать файл
│   │
│   ├── parser/                        # Система парсинга и кодированных команд
│   │   ├── core/
│   │   │   ├── CodeParser.ts          # Основной парсер кода
│   │   │   ├── InstructionParser.ts   # Парсинг кодированных инструкций
│   │   │   ├── ContextExtractor.ts    # Извлечение контекста файлов
│   │   │   └── DiffCalculator.ts      # Вычисление различий в коде
│   │   │
│   │   ├── instructions/              # Система кодированных инструкций
│   │   │   ├── InstructionCodes.ts    # Коды операций (12345, 34567, ...)
│   │   │   ├── FileOperations.ts      # Операции с файлами
│   │   │   ├── CodeOperations.ts      # Операции с кодом
│   │   │   └── InstructionExecutor.ts # Выполнение инструкций
│   │   │
│   │   ├── languages/                 # Парсеры языков программирования
│   │   │   ├── JavaScriptParser.ts    # Приоритет: JavaScript
│   │   │   ├── TypeScriptParser.ts    # Приоритет: TypeScript
│   │   │   ├── ReactParser.ts         # Приоритет: React/JSX
│   │   │   ├── VueParser.ts           # Приоритет: Vue
│   │   │   ├── HTMLParser.ts          # Приоритет: HTML
│   │   │   ├── CSSParser.ts           # Приоритет: CSS/SCSS
│   │   │   └── GenericParser.ts       # Остальные языки
│   │   │
│   │   └── diff/                      # Система подсветки изменений
│   │       ├── DiffHighlighter.ts     # Подсветка различий
│   │       ├── LineHighlighter.ts     # Построчная подсветка
│   │       └── DiffRenderer.ts        # Отображение diff в UI
│   │
│   ├── context/                       # Система управления контекстом
│   │   ├── ContextManager.ts          # Главный менеджер контекста
│   │   ├── MessageContext.ts          # Контекст последних N сообщений
│   │   ├── SessionSummary.ts          # Генерация итогов сессии для контекста
│   │   ├── FileContextProvider.ts     # Контекст открытых файлов
│   │   ├── ProjectContextProvider.ts  # Контекст структуры проекта
│   │   └── WorkspaceContextProvider.ts # Контекст workspace
│   │
│   ├── rollback/                      # Система откатов изменений
│   │   ├── RollbackManager.ts         # Менеджер откатов
│   │   ├── ChangePoint.ts             # Точка изменений для отката
│   │   ├── FileSnapshot.ts            # Снимок состояния файла
│   │   └── RollbackStorage.ts         # Хранение точек отката
│   │
│   ├── providers/                     # AI провайдеры
│   │   ├── base/
│   │   │   ├── BaseProvider.ts        # Базовый класс провайдера
│   │   │   └── ProviderInterface.ts   # Интерфейс провайдера
│   │   ├── implementations/
│   │   │   ├── OpenAIProvider.ts      # OpenAI (GPT-4, GPT-3.5)
│   │   │   ├── AnthropicProvider.ts   # Anthropic (Claude)
│   │   │   ├── GoogleProvider.ts      # Google (Gemini)
│   │   │   ├── LocalProvider.ts       # Локальные модели (Ollama)
│   │   │   └── AzureProvider.ts       # Azure OpenAI
│   │   └── ProviderManager.ts         # Менеджер провайдеров
│   │
│   ├── config/                        # Конфигурация и настройки
│   │   ├── models/
│   │   │   ├── ModelDefinitions.ts    # Определения моделей по провайдерам
│   │   │   ├── ModelConfig.ts         # Конфигурация моделей
│   │   │   └── ModelCapabilities.ts   # Возможности моделей
│   │   │
│   │   ├── settings/
│   │   │   ├── SettingsManager.ts     # Главный менеджер настроек
│   │   │   ├── ProviderSettings.ts    # Настройки провайдеров/API ключей
│   │   │   ├── ContextSettings.ts     # Настройки контекста (N сообщений)
│   │   │   ├── ParserSettings.ts      # Настройки парсера
│   │   │   ├── UISettings.ts          # Настройки интерфейса
│   │   │   └── RollbackSettings.ts    # Настройки системы откатов
│   │   │
│   │   └── defaults/
│   │       ├── DefaultCommands.ts     # Команды по умолчанию для режимов
│   │       ├── DefaultContext.ts      # Контекст по умолчанию
│   │       ├── DefaultModels.ts       # Модели по умолчанию
│   │       └── DefaultInstructions.ts # Инструкции по умолчанию
│   │
│   ├── storage/                       # Система хранения данных
│   │   ├── ChatStorage.ts             # Хранение чатов
│   │   ├── SettingsStorage.ts         # Хранение настроек
│   │   ├── HistoryStorage.ts          # Хранение истории
│   │   ├── ContextStorage.ts          # Хранение контекста и итогов
│   │   ├── RollbackStorage.ts         # Хранение точек отката
│   │   └── migrations/
│   │       ├── Migration.ts           # Базовый класс миграции
│   │       ├── v1.0.0.ts             # Миграция версии 1.0.0
│   │       └── MigrationManager.ts    # Менеджер миграций
│   │
│   ├── ui/                            # Пользовательский интерфейс
│   │   ├── webview/
│   │   │   ├── ChatPanel/             # Основное окно чата
│   │   │   │   ├── assets/
│   │   │   │   │   ├── styles.css     # Стили панели
│   │   │   │   │   └── icons.css      # Иконки команд
│   │   │   │   ├── ChatPanel.ts       # Логика панели чата
│   │   │   │   ├── MessageRenderer.ts # Рендер сообщений
│   │   │   │   ├── CommandDropdown.ts # Выпадающий список команд
│   │   │   │   └── index.html         # HTML-шаблон
│   │   │   │
│   │   │   ├── HistoryPanel/          # Панель истории чатов
│   │   │   │   ├── HistoryPanel.ts    # Логика панели истории
│   │   │   │   ├── ChatListRenderer.ts # Рендер списка чатов
│   │   │   │   └── index.html
│   │   │   │
│   │   │   ├── SettingsPanel/         # Панель настроек
│   │   │   │   ├── SettingsPanel.ts   # Логика настроек
│   │   │   │   ├── ProviderSelector.ts # Выбор провайдера
│   │   │   │   ├── ModelSelector.ts   # Выбор модели
│   │   │   │   └── index.html
│   │   │   │
│   │   │   ├── DiffPanel/             # Панель показа различий
│   │   │   │   ├── DiffPanel.ts       # Логика diff панели
│   │   │   │   ├── DiffRenderer.ts    # Отображение различий
│   │   │   │   └── index.html
│   │   │   │
│   │   │   └── RollbackPanel/         # Панель управления откатами
│   │   │       ├── RollbackPanel.ts   # Логика панели откатов
│   │   │       ├── PointSelector.ts   # Выбор точки отката
│   │   │       └── index.html
│   │   │
│   │   ├── components/                # Переиспользуемые UI компоненты
│   │   │   ├── Button.ts
│   │   │   ├── Dropdown.ts
│   │   │   ├── MessageBubble.ts
│   │   │   └── ProgressBar.ts
│   │   │
│   │   └── themes/                    # Темы оформления
│   │       ├── dark.css
│   │       ├── light.css
│   │       └── high-contrast.css
│   │
│   ├── utils/                         # Вспомогательные утилиты
│   │   ├── FileUtils.ts               # Работа с файлами
│   │   ├── DateUtils.ts               # Форматирование дат
│   │   ├── StringUtils.ts             # Работа со строками
│   │   ├── ValidationUtils.ts         # Валидация данных
│   │   ├── ErrorHandler.ts            # Обработка ошибок
│   │   └── Logger.ts                  # Логирование
│   │
│   └── extension.ts                   # Точка входа расширения
│
├── data/                              # Данные приложения
│   ├── chats/                         # История чатов по режимам
│   │   ├── chat/                      # Чаты режима "Чат"
│   │   │   ├── session-1.json
│   │   │   └── session-2.json
│   │   ├── edit/                      # Чаты режима "Редактирование"
│   │   │   ├── session-1.json
│   │   │   └── session-2.json
│   │   ├── turbo/                     # Чаты режима "Турбо"
│   │   │   └── session-1.json
│   │   └── debug/                     # Чаты режима "Отладка"
│   │       └── session-1.json
│   │
│   ├── context/                       # Данные контекста
│   │   ├── session-summaries.json     # Итоги сессий для контекста
│   │   ├── file-context.json          # Контекст файлов
│   │   └── project-context.json       # Контекст проекта
│   │
│   ├── rollback/                      # Данные для откатов
│   │   ├── snapshots/                 # Снимки файлов
│   │   └── points.json                # Точки отката
│   │
│   └── settings.json                  # Настройки расширения
│
├── resources/                         # Ресурсы
│   ├── icons/
│   │   ├── icon.png                   # Основная иконка
│   │   ├── chat-mode.svg              # Иконка режима "Чат"
│   │   ├── edit-mode.svg              # Иконка режима "Редактирование"
│   │   ├── turbo-mode.svg             # Иконка режима "Турбо"
│   │   └── debug-mode.svg             # Иконка режима "Отладка"
│   │
│   └── templates/                     # Шаблоны
│       ├── command-templates.json     # Шаблоны команд
│       └── prompt-templates.json      # Шаблоны промптов
│
├── package.json
├── tsconfig.json
└── README.md
```

## Ключевые архитектурные решения

### 1. Система контекста (Context System)
- **MessageContext**: Управляет количеством последних N сообщений для загрузки ИИ
- **SessionSummary**: В конце сессии просит ИИ создать итог для подгрузки в следующей сессии
- **Настраиваемый контекст**: Количество сообщений, включение файлов, проекта

### 2. Система откатов (Rollback System)
- **Снимки состояния**: Сохранение состояния файлов перед изменениями
- **Точки отката**: Возможность вернуться к любой точке редактирования
- **История изменений**: Отслеживание всех модификаций кода

### 3. Расширяемая система команд
- **Базовые команды**: Общие для всех режимов
- **Специализированные команды**: Уникальные для каждого режима
- **Легкое добавление**: Новые команды через CommandRegistry

### 4. Система кодированных инструкций
- **7 основных кодов**: 12345, 34567, 59173, 67890, 82647, 36048, 91827
- **Расширяемость**: Легкое добавление новых кодов операций
- **Парсинг**: Автоматическое распознавание и выполнение инструкций

### 5. Модульная архитектура провайдеров
- **Единый интерфейс**: Все провайдеры реализуют BaseProvider
- **Легкое переключение**: Между OpenAI, Anthropic, Google, локальными моделями
- **Настройки моделей**: Отдельные настройки для каждого провайдера

## Приоритеты разработки

### Фаза 1: Основа
1. Базовые классы (BaseMode, Command, BaseProvider)
2. ChatManager и MessageManager
3. Простой UI с режимами

### Фаза 2: Команды и парсер
1. Система команд для всех режимов
2. Парсер кодированных инструкций
3. Базовые операции с файлами

### Фаза 3: Продвинутые функции
1. Система контекста и итогов сессий
2. Система откатов
3. Подсветка различий

### Фаза 4: Полировка
1. Дополнительные провайдеры
2. Расширенные настройки
3. Оптимизация производительности

Эта архитектура обеспечивает:
- ✅ **Масштабируемость**: Легкое добавление новых режимов, команд, провайдеров
- ✅ **Модульность**: Четкое разделение ответственности между компонентами
- ✅ **Расширяемость**: Все системы готовы к будущим улучшениям
- ✅ **Поддерживаемость**: Небольшие файлы, понятная структура