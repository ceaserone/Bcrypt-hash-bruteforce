import json

def extract_hashes(json_file, output_file):
    """Extract bcrypt hashes from JSON file and save them to hash.txt"""
    try:
        with open(json_file, "r", encoding="utf-8") as f:
            lines = f.readlines()  # Read file line by line

        hashes = []
        for line in lines:
            try:
                data = json.loads(line.strip())  # Parse each JSON line
                if "password" in data:
                    hashes.append(data["password"])  # Extract hash
            except json.JSONDecodeError:
                print(f"[ERROR] Skipping invalid JSON: {line.strip()}")

        # Save hashes to file
        with open(output_file, "w", encoding="utf-8") as f_out:
            f_out.write("\n".join(hashes) + "\n")  # Write each hash on a new line

        print(f"[SUCCESS] Extracted {len(hashes)} hashes and saved to '{output_file}'.")

    except FileNotFoundError:
        print(f"[ERROR] File '{json_file}' not found.")

# Example Usage
if __name__ == "__main__":
    input_json_file = "users.json"  # Change this to your JSON filename
    output_hash_file = "hash.txt"   # Output file for hashes
    extract_hashes(input_json_file, output_hash_file)