#!/usr/bin/env python3
"""
Magic UI Component CLI - Fast access to Magic UI components
"""

import json
import sys
import subprocess
from pathlib import Path

# Path to registry
REGISTRY_PATH = Path.home() / "magicui" / "registry.json"
GITHUB_RAW = "https://raw.githubusercontent.com/magicuidesign/magicui/main"

def load_registry():
    """Load the Magic UI registry"""
    try:
        with open(REGISTRY_PATH) as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"❌ Registry not found at {REGISTRY_PATH}")
        print("Make sure Magic UI repo is cloned to ~/magicui")
        sys.exit(1)

def search_components(query):
    """Search components by name, title, or description"""
    registry = load_registry()
    query_lower = query.lower()
    results = []

    for item in registry.get("items", []):
        if item["type"] != "registry:ui":
            continue

        name = item.get("name", "").lower()
        title = item.get("title", "").lower()
        desc = item.get("description", "").lower()

        if query_lower in name or query_lower in title or query_lower in desc:
            results.append(item)

    return results

def show_component(name):
    """Show details for a specific component"""
    registry = load_registry()

    for item in registry.get("items", []):
        if item.get("name") == name and item["type"] == "registry:ui":
            return item

    return None

def list_all():
    """List all components"""
    registry = load_registry()
    components = [item for item in registry.get("items", []) if item["type"] == "registry:ui"]
    return components

def print_component(component):
    """Pretty print component info"""
    print(f"\n📦 {component.get('title', component['name'])}")
    print(f"   Name: {component['name']}")
    if component.get("description"):
        print(f"   Description: {component['description']}")

    deps = component.get("dependencies", [])
    if deps:
        print(f"   Dependencies: {', '.join(deps)}")

    files = component.get("files", [])
    if files:
        file_path = files[0].get("path", "")
        github_url = f"{GITHUB_RAW}/{file_path}"
        print(f"   Code: {github_url}")

def main():
    if len(sys.argv) < 2:
        print("""
🪄 Magic UI CLI - Easy component access

Usage:
  magicui search <query>     Search for components
  magicui list               List all components
  magicui get <name>         Show component details
  magicui code <name>        Get component code URL

Examples:
  magicui search card
  magicui search text animation
  magicui get magic-card
  magicui code aurora-text
        """)
        sys.exit(0)

    command = sys.argv[1]

    if command == "search" and len(sys.argv) > 2:
        query = " ".join(sys.argv[2:])
        results = search_components(query)

        if not results:
            print(f"❌ No components found matching '{query}'")
            sys.exit(1)

        print(f"\n✅ Found {len(results)} component(s):\n")
        for component in results:
            print_component(component)

    elif command == "list":
        components = list_all()
        print(f"\n📚 {len(components)} Magic UI Components:\n")
        for comp in sorted(components, key=lambda x: x.get("title", x["name"])):
            title = comp.get("title", comp["name"])
            print(f"  • {title:30} ({comp['name']})")

    elif command == "get" and len(sys.argv) > 2:
        name = sys.argv[2]
        component = show_component(name)
        if component:
            print_component(component)
        else:
            print(f"❌ Component '{name}' not found")
            sys.exit(1)

    elif command == "code" and len(sys.argv) > 2:
        name = sys.argv[2]
        component = show_component(name)
        if component:
            files = component.get("files", [])
            if files:
                file_path = files[0].get("path", "")
                github_url = f"{GITHUB_RAW}/{file_path}"
                print(github_url)
        else:
            print(f"❌ Component '{name}' not found")
            sys.exit(1)

    else:
        print(f"❌ Unknown command: {command}")
        print("Run 'magicui' with no arguments for help")
        sys.exit(1)

if __name__ == "__main__":
    main()
