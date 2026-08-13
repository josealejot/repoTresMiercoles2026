from funciones import registrar_equipo, calcular_nota_general

equipo_uno = registrar_equipo(5, "equipo 1")
equipo_dos = registrar_equipo(5, "equipo 2")
equipo_tres = registrar_equipo(5, "equipo 3")
equipo_cuatro = registrar_equipo(5, "equipo 4")

nota_equipo_uno = calcular_nota_general(equipo_uno, [1, 2, 3, 3, 5], [1, 1, 1, 1, 1], [5, 4, 3, 3, 3])