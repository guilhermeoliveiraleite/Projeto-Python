from fpdf import FPDF

class PDF(FPDF):

    def titulo(self, label):
        self.set_font('helvetica', 'B', size=24)
        self.cell(0, 60, label, 0, 1, 'C')

    def sub_titulo(self, label):
        self.set_font('helvetica', 'I', size=16)
        self.cell(0, 10, label, 0, 1, 'C')
    
    def linha_centralizada(self, label):
        self.set_font('helvetica', '', size=12)
        self.cell(0, 10, label, 0, 1, 'C')
    
    def titulo_base(self, label):
        self.set_font('helvetica', 'B', size=16)
        self.cell(0, 10, label, 0, 1, 'L')
        self.ln()

    def paragrafo(self, text):
        self.set_font('helvetica', '', size=12)
        self.multi_cell(0, 7, text)
        self.ln()

    def imagem(self, img, x, y, w):
        self.image(img, x, y, w)

pdf = PDF()

# ------------- Fazendo a capa -------------
pdf.add_page()

pdf.titulo("Desigualdade na educação")
pdf.sub_titulo("Como a desigualdade afetar no resultado do Enem 2023 - SP")
pdf.sub_titulo("Análisando: Tipo de escola, raça, renda e tipo de localização")
pdf.imagem("enemimg.png", 40, 90, 130)
pdf.ln(100)
pdf.linha_centralizada("Autor: Guilherme de Oliveira Leite")
pdf.linha_centralizada("Data: 15 de Setembro, 2024")
pdf.linha_centralizada("Fonte de dados : INEP")
# ------------- 1 pagina -------------
pdf.add_page()

pdf.titulo_base("Intrução")

pdf.paragrafo("A desigualdade educacional em São Paulo é um problema complexo que pode ser analisado a partir de diversos fatores, como a origem social, a raça, o gênero e a região geográfica.")

pdf.paragrafo("entre escolas públicas e privadas no Enem 2023 aumentou em Matemática e Ciências da Natureza, revertendo tendência anterior.")

pdf.imagem("media_por_escola.png", 30, 105, 150)
pdf.ln(160)

pdf.paragrafo("Com base a análise inicial podemos concluir que está bem equilibrado a questão de notas com escolas publicas e privadas, porém não podemos esquecer que o mesmo número se dá para os canditados que optaram por não responder.")

# ------------- 2 pagina -------------
pdf.add_page()

pdf.titulo_base("Análise de raça")

pdf.paragrafo("Agora iremos análisar os candidatos por raça.")

pdf.imagem("raca.png", 40, 50, 130)
pdf.ln(93)

pdf.paragrafo("O gráfico mostra que a quantidade por raça, está bem equilibrada. Isso mostra que o estado de São Paulo, tem um equilibrio em sua população referente a raça, e isso se espelha na educação.")


pdf.ln(93)



# ------------- 3 pagina -------------
pdf.add_page()
pdf.titulo_base("Análise da renda")


pdf.imagem("media_renda.png", 10, 20, 200)
pdf.ln(93)

pdf.paragrafo("No terceiro gráfico, podemos ver como a renda tem forte impacto no resultado final (notas). Podemos concluir que até o momento é o maior impacto sobre as notas.")
pdf.ln(93)



# ------------- 4 pagina -------------
pdf.add_page()
pdf.titulo_base("Análise tipo de localidade")
pdf.ln(120)
pdf.imagem("local.png", 30, 20, 130)


pdf.paragrafo("Análisando o quarto gráfico, a área rural (interior do estado), tem uma leve vantagem em pontos totais.")


pdf.paragrafo("Podemos concluir que as cidades do interior, mesmo com menos escolas, dependendo das cidades, conseguem superar em média de notas a capital.")

# ------------- 5 página -------------
pdf.add_page()

pdf.titulo_base("Conclusão")

pdf.paragrafo("Com o término desta análise podemos concluir que a desigualdade na renda, tem o maior impacto para os candidatos ao ENEM no estado de São Paulo, no ano de 2023. Podemos dizer que o investimento na educação, como escolas privadas ou cursos complementares, contribuem muito em uma melhor nota, e como candidatos com renda baixa não conseguem investir em sua educação, por falta de tempo ou por falta de dinheiro, acabam ficando pra trás no desenvolvimento educacional.")

pdf.output("relatório.pdf")