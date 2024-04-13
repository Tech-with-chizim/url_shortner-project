### URL Shortener Project

This is a simple URL shortener project that helps you generate shorter versions of long URLs for easier sharing. The project consists of two main files:

- **main.py**: Contains the Python code for generating and managing shortened URLs.
- **index.html**: Provides a user interface for inputting URLs and displaying the shortened version.

#### main.py

```python
import random
import string

# Dictionary to store URL mappings
url_mappings = {}

def generate_short_url():
    characters = string.ascii_letters + string.digits
    short_url = ''.join(random.choice(characters) for _ in range(6))
    return short_url

def shorten_url(original_url):
    if original_url not in url_mappings:
        short_url = generate_short_url()
        url_mappings[original_url] = short_url
    return url_mappings[original_url]

def redirect_to_original(short_url):
    for original_url, generated_short_url in url_mappings.items():
        if generated_short_url == short_url:
            return original_url

    return 'URL not found!'

# Example usage:
original_url = "https://www.example.com"
short_url = shorten_url(original_url)
print(f"Original URL: {original_url}, Shortened URL: {short_url}")

shortened_url_to_check = "abc123"  # Replace with an actual shortened URL
redirected_url = redirect_to_original(shortened_url_to_check)
print(f"Redirected URL: {redirected_url}")
```

#### index.html

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>URL Shortener</title>
</head>
<body>
    <h1>URL Shortener</h1>
    <form action="/shorten" method="post">
        <label for="url">Enter URL</label>
        <input type='text' id="url" name="url" required>
        <button type="submit">Shorten URL</button>
    </form>

    {% if original_url %}
        <p>Original URL: {{original_url}}</p>
        <p>Shortened URL: {{short_url}}</p>
    {% endif %}
    
</body>
</html>
```

#### Usage

1. Run `main.py` to start the URL shortening service.
2. Access the web interface by opening `index.html` in your browser.
3. Enter a URL in the input field and click "Shorten URL" to generate a shortened version.
4. The original and shortened URLs will be displayed on the webpage.

Feel free to customize and expand upon this project as needed!
