# Nostr Compass

Technical resource for the Nostr protocol. Weekly newsletter covering NIP
proposals, client updates, relay developments, and notable code changes.
Weekly podcast featuring conversations with the developers whose work is
covered in each newsletter. Comprehensive topic index documenting key Nostr
concepts with links to primary sources and our coverage.

All materials open source under MIT license.

## What We Provide

- **Weekly Newsletter**: Coverage of NIP proposals, client updates, relay
  developments, and notable code changes across the Nostr ecosystem
- **Podcast**: Conversations with the developers building Nostr
- **Topic Index**: Documentation of key protocol concepts, NIPs, and
  implementations with links to primary sources

## Goals

The Nostr ecosystem is growing fast but lacks a central, neutral technical
resource that documents what's actually shipping and changing week to week.
Developers building clients don't have time to monitor every other client's
repo. Relay operators miss NIP discussions that affect them. New contributors
have no on-ramp to understand how the protocol has evolved.

Our goal is to create that resource: a consistent, technically accurate,
non-promotional publication that helps developers stay informed, helps
businesses evaluate Nostr for their use cases, and creates a durable archive
of protocol evolution.

## Development Workflow

**Local development (with live reload):**
```bash
hugo server
# Visit http://localhost:1313
```

**Using Docker:**
```bash
docker-compose up
# Visit http://localhost:1313
```

**Build static site:**
```bash
hugo
# Output in /public/
```

## Adding Content

**Newsletter edition:**
```bash
hugo new content/en/newsletters/2024-01-15-edition-1.md
```

**Blog post:**
```bash
hugo new content/en/blog/my-post.md
```

**Edit content:** Files in `/content/en/` - Markdown with front matter

**Fetch project updates:**
```bash
python3 scripts/fetch_project_updates.py --since-days 7
# Outputs to data/project_updates/*.json
```

## Contributing

We welcome contributions. Please review the [contributing guidelines](CONTRIBUTING.md).

If you're building on Nostr and would like to contribute or appear on the
podcast, contact us at [info@nostrcompass.org](mailto:info@nostrcompass.org).

## License

All materials are released under the MIT license.
