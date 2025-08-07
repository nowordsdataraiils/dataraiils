# Color Tokens

This project defines reusable color tokens in `style.css` under the `:root` selector.
The table below lists each token, its hex value, and example contrast ratios checked
with `scripts/contrast_check.py`.

| Token | Hex | Description | Contrast vs White | Contrast vs `#F5F5F5` |
|-------|-----|-------------|-------------------|-----------------------|
| `--color-ink` | `#1B1B1F` | Primary text | 17.17 | 15.75 |
| `--color-muted` | `#4B5563` | Muted text | 7.56 | 6.93 |
| `--color-gray-500` | `#444444` | Blockquote text | 9.74 | 8.93 |
| `--color-gray-600` | `#4B4B50` | Secondary headings | 8.67 | 7.95 |
| `--color-brand` | `#9605DF` | Brand purple | 6.21 | 5.69 |
| `--color-brand-dark` | `#7E04B9` | Brand hover | 8.06 | 7.39 |
| `--color-brand-accent` | `#6D2EFF` | Accent borders | n/a | n/a |
| `--color-white` | `#FFFFFF` | Base background | n/a | n/a |
| `--color-bg-muted` | `#F5F5F5` | Muted background | n/a | n/a |
| `--color-bg-light` | `#FAFAFA` | Light background | n/a | n/a |
| `--color-border` | `#E5E7EB` | Border gray | n/a | n/a |
| `--color-border-light` | `#EEEEEE` | Light border | n/a | n/a |

*Contrast ratios use [WCAG 2.1](https://www.w3.org/TR/WCAG21/#contrast-minimum) formula.*
