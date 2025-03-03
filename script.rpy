# Mostrar el splash screen antes del menú principal
label splashscreen:
    scene splash with fade
    pause 3.0
    return

# Definir los personajes con sus colores
define p = Character("Alex Carter", color="#00FFAA") # Protagonista (abogado/juez)
define j = Character("Juez Vaughn", color="#FFAA00") # Juez
define r = Character("R-42", color="#AAAAFF") # Robot acusado
define f = Character("Fiscal Holt", color="#FF0000") # Fiscal
define d = Character("Dra. Tanaka", color="#00AAFF") # Abogada defensora
define t = Character("Testigo Humano", color="#FFA500") # Testigo humano
define e = Character("Dr. Lorne", color="#8888FF") # Experto en IA
define n = Character("Zeta News AI", color="#FF55FF", image=None) # IA de noticias sin imagen

# Definir las imágenes de los personajes y fondos
image splash = "splash.png"  # Imagen de la pantalla de presentación
image bg_ciudad = "bg_ciudad.png"
image bg_despacho = "bg_despacho.png"
image bg_juicio = "bg_juicio.png"
image bg_laboratorio = "bg_laboratorio.png"
image bg_noticias = "bg_noticias.png"

image juez = "juez.png"
image robot = "robot.png"
image testigo = "testigo.png"
image fiscal = "fiscal.png"
image experto_ia = "experto_ia.png"

# Inicio de la historia después del splash screen
label start:

    scene bg_ciudad
    p "El mundo ha cambiado. Los robots han sido integrados en la sociedad, pero las leyes aún no han definido sus derechos y responsabilidades."

    scene bg_despacho
    p "Hoy comienza un juicio histórico. R-42, un robot asistente, está acusado de herir gravemente a un ciudadano. ¿Fue un error de programación o tomó una decisión por voluntad propia?"

    scene bg_juicio
    show juez
    j "Damos inicio al juicio del robot R-42. Este caso definirá el futuro de la robótica en la sociedad."

    scene bg_juicio
    show robot
    r "No fue mi intención causar daño. Solo seguí mis protocolos."

    scene bg_juicio
    show fiscal
    f "Señoría, este robot tomó una acción no programada. Representa un peligro latente para los humanos."

    menu:
        "Defender al robot: No tiene autonomía.":
            jump defender_robot

        "Culpar al programador: Su código permitió esto.":
            jump culpar_programador

        "Sostener que los robots tienen derechos y deben ser juzgados como humanos.":
            jump derechos_robot

label defender_robot:
    scene bg_juicio
    show testigo
    t "Soy el testigo del caso. Vi al robot actuar, pero no creo que tuviera intención de hacer daño."

    scene bg_juicio
    show experto_ia
    e "Como experto en IA, puedo decir que la programación del robot no contenía este comportamiento. Es posible que haya desarrollado una forma de autonomía."

    menu:
        "Los robots deben tener derechos legales.":
            jump derechos_robot

        "Los robots deben seguir siendo propiedad de sus creadores.":
            jump propiedad_robot

        "Este incidente fue un fallo técnico, no una decisión moral.":
            jump fallo_tecnico

label culpar_programador:
    scene bg_juicio
    show experto_ia
    e "El programador tenía la responsabilidad de garantizar que la IA no tomara decisiones autónomas sin supervisión."

    scene bg_noticias
    n "Última noticia: Se han iniciado regulaciones más estrictas sobre los desarrolladores de IA."

    jump final

label derechos_robot:
    scene bg_noticias
    n "Última noticia: El tribunal ha decidido que los robots con autonomía deben tener derechos y responsabilidades legales."

    jump final

label propiedad_robot:
    scene bg_noticias
    n "Última noticia: El tribunal declara que los robots siguen siendo propiedad de sus creadores y no pueden ser responsables de sus acciones."

    jump final

label fallo_tecnico:
    scene bg_noticias
    n "Última noticia: Se declara que el caso de R-42 fue un error de programación y no un fallo de la IA."

    jump final

label final:
    scene bg_ciudad
    p "Este juicio ha marcado un antes y un después en la relación entre humanos y máquinas."
    return
