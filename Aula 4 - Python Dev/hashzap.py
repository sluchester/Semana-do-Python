# Título:  Hashzap
# Botão de iniciar chat
    # popup (janela na frente da tela)
    # Título: bem vindo ao hashzap
    # campo de texto -> Escreva seu nome no chat
    # Botão entrar no chat
        # Sumir com o titulo hashzap
        # Sumir com o botao iniciar chat
        # Fechar a janela de popup
        # Carregar o chat
            # As mensagens que já foram enviadas
            # Campo: digite sua mensagem
            # botão de enviar

# flet: ferramenta que cria o frontend e o backend
# pip install flet

import flet as ft

# criar a funcao principal do aplicativo
def main(pagina):
    # cria o elemento de texto
    titulo = ft.Text("HashZap")

    titulo_janela = ft.Text("Bem vindo ao HashZap")
    campo_nome_usuario = ft.TextField(label="Escreva seu nome no chat")

    # um chat nada mais é do que uma mensagem em cima de outra -> uma coluna
    chat = ft.Column()

    def tunel_comunicacao(mensagem):
        texto_chat = ft.Text(mensagem)
        chat.controls.append(texto_chat)
        pagina.update()
    pagina.pubsub.subscribe(tunel_comunicacao)    

    def enviar_mensagem(evento):
        texto_mensagem = campo_mensagem.value
        nome_usuario = campo_nome_usuario.value
        # texto dinamico/ concatencao de strings
        mensagem = f"{nome_usuario}: {texto_mensagem}"
        pagina.pubsub.send_all(mensagem)
        campo_mensagem.value = ""
        pagina.update()
    
    campo_mensagem = ft.TextField(label="Digite sua mensagem", on_submit=enviar_mensagem)
    botao_enviar_mensagem = ft.ElevatedButton("Enviar", on_click=enviar_mensagem)
    # faz com que os elementos aparecam um do lado do outro
    linha_mensagem = ft.Row([campo_mensagem, botao_enviar_mensagem])

    def entrar_no_chat(evento):
        pagina.remove(titulo)
        pagina.remove(botao_iniciar)
        janela.open = False
        pagina.add(chat)
        pagina.add(linha_mensagem)
        mensagem_entrar_no_chat = f"{campo_nome_usuario.value} entrou no chat"
        pagina.pubsub.send_all(mensagem_entrar_no_chat)
        pagina.update()

        # texto_entrar_chat = ft.Text(mensagem_entrar_no_chat)
        # chat.controls.append(texto_entrar_chat)

    botao_entrar_chat = ft.ElevatedButton("Entrar no chat", on_click=entrar_no_chat)
    janela = ft.AlertDialog(title=titulo_janela, content=campo_nome_usuario, actions=[botao_entrar_chat])

    def iniciar_chat(evento):
        pagina.dialog = janela
        janela.open = True
        pagina.update()

    botao_iniciar = ft.ElevatedButton("Iniciar chat", on_click=iniciar_chat)

    # add o elemento na pagina
    pagina.add(titulo)
    pagina.add(botao_iniciar)


# rodar o aplicativo
# ft.app(main)
ft.app(main, view=ft.WEB_BROWSER)

# para publicar ou tornar visivel (deploy), abrir a prorpia documentacao do flet
# ir na parte de "Publishing flet app"