# 🪄 Magic UI CLI

Fast, simple command-line access to **200+ Magic UI components**. Search, browse, and get component code in seconds.

## Installation

```bash
# Clone this repo
git clone https://github.com/boobboom2026/magic-ui-cli
cd magic-ui-cli

# Make it executable
chmod +x magicui.py

# Optional: Add to PATH for global access
alias magicui="python3 ~/magic-ui-cli/magicui.py"
```

## Prerequisites

You need the Magic UI repository cloned locally:

```bash
git clone https://github.com/magicuidesign/magicui ~/magicui
```

The CLI reads from `~/magicui/registry.json` to access component metadata.

## Quick Start

```bash
# Search for components
magicui search card
magicui search "text animation"
magicui search background

# List all components
magicui list

# Get component details
magicui get magic-card

# Get direct GitHub URL to component code
magicui code aurora-text
```

## Commands

### `magicui search <query>`
Search for components by name, title, or description.

```bash
$ magicui search card
✅ Found 5 component(s):

📦 Magic Card
   Name: magic-card
   Description: A spotlight effect that follows your mouse cursor...
   Dependencies: motion
   Code: https://raw.githubusercontent.com/...
```

### `magicui list`
List all 200+ available components.

```bash
$ magicui list
📚 150+ Magic UI Components:
  • Aurora Text (aurora-text)
  • Animated Gradient Text (animated-gradient-text)
  • ...
```

### `magicui get <name>`
Show full details for a specific component.

```bash
$ magicui get magic-card
📦 Magic Card
   Name: magic-card
   Description: A spotlight effect that follows your mouse cursor...
   Dependencies: motion
   Code: https://raw.githubusercontent.com/...
```

### `magicui code <name>`
Get the direct GitHub URL to component code (useful for copying).

```bash
$ magicui code magic-card
https://raw.githubusercontent.com/magicuidesign/magicui/main/registry/magicui/magic-card.tsx
```

## Usage Examples

### Find an animation
```bash
magicui search animation
```

### Find text effects
```bash
magicui search text
```

### Find background effects
```bash
magicui search background
```

### Find hover effects
```bash
magicui search hover
```

### Get a specific component's code
```bash
magicui code magic-card
# Output: Direct GitHub link you can open in browser
```

## How It Works

1. **Reads `~/magicui/registry.json`** - The component registry from the Magic UI repo
2. **Searches by name/title/description** - Fast substring matching
3. **Outputs component details** - With GitHub links to actual code
4. **Links directly to raw code** - Click the link to view/copy component

## Features

✅ **Fast** - Instant search from local registry  
✅ **Offline** - No network calls needed  
✅ **Simple** - One file, no dependencies  
✅ **Direct links** - Click to view code on GitHub  
✅ **Dependency info** - See what each component needs  

## Prerequisites

- Python 3.7+
- Magic UI repo cloned to `~/magicui`

## Workflow

1. **Search** for a component: `magicui search card`
2. **View details**: `magicui get magic-card`
3. **Get code URL**: `magicui code magic-card`
4. **Open in browser** or copy code from GitHub
5. **Paste into your project**

## Magic UI Links

- 🌐 **Website**: https://magicui.design
- 📦 **GitHub**: https://github.com/magicuidesign/magicui
- 💬 **Discord**: https://discord.com/invite/87p2vpsat5

## License

MIT - This is just a helper tool for Magic UI components

---

**Happy building!** 🚀
