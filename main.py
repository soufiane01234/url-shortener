def shorten_url(original_url: str, custom_alias: str | None = None) -> dict[str, str]:
    if custom_alias:
        alias = custom_alias
    else:
        alias = "rand123"
        
    return {
        "original_url": original_url, 
        "short_url": f"http://localhost:8000/{alias}"
    }

if __name__ == "__main__":
    # Test 1: Without a custom alias
    print(shorten_url("https://vistula.edu.pl"))
    
    # Test 2: With a custom alias
    print(shorten_url("https://vistula.edu.pl", "my-school"))