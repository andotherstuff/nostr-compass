## NIP Deep Dive

### Badges (NIP-58)

[NIP-58](/en/topics/nip-58/), defined by its [primary specification](https://github.com/nostr-protocol/nips/blob/master/58.md), gives one Nostr identity a way to award a named token to another, and gives the recipient control over whether it appears on their profile. The problem it addresses is that any statement about a person on Nostr is otherwise just a note: there is no structure that says who issued a claim, what the claim is called, what it looks like, or whether the subject accepted it. Badges give that claim three separate signed events with three separate authors' intentions encoded in them.

The [mechanics](https://github.com/nostr-protocol/nips/blob/master/58.md) are built from an addressable definition, an award, and a display list. A badge definition is a kind `30009` event published by the issuer, addressable through its `d` tag, so the issuer can revise the badge's `name`, `description`, `image`, and `thumb` tags later without changing the identifier anything else points at. The award is a kind `8` event published by the same issuer, carrying an `a` tag holding the `30009:<issuer-pubkey>:<d-identifier>` coordinate of the definition and one or more `p` tags naming recipients. The display list is a kind `30008` event published by the recipient with the fixed `d` value `profile_badges`, listing `a` and `e` tag pairs where the `a` tag is the definition coordinate and the `e` tag is the specific award event. Those pairs are ordered and are read as pairs: an `a` tag whose matching award is absent, or an `e` tag whose matching definition is absent, is ignored, so a half-referenced badge silently does not render.

The design tradeoffs are visible in what the [specification](https://github.com/nostr-protocol/nips/blob/master/58.md) refuses to do. There is no revocation mechanism and no expiry, so an award is a permanent statement by the issuer about a moment in time, and an issuer who changes their mind can only change the definition the award points at. There is no transfer, so a badge cannot circulate as a token. There is no notion of a trusted issuer registry, which pushes the entire trust question to the client and the reader: a badge is worth exactly what its issuer's public key is worth to the person looking at it. The specification also grants clients latitude to display fewer badges than the recipient listed and to choose which image size to render, which keeps a profile from becoming a wall of graphics chosen entirely by third parties.

The closest adjacent specification is [NIP-51](/en/topics/nip-51/), the [list specification](https://github.com/nostr-protocol/nips/blob/master/51.md), and comparing the two shows why badges need three events instead of one. A list is a single author curating references; the author of the list is the author of the claim. A badge splits authorship in half, with the issuer signing that the award happened and the recipient signing that they accept its display. Neither party can produce the visible result alone, which is what separates a badge from a self-applied label.

A live kind `8` award recovered from [nos.lol](https://nos.lol) and [relay.primal.net](https://relay.primal.net) this week:

```json
{
  "id": "08504dec368939bd63849a349cab83dea0ac199a852129dbf68cf35fe5c64e96",
  "pubkey": "bef514bd58c8ceea4beb9e6b84a8d983935f7be26f49e14df68098f1ba64156e",
  "created_at": 1787051248,
  "kind": 8,
  "tags": [
    ["a", "30009:bef514bd58c8ceea4beb9e6b84a8d983935f7be26f49e14df68098f1ba64156e:blocks_orange_league"],
    ["p", "92dfa05d915196a7a09152fa3f57871debfd422e1d278ac5af266a70c3350b1f", "wss://relay.damus.io"]
  ],
  "content": "Badge awarded!",
  "sig": "5bf0218dfec5e56b47339b0b4b992cceedd2e18798fb3d47cafea51850c00827f66251e4a3e08190370e04a5e1d4d092eeb441141b7219acdd18b80290a022f8"
}
```

Current implementations cover issuance, display, and reading. [Divine Mobile 1.0.20](https://github.com/divinevideo/divine-mobile/releases/tag/1.0.20) mints and awards a badge inside the app and explains an earned badge when a reader taps it, [Nostter PR #2281](https://github.com/SnowCait/nostter/pull/2281) updates profile badge handling in a web client, and [Amethyst](https://github.com/vitorpamplona/amethyst) publishes award events carrying its own client tag, one of which appears in relay data alongside the example above.

### Comments (NIP-22)

[NIP-22](/en/topics/nip-22/), defined by its [primary specification](https://github.com/nostr-protocol/nips/blob/master/22.md), provides a general comment event for replying to things that are not short text notes. Short-note threading already had [NIP-10](/en/topics/nip-10/), whose tag conventions grew around kind `1` and its reply chains. NIP-22 exists because a video, an article, a calendar event, a wiki page, or a URL needs a reply structure that identifies what kind of thing is being replied to, and that works when the target is addressable, or is an external resource with no Nostr event at all.

The [mechanics](https://github.com/nostr-protocol/nips/blob/master/22.md) turn on a case distinction. A comment is a kind `1111` event that carries two sets of tags: uppercase tags describing the root of the discussion and lowercase tags describing the immediate parent. `E`, `A`, and `I` name a root event, a root addressable coordinate, or a root external identifier, `K` names the root's kind, and `P` names the root author. The lowercase `e`, `a`, `i`, `k`, and `p` name the same facts about the parent, which is the root itself for a top-level comment and another kind `1111` comment for a nested reply. Splitting them means a client can fetch an entire discussion with one filter on the uppercase root tags, without walking the reply chain, while still rendering nesting correctly from the lowercase parent tags. The `I` and `i` variants carry external identifiers in the [NIP-73](/en/topics/nip-73/) format, which is what lets a comment thread attach to a web page, a podcast episode, or a book.

The tradeoffs are mostly about what NIP-22 declines to absorb. The [specification](https://github.com/nostr-protocol/nips/blob/master/22.md) states that comments must not be used to reply to kind `1` notes, which keeps two threading models from competing over the same objects and leaves NIP-10 in place where it already works. Nesting is permitted but the root stays fixed, so a deep thread never loses its anchor even when intermediate events are unavailable. The kind tags are the load-bearing part: a client that fetches a comment without its target can still tell what it is looking at from `K` and `k`, and decide whether it can render that kind at all. What the specification does not provide is any ordering or moderation model, so display order, collapsing, and hiding are entirely client policy.

Compared to [NIP-10](https://github.com/nostr-protocol/nips/blob/master/10.md), the difference lies in typing. NIP-10 assumes the target is a note and encodes position in a thread; NIP-22 encodes the target's identity and kind explicitly and assumes nothing else about it. That explicit typing is why the newer proposals in this issue reach for kind `1111`: a comment already carries a machine-readable statement about what it is attached to.

A live kind `1111` comment recovered from [nos.lol](https://nos.lol) and [relay.primal.net](https://relay.primal.net) this week, replying to another comment under a video:

```json
{
  "id": "c8d335f8bfea58ecd1a943d6000fb2045f4bddf4a36c67df53eb661671f7ab45",
  "pubkey": "3e911baba55ae247339cf805dd6ff49ad2cd6bee84ac44e088ce66450c49104f",
  "created_at": 1787062681,
  "kind": 1111,
  "tags": [
    ["E", "1c492f2bac17b79d66934a340fa43d8d30d0aea4c9fa329346c05573ef912d70", "", "482d024b8acfde50e7429e5ac561d764f3a53a8b4fb0b6975369d9f0926ef839"],
    ["A", "34236:482d024b8acfde50e7429e5ac561d764f3a53a8b4fb0b6975369d9f0926ef839:e64ba9ea157b1a315caff51dbca656ed73ce817d4494e3966adf24055a86f5c5", ""],
    ["K", "34236"],
    ["P", "482d024b8acfde50e7429e5ac561d764f3a53a8b4fb0b6975369d9f0926ef839"],
    ["e", "7a14723b9ef999e74b1757a0fb74942cb6c121138d4ddafe096a57a67ed0a442", "", "8b69e548402afa997343d73e8088224a440f256350f6257b61acc4bb1fa4af4f"],
    ["k", "1111"],
    ["p", "8b69e548402afa997343d73e8088224a440f256350f6257b61acc4bb1fa4af4f"],
    ["client", "Divine", "31990:d95aa8fc0eff8e488952495b8064991d27fb96ed8652f12cdedc5a4e8b5ae540:divine-mobile", "wss://relay.divine.video"]
  ],
  "content": "niiice",
  "sig": "a5517fdea07647efa7ab1730fbea8df882690bba667e93ea5aeba4a73be6a49af1ee17c045535483650caf41dbbcb0897d5803fa39b59f395fd6f9bb193bb789"
}
```

The uppercase tags hold the video and its author while the lowercase `e` and `k` point at the parent comment, which is the shape the specification describes. Implementations reading and writing kind `1111` include [Divine Mobile](https://github.com/divinevideo/divine-mobile), whose client tag appears in the event above, [Amethyst](https://github.com/vitorpamplona/amethyst), whose comments appear in the same relay results, and [nostrord](https://github.com/nostrord/nostrord/pull/274), which renders thread posts as forum posts this week. The proposed patch format in [NIPs PR #2438](https://github.com/nostr-protocol/nips/pull/2438) builds on the same kind.

---

Send a NIP-17 DM to share a project or news item through the [Nostr Compass project](https://github.com/andotherstuff/nostr-compass).

GATE: PENDING REVIEW
