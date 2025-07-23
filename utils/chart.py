import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
import numpy as np
from scipy.interpolate import make_interp_spline
import io
import base64
from db.database import conectar
from core.state import estado
from collections import defaultdict
from datetime import datetime, timedelta

def gerar_grafico_minimalista():
    u = estado.usuario_logado

    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT acertos, erros, data FROM desempenho WHERE user_id = ?", (u.id,))
    resultados = cursor.fetchall()
    conn.close()

    dias = ["Seg", "Ter", "Qua", "Qui", "Sex", "Sáb", "Dom"]
    acertos_por_dia = defaultdict(int)
    erros_por_dia = defaultdict(int)

    for acertos, erros, data in resultados:
        dia_semana = datetime.strptime(data, "%Y-%m-%d").weekday()
        # Quando for segunda-feira, zerar todos os dados de acertos e erros
        if dia_semana == 0:
            acertos_por_dia = defaultdict(int)
            erros_por_dia = defaultdict(int)

        acertos_por_dia[dia_semana] += acertos
        erros_por_dia[dia_semana] += erros

    acertos_valores = [acertos_por_dia.get(i,0) for i in range(7)]
    erros_valores = [erros_por_dia.get(i,0) for i in range(7)]
    fig, ax = plt.subplots(figsize=(8, 2.5))

    x = np.arange(len(dias))
    largura_barra = 0.2

    def desenhar_barra(x_pos, altura, cor):
        if altura == 0:
            return
        radius = 0.15
        ax.add_patch(FancyBboxPatch(
            (x_pos, 0), largura_barra, altura,
            boxstyle=f"round,pad=0.1,rounding_size={radius}",
            linewidth=0, facecolor=cor
        ))

    # Desenhar barras de acertos
    for i, valor in enumerate(acertos_valores):
        desenhar_barra(x[i] - largura_barra, valor, "#01C6D3")

    # Desenhar barras de erros
    for i, valor in enumerate(erros_valores):
        desenhar_barra(x[i] + largura_barra - 0.1, valor, "#F56A5F")
        

    ax.set_xlim(-0.5, len(dias) - 0.5)
    ax.set_xticks(x)
    ax.set_xticklabels(dias, fontsize=16,  color="#006A71")
    ax.tick_params(axis='x', pad=15, length=0)
    ax.set_ylim(0, max(max(acertos_valores), max(erros_valores)) + 1)

    for spine in ax.spines.values():
        spine.set_visible(False)
    ax.set_yticks([])
    ax.set_facecolor("none")
    fig.patch.set_alpha(0)

    buf = io.BytesIO()
    plt.savefig(buf, format='png', bbox_inches='tight', transparent=True)
    plt.close(fig)
    return base64.b64encode(buf.getvalue()).decode('utf-8')