# 03 — Recipe Engineering Notes

The founder's protocol works: people who taste it rate it highly. This doc doesn't change it.
It lists the **open questions** as hypotheses, explains the likely mechanism behind each, and
says how to test it without risking the baseline (spec v1.0, Doc 01).

## 1. Pistachio: on the side, not in the pot

- **Risk if ground into the coffee:** pistachio is roughly half fat. Oil suppresses foam, and
  the foam is the signature of good Turkish coffee. It also adds a nutty, oily note that competes
  with cardamom.
- **Risk if whole nuts sit in the pot:** after slow heating they soften and pick up grounds, so
  the "crunchy surprise at the bottom" becomes a soggy, gritty one.
- **Recommendation:** serve 15–20 g of lightly roasted pistachios **in a small dish beside the
  cup**. It keeps the idea (a crunchy, rich finish) and makes better theatre.
- **Test:** three pots — none, ground in, whole in — scored blind on foam and taste.

## 2. Mastic and saffron: separate variants, small doses

| | Mastic (Chios PDO) | Saffron (Persian) |
|---|---|---|
| Flavour | Piney, resinous, slightly cooling | Honeyed, floral, slightly bitter at high dose |
| Overdose failure | Turns medicinal/turpentine-like | Turns bitter and metallic |
| Starting dose per pot | 1–2 small tears, crushed with sugar | 10–20 threads (≈0.03–0.05 g), bloomed 10 min in a spoon of warm water |
| Format | **Variant A** | **Variant B** |

Don't combine both with cardamom in one cup at launch; three strong aromatics compete. A
"grand" combined cup can be a later, ceremonial special if blind tests support it.

## 3. "Freshly roasted" vs rested beans

- Grinding fresh is essential; ground coffee loses aroma within minutes to hours.
- Roasting fresh is good, but beans straight from the roaster release a lot of CO₂, which can
  disrupt extraction and foam. Most specialty roasters rest beans for days before brewing.
- **Test:** the same roast brewed at day 0, 2, 5 and 10. Fix the best window in the spec.

## 4. Fridge-cold water + ice cubes

- **Likely mechanism:** starting cold makes the heat-up long and gentle, which builds a fine,
  stable foam and gives grounds time to settle and extract evenly. The "freezing smoke" is
  condensation; it isn't the cause.
- **Test:** (a) fridge water + ice, (b) fridge water only, (c) room-temperature water with the
  burner set to give the **same total heat-up time**. If (c) matches (a), the real variable is
  time-to-foam, which is far easier to teach and reproduce.

## 5. The 1,000 stirs

- **Likely mechanism:** constant stirring keeps the powder suspended, dissolves sugar evenly and
  prevents scorching on the base of the copper while the foam forms.
- **Test:** 0, 100, 300 and 1,000 stirs at identical heat and time. If 300 matches 1,000 blind,
  the process is still hand-made but needs ~60% less labour per pot (Doc 05). If 1,000 wins, it
  becomes part of the story, and the price must carry it.

## 6. Sugar level

27 g in 200–250 ml is very sweet, around the "ziyada" level. Egyptian coffeehouses always ask
*sada, aryaha, mazbout, ziyada*. Offer four levels, keep 27 g as "house sweet", and record which
level sells.

## 7. Light roast for Turkish coffee

Light-to-medium roasts are common in Egypt's Turkish coffee ("fateh"), so this isn't exotic
locally. Note for export markets: very light roasts can taste sharp when brewed this way; check
acidity scores in blind tests with Gulf and Western panels.

## 8. Cardamom ratio

10% cardamom is the signature, but it's a lot, and it may mask the floral and fruity notes that
make Yemeni coffee special. Keep 90:10 as the control and test 99:1, 97:3, 95:5 and 90:10 blind.
Don't assume less is better; let tasters decide. Run it with both Egyptian/Gulf and non-Arab
panels, since the best ratio may differ by market.

## 9. Roast profile

The original belief was that a light roast suits everyone who likes medium or dark, but not the
reverse. That isn't reliably true: light roasts keep more acidity and taste less "traditional" to
many drinkers. Test light, medium and dark versions of the same lot blind.

## 10. Allergen

Pistachio is a tree-nut allergen. Disclose it on menus and packs, keep the side dish separate,
and keep nut-free packs free of cross-contact.

## 11. Decomposition: the machine's spec comes from here

These tests do double duty. Besides improving the cup, they show **which variables are
load-bearing**: the stirs, the ice, the heat curve, the cardamom ratio, the roast. A machine can't
be built to "make it taste like mine"; it needs "variable X within range Y". Doc 12 takes its spec
from these results.

## 12. Testing rules

- One variable at a time; everything else at spec v1.0.
- At least 12 blind tasters per comparison, triangle test first ("which one is different?"),
  preference second.
- Log every pot (Doc 01 §4).
