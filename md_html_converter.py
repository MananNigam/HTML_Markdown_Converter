import argparse
import markdown
import markdown2

def markdown_to_html(input_file, output_file):
    markdown_text = open(input_file, 'r').read()
    html_text = markdown.markdown(markdown_text)
    open(output_file, 'w').write(html_text)

def html_to_markdown(input_file, output_file):
    html_text = open(input_file, 'r').read()
    markdown_text = markdown2.markdown(html_text)
    open(output_file, 'w').write(markdown_text)

def main():
    parser = argparse.ArgumentParser(description = "Markdown HTML converter")
    parser.add_argument("input_file", help="Input file to convert")
    parser.add_argument("output_file", help="Output file to write converted code")

    args = parser.parse_args()
    if args.input_file.endswith('.html'):
        html_to_markdown(args.input_file, args.output_file)
    elif args.input_file.endswith('.md'):
        markdown_to_html(args.input_file, args.output_file)
    else:
        print("Incorrect file format")

if __name__ == "__main__":
    main()
