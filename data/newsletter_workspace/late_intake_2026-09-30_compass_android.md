# Late owner intake — Compass Android app, September 29

The owner supplied the [Nostr Compass Android Zapstore listing](https://zapstore.dev/apps/naddr1qq2x7un89ehx7um5wf3k7mtsv9ehxtnpwpcqzxrhwden5te0wfjkccte9eaxzurnw3hhyefwv3jhvq3qwav4fae3gyfy3xj298kxj2mj8phavz7vavps34przq02j7w902qqxpqqqplqk563kdn) and asked for an announcement at the beginning of the still-unpublished issue. The owner describes the app's intended role as a dedicated Android home for Compass newsletter and podcast work.

The naddr decodes to kind 32267, identifier `org.nostrcompass.app`, author `775954f7314112489a4a29ec692b72386fd60bcceb0308d423101ea979c57a80`, and `wss://relay.zapstore.dev`. An exact relay query with NAK's default signature verification returned app event `d28ccebe051018e97af4fa0746e68c54103168f6a355fe68c66aa1a011d6ec45`. Its author maps to the `Nostr Compass` npub in `data/npubs.yml` and `publish/config/author.json`. The linked page returned HTTP 200.

After the owner's correction, the app-name link in the opening points to the [ngit repository](https://gitworkshop.dev/npub1wav4fae3gyfy3xj298kxj2mj8phavz7vavps34przq02j7w902qq902923/relay.ngit.dev/nostr-compass-android). That exact URL is the `web` tag of signature-verified kind 30617 repository event `86c1cdf20abe18696078d66ab97e9799a6f81f56ce37966bbfb792a073a04770`, signed by the same Compass author and fetched from `wss://relay.ngit.dev`. The repository page returned HTTP 200. The Zapstore link remains on the separate release-notes phrase to source shipped-feature claims.

The same signer published kind 30063 release event `8282c64231f2316c92098b40188cccd80e614609abe5a0f6f28fbc4c8452afc6`, tagged `org.nostrcompass.app@1.0.0`, at 2026-09-29 17:54:28 UTC. This is after the Tuesday source pass cutoff of 14:00 UTC, so it is recorded as a late owner-directed addition. Its notes support issue browsing, section voice notes and replies, episode curation, public Nostr/Blossom recordings, and Amber signing. They do not establish that every future newsletter or podcast function has already shipped.

The announcement in the article distinguishes the intended dedicated role from what the first release does. This is Compass's own app; no third-party review outreach is due for this announcement.

GATE: PASS


## September 30 live refresh

Same-author signed Zapstore listing `68c907aedaf378d8ff138ff799aab72c3889f22cb35cfaa0eced4c0bfab99ac6` and release notes 1.1.0 `66579d6983ec7b628dec1e2dfe3c1a98203fb12b1cf3648d3f38612b06c5d7f4`, 1.1.1 `824285261139e95ece800828a1af8ac43ec478a3569ef4a1770ecb41a440fb6b`, 1.1.2 `003c18f2ea16b8e22178fd9c6d7133871a5dcf4522c1e38e7c1df84462571ec7` recovered through nak signature validation from relay.zapstore.dev. Full public notes retained in /opt/data/tmp/compass_app_releases_live_20260930.jsonl. Latest listing continues to identify https://gitworkshop.dev/npub1wav4fae3gyfy3xj298kxj2mj8phavz7vavps34przq02j7w902qq902923/relay.ngit.dev/nostr-compass-android. Primary reader source: https://zapstore.dev/apps/naddr1qq2x7un89ehx7um5wf3k7mtsv9ehxtnpwpcqzxrhwden5te0wfjkccte9eaxzurnw3hhyefwv3jhvq3qwav4fae3gyfy3xj298kxj2mj8phavz7vavps34przq02j7w902qqxpqqqplqk563kdn. Opening refreshed to current functionality, with notification/platform limits preserved.
