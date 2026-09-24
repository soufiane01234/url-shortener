from fastapi import FastAPI

# We add professional metadata directly into the FastAPI initialization
app = FastAPI(
    title="URL Shortener API",
    description="A high-performance backend service for generating custom short links.",
    version="1.0.0",
    contact={
        "name": "Soufiane Soulami",
        "url": "https://github.com/soufiane01234/url-shortener",
    }
)

# The 'tags' argument categorizes the endpoint in the UI for better organization
@app.get("/shorten", tags=["Core Features"])
def shorten_url(original_url: str, custom_alias: str | None = None) -> dict[str, str]:
    if custom_alias:
        alias = custom_alias
    else:
        alias = "rand123"
        
    return {
        "original_url": original_url, 
        "short_url": f"http://localhost:8000/{alias}"
    }