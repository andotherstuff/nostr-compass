## Unreleased changes


### nostream merges seven PRs without cutting a release

[nostream](https://github.com/Cameri/nostream), the TypeScript relay implementation, merged seven PRs this week without cutting a release. The headline pair is [PR #702](https://github.com/Cameri/nostream/pull/702) and [PR #676](https://github.com/Cameri/nostream/pull/676), which together give relay operators a working authentication-plus-membership access-control stack; this week's NIP Deep Dive walks through exactly that handshake.

### FIPS v0.4.1 tightens the transport the Iris ecosystem builds on

[jmcorgan/fips](https://github.com/jmcorgan/fips) shipped [v0.4.1](https://github.com/jmcorgan/fips/releases/tag/v0.4.1), a maintenance release capping antipoison state, fixing convergence and MTU handling, and cutting CPU use. On its own this is plumbing, but this week it is connective tissue: the browser TypeScript runtime [fips-ts](https://github.com/mmalmi/fips-ts) from the Iris-ecosystem cluster in this issue's News section is wire-compatible with this Rust transport, so fixes here propagate directly to what the browser runtime interoperates with.


GATE: PASS
