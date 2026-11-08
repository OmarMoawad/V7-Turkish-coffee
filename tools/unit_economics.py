# Unit-economics calculator for docs/05. All inputs are assumptions; edit and re-run: python3 tools/unit_economics.py
FX=56.3  # EGP per USD, late Oct 2026
# Coffee: green FOB $65-68/kg (Typica); assume landed $75-95/kg; roast loss 16%
for green in (75,95):
    roasted=green/0.84
    print(f"green ${green}/kg -> roasted cost ${roasted:.0f}/kg = EGP {roasted*FX:,.0f}/kg")
lo_r, hi_r = 75/0.84, 95/0.84
def pot(coffee_g, card_g, extras_usd=0.0, r=None):
    c = coffee_g*r/1000 + card_g*0.035 + 27*0.0008 + extras_usd   # cardamom $35/kg, sugar ~$0.8/kg
    return c
for name,cg,kg,ex in [("Signature 18g+2g",18,2,0),("Signature 22g+2.4g",22,2.4,0)]:
    a=pot(cg,kg,ex,lo_r); b=pot(cg,kg,ex,hi_r)
    print(f"{name}: ${a:.2f}-{b:.2f} = EGP {a*FX:.0f}-{b*FX:.0f}")
# extras
saffron = (0.03*1.88, 0.05*1.88*3)   # 0.03-0.05 g; wholesale $1.88/g Super Negin; up to 3x retail
mastic  = (0.1*0.15, 0.2*0.30)       # assume $150-300/kg retail
pist    = (15*0.030, 20*0.050)       # 15-20 g side dish, assume $30-50/kg
print("saffron", [round(x,2) for x in saffron], "mastic", [round(x,3) for x in mastic], "pistachio", [round(x,2) for x in pist])
res_lo = pot(20,2.2,saffron[0]+mastic[0]+pist[0],lo_r); res_hi=pot(22,2.4,saffron[1]+mastic[1]+pist[1],hi_r)
print(f"Reserve pot: ${res_lo:.2f}-{res_hi:.2f} = EGP {res_lo*FX:.0f}-{res_hi*FX:.0f}")
# packaged 250g: 225 g coffee + 25 g cardamom + $1.2 packaging
for r in (lo_r,hi_r):
    p=225*r/1000+25*0.035+1.2
    print(f"250g bag cost ${p:.2f} = EGP {p*FX:,.0f}")
# mass-market comparison (Carrefour Egypt)
abu=149.98/200*20; ameed=398.99/200*20
print(f"Abu Auf 20g = EGP {abu:.0f}; Al Ameed 20g = EGP {ameed:.0f}; per-kg Abu {149.98*5:.0f}, Ameed {398.99*5:.0f}")
print(f"Al Ameed 250g equiv EGP {398.99*1.25:.0f}")
# throughput & flagship scenario
pots_per_hr=5; labor_hr=100
print("labor per pot EGP", labor_hr/pots_per_hr)
for pots_day,price in ((40,400),(60,400),(60,650)):
    rev=pots_day*price*360
    print(f"{pots_day} pots/day @EGP{price}: EGP {rev/1e6:.1f}M/yr = ${rev/FX/1e3:.0f}k")
# margins at price points
sig_cost_hi = pot(22,2.4,0,hi_r)*FX + 20 + 15  # +labor +cup/water/overheads? (15 = consumables/waste)
for price in (350,450):
    print(f"Signature @{price}: cost ~{sig_cost_hi:.0f} -> ingredient+labor margin {(1-sig_cost_hi/price)*100:.0f}%")
res_cost_hi = res_hi*FX+20+20
for price in (650,900):
    print(f"Reserve @{price}: cost ~{res_cost_hi:.0f} -> {(1-res_cost_hi/price)*100:.0f}%")
print("Caribou double 78.75 per serving; Signature per serving (pot=2):", 350/2, 450/2, "ratio", round(175/78.75,1), round(225/78.75,1))
print("Wild Fox $105 in EGP", 105*FX)
print("Port of Mokha $13/oz -> $/250g", round(13/28.35*250,0))

print("\n--- Sensitivity: Yemeni coffee bought on the Cairo retail market (ChatGPT review refs) ---")
for label,price,grams in (("EGP 417 / 200 g",417,200),("EGP 850 / 250 g",850,250)):
    per_g=price/grams
    print(f"{label}: EGP {per_g*1000:,.0f}/kg -> 18-24 g = EGP {18*per_g:.0f}-{24*per_g:.0f} per pot")

print("\n--- Labour sensitivity (DeepSeek review: 15-20 min per pot) ---")
for pph in (3,4,5,8):
    print(f"{pph} pots/brewer-hour -> labour EGP {100/pph:.0f}/pot at EGP 100/hr; 60 pots/day needs {60/pph:.0f} brewer-hours")

print("\n--- Honest daily tier (machine-brewed single cup, ~70 ml) ---")
# assume fine robusta / commercial blend green $5-8/kg landed, 16% roast loss
for green in (5,8):
    r=green/0.84*FX/1000   # EGP per g roasted
    coffee=8*r; card=0.8*0.035*FX; sugar=7*0.0008*FX; cup_misc=4; labour=3
    total=coffee+card+sugar+cup_misc+labour
    print(f"green ${green}/kg: coffee EGP {coffee:.1f} + cardamom {card:.1f} + sugar {sugar:.1f} + cup/misc {cup_misc} + labour {labour} = EGP {total:.1f}; at EGP 50 contribution {(1-total/50)*100:.0f}%")
