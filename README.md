# IFB104 Revision Pack

A practice quiz and short revision notes for **IFB104 Building IT Systems**, written in the style of the unit's quiz questions.

> [!IMPORTANT]
> The answers are at the bottom of [mcq.md](mcq.md). Do the quiz from the PDF first, and only open the solutions once you have committed to an answer for every question.

## What's inside

| File | What it is |
|---|---|
| [IFB104_Practice_Quiz.pdf](IFB104_Practice_Quiz.pdf) | 22 multiple-choice questions, **no answers**, ready to print |
| [mcq.md](mcq.md) | The same questions, followed by an answer key and a worked explanation for every question |
| [revision.md](revision.md) | Quick revision of regex building blocks and PySide6/Qt components, with diagrams |
| [common_pattern_regex.md](common_pattern_regex.md) | Ready-to-use regex patterns (email, phone, dates, student IDs, ...) |
| [IFB104-CodePresentationGuide.pdf](IFB104-CodePresentationGuide.pdf) | The official guide to presenting your code in the assignments |
| [build_pdf.py](build_pdf.py) | Script that turns `mcq.md` into the question-only PDF |

## How to use it

1. **Do the quiz** in [IFB104_Practice_Quiz.pdf](IFB104_Practice_Quiz.pdf) on paper, without running any code. Allow about 40 minutes.
2. **Mark it** using the answer key at the end of [mcq.md](mcq.md).
3. **Read the explanations** for every question you got wrong *or guessed*.
4. **Revise the weak spots** with [revision.md](revision.md) and [common_pattern_regex.md](common_pattern_regex.md).
5. **Check your answers** by running the code. Only do this once you've marked the quiz, so it doesn't spoil the practice.

> [!TIP]
> For "what is printed?" questions, trace the code by hand in a small table with one column per variable. It's slower than guessing, but it's how you catch the trick in questions like 1, 7, 9 and 11.

> [!NOTE]
> Questions marked with **\*** (20 and 22) are advanced. Questions marked **(multiple answer)** can have more than one correct option, and you must select all of them.

## Topics covered

| Topic | Questions |
|---|---|
| Selection (`if` / `elif` / `else`, Boolean operators) | 1, 2 |
| Functions, return values, values vs references | 3, 4, 5 |
| Indexing, slicing and loops | 6, 7, 11 |
| Arithmetic (`//`, `%`, `/`) | 9 |
| Errors and exceptions (`IndexError`, `ZeroDivisionError`, `NameError`, ...) | 7, 8, 10, 12 |
| PySide6/Qt widgets, layouts, signals and slots | 13, 14, 15, 16 |
| Regular expressions | 17, 18, 19 |
| Code presentation | 21 |
| Recursion \* | 20 |
| Lists as arrays (Fibonacci) \* | 22 |

## Viewing the files

The markdown files look best on GitHub or in VS Code's markdown preview.

> [!TIP]
> The diagrams in [revision.md](revision.md) and the Q20 solution are written in [Mermaid](https://mermaid.js.org/). GitHub draws them automatically. In VS Code, install the *Markdown Preview Mermaid Support* extension.

## Rebuilding the PDF

If you edit the questions in [mcq.md](mcq.md), rebuild the PDF so it matches. The script only uses the part of `mcq.md` above the `<!-- SOLUTIONS -->` line, so the answers never end up in the PDF.

```bash
pip install markdown pygments
python build_pdf.py mcq.md quiz.html
```

Then open `quiz.html` in a browser and use **Print > Save as PDF**, turning off headers and footers.

> [!WARNING]
> Keep the `<!-- SOLUTIONS -->` line in `mcq.md` exactly as it is. If it's removed or renamed, the answer key will be printed in the PDF.
