TITLE = 'Assetto Corsa Competizione - Discord Rich Presence'
AUTHOR = 'Manuel Cabral'
GITHUB = 'https://github.com/manucabral'
REPO_URL = "https://api.github.com/repos/manucabral/acc-discord-rpc/releases"
VERSION = '0.1'
GAME = 'Assetto Corsa Competizione'

LANGUAGE = {
    'es': 0,
    'en': 1
}

TAGNAME = {
    'statics': u"Local\\acpmf_static",
    'graphics': u"Local\\acpmf_graphics"
}

STATUS = {
    0: ('En el menú principal', 'In main menu'),
    1: ('Viendo una repeticion', 'Watching a replay'),
    2: ('Conduciendo', 'Live'),
    3: ('En pausa', 'In pause')
}

RAIN = {
    0: ('Sin lluvia', 'No Rain'),
    1: ('Llovizna', 'Drizzle'),
    2: ('Lluvia ligera', 'Light Rain'),
    3: ('Lluvia', 'Rain'),
    4: ('Lluvia fuerte', 'Heavy Rain'),
    5: ('Tormenta', 'Thunderstorm')
}
SESSION = {
    -1: ('Desconocido', 'Unknown'),
    0: ('Practica', 'Practice'),
    1: ('Calificatoria', 'Qualify'),
    2: ('Carrera', 'Race'),
    3: ('Hotlap', 'Hotlap'),
    4: ('Ataque de tiempo', 'Time Attack'),
    5: ('Drift', 'Drift'),
    6: ('Drag', 'Drag'),
    7: ('Hotstint', 'Hotstint'),
    8: ('Hotlapsuperpole', 'Hotlapsuperpole')
}

CAR_MODEL = {
    'amr_v12_vantage_gt3': 'Aston Martin Vantage V12 GT3 2013',
    'audi_r8_lms': 'Audi R8 LMS 2015',
    'bentley_continental_gt3_2016': 'Bentley Continental GT3 2015',
    'bentley_continental_gt3_2018': 'Bentley Continental GT3 2018',
    'bmw_m6_gt3': 'BMW M6 GT3 2017',
    'jaguar_g3': 'Emil Frey Jaguar G3 2012',
    'ferrari_488_gt3': 'Ferrari 488 GT3 2018',
    'honda_nsx_gt3': 'Honda NSX GT3 2017',
    'lamborghini_gallardo_rex': 'Lamborghini Gallardo G3 Reiter 2017',
    'lamborghini_huracan_gt3': 'Lamborghini Huracan GT3 2015',
    'lexus_rc_f_gt3': 'Lexus RCF GT3 2016',
    'mclaren_650s_gt3': 'McLaren 650S GT3 2015',
    'mercedes_amg_gt3': 'Mercedes AMG GT3 2015',
    'nissan_gt_r_gt3_2017': 'Nissan GTR Nismo GT3 2015',
    'nissan_gt_r_gt3_2018': 'Nissan GTR Nismo GT3 2018',
    'porsche_991_gt3_r': 'Porsche 991 GT3 R 2018',
    'amr_v8_vantage_gt3': 'Aston Martin V8 Vantage GT3 2019',
    'audi_r8_lms_evo': 'Audi R8 LMS Evo 2019',
    'honda_nsx_gt3_evo': 'Honda NSX GT3 Evo 2019',
    'lamborghini_huracan_gt3_evo': 'Lamborghini Huracan GT3 EVO 2019',
    'mclaren_720s_gt3': 'McLaren 720S GT3 2019',
    'porsche_991ii_gt3_r': 'Porsche 911 II GT3 R 2019',
    'ferrari_488_gt3_evo': 'Ferrari 488 GT3 Evo 2020',
    'mercedes_amg_gt3_evo': 'Mercedes AMG GT3 Evo 2020',
    'alpine_a110_gt4': 'Alpine A110 GT4 2018',
    'amr_v8_vantage_gt4': 'ston Martin Vantage AMR GT4 2018',
    'audi_r8_gt4': 'Audi R8 LMS GT4 2016',
    'bmw_m4_gt4': 'BMW M4 GT4 2018',
    'chevrolet_camaro_gt4r': 'Chevrolet Camaro GT4 R 2017',
    'ginetta_g55_gt4': 'Ginetta G55 GT4 2012',
    'ktm_xbow_gt4': 'Ktm Xbow GT4 2016',
    'maserati_mc_gt4': 'Maserati Gran Turismo MC GT4 2016',
    'mclaren_570s_gt4': 'McLaren 570s GT4 2016',
    'mercedes_amg_gt4': 'Mercedes AMG GT4 2016',
    'porsche_718_cayman_gt4_mr': 'Porsche 718 Cayman GT4 MR 2019',
    'porsche_991ii_gt3_cup': 'Porsche9 91 II GT3 Cup 2017',
    'lamborghini_huracan_st': 'Lamborghini Huracan ST 2015'
}

MSG = [
    ('Autor', 'Author'),
    ('Gracias por usar el programa, todavía se encuentra en desarrollo.', 'Thanks for using the program, it is still under development.'),
    ('Obteniendo el idioma de tu sistema ..', 'Checking your system language ..'),
    ('Lenguaje detectado:', 'Language detected:'),
    (f'Esperando ejecución de {GAME} ..', f'Waiting for {GAME} process ..'),
    (f'Proceso de {GAME} detectado', f'{GAME} process detected'),
    ('Conectandose con Discord ..', 'Connecting with Discord ..'),
    ('Conectado con Discord correctamente', 'Discord connected successfully'),
    ('Un jugador', 'Singleplay'),
    ('Multijugador', 'Multiplayer'),
    ('Tiempo', 'Time'),
    ('Posición', 'Position'),
    ('En los pits', 'In the pits'),
    ('Vueltas completadas', 'laps completed'),
    ('En el menú de configuración', 'In configuration menu'),
    ('Buscando actualizaciones ..', 'Checking updates ..'),
    ('Nueva actualización disponible, por favor actualiza a la versión', 'New update is available, please update to version'),
    ('Actualizado', 'Up to date')
]

ERROR = [
    ('Programa interrumpido por el usuario', 'Program interrupt by user'),
    ('Lenguaje no encontrado', 'Language not detected'),
    ('Se excedió el limite de re-conexión con Discord, cerrando programa', 'Discord reconnection limit exceeded, closing program ..'),
    ('Hubo un error al conectarse con Discord', 'An error occurred when trying to connect'),
    ('Re-conectandose con Discord en 5s ..', 'Reconnecting with Discord in 5s ..'),
    (f'{GAME} se ha cerrado, re-conectando ..', f'{GAME} has closed, reconnecting ..'),
    ('Error al manipular el archivo de registro', 'Error on generating log file')
]