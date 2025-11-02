# White Book — Complete Math (Scaffold)

**You do NOT need an existing PDF.** The Makefile compiles your `Volume_II_Onu_Calculus.tex` into `build/Volume_II_Onu_Calculus.pdf`, then assembles `whitebook.pdf`.

## Build
```bash
cd whitebook
make            # builds Volume II PDF from TeX, then master book
```

## Layout
- `whitebook.tex` master book
- `preamble.tex` shared setup
- `vol1/.. vol4/..` chapter stubs
- `src/Volume_II_Onu_Calculus.tex` your original TeX
- `build/Volume_II_Onu_Calculus.pdf` auto-generated

> If your Volume II defines custom macros in its preamble, they are preserved because it is compiled separately and included as a PDF.
