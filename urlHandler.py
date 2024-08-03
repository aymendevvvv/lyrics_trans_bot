import hashlib

class URLShortener:
    def __init__(self):
        self.url_mapping = {}

    def shorten_url(self, original_url):
        # Use MD5 hash as a short identifier (you can use other hash functions too)
        hash_object = hashlib.md5(original_url.encode())
        short_identifier = hash_object.hexdigest()[:8]  # Using the first 8 characters for simplicity

        # Store the mapping between short identifier and original URL
        self.url_mapping[short_identifier] = original_url

        return short_identifier

    def expand_url(self, short_url):
        # Extract the short identifier from the short URL
        short_identifier = short_url.split("/")[-1]

        # Retrieve the original URL from the mapping
        original_url = self.url_mapping.get(short_identifier, None)

        return original_url


