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

## Building The Site Locally

### Using Docker (Recommended)

Ensure Docker and Docker Compose are installed, then run:

    docker compose up

The site preview will be available at http://localhost:4000.

To rebuild and restart:

    docker compose down && docker compose up --build

### Manual Setup

#### Install Dependencies

**Install RVM**

Install RVM using either the [easy instructions](https://rvm.io/) or the
[more secure instructions](https://rvm.io/rvm/security).

    source ~/.rvm/scripts/rvm

**Install Ruby**

    rvm install 2.6.4
    rvm alias create default ruby-2.6.4
    rvm use default

**Install Bundle**

    gem install bundle

**Install Ruby dependencies**

    cd nostr-compass
    bundle install

#### Preview The Site

    make preview

Visit http://localhost:4000 in your browser.

#### Build The Site

    make

The resulting HTML will be placed in the `_site` directory.

## Contributing

We welcome contributions. Please review the [contributing guidelines](CONTRIBUTING.md).

If you're building on Nostr and would like to contribute or appear on the
podcast, contact us at [info@nostrcompass.org](mailto:info@nostrcompass.org).

## License

All materials are released under the MIT license.
