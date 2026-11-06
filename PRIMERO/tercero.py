def generar_tabla_desde_texto(texto):
    comandos = []

    # Procesa cada línea del texto
    for linea in texto.splitlines():
        linea = linea.strip()
        if not linea:
            continue

        # Separar comando y descripción por el primer grupo de espacios
        partes = linea.split(None, 1)

        if len(partes) == 2:
            cmd, desc = partes
            comandos.append((cmd.strip(), desc.strip()))

    # Determinar anchos máximos
    max_cmd = max(len(cmd) for cmd, _ in comandos)
    max_desc = max(len(desc) for _, desc in comandos)

    # Construir tabla
    tabla = []
    tabla.append(f"| {'COMANDO'.ljust(max_cmd)} | {'DESCRIPCIÓN'.ljust(max_desc)} |")
    tabla.append(f"|{'-'*(max_cmd+2)}|{'-'*(max_desc+2)}|")

    for cmd, desc in comandos:
        fila = f"| {cmd.ljust(max_cmd)} | {desc.ljust(max_desc)} |"
        tabla.append(fila)

    return "\n".join(tabla)


# ------------------------
# EJEMPLO DE USO
# ------------------------

texto = """
am                      Apply a series of patches from a mailbox
archive                 Create an archive of files from a named tree
backfill                Download missing objects in a partial clone
bisect                  Use binary search to find the commit that introduced a bug
branch                  List, create, or delete branches
bundle                  Move objects and refs by archive
checkout                Switch branches or restore working tree files
cherry-pick             Apply the changes introduced by some existing commits
"""

print(generar_tabla_desde_texto(texto))