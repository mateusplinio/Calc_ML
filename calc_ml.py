import openpyxl
from flet import *
import flet as ft
import pandas as pd
from math import floor

def main(pagina: ft.Page):
    pagina.title = "Calculadora ML - GHPC"
    pagina.vertical_alignment = ft.MainAxisAlignment.CENTER

    def calc(e):
        preco_lista = pl.value
        percentual_ipi = ip.value
        percentual_ml = tml.value
        percentual_publicidade = tp.value
        peso = ps.value
        frete_gratis = fg.value

        if preco_lista == '':
            dlg = ft.AlertDialog(title=ft.Text("Insira o Preço Lista!!!"), on_dismiss=lambda e: print("Dialog dismissed!"))
            pagina.dialog = dlg
            dlg.open = True
            pagina.update()
        else:
            pass

        if percentual_ipi == '':
            percentual_ipi = "0"
        else:
            pass

        if percentual_ml == '':
            percentual_ml = '0'
        else:
            pass

        if percentual_publicidade == '':
            percentual_publicidade = '0'
        else:
            pass

        if peso == '':
            peso = '0'
        else:
            pass

        preco_lista = float(preco_lista.replace(',', '.'))
        percentual_ipi = float(percentual_ipi.replace(',', '.'))
        percentual_ml = float(percentual_ml.replace(',', '.'))
        percentual_publicidade = float(percentual_publicidade.replace(',', '.'))
        peso = float(peso.replace(',', '.'))
     
        if peso < 0.3 or peso >= 1:
            peso_adaptado = floor(peso)
        elif peso < 0.5:
            peso_adaptado = peso - (peso - 0.3)
        else:
            peso_adaptado = peso - (peso - 0.5)
        
        if frete_gratis == False:
            valor_frete = 0
        else:
            frete_ml = pd.DataFrame(data={'DE':[0, 0.30, 0.50, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150],
                                          'VL_FRETE':[40.90, 41.90, 43.90, 46.90, 47.90, 49.90, 51.90, 83.90, 83.90, 83.90, 83.90, 131.90, 131.90, 131.90, 131.90, 146.90, 146.90, 146.90, 146.90, 171.90, 171.90, 171.90, 171.90, 171.90, 171.90, 197.90, 197.90, 197.90, 197.90, 197.90, 197.90, 197.90, 218.90, 218.90, 218.90, 218.90, 218.90, 218.90, 218.90, 218.90, 218.90, 218.90, 233.90, 233.90, 233.90, 233.90, 233.90, 233.90, 233.90, 233.90, 233.90, 233.90, 249.90, 249.90, 249.90, 249.90, 249.90, 249.90, 249.90, 249.90, 249.90, 249.90, 282.90, 282.90, 282.90, 282.90, 282.90, 282.90, 282.90, 282.90, 282.90, 282.90, 313.90, 313.90, 313.90, 313.90, 313.90, 313.90, 313.90, 313.90, 313.90, 313.90, 349.90, 349.90, 349.90, 349.90, 349.90, 349.90, 349.90, 349.90, 349.90, 349.90, 399.90, 399.90, 399.90, 399.90, 399.90, 399.90, 399.90, 399.90, 399.90, 399.90, 446.90, 446.90, 446.90, 446.90, 446.90, 446.90, 446.90, 446.90, 446.90, 446.90, 446.90, 446.90, 446.90, 446.90, 446.90, 446.90, 446.90, 446.90, 446.90, 446.90, 446.90, 446.90, 446.90, 446.90, 446.90, 474.90, 474.90, 474.90, 474.90, 474.90, 474.90, 474.90, 474.90, 474.90, 474.90, 474.90, 474.90, 474.90, 474.90, 474.90, 474.90, 474.90, 474.90, 474.90, 474.90, 474.90, 474.90, 474.90, 474.90, 474.90, 498.90]})

            valor_frete = frete_ml.loc[frete_ml["DE"] == peso_adaptado, "VL_FRETE"].iloc[0]

        taxa_fixa = 6
        limitetaxafixa = 79
        markup = 0.6
        menor_recebivel = 10
        taxa_total = (percentual_ml / 100) + (percentual_publicidade / 100)
        valor_minimo_receber_calculado = preco_lista / 4 * (1 + markup)

        if valor_minimo_receber_calculado <= menor_recebivel:
            valor_minimo_receber = menor_recebivel
        else:
            valor_minimo_receber = valor_minimo_receber_calculado

        condicao_a = (valor_minimo_receber + valor_frete) / (1 - taxa_total) * (1 + (percentual_ipi / 100))
        condicao_b = (valor_minimo_receber + (valor_frete / 2)) / (1 - taxa_total) * (1 + (percentual_ipi / 100))
        condicao_c = (valor_minimo_receber + valor_frete + taxa_fixa) / (1 - taxa_total) * (1 + (percentual_ipi / 100))

        if condicao_a >= limitetaxafixa:
            if condicao_b >= limitetaxafixa:
                valor_anuncio = condicao_b
            else:
                valor_anuncio = limitetaxafixa
        else:
            if condicao_c >= limitetaxafixa:
                valor_anuncio = limitetaxafixa
            else:
                valor_anuncio = condicao_c

        if valor_anuncio >= limitetaxafixa:
            valorfretedisplay = valor_frete / 2
        else:
            valorfretedisplay = valor_frete

        vf.value = round(valorfretedisplay, 2)
        vma.value = round(valor_anuncio, 2)
        vmr.value = round(valor_minimo_receber, 2)
        pagina.update()

    titulo = ft.Image(src_base64="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")
    pl = ft.TextField(label="Preço Lista:")
    ip = ft.TextField(label="IPI (%):")
    tml = ft.TextField(label="Taxa Mercado Livre (%):")
    tp = ft.TextField(label="Taxa Publicidade (%):")
    ps = ft.TextField(label="Peso (Kg):")
    fg = ft.Checkbox(label="Frete Grátis", value=False)
    calcular = ft.ElevatedButton("Calcular", on_click=calc)
    vf = ft.TextField(label="Valor de Frete:")
    vma = ft.TextField(label="Valor Mín. de Anúncio:")
    vmr = ft.TextField(label="Valor Mín. à Receber:")

    pagina.add(
        ft.Column([titulo, pl, ip, tml, tp, ps, fg, calcular, vf, vma, vmr])
    )

ft.app(target=main)