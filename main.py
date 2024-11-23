from config_loader import ConfigLoader

def main():
    # Access a top-level key
    config = ConfigLoader.get_config()
    api_key = config["api"]["key"]
    print(f"API Key: {api_key}")
    db_username = config["database"]["username"]
    db_password = config["database"]["password"]
    print(f"Database Username: {db_username}")
    print(f"Database Password: {db_password}")

if __name__ == "__main__":
    main()