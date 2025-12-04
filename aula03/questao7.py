# Classifique cada valor de glicemia e gere tuplas contendo o rótulo e o número.

glicemia = [129, 82, 60, 97, 101, 65, 62, 167, 87, 53, 58, 92, 66, 120, 109, 62, 86, 96, 103, 88, 155, 52, 89, 73]

rotulos = [('Hipoglicemia', glicose) if glicose < 70 else ('Normal', glicose) if 70 <= glicose <= 99 else ('Pré-diabetes', glicose) if 100 <= glicose <= 125 else ('Diabetes', glicose) for glicose in glicemia]
print(rotulos)