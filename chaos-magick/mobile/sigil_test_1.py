from sigil_generator_AI_v0 import generate_sigil
import os

out_dir = r'C:\Users\is_olson\Documents\Projects\GitHub\Python-Projects\chaos-magick\mobile'
os.makedirs(out_dir, exist_ok=True)

result = generate_sigil(
    intent_text='my flies attract big trout',
    style='3',
    line_width='12',
    output_dir=out_dir,
)

print('Generated: ', result)
print('Exists:', os.path.exists(result))