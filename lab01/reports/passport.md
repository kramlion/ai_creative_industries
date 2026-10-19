# Паспорт эксперимента ЛР 1 — вариант 11

Дата: 2026-10-18 23:04:06 UTC

**Контекст:** бумажная текстура (подложка макета). **Фактор:** квантование до 4 бит.

## Протокол воспроизводимости (полные массивы пикселей)

| Запуск | seed | sha256 массива (первые 16 символов) |
|---:|---:|---|
| 1 | 101 | `c05137283673ac4e` |
| 2 | 101 | `c05137283673ac4e` |
| 3 | 1101 | `5db76f00da9a3ddc` |
| 4 | 101 | `c05137283673ac4e` |

```text
EQ_1_2 = true
EQ_1_4 = true
EQ_1_3 = false
EQ_2_4 = true
```

## Разброс и влияние фактора (n = 5, seed 101…105)

Критерий: |Δ| > 2.0·s_base (задан до эксперимента).

| Метрика | среднее (база) | s (база) | среднее (фактор) | Δ | |Δ|/s | существенно |
|---|---:|---:|---:|---:|---:|:---:|
| mean | 0.5037 | 0.0078 | 0.5037 | +0.0000 | 0.01 | нет |
| contrast | 0.1394 | 0.0022 | 0.1407 | +0.0013 | 0.58 | нет |
| edge | 0.0835 | 0.0008 | 0.0835 | +0.0000 | 0.05 | нет |
| entropy | 7.1741 | 0.0206 | 3.1181 | -4.0560 | 197.04 | да |

## Среда

* python: 3.14.4
* implementation: CPython
* platform: Windows-10-10.0.19045-SP0
* machine: AMD64
* zlib: 1.3.1.zlib-ng
* generator_version: 1.0
* third_party_packages: не используются (стандартная библиотека)

Скрипты (sha256): {"lab01_generator.py": "8f07d340a5a765a8e44f1fec407489cf00114ba54216aa7539c4e7116680e152", "lab01_experiment.py": "69257206dab50ef35de448b45764daad0d4f60dbc98febd8953c6faee28e06b5"}

# Часть Б. Рабочая область Engee

| Версия среды | Engee 26.9.2-H4 |
| Версия личного кабинета | 26.10.1 |
| Дата и время начала работы | 19.10.2026 14:25 |

## Создание папок и скриптов

```text
AI - папка для курса
LR01 - папка для лабораторной работы 1
LR01_environment.ngscript - скрипт
passport.md - паспорт
```

## Вывод VERSION и versioninfo()

```text
VERSION = 1.12.4
Julia Version 1.12.4
Commit 01a2eadb047 (2026-01-06 16:56 UTC)
Build Info:
 Official https://julialang.org release
Platform Info:
 OS: Linux (x86_64-linux-gnu)
 CPU: 112 × Intel(R) Xeon(R) Platinum 8180 CPU @ 2.50GHz
 WORD_SIZE: 64
 LLVM: libLLVM-18.1.7 (ORCJIT, skylake-avx512)
 GC: Built with stock GC
Threads: 5 default, 3 interactive, 5 GC (on 112 virtual cores)
Environment:
 JULIA_LSP_STORE_PATH = /user/lsp_store
 JULIA_CPU_TARGET = generic;sandybridge,-xsaveopt,clone_all;haswell,-rdrnd,base(1)
 JULIA_LSP_PORT = 3751
 JULIA_NUM_PRECOMPILE_TASKS = 8
 JULIA_PKG_PRECOMPILE_AUTO = 0
 JULIA_DEPOT_PATH = /user/.packages:/opt/depot/core:/opt/depot/mtl:/opt/depot/demos:/opt/depot/stdlib
 JULIA_PATH = /usr/local/julia
 LD_LIBRARY_PATH = /usr/local/nvidia/lib:/usr/local/nvidia/lib64
 JULIA_PROJECT = /user/.project/
 JULIA_DA_STORE_PATH = /user/da_store
 JULIA_PKG_SERVER = http://pkgserver.pkgserver.svc.cluster.local
 JULIA_NUM_THREADS = 7,1
 JULIA_DA_PORT = 3752
 JULIA_DEBUG = BackendLib,AbstractAPI
 ```

 ## результат шагов 4-5

 Объявление seed = 101 привело к созданию переменной в рабочей области с именем – seed, значением – 101, классом – Int64.
 При запуске «Очистить все переменные» таблица очистилась, но вывод ячейки сохранился.
 При нажатии «Перезапуск ядра» изменений по сравнению с прошлым вариантом не наблюдается.