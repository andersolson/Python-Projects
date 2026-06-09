
# --- Intent Cleaning Function ---
def clean_intent(intent_text):
    intent = intent_text.upper()
    vowels = ['A','E','I','O','U',' ']
    for v in vowels:
        intent = intent.replace(v, '')
    intent = removeDuplicate(intent)
    return intent

# --- Master Dispatcher Function ---
def generate_sigil(intent_text, style, line_width, output_dir):
    line_width = float(line_width)
    phrase = clean_intent(intent_text)
    now = dt.now()
    tdy = now.strftime('%Y%m')
    filename = f'{phrase}_{tdy}.png'
    output_path = os.path.join(output_dir, filename)
    if style == '1':
        createSquareSigil(phrase, line_width, output_path)
    elif style == '2':
        createTeslaSigil(phrase, line_width, output_path)
    elif style == '3':
        createTrolldomSigil(phrase, line_width, output_path)
    else:
        raise ValueError('Invalid style code. Use 1, 2, or 3.')
    return output_path

