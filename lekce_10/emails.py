def projdi_udaje(*args) -> list:
    for udaj in args:
        if "quit" in udaj.lower():
            break
        else:
            jmeno, domena = udaj.split("@")
            print(
                {
                    "jmeno": jmeno,
                    "domena": domena
                }
            )


projdi_udaje(
    'p.fulinova@firma.cz',
    'a.vancurova@firma.cz',
    'a.hertlova@firma.cz',
    'p.vyhnis@firma.cz',
    'j.feckanin@firma.cz',
    'p.harant@firma.cz',
    'm.miczova@firma.cz',
    'j.mosquito@firma.cz',
    'b.suvova@firma.cz',
    'l.kafkova@firma.cz',
    'n.hoffmannova@firma.cz',
    'd.sedlakova@firma.cz',
    'i.jerabkova@firma.cz',
    'v.jagerska@firma.cz',
    'h.bayerova@firma.cz',
    't.zamecnik@firma.cz',
    'h.strasilova@firma.cz',
    'j.kralova@firma.cz',
    'h.duskova@firma.cz',
    'd.mirgova@firma.cz',
    "quit"
)