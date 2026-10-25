import re
import sys

import markdown
from pygments.formatters import HtmlFormatter

source_path, output_path = sys.argv[1], sys.argv[2]

with open(source_path, encoding='utf-8') as source_file:
    text = source_file.read()

# Questions only: drop everything from the solutions marker onwards
text = text.split('<!-- SOLUTIONS -->')[0]

body = markdown.markdown(
    text,
    extensions=['fenced_code', 'codehilite', 'tables'],
    extension_configs={'codehilite': {'guess_lang': False}},
)


# GitHub alerts (> [!TIP] ...) become styled boxes
body = re.sub(r'<blockquote>\s*<p>\[!(\w+)\]\s*',
              lambda match: f'<blockquote class="alert {match.group(1).lower()}">'
                            f'<p><b>{match.group(1).title()}:</b> ',
              body)


def wrap_question(chunk):
    if '<h3>' not in chunk:
        return chunk
    # Keep a part heading outside the block of the question that follows it
    heading, question = chunk.split('<h3>', 1)
    return f'{heading}<section class="question"><h3>{question}</section>'


body = ''.join(wrap_question(chunk) for chunk in body.split('<hr />'))

css = HtmlFormatter(style='default').get_style_defs('.codehilite')

html = f'''<!doctype html>
<html><head><meta charset="utf-8"><title>IFB104 Practice Quiz</title>
<style>
@page {{ size: A4; margin: 20mm 18mm; }}
body {{ font-family: "Helvetica Neue", Arial, sans-serif; color: #000;
       font-size: 10.5pt; line-height: 1.45; margin: 0; }}
h1 {{ font-size: 18pt; text-align: center; margin: 0 0 12px; }}
h2 {{ font-size: 12.5pt; margin: 24px 0 4px; padding-bottom: 3px;
     border-bottom: 1px solid #000; break-after: avoid; }}
h3 {{ font-size: 11pt; margin: 0 0 6px; }}
blockquote {{ margin: 0 0 12px; padding: 0; font-size: 10pt; }}
blockquote p {{ margin: 2px 0; }}
.question {{ padding: 12px 0; border-bottom: 1px solid #ccc; break-inside: avoid; }}
.question p {{ margin: 5px 0; }}
.question p + p {{ margin-top: 3px; }}
.question h3 + p {{ margin-bottom: 8px; }}
ol {{ margin: 4px 0 8px; }}
.question table {{ width: 100%; border-collapse: collapse; }}
.question td {{ width: 50%; vertical-align: top; padding: 0 10px 0 0; }}
.question td .codehilite pre {{ font-size: 8.5pt; }}
blockquote.alert {{ border-left: 3px solid #555; padding: 4px 10px; margin: 8px 0; }}
code {{ font-family: Menlo, Consolas, monospace; font-size: 9pt; }}
.codehilite {{ background: #f5f5f5; border: 1px solid #ddd;
              padding: 0 10px; margin: 6px 0 8px; }}
.codehilite pre {{ margin: 6px 0; font-size: 9pt; line-height: 1.4; }}
{css}
.codehilite {{ background: #f5f5f5; }}
</style></head>
<body>{body}</body></html>'''

with open(output_path, 'w', encoding='utf-8') as output_file:
    output_file.write(html)
