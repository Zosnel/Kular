### KULAR ###

class HTMLGenerator:
    def __init__(self):
        self.title = "Kular Project"
        self.body_content = []
        self.styles = []

    def set_title(self, title):
        self.title = title

    def para(self, text):
        self.body_content.append(f"<p>{text}</p>")

    def heading(self, text, level=1):
        if 1 <= level <= 6:
            self.body_content.append(f"<h{level}>{text}</h{level}>")
        else:
            print("KULAR ERROR: Heading level must be between 1 and 6.")

    def url(self, text, url):
        self.body_content.append(f'<a href="{url}">{text}</a>')

    def image(self, src, alt=""):
        self.body_content.append(f'<img src="{src}" alt="{alt}">')

    def ccccccccccccccccccccccccccccccccccccccccccccccccccccc(self):
        self.body_content.append(f'<h6>hello</h6>')

    def breakline(self):
        self.body_content.append(f'<hr>')

    def sep(self):
        self.body_content.append(f'<br>')

    def add_css(self, css):
        self.styles.append(css)

    def generate_html(self):
        html = f"<!DOCTYPE html>\n<html>\n<head>\n<title>{self.title}</title>\n"
        html += '<link rel="stylesheet" href="style.css">\n'  # Link to external CSS
        html += "</head>\n<body>\n"
        html += "\n".join(self.body_content)
        html += "\n</body>\n</html>"
        return html

    def generate_css(self):
        return "\n".join(self.styles)

    def save_to_file(self, html_filename, css_filename):
        with open(html_filename, 'w') as html_file:
            html_file.write(self.generate_html())
        with open(css_filename, 'w') as css_file:
            css_file.write(self.generate_css())
        print(f"HTML file '{html_filename}' and CSS file '{css_filename}' have been created.")

if __name__ == "__main__":
    generator = HTMLGenerator()

    # Example usage
    generator.set_title("Welcome to My Website")
    generator.heading("Hello World", level=1)
    generator.para("This is a simple paragraph.")
    generator.para("You can add more content as needed.")
    generator.heading("About This Page", level=2)
    generator.para("This page is generated using Python.")

    # Adding some CSS styles
    generator.add_css("body { font-family: Arial, sans-serif; }")
    generator.add_css("h1 { color: blue; }")
    generator.add_css("p { color: green; }")

    # Save the generated HTML and CSS to files
    generator.save_to_file("index.html", "style.css")