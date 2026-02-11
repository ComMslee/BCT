# CLAUDE.md — BCT (Battery Cycle Tester)

## Project Overview

BCT is a desktop GUI application for battery cycle testing and factory testing of battery management systems (BMS). It communicates with battery devices over serial ports to run cycle tests, factory validation tests (electricity, temperature, error codes), and push serial numbers. Built with Python and PySide6 (Qt6).

Current version: **v1.0.3**

## Directory Structure

```
BCT/
├── src/
│   ├── main.py                  # Application entry point
│   ├── MainUI.py                # AUTO-GENERATED from BCT_UI.ui — do not edit manually
│   ├── BCT_UI.ui                # Qt Designer UI definition (edit this for UI changes)
│   ├── repository/              # Data persistence layer
│   │   ├── DataConfig.py        # Singleton configuration manager (JSON)
│   │   └── DataLog.py           # CSV test data logging
│   ├── util/                    # Serial communication & worker threads
│   │   ├── define.py            # Constants: test cases, error codes, BCT mapping tables
│   │   ├── ReadThread.py        # Thread for reading serial data
│   │   ├── SerialWork.py        # Serial worker for push serial number
│   │   ├── SerialWorkCycle.py   # Serial worker for battery cycle testing
│   │   ├── FactoryWork.py       # Serial worker for factory tests
│   │   ├── InfoWork.py          # Serial worker for device info queries
│   │   └── TempWork.py          # Serial worker for temperature testing
│   └── view/                    # UI view controllers
│       ├── RootView.py          # Device config/info tab
│       ├── BatteryCycleView.py  # Battery cycle test tab
│       ├── BatteryFactoryView.py      # Factory test tab
│       ├── BatteryFactoryTempView.py  # Temperature test tab
│       ├── PushSerialView.py    # Serial number push tab
│       └── unit/
│           └── LEDBar.py        # Custom LED bar blinking widget
├── makeUI.bat / makeUI.sh       # Compile .ui → MainUI.py
├── makeEXE.bat / makeExe.sh     # Build standalone executable
└── .gitignore
```

## Tech Stack

- **Language:** Python 3.7+
- **GUI Framework:** PySide6 (Qt6)
- **Serial Communication:** pyserial (115200 baud default)
- **Build Tool:** PyInstaller (standalone executables)
- **UI Compiler:** pyside6-uic (Qt Designer .ui → Python)

## Architecture

MVC pattern:

- **Model:** `src/repository/` — `DataConfig` (singleton, persists to `data/config.json`), `DataLog` (CSV export)
- **View:** `src/view/` — Tab controllers that bind UI elements from `MainUI.py` to logic
- **Controller:** `src/util/` — QThread-based serial workers handling device communication

Each serial worker (`SerialWork`, `SerialWorkCycle`, `FactoryWork`, `TempWork`, `InfoWork`) runs in its own QThread and communicates with views via Qt Signals/Slots.

## Build & Run Commands

```bash
# Compile UI (required after editing BCT_UI.ui)
pyside6-uic ./src/BCT_UI.ui -o ./src/MainUI.py

# Run the application
python src/main.py

# Build executable (Windows)
makeEXE.bat

# Build executable (macOS/Linux)
bash makeExe.sh
```

## Key Conventions

- **MainUI.py is auto-generated.** Never edit it directly. Edit `BCT_UI.ui` in Qt Designer, then recompile with `pyside6-uic`.
- **One class per file** as a general rule.
- **Constants go in `src/util/define.py`** — error codes, test case definitions, BCT mapping tables.
- **DataConfig is a singleton** — accessed via `DataConfig()` from anywhere in the codebase.
- **Naming:** PascalCase for classes, camelCase for most attributes/methods (Qt style), `b` prefix for boolean flags (e.g., `bRunning`).
- **Serial protocol:** Commands sent as formatted strings over serial at 115200 baud. Workers parse responses line-by-line.
- **Logging:** Test data is written to CSV files organized by date: `data/[YYMMDD]/[YYMMDD_HHMMSS]_[SerialNum]_[DevNum].csv`.

## Runtime Data

- `data/config.json` — Persisted application configuration (created at first run)
- `data/[YYMMDD]/` — Daily directories containing CSV test log files
- `release/` — Built executables (gitignored)
- `capture/` — Test capture files (gitignored)

## No Automated Testing or CI

There are no unit tests, test frameworks, linting configs, or CI/CD pipelines in this project. Changes should be validated by manual testing with the application and connected hardware.

## Platform Notes

- **Windows:** Uses `venv\` virtual environment, COM3/COM4 default serial ports
- **macOS:** Uses `venv_mac/` virtual environment, `/dev/tty.usbserial-*` serial ports
- Serial port and baud rate are configurable through the application UI
