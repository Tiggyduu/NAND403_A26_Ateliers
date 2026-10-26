import random
from maya import cmds

# Permet le Ctrl Z
cmds.undoInfo(openChunk=True)

try:

    # Vérifie si "la_cavalry" existe déjà
    if cmds.objExists("la_cavalry"):

        # Si oui, on dit que "la_cavalry" est la même que celle du projet maya et on supprime ses keys
        la_cavalry = "la_cavalry"
        cmds.cutKey(la_cavalry, clear=True)

    else:

            # Si "la_cavalry" n'est pas encore, on la crée
            la_cavalry = cmds.polyCube(name="la_cavalry")

    # Change les options de playback pour que l'animation dure 100 frames
    cmds.playbackOptions(min=0, max=100)

    # Initie "time" à 0 avant la for loop
    time = 0

    for loop in range(3):

        # Set des valeurs random en int dans tous les axes
        cmds.setKeyframe(la_cavalry, attribute="translateX", value=random.randint(-50, 50), time=time)
        cmds.setKeyframe(la_cavalry, attribute="translateY", value=random.randint(-50, 50), time=time)
        cmds.setKeyframe(la_cavalry, attribute="translateZ", value=random.randint(-50, 50), time=time)

        # Incrémente "time" avec un +50 pour arriver à un total de 100 frames (0, 50, 100)
        time = time + 50

finally:

    cmds.undoInfo(closeChunk=True)


#### NOTES POUR PLUS TARD #####

# Ajout de keyframe
# cmds.setKeyframe(objet, attribute, value, time)

# Tout effacer
# cmds.cutKey(la_cavalry, clear=True) 

# Configurer la durée de l'animation
# cmds.playbackOptions(min, max)