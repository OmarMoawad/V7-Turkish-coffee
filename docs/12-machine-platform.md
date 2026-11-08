# 12 — The Machine Platform (Fidelity Automation)

**What changed:** v1 of this repo said "no machine for now." The founder has since clarified two
things that change that call: (1) "fast" means **non-human**, not faster brewing — the pot stays
slow; and (2) he is an engineer with direct access to V7's engineering facilities. With
engineering capacity in hand, a machine becomes a reasonable parallel track. The goal is
**fidelity, not speed**: a machine that reproduces the founder's pot so a franchisee doesn't need
eight years of practice.

> Design principle: **automate fidelity, not throughput.** The heat ramp stays slow. One operator
> supervises several machines instead of stirring one cezve, which is where throughput comes from.

## 1. The six subsystems

| # | Subsystem | What it must do | Notes |
|---|---|---|---|
| 1 | **Water** | Measured volume at a fixed start temperature (the "fridge-cold" spec, in °C) | Cooled reservoir; ice step only if Doc 03 tests prove it matters |
| 2 | **Dosing** | Exact coffee + cardamom + sugar (+ mastic / saffron) by weight | Simplest route: pre-dosed sealed packs (§4), so the machine doesn't meter powder |
| 3 | **Heating** | Reproduce the founder's measured heat-up curve (time to first foam, time to pour) | Programmable electric or induction element. Temperature-controlled electric heating can replicate a low gas flame once the curve is measured; the "avoid electric stoves" rule applies to uncontrolled domestic hobs |
| 4 | **Stirring** | Reproduce the validated stirring pattern: rate, depth, direction, and how it changes as temperature rises | Spec comes from Doc 03 §5 decomposition test, not from the number 1,000 |
| 5 | **Sensing** | Temperature, elapsed time, foam-rise detection; stop before boil | Foam detection is the hard part; optical or capacitive level sensing |
| 6 | **Serving** | Removable copper cezve; pour into the cup; machine cleans itself | Keeps the traditional look and the copper heat-transfer behaviour |

## 2. Build order (minimum viable machine)

1. **MVP:** automate only dosing (via packs), heating curve, and stirring. Keep the copper cezve
   and manual pour.
2. **v2:** add foam sensing and auto-stop.
3. **v3:** multi-cezve station (one operator, 3–4 pots in parallel), self-cleaning.
4. **Recipe slots from day one:** store each protocol (Signature, Mastic, Saffron, Daily) as a
   software profile so new products are a firmware change, not new hardware.

Start from an existing automatic Turkish coffee machine (Arçelik Telve, Arzum Okka and others
already exist) as a test rig and benchmark. The value is your measured protocol, not new
mechanics. Buy one, measure what it does, and change the heating and stirring to match your curve.

## 3. The gate that matters most: machine parity

No machine reaches a franchisee until it passes a **founder-vs-machine blind triangle test**
(Doc 07, Gate M). The question isn't "is the machine's coffee good?" It's "can trained tasters
tell the machine's pot from the founder's hand-brewed pot?" One inconsistent machine in a
franchisee's shop damages the brand in a city you don't control.

## 4. Where the quality guarantee should live: the consumable

A "low-price machine that guarantees quality" is a contradiction if the machine carries the
guarantee: precision costs money, and cheap hardware varies unit to unit. The workable design:

- **Quality lives in the sealed, pre-dosed pack**: roasted, ground, blended with cardamom (and
  the variant ingredient) at your facility, nitrogen-flushed, dated.
- **The machine only has to be good enough** to run the heating and stirring profile within
  tolerance. That keeps it affordable to place with operators.
- This is the Nespresso-style model, and it is also the franchise moat (Doc 13).

Open engineering question: Turkish coffee is ground very fine and loses aroma fast after
grinding. Pack format must pass a shelf-life test: same pack tasted blind at day 1, 14, 30, 60.

## 5. Grinding R&D: spend on the variable, not the tool

The founder floated laser grinding. Laser processing risks localized heating that drives off the
aromatics the protocol depends on, and it's far more expensive than needed. Turkish fineness is
achieved routinely with dedicated burr grinders. If burr grinding proves limiting, **cryogenic or
jet milling** are the established routes to a tight particle-size distribution with low thermal
load. Measure particle-size distribution first; only change the grinder if the data shows it
limits the cup.

## 6. Transit preservation (for the executive line, Doc 14)

Turkish coffee degrades fast after brewing: the foam collapses, it cools, and the grounds settle
unevenly. An executive who wants the pot at his desk needs one of:

- **Brew on site** (a master travels with a kit), or
- **Engineered serve-ware** that holds temperature and foam for 30–45 minutes.

The second is a genuine R&D project where V7's facilities give a real edge. Treat it as its own
work package with its own blind test (fresh vs 30-minute-held pot).

## 7. What to measure on every prototype run

Water start temperature, heating curve (logged), time to first foam, stir profile, final
temperature, foam score, particle-size distribution of the batch, total dissolved solids if a
refractometer is available, and blind taste score against the founder's reference pot.

## 8. Money and ownership

Keep the machine as a **separate work package with its own budget**, so its R&D can't quietly
consume the coffee brand's cash or the future sherbet budget (Doc 10). Patent only a genuinely
novel mechanism, and only after IP advice: a patent requires novelty and disclosure, which may
conflict with keeping the protocol a trade secret (Doc 06).
