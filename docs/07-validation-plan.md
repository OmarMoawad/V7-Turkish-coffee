# 07 — Validation Plan & Stage Gates

The founder has had many people taste this coffee over seven years, and they consistently rate it
far above ordinary Turkish coffee. That's real evidence that **the finished cup is excellent**.
What it can't show yet:

- **Which inputs produce the quality.** Every tasting cup had every variable. The machine needs
  the decomposition (Doc 03 §11).
- **How it does against the right competitor.** Beating ordinary Turkish coffee is a low bar; the
  price is set by the best Cairo coffeehouses.
- **What strangers will pay.** People who know the maker, tasting for free, are the most biased
  sample in sensory work, through no fault of theirs. Unanimous praise is itself a mild warning
  sign; real preference panels almost always show some spread.

So the gates below aren't about doubting the coffee. They turn it into evidence a franchisee, a
lender or V7 will accept, and into a spec an engineer can build to. Each gate has pass and kill
criteria, in the same spirit as `vcola-tech-strategy` Doc 25.

## Gate 0 — Specification frozen (week 0–2)
- Doc 01 written; 20 pots logged with all measurements; video protocol recorded.
- **Pass:** a second person can brew from the spec with founder supervision.

## Gate 1 — Blind superiority (week 2–6)
- Panel: 40–60 regular Turkish coffee drinkers who don't know the founder.
- Samples (blind, randomised order, same cups, same sugar level):
  1. This coffee (spec v1.0)
  2. A respected traditional Cairo coffeehouse's Turkish coffee
  3. A premium supermarket brand (e.g. Al Ameed) brewed well
  4. A specialty café's Turkish coffee, if one serves it
- Measures: 9-point hedonic liking, preference ranking, "would you order this again?"
- **Pass:** ranked first by a clear majority and a mean liking ≥ 1 point above the next best.
- **Kill or rework:** not clearly preferred over the best traditional coffeehouse.

## Gate 2 — Variant selection (week 4–8)
- Run the Doc 03 tests: pistachio placement, mastic and saffron dosing, bean rest, stir count.
- **Pass:** a final menu of Signature + up to two Reserve variants, each blind-validated.

## Gate 3 — Paid demand (month 2–4)
- Format: weekend tasting counter (pop-up in a premium café, hotel lobby or market).
- Price tests: rotate Signature at EGP 350 / 450 / 550 across weekends; Reserve at 650 / 900.
- Measures: conversion, average spend, **repeat within 30 days**, home-blend attach rate.
- **Pass:** ≥ 25% of first-time buyers return or buy the blend within 30 days at ≥ EGP 400.
- **Kill:** fewer than 10% return at any price above EGP 350.

## Gate 4 — Reproducibility (month 3–6)
- Second brewer trained (Doc 06). Blind triangle tests: founder's pot vs trainee's pot.
- **Pass:** tasters can't reliably tell them apart.
- **Kill (for scaling):** only the founder can produce the cup. The venture then stays a
  founder-led boutique, which is still valuable for the V7 story, but don't open a second site.

## Gate M — Machine parity (runs in parallel with Gates 2–4)
- The machine prototype (Doc 12) brews against the founder's hand-brewed reference pot.
- Blind triangle tests with trained tasters; then a preference test with strangers.
- Also test: a pack aged 30 days vs a fresh pack; a 30-minute held pot vs fresh (Executive line).
- **Pass:** tasters can't reliably pick the odd one out across repeated rounds.
- **Kill (for franchising):** the machine is distinguishable. Fix and retest; nothing goes to an
  operator before this passes.

## Gate D — Daily tier (before the separate-brand launch)
- The Daily cup blind against premium supermarket coffee brewed well and a chain café's cup.
- Lab certificate of 100% coffee for the blend.
- **Pass:** preferred over the supermarket benchmark at the EGP 50 test price.

## Gate 5 — Permanent counter & export test (month 6–12)
- Only if Gates 1–4 pass. Permanent counter or residency; first Gulf pop-up; home blend online.
- **Pass:** counter covers its costs within 6 months; Gulf pop-up sells out at the hypothesised
  prices (Doc 05 §4).

## What to record for the V7 pitch

Keep every result, including failures. The blind-test protocol, paid pilots and repeat-purchase
data are exactly the evidence the sherbet line needs (Doc 10).
