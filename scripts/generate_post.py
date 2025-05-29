#!/usr/bin/env python3
import os
import glob
from datetime import date

# Paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
POSTS_DIR = os.path.join(BASE_DIR, '..', 'posts')
TEMPLATE_PATH = os.path.join(POSTS_DIR, 'post_template.html')

# Read template
with open(TEMPLATE_PATH, 'r', encoding='utf-8') as f:
    template = f.read()

# Count existing posts (exclude template)
all_posts = glob.glob(os.path.join(POSTS_DIR, '*.html'))
posts = [p for p in all_posts if os.path.basename(p) != 'post_template.html']
number = len(posts) + 1

# Prepare content
today = date.today()
date_str = today.strftime('%d %B %Y')
title = f"Veckans AI-tips #{number} – [Rubrik här]"
content = "<p>[Skriv ditt AI-tips här]</p>"

# Fill template
post_html = (template.replace('{{title}}', title)
                     .replace('{{date}}', date_str)
                     .replace('{{content}}', content))

# Output file
filename = f"{today.strftime('%Y-%m-%d')}-ai-tips-{number}.html"
output_path = os.path.join(POSTS_DIR, filename)

with open(output_path, 'w', encoding='utf-8') as f:
    f.write(post_html)

print(f"Generated new post: {output_path}")