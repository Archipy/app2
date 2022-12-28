import pandas

# archivo = "C:/Users/Usuario/Desktop/SG010.xlsm"
archivo = "./static/archivos/SG010"

df2 = pandas.read_excel(archivo, sheet_name="Data")
df = df2[["PRIMARY", "UNCONF_OUT", "SALESMETHOD"]].dropna()
df = df[(df['UNCONF_OUT'] != 0) & (df['SALESMETHOD'] == 1)]

pares_pasillos = ("8", "10", "12", "14", "16", "18", "20", "22")
impares_pasillos = ("5", "7", "9", "11", "13", "15", "17", "19")
pax_pasillos = ("21", "23")
veinticuatro_pasillos = ("24", "26")
fondopar_pasillos = ("28", "30", "32", "34", "36", "38", "40", "42")
fondoimpar_pasillos = ("25", "27", "29", "31", "33", "35", "37", "39", "41", "43")
pasillo1a3_pasillos = ("1", "3")


def check_repoaire():
    zona1 = 0
    zona2 = 0
    zona3 = 0
    zona4 = 0
    pasillo1a3 = 0
    impares = 0
    pares = 0
    pax = 0
    veinticuatro = 0
    fondopar = 0
    fondoimpar = 0

    for lv in df["PRIMARY"]:
        if str(lv).startswith("1") and len(str(lv)) <= 3:
            zona1 += 1
        elif str(lv).startswith("2") and len(str(lv)) <= 3:
            zona2 += 1
        elif str(lv).startswith("3") and len(str(lv)) <= 3:
            zona3 += 1
        elif str(lv).startswith("4") and len(str(lv)) <= 3:
            zona4 += 1
        elif str(lv).startswith("4") and len(str(lv)) <= 3:
            zona4 += 1
        elif str(lv).startswith(pasillo1a3_pasillos) and len(str(lv)) <= 5:
            pasillo1a3 += 1
        elif str(lv).startswith(pares_pasillos):
            pares += 1
        elif str(lv).startswith(impares_pasillos):
            impares += 1
        elif str(lv).startswith(pax_pasillos):
            pax += 1
        elif str(lv).startswith(veinticuatro_pasillos):
            veinticuatro += 1
        elif str(lv).startswith(fondopar_pasillos):
            fondopar += 1
        elif str(lv).startswith(fondoimpar_pasillos):
            fondoimpar += 1

    return zona1, zona2, zona3, zona4, pares, impares, pax, veinticuatro, fondopar, fondoimpar, pasillo1a3