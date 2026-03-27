# Installing Ask Naval

## Prerequisites

- [Claude Code](https://docs.anthropic.com/en/docs/claude-code) installed and working

## Installation

```bash
claude install-plugin github:cdeistopened/naval-wiki
```

Or add the plugin directory manually:

```bash
# From your project directory
claude plugin add /path/to/naval-wiki/plugin
```

Or add it to your `.claude/settings.json`:

```json
{
  "plugins": [
    "/path/to/naval-wiki/plugin"
  ]
}
```

## First Question to Try

```
How do I find my specific knowledge?
```

This routes to the Specific Knowledge Identifier — Naval's most actionable framework — and walks you through discovering the intersection of your innate talents, genuine curiosity, and market value.

## Other Good Starting Questions

- "Am I building wealth or just renting time?"
- "Should I quit my job and start a company?"
- "Teach me about leverage"
- "Evaluate this potential co-founder"
- "How should I think about happiness?"

## Troubleshooting

- **Skills not showing:** Make sure the plugin path is correct and Claude Code has been restarted
- **Transcripts not found:** The plugin references chunked data in `../data/chunks/` — ensure the full wiki directory is present
- **Generic answers:** Try invoking a specific skill directly: `/ask-naval:specific-knowledge-identifier`

## Learn More

Visit [creativeintel.agency](https://creativeintel.agency) for more Ask [Creator] plugins.
