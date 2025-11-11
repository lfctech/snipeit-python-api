import json
import os

# Load the original API spec
with open("snipe-it-rest-api.json", "r") as f:
    data = json.load(f)

# Extract paths
paths = data.get("paths", {})

# Group paths by category (first part after /)
groups = {}
for path, methods in paths.items():
    parts = path.strip("/").split("/")
    if parts:
        category = parts[0]
        if category not in groups:
            groups[category] = {}
        groups[category][path] = methods

# For each group, create a new spec file
for category, category_paths in groups.items():
    # Create a new spec dict
    new_spec = {
        "openapi": data.get("openapi"),
        "info": data.get("info"),
        "servers": data.get("servers"),
        "security": data.get("security"),
        "components": data.get("components"),
        "paths": category_paths,
    }

    # Write to file
    filename = f"{category}.json"
    with open(filename, "w") as f:
        json.dump(new_spec, f, indent=2)

    print(f"Created {filename}")

print("Splitting complete.")
