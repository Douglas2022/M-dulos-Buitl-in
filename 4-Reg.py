import re
text = "Undermy - uma plataforma com muitos  cursos"
# 1 - Indice inicial e final de palavras
#  O r significa uma row string(string bruta)
match = re.search(r"uma plataforma",text)
print(f"Indice inicial: {match.start()}")
print(f"Indice final: {match.end()}")