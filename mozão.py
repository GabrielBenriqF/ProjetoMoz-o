import tkinter as Tk
import random
import math

def calcular_distancia(x1, y1, x2, y2):
    """Calcula a distância euclidiana entre dois pontos"""
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def verificar_proximidade_mouse(event):
    """Verifica se o mouse está próximo do botão NÃO e move se necessário"""
    try:
        mouse_x = event.x_root
        mouse_y = event.y_root
        
        botao_x = janela.winfo_rootx() + botao_nao.winfo_x()
        botao_y = janela.winfo_rooty() + botao_nao.winfo_y()
        botao_width = botao_nao.winfo_width()
        botao_height = botao_nao.winfo_height()
        
        centro_botao_x = botao_x + botao_width // 2
        centro_botao_y = botao_y + botao_height // 2

        distancia = calcular_distancia(mouse_x, mouse_y, centro_botao_x, centro_botao_y)

        zona_deteccao = 80  
        
        if distancia < zona_deteccao:
            mover_botao_nao()
            
            janela.after(200, lambda: None)
            
    except Exception as e:
        pass

def mover_botao_nao():
    """Move o botão NÃO para uma posição aleatória, evitando sobreposições"""
    janela.update_idletasks()
    largura_janela = janela.winfo_width()
    altura_janela = janela.winfo_height()
    
    largura_botao = botao_nao.winfo_width()
    altura_botao = botao_nao.winfo_height()
    
    try:
        pergunta_x = pergunta.winfo_x()
        pergunta_y = pergunta.winfo_y()
        pergunta_width = pergunta.winfo_width()
        pergunta_height = pergunta.winfo_height()
        
        area_proibida_x1 = pergunta_x - 30
        area_proibida_x2 = pergunta_x + pergunta_width + 30
        area_proibida_y1 = pergunta_y - 30
        area_proibida_y2 = pergunta_y + pergunta_height + 30
    except:
        area_proibida_x1 = largura_janela // 4
        area_proibida_x2 = 3 * largura_janela // 4
        area_proibida_y1 = altura_janela // 6
        area_proibida_y2 = altura_janela // 3
    
    try:
        sim_x = frame_botoes.winfo_x() + botao_sim.winfo_x()
        sim_y = frame_botoes.winfo_y() + botao_sim.winfo_y()
        sim_width = botao_sim.winfo_width()
        sim_height = botao_sim.winfo_height()
        
        area_sim_x1 = sim_x - 20
        area_sim_x2 = sim_x + sim_width + 20
        area_sim_y1 = sim_y - 20
        area_sim_y2 = sim_y + sim_height + 20
    except:
        area_sim_x1 = area_sim_x2 = area_sim_y1 = area_sim_y2 = 0
    
    x_min = 10
    x_max = largura_janela - largura_botao - 10
    y_min = 10
    y_max = altura_janela - altura_botao - 10
    
    for tentativa in range(100):
        x = random.randint(x_min, max(x_min, x_max))
        y = random.randint(y_min, max(y_min, y_max))
        
        colide_texto = (area_proibida_x1 <= x <= area_proibida_x2 and 
                       area_proibida_y1 <= y <= area_proibida_y2)
        
        colide_sim = (area_sim_x1 <= x <= area_sim_x2 and 
                     area_sim_y1 <= y <= area_sim_y2)
        
        if not colide_texto and not colide_sim:
            break
    
    botao_nao.place(x=x, y=y)
    
    textos_fuga = [
        "NÃO\n😰", "NAM\n🏃‍♂️", "NEVER\n😱", 
        "NO\n🙈", "SAI!\n😵", "NEM\n😭"
    ]
    novo_texto = random.choice(textos_fuga)
    botao_nao.configure(text=novo_texto)

def clicar_sim():
    """Exibe a tela de declaração de amor"""
    for widget in janela.winfo_children():
        widget.destroy()
    
    janela.configure(bg="#FF69B4")
    
    frame_principal = tk.Frame(janela, bg="#FF69B4")
    frame_principal.pack(expand=True, fill="both")
    
    largura = janela.winfo_width()
    altura = janela.winfo_height()
    
    tamanho_fonte = max(24, min(48, largura // 20))
    
    mensagem = tk.Label(
        frame_principal, 
        text="TE AMO ❤️", 
        font=("Comic Sans MS", tamanho_fonte, "bold"), 
        fg="white",
        bg="#FF69B4"
    )
    mensagem.pack(expand=True, pady=(50, 20))

    try:
        coracao_img = tk.PhotoImage(file="coracao.png")
        imagem_label = tk.Label(frame_principal, image=coracao_img, bg="#FF69B4")
        imagem_label.image = coracao_img
        imagem_label.pack(expand=True)
    except Exception as e:
        tamanho_emoji = max(32, min(72, largura // 25))
        emoji_coracao = tk.Label(
            frame_principal,
            text="💖💕💖💗💕💖",
            font=("Arial", tamanho_emoji),
            fg="white",
            bg="#FF69B4"
        )
        emoji_coracao.pack(expand=True, pady=10)
        
        tamanho_aviso = max(10, min(18, largura // 40))
        aviso = tk.Label(
            frame_principal, 
            text="Quiser namorar comigo agora, só escolher,\nse não quiser tudo bem mas pra frente eu peço denovo <3", 
            font=("Comic Sans MS", tamanho_aviso),
            fg="white",
            bg="#FF69B4",
            justify="center"
        )
        aviso.pack(expand=True, pady=(10, 50))

def ajustar_tamanho_botoes():
    try:
        largura = janela.winfo_width()
        altura = janela.winfo_height()
        
        if largura < 800:
            # Janela pequena
            width_botao = 6
            height_botao = 2
            fonte_botao = 12
            fonte_pergunta = 20
        elif largura < 1200:
            # Janela média
            width_botao = 7
            height_botao = 3
            fonte_botao = 14
            fonte_pergunta = 24
        else:
            # Janela grande/tela cheia
            width_botao = 10
            height_botao = 4
            fonte_botao = 18
            fonte_pergunta = 32
        
        botao_sim.configure(
            width=width_botao,
            height=height_botao,
            font=("Comic Sans MS", fonte_botao, "bold")
        )
        
        botao_nao.configure(
            width=width_botao,
            height=height_botao,
            font=("Comic Sans MS", fonte_botao, "bold")
        )
        
        pergunta.configure(font=("Comic Sans MS", fonte_pergunta, "bold"))
        
    except Exception as e:
        pass
#PARTE JADSON A BAIXO 
def on_enter_nao(event):
    """Quando o mouse entra na área do botão NÃO"""
    botao_nao.configure(bg="#DC143C", fg="white")
    # Mover imediatamente quando o mouse entra na área do botão
    mover_botao_nao()

def on_leave_nao(event):
    """Quando o mouse sai da área do botão NÃO"""
    botao_nao.configure(bg="#E70F2F", fg="white")

def on_enter_sim(event):
    """Quando o mouse entra na área do botão SIM"""
    botao_sim.configure(bg="#1E8B1E", fg="white")

def on_leave_sim(event):
    """Quando o mouse sai da área do botão SIM"""
    botao_sim.configure(bg="#26C226", fg="white")
    
janela = Tk.Tk()
janela.title("💕 Para Minha Namorada 💕")
janela.geometry("600x500")
janela.configure(bg="#FFB6C1") 
janela.resizable(True, True) 

def toggle_fullscreen(event=None):
    janela.attributes('-fullscreen', not janela.attributes('-fullscreen'))
    janela.after(100, ajustar_tamanho_botoes)

def exit_fullscreen(event=None):
    janela.attributes('-fullscreen', False)
    janela.after(100, ajustar_tamanho_botoes)


janela.bind('<F11>', toggle_fullscreen)
janela.bind('<Escape>', exit_fullscreen)


janela.bind('<Motion>', verificar_proximidade_mouse)


frame_principal = tk.Frame(janela, bg="#FFB6C1")
frame_principal.pack(expand=True, fill="both", padx=20, pady=20)


pergunta = tk.Label(
    frame_principal, 
    text="VOCÊ ME AMA?", 
    font=("Comic Sans MS", 24, "bold"),
    fg="#FA8BC2", 
)
pergunta.pack(pady=(40, 60), expand=True)


frame_botoes = tk.Frame(frame_principal, bg="#FFB6C1")
frame_botoes.pack(expand=True)


botao_sim = tk.Button(
    frame_botoes, 
    text="SIM\n💕", 
    font=("Comic Sans MS", 14, "bold"),
    bg="#26C226",
    fg="white",
    command=clicar_sim,
    cursor="hand2",
    relief="solid",
    bd=3,
    width=7,
    height=3,
    highlightthickness=0,
    borderwidth=2
)
botao_sim.pack(side="left", padx=50, expand=True)


botao_nao = tk.Button(
    janela, 
    text="NÃO\n😢", 
    font=("Comic Sans MS", 14, "bold"),
    bg="#E70F2F",
    fg="white",
    command=mover_botao_nao, 
    cursor="hand2",
    relief="solid",
    bd=3,
    width=7,
    height=3,
    highlightthickness=0,
    borderwidth=2
)


janela.update_idletasks()
botao_nao.place(x=400, y=300)


botao_sim.bind("<Enter>", on_enter_sim)
botao_sim.bind("<Leave>", on_leave_sim)
botao_nao.bind("<Enter>", on_enter_nao) 
botao_nao.bind("<Leave>", on_leave_nao)


def on_configure(event):
    if event.widget == janela:
       
        ajustar_tamanho_botoes()
        
     
        largura = janela.winfo_width()
        altura = janela.winfo_height()
        
        try:
            x_atual = botao_nao.winfo_x()
            y_atual = botao_nao.winfo_y()
            
          
            if x_atual > largura - 120 or y_atual > altura - 80 or x_atual < 0 or y_atual < 0:
               
                novo_x = min(max(50, largura - 200), largura // 2)
                novo_y = min(max(50, altura - 150), altura // 2)
                botao_nao.place(x=novo_x, y=novo_y)
        except:
            pass

janela.bind("<Configure>", on_configure)

def configuracao_inicial():
    try:
        ajustar_tamanho_botoes()
        botao_sim.configure(relief="solid", bd=3)
        botao_nao.configure(relief="solid", bd=3)
    except:
        pass


janela.after(200, configuracao_inicial)


janela.after(1000, lambda: janela.title("💕 Para Minha Namorada 💕 (F11 = Tela Cheia)"))


janela.mainloop()

