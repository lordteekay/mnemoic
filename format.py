def process_wordlist(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as infile:
        content = infile.read()

    # Remove numbers and excessive spaces
    import re
    words = re.findall(r'\b[a-zA-Z]+\b', content)

    # Write the cleaned words to a new output file, each word on a new line
    with open(output_file, 'w', encoding='utf-8') as outfile:
        for word in words:
            outfile.write(word + '\n')

    print(f"Processed {len(words)} words.")
    print(f"First 10 words: {words[:10]}")

# Run the script with your file names
process_wordlist('output.txt', 'cleaned_wordlist.txt')
