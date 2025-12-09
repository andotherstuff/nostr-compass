# Contributing

Thank you for your interest in contributing to Nostr Compass. We welcome
contributions from the community.

## Newsletter

The newsletter is published weekly. Typically a pull request for the newsletter
is opened several days before publishing. Any review of the newsletter PRs is
appreciated.

### Newsletter Content

Each newsletter typically covers:

- **NIP Updates**: New proposals, updates to existing NIPs, and discussions
- **Client Updates**: Notable changes to Nostr clients
- **Relay Developments**: Updates to relay software and operations
- **Notable Code Changes**: Significant commits across the ecosystem

## Topic Pages

New topic pages are added to the topic index periodically. If you are
interested in writing a new topic page, please open an issue or contact us.

Each topic page should include:

- Clear explanation of the concept
- Links to relevant NIPs
- Links to implementations
- References to our newsletter coverage

## Translations

We welcome translations of newsletters and other content. If you are interested
in contributing translations:

- Ensure your language is listed under the `languages` field in `_config.yml`
  - We use [2 character ISO 639-1 language codes](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes)
- Create a file with the same name as the `en` language variant:
  - For newsletters, place the file in `_posts/<language code>/newsletters/`
- Set the `lang` field to your language code
- Append `-<language code>` to both the `slug` and `name` fields

### Testing Your Translation

- Follow the instructions in the [README.md](README.md) to build locally
- Run `make preview` to view the site locally
- Check that the page renders properly and language links appear

## Pull Requests

- One newsletter or topic per PR allows for easier review
- Enabling "Allow edits from maintainers" permits us to make small fixes
- Squash commits where it makes sense

## Questions

For questions about contributing, contact us at
[info@nostrcompass.org](mailto:info@nostrcompass.org).
