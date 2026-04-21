consultas_entrenamiento = [
    # INTERNET
    "no tengo internet",
    "internet no funciona",
    "la conexion se cae",
    "no puedo conectarme a la red",
    "no puedo conectarme al wifi",
    "el wifi no funciona",
    "no tengo conexion wifi",
    "mi wifi falla",
    "no me va el internet",
    "la red no responde",
    "no carga ninguna pagina",
    "se ha ido internet",
    "el router no da señal",
    "mi ordenador no se conecta a internet",
    "no puedo navegar",
    "la conexion es inestable",
    "se corta el wifi",
    "el cable de red no funciona",
    "no tengo acceso a internet",
    "la red va muy lenta",

    # CONTRASENA
    "olvide mi contraseña",
    "no recuerdo la clave",
    "no puedo iniciar sesion",
    "me rechaza la contraseña",
    "no puedo entrar en mi cuenta",
    "he perdido la clave",
    "mi usuario no entra",
    "no puedo acceder al sistema",
    "la contraseña no funciona",
    "bloquearon mi cuenta",
    "no me deja iniciar sesion",
    "tengo problemas para acceder",
    "no puedo entrar al correo",
    "no acepta mi usuario y contraseña",
    "he olvidado la contraseña del ordenador",
    "me dice credenciales incorrectas",
    "no puedo desbloquear mi cuenta",
    "no puedo entrar en la plataforma",
    "mi cuenta aparece bloqueada",
    "no recuerdo mis datos de acceso",

    # IMPRESORA
    "la impresora no imprime",
    "no sale nada por la impresora",
    "la impresora esta atascada",
    "no detecta la impresora",
    "la impresora da error",
    "no imprime el documento",
    "la impresora no responde",
    "no puedo imprimir",
    "sale el papel en blanco",
    "la impresora no tiene conexion",
    "el ordenador no encuentra la impresora",
    "la cola de impresion se queda bloqueada",
    "la impresora imprime mal",
    "la impresora esta desconectada",
    "no salen las hojas",
    "me da error de impresion",
    "la impresora no aparece disponible",
    "no imprime en red",
    "no reconoce la impresora usb",
    "la impresion se cancela sola",

    # RENDIMIENTO
    "el ordenador va lento",
    "mi pc tarda mucho en arrancar",
    "el equipo se queda bloqueado",
    "el sistema esta muy lento",
    "el ordenador se congela",
    "todo va muy despacio",
    "el pc tarda mucho en abrir programas",
    "se queda pensando todo el rato",
    "mi portatil funciona lento",
    "el equipo responde con retraso",
    "el ordenador se cuelga",
    "va lento desde esta mañana",
    "las aplicaciones tardan en abrir",
    "el sistema se bloquea con frecuencia",
    "mi pc consume muchos recursos",
    "el ventilador va muy fuerte y va lento",
    "el equipo arranca muy despacio",
    "el ordenador no responde bien",
    "todo tarda demasiado",
    "el rendimiento del pc es muy bajo"
]

etiquetas_entrenamiento = [
    # INTERNET (20)
    "internet","internet","internet","internet","internet",
    "internet","internet","internet","internet","internet",
    "internet","internet","internet","internet","internet",
    "internet","internet","internet","internet","internet",

    # CONTRASENA (20)
    "contrasena","contrasena","contrasena","contrasena","contrasena",
    "contrasena","contrasena","contrasena","contrasena","contrasena",
    "contrasena","contrasena","contrasena","contrasena","contrasena",
    "contrasena","contrasena","contrasena","contrasena","contrasena",

    # IMPRESORA (20)
    "impresora","impresora","impresora","impresora","impresora",
    "impresora","impresora","impresora","impresora","impresora",
    "impresora","impresora","impresora","impresora","impresora",
    "impresora","impresora","impresora","impresora","impresora",

    # RENDIMIENTO (20)
    "rendimiento","rendimiento","rendimiento","rendimiento","rendimiento",
    "rendimiento","rendimiento","rendimiento","rendimiento","rendimiento",
    "rendimiento","rendimiento","rendimiento","rendimiento","rendimiento",
    "rendimiento","rendimiento","rendimiento","rendimiento","rendimiento"
]

respuestas_soporte = {
    "internet": {
        "respuesta": "Parece un problema de conectividad de red.",
        "pasos": [
            "Comprueba si el router está encendido.",
            "Reinicia el router y espera unos segundos.",
            "Verifica si otros dispositivos tienen conexión.",
            "Comprueba que el WiFi o el cable de red estén activos."
        ]
    },
    "contrasena": {
        "respuesta": "Parece un problema de acceso o autenticación.",
        "pasos": [
            "Comprueba que el usuario sea correcto.",
            "Revisa si la tecla de mayúsculas está activada.",
            "Intenta restablecer la contraseña.",
            "Si continúa el problema, contacta con soporte."
        ]
    },
    "impresora": {
        "respuesta": "Parece una incidencia relacionada con la impresora.",
        "pasos": [
            "Comprueba que la impresora esté encendida.",
            "Revisa si tiene papel o tinta.",
            "Comprueba la conexión al equipo o a la red.",
            "Vuelve a intentar la impresión."
        ]
    },
    "rendimiento": {
        "respuesta": "Parece un problema de rendimiento del equipo.",
        "pasos": [
            "Cierra programas que no estés usando.",
            "Reinicia el ordenador.",
            "Comprueba si queda espacio libre en disco.",
            "Pasa un análisis antivirus si notas algo extraño."
        ]
    }
}