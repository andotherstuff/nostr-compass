## Top Stories

### Marmot projects at bitcoin++ Seoul

[bitcoin++ Seoul](https://btcpp.dev/seoul), a privacy-themed Bitcoin developer conference held 5 and 6 November, ran a hackathon whose [gallery](https://btcpp.dev/seoul/hackathon) lists 20 projects, several of them built on [Marmot](/en/topics/marmot/) encrypted groups. [BlackIce](https://github.com/rademenezbtc/blackice) took first place and the Best Use of the Marmot Protocol award. In it, Frostsnap hardware wallets jointly sign Bitcoin payments to silent-payment addresses (reusable addresses that keep each payment private), coordinating over a Marmot group. [mdk squared](https://github.com/samthomson/mdk-squared) earned an honorable mention for controlling mining air purifiers through a Marmot channel, and [iLCHON](https://github.com/dongguri-jun/ilchon), which matches bitcoin trades only between people who have met, won Best Beginner Hack.

Other Marmot entries include [Kimchi](https://github.com/ye0man/kimchi) for splitting bills with [Cashu](/en/topics/cashu/) ecash, [SatsRoadMarket](https://github.com/shroominic/satsroadmarket) for private marketplace negotiation, [Quiet Ledger](https://github.com/murdawkmedia/quiet-ledger) for invoices, an open [pull request adding chat to Shroud](https://github.com/CypherCommons/shroud/pull/233), a silent-payment wallet, and [kiss-bdk](https://github.com/kkdao/kiss-bdk), a multi-signer silent-payment wallet. Most depend on marmot-ts 0.9.0, the TypeScript Marmot library. All are [hackathon code](https://github.com/marmot-protocol/awesome-marmot/compare/57d5bb868aa7...e0a960475372): test networks only, unaudited, often with keys or group state stored unencrypted. White Noise, the Marmot messenger, rejects mdk squared's KeyPackages, the keys a device publishes so others can add it to a group.

writer_model: direct-codex

GATE: PENDING REVIEW
