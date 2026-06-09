import os
from sigil_generator_AI_v0 import generate_sigil

# Create and output directory
out_dir = r'C:\Users\is_olson\Documents\Projects\GitHub\Python-Projects\chaos-magick\mobile'
os.makedirs(out_dir, exist_ok=True)

# Test input values
intent = 'my flies attract big trout'
style = 'square'
line_width = 3

results_path = generate_sigil(intent, style, line_width, out_dir)

print("Generated sigil output path: ", results_path)
print("Exists on disk", os.path.exists(results_path))