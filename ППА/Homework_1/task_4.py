from opcode import jrel_op

companions = ["Astarion", "Gale", "Karlach", "Lae'zel",
              "Shadowheart", "Wyll", "The Dark Urge", "Halsin",
              "Jaheira", "Minsc", "Minthara", "Alfira", "Losiir"]


# ["Gale", "Karlach", "Lae'zel"]
# ["Gale", "Lae'zel", "Wyll", "Halsin", "Halsin", "Minsc", "Alfira"]
# ["Alfira", "Jaheira", "Wyll", "Karlach"]
# ["Astarion", "Losiir"]


print(companions[1:4])
print(companions[1::2])
print(companions[-2::-3])
print(companions[0::12])

