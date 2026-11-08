# V7-Turkish-coffee — The Heritage Coffee Proof Venture

A founder playbook for turning an eight-year, hand-perfected Turkish coffee method into a
**heritage coffee platform**: master-brewed ceremonies, a machine that reproduces the founder's
pot, a franchise built on machine + sealed packs, and an honest daily cup under a second brand.
The proven platform then becomes leverage to revive the heritage **sherbet line at V7 / V-Cola**
(companion repo `vcola-tech-strategy`, Docs 12–15).

> **Status:** Draft v2 (November 2026). v2 adds the machine platform, franchise model and tier
> architecture, and folds in points from three independent AI reviews (ChatGPT, Kimi, DeepSeek)
> after fact-checking. Founder working document, not investment or legal advice. Market facts are
> cited in [`docs/references.md`](docs/references.md); figures marked *estimate* or *hypothesis*
> must be validated (Doc 07).

---

## The idea in one paragraph

Omar spent about a year researching historic Turkish coffee preparation, including interviews
with Cairo's oldest coffeehouses, then about seven years of trial and error. The result is a
specific protocol: high-altitude **Yemeni Arabica**, light roast, **9:1 coffee to cardamom**,
optional **Chios mastic** or **Persian saffron**, a side of lightly roasted **pistachios**, and a
slow, cold-start, hand-stirred brew in a copper cezve. Many tasters rate it far above ordinary
Turkish coffee. The plan is to keep the hand method as the brand's heart, and build a machine
that reproduces it faithfully so the coffee can scale without eight years of training per brewer.

## The verdict up front

| Question | Short answer |
|---|---|
| Can it compete with *all* coffee? | Not as one product. It can **own defined occasions**: the premium café cup, hosting, gifting, the executive morning, and (second brand) the honest daily cup. |
| Is the cup good? | Strong informal evidence says yes. Still needed: blind tests with strangers, against the best local competitor, and **which variables make the difference** (Doc 07). |
| Machine? | **Yes, as fidelity automation**, not speed: same slow curve, no human stirring. Built with V7 engineering, gated by a founder-vs-machine blind test (Doc 12). |
| Where's the moat? | The protocol (trade secret), trained masters, sealed packs, the machine, the brand and the sourcing (Docs 06, 12, 13). |
| Business model | Flagship + masters → machine-led Signature → franchise (machine + packs + brand standards) → Daily brand (Docs 13–14). |
| Biggest risks | Building everything at once, machine parity, Yemen supply, resale-price law, and overclaiming (Doc 11). |

## The playbook

| # | Document | What it settles |
|---|---|---|
| 01 | [The recipe specification](docs/01-recipe-specification.md) | The protocol as a controlled, versioned spec |
| 02 | [Fact-check & claims policy](docs/02-fact-check-and-claims.md) | What's true, what to correct, what we may say |
| 03 | [Recipe engineering notes](docs/03-recipe-engineering-notes.md) | Pistachio, mastic, saffron, cardamom ratio, roast, ice, stirs — and the decomposition tests that become the machine spec |
| 04 | [Competitive landscape](docs/04-competitive-landscape.md) | How it stacks up against every kind of coffee |
| 05 | [Unit economics & pricing](docs/05-unit-economics-and-pricing.md) | Cost per pot, sensitivities, price ladder, Daily tier, scenarios |
| 06 | [Process preservation](docs/06-process-preservation.md) | Protecting eight years of know-how; the master-brewer apprenticeship |
| 07 | [Validation plan & stage gates](docs/07-validation-plan.md) | Blind tests, paid pilots, machine parity (Gate M), Daily tier (Gate D) |
| 08 | [Go-to-market](docs/08-go-to-market.md) | Formats, channels, Cairo first, Gulf next |
| 09 | [Sourcing & supply chain](docs/09-sourcing-and-supply.md) | Yemeni beans, cardamom, mastic, saffron, pistachio, and the risks |
| 10 | [Bridge to the V7 sherbet line](docs/10-bridge-to-v7-sherbet.md) | Working with V7's engineering team, capital firewall, the sherbet pitch |
| 11 | [Risks & mitigations](docs/11-risks.md) | What could kill it |
| 12 | [Machine platform](docs/12-machine-platform.md) | Six subsystems, MVP, parity gate, packs, grinding, transit |
| 13 | [Franchise model](docs/13-franchise-model.md) | Machine + packs + brand standards; legal price discipline |
| 14 | [Tier architecture](docs/14-tier-architecture.md) | Ceremony, Executive line, Reserve, Signature, Daily (second brand), packs |
| — | [References](docs/references.md) | Sources and the reviews that informed v2 |
| — | [`tools/unit_economics.py`](tools/unit_economics.py) | Re-runnable cost and pricing calculator |

## Sequencing: pour the floors in order

| Step | What | Depends on |
|---|---|---|
| 1 | Write the spec; run blind tests with strangers and the **decomposition tests** (Docs 01, 03, 07) | Nothing |
| 2 | **Master-brewed Ceremony and Executive line**: weekend tables, private hosting; train the first apprentices | Step 1 |
| 3 | **Machine MVP** with V7 engineering, in parallel; spec from Step 1's decomposition | Step 1 |
| 4 | **Machine parity** (Gate M) → machine-led Signature at a flagship counter | Steps 2–3 |
| 5 | **Packs** and home bags; shelf-life validated | Step 4 |
| 6 | **Franchise pilot**: 2–3 vetted operators in one city; Daily brand launched through their machines (Gate D) | Steps 4–5 |
| 7 | **Sherbet**: pitch V7 with paid, repeat-purchase data; sherbets poured at the counters | Step 6 |

Each step funds the next. Resist building all floors to 80% at once.
