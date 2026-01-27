# Definições de Personagens
define a = Character("Haruto", color="#3498db")
define c = Character("Cain", color="#e74c3c")
define f = Character("Funcionária", color="#95a5a6")
define cy = Character("Cain (Jovem)", color="#f1948a")
define cw = Character("Cain (Fraco)", color="#d98880")
define ca = Character("Cain (Adulto)", color="#c0392b")
define p = Character("Passageiro", color="#7f8c8d")

# Imagens de Fundo
image bg train_interior = "images/bg/train_interior.jpg"
image bg black = "images/bg/black.jpg"
image bg school_rain = "images/bg/school_rain.jpg"
image bg classroom = "images/bg/classroom.png"
image bg school_corridor = "images/bg/school_corridor.png"
image bg dream = "images/bg/dream.png"
image bg train_night = "images/bg/train_night.jpg"
image bg station_intervalla = "images/bg/station_intervalla.jpg"
image bg white_room = "images/bg/dream.png"
image bg memory_park = "images/bg/memory_park.png"
image bg memory_hospital = "images/bg/memory_hospital.png"
image bg memory_future = "images/bg/memory_future.png"
image bg library = "images/bg/library.png"

# Imagens de Personagens
image cain calm_smile = "images/cain/calm_smile.png"
image cain laugh = "images/cain/cain_laugh.png"
image cain blurred = "images/cain/cain_blurred.png"
image cain hand_out = "images/cain/cain_hand_out.png"
image cain young_sad = "images/cain/cain_young_sad.png"
image cain adult_happy = "images/cain/cain_adult_happy.png"
image cain weak = "images/cain/cain_weak.png"
image cain solid = "images/cain/cain_solid.png"
image ari young_distracted = "images/cain/ari_young_distracted.png"
image staff serious = "images/cain/staff_serious.png"
image cain maozinhas = "images/cain/cain_maozinhas.png"
image cain calm_smilee = "images/cain/calm_smilee.png"

# Variáveis de Estado
default solidez = 0
default dungeon_1_feita = False
default dungeon_2_feita = False
default dungeon_3_feita = False
default conversou_trem = False

# Início do Jogo
label start:

    stop music fadeout 2.0

    scene bg train_interior with fade
    play music "audio/train_ambience.mp3" loop
    
    "O som rítmico das rodas do trem contra os trilhos sempre foi o metrônomo da minha vida."
    "Mas hoje, o ritmo parece... fora de compasso."
    "As aulas recomeçam."
    "O ar dentro do vagão está pesado com o cheiro de café barato e o hálito de gente que ainda não acordou para o mundo."
    
    "Eu seguro meu livro de latim como se fosse um escudo."
    "{i}Grammatica Latina{/i}."
    "Palavras mortas para um mundo que insiste em seguir em frente."

    "Procuro um lugar vazio."
    "Não encontro."
    "Mas meus olhos travam em um ponto específico."

    "Lá está ele."

    show cain calm_smile at center with dissolve

    "Cain."
    "Meu melhor amigo."
    "Ou o que restou dele depois de um verão de silêncio absoluto."

    "Ele não parece o garoto que ignorou minhas mensagens por três meses."
    "Ele parece... em paz."
    "Uma paz que me incomoda."

    c "Haruto."
    c "Eu sabia que você estaria nesse vagão."
    c "Você é uma criatura de hábitos, não é?"

    menu:
        "Por que você sumiu?":
            $ conversou_trem = True
            $ haruto_magoado = True

            a "Hábitos?"
            a "Você fala de hábitos depois de desaparecer da face da terra?"
            a "Eu quase fui até a sua casa, Cain."
            a "Por um tempo, eu realmente achei que você tinha se cansado de mim."

            c "…"
            c "Eu nunca me cansaria de você."
            c "Mas às vezes o ruído do mundo fica alto demais."
            c "Alto a ponto de a gente não conseguir escutar nem a própria respiração."

            a "E o silêncio incluía me ignorar?"

            c "Incluía me preparar."
            c "Algumas conversas não podem acontecer pela tela de um celular."
            c "Elas precisam de… presença."

        "Você parece diferente.":
            $ haruto_observador = True

            a "Você está estranho, Cain."
            a "Onde está o sarcasmo?"
            a "A reclamação sobre o sono?"
            a "Você parece… mais leve."

            c "Eu deixei essas coisas no verão."
            c "Elas pesavam demais."

            a "Ser infeliz virou bagagem agora?"

            c "Virou excesso."
            c "Você não acha que a gente passa tempo demais sofrendo por hábito?"

            a "Eu acho que a gente passa tempo sendo humano."
            a "E humanos reclamam."

            c "Talvez."
            c "Mas hoje…"
            c "Hoje eu só quero observar."

    c "Olhe para essas pessoas, Haruto."
    c "Cada uma carregando um universo inteiro."
    c "E, ainda assim…"
    c "Todos temporários."

    "Ele enfia a mão no bolso do casaco."
    "Por um instante, acho que ele vai tirar o celular."
    "Mas não."

    "Ele estende a mão."
    "Um pequeno objeto repousa na palma."

    "Um marcador de página feito de papel grosso."
    "As bordas foram cortadas com cuidado."
    "Há algo de íntimo nisso."
    "Algo feito com tempo."

    "{i}“Memoria te servat.”{/i}"

    a "Cain…"
    a "Você sabe que isso está errado, né?"
    a "{i}Servat{/i} é preservar."
    a "Se você queria dizer que a memória me mantém, deveria ser {i}tenet{/i}."

    show cain laugh with dissolve

    c "Hahaha!"
    c "Eu sabia."
    c "Apostei comigo mesmo que você corrigiria a gramática antes de agradecer."

    a "Você me conhece demais."

    c "Ou talvez eu só tenha prestado atenção."

    c "Mas e se eu não estiver errado, Haruto?"
    c "E se a memória for a única coisa que realmente pode salvar alguém?"

    a "Salvar de quê?"

    show cain calm_smile with dissolve

    c "Do nada."
    c "Do vazio que fica quando a gente para de ocupar espaço no mundo."

    "O trem freia."
    "O impacto reverbera pelo vagão."
    "A estação dele."

    c "Eu preciso ir."

    a "Cain—"

    c "A gente se vê por aí, Haruto."
    c "Não esqueça de marcar a página."
    c "É importante saber onde você parou."

    hide cain with dissolve

    scene bg black with fade
    stop music fadeout 2.0

    "Eu não sabia."
    "Mas aquela foi a última vez que o vi respirar o mesmo ar que eu."

label dia_seguinte:
    show expression Movie(channel="movie_channel", play="images/bg/rain.webm", loop=True) at truecenter with fade
    play music "audio/sad_piano.mp3" loop

    "A chuva caía fina."
    "Daquelas que não chegam a lavar a rua."
    "Só deixam tudo frio."
    "Inacabado."

    hide expression Movie(channel="movie_channel") with fade

    scene bg school_rain with dissolve

    "A escola parecia um funeral antes mesmo do anúncio."
    "Passos ecoavam demais."
    "Portas fechavam baixo demais."
    "O silêncio nos corredores era denso."
    "Quase sólido."

    scene bg classroom with dissolve

    "Eu estava sentado na minha mesa."
    "Olhando para o lugar vazio ao meu lado."
    "O lugar de Cain."

    "Meu corpo ainda esperava que ele chegasse atrasado."
    "Que reclamasse da chuva."
    "Que fizesse algum comentário inútil só para quebrar o clima."

    "A porta da sala se abriu."
    play music "audio/door_creak.mp3"
    "O rangido ecoou."
    "Alto demais."
    "Como um grito em um quarto vazio."

    show staff serious at center

    f "Alunos..."
    f "Por favor, prestem atenção."

    "A voz dela tremia."
    "Ela não olhava para ninguém."
    "Seus olhos estavam fixos em um ponto qualquer da parede."
    "Como se encarar a gente tornasse aquilo real demais."

    f "Recebemos uma notícia muito triste esta manhã."

    "Meu estômago afundou."
    "Antes mesmo do nome."

    f "O aluno Cain..."
    f "Ele faleceu ontem à noite."
    f "Em sua casa."

    hide staff serious with dissolve

    "O mundo não parou."
    "Ele não explodiu."
    "Ele simplesmente… se quebrou."

    "Ouvi alguém soluçar."
    "Ouvi uma cadeira arrastar."
    "Uma caneta caiu no chão."

    "Mas para mim—"
    "Foi como vidro estilhaçando dentro dos meus ouvidos."

    a "(Não.)"
    a "(Não, não, não.)"

    a "(Ontem ele estava no trem.)"
    a "(Ele sorriu.)"
    a "(Ele me entregou o marcador.)"

    a "(Ele estava se despedindo.)"
    a "(Ele sabia.)"
    a "(Ele sabia e eu estava corrigindo o latim dele.)"

    menu:
        "…":
            $ culpa_haruto = True

            "Eu apertei o marcador dentro do bolso."
            "As bordas de papel machucaram meus dedos."
            "Não o suficiente."

            a "(Se eu tivesse perguntado mais.)"
            a "(Se eu tivesse ido atrás.)"
            a "(Se eu tivesse percebido.)"

        "Não pensar.":
            $ negacao_haruto = True

            "Eu encarei a lousa."
            "Os números escritos nela não faziam sentido."
            "Nada fazia."

            a "(Isso não está acontecendo.)"
            a "(Isso não pode estar acontecendo.)"

    show staff serious at center with dissolve

    "A funcionária continuava falando."
    "Palavras sobre luto."
    "Apoio psicológico."
    "Minuto de silêncio."

    hide staff serious with dissolve

    "Eu não ouvi nada."

    "O lugar ao meu lado permanecia vazio."
    "E, pela primeira vez…"
    "Eu entendi que sempre estaria."

    "A culpa é uma substância ácida."
    "Ela não grita."
    "Ela não sangra."

    "Ela corrói a memória."
    "Aos poucos."
    "Até que tudo o que sobra…"
    "É arrependimento."

    scene bg black with fade
    stop music fadeout 2.0

    jump rupturas_expandidas

label rupturas_expandidas:
    show expression Movie(channel="movie_channel1", play="images/bg/rainn2.webm", loop=True) at truecenter with fade

    "Os dias que se seguiram foram um borrão de cinza."
    "Não havia manhã."
    "Não havia noite."
    "Só intervalos."

    "Eu via o rosto dele em cada sombra."
    "Não como um fantasma."
    "Como um erro."
    "Algo que o mundo esqueceu de apagar."

    hide expression Movie(channel="movie_channel1")
    scene bg library with dissolve

    "Na biblioteca, eu jurava ouvir a risada dele entre as estantes de história."
    play music "audio/laugh.mp3"
    "Baixa."
    "Cúmplice."
    "A mesma risada que surgia quando eu errava uma tradução óbvia."

    "Eu virei a cabeça."
    "As estantes estavam imóveis."
    "Antigas."
    "Indiferentes."

    "Mas o som ficou."
    "Por tempo demais."

    "Eu engoli em seco."

    "Eu estava ficando louco?"
    "Ou o mundo estava se recusando a aceitar que ele tinha ido?"

    scene bg dream with dissolve

    "O primeiro sonho veio sem aviso."
    "Sem lógica."
    "Sem cor."

    "Não era escuro."
    "Era… desbotado."
    "Como uma fotografia esquecida ao sol."

    "Eu estava em um lugar sem chão."
    "Sem céu."
    "Sem direção."

    "E Cain estava lá."

    "Não como uma lembrança."
    "Mas como presença."

    show cain hand_out at center:
        alpha 0.8

    "Ele parecia incompleto."
    "Levemente desfocado."
    "Como se não tivesse sido totalmente renderizado."

    c "Não demora, Haruto."

    "A voz dele não ecoava."
    "Ela surgia dentro da minha cabeça."

    c "O intervalo é curto."
    c "E o esquecimento é rápido."

    "Meu corpo queria correr."
    "Mas não havia para onde."

    c "Se você não vier agora…"

    "Ele deu um passo à frente."
    "O mundo ao redor dele tremeu."
    "Como um arquivo corrompido sendo aberto."

    c "…não sobrará nada de mim."
    c "Nada que você possa salvar."

    menu:
        "Estender a mão.":
            $ travessia_aceita = True

            "Meu braço se moveu antes do pensamento."
            "Antes do medo."
            "Antes da razão."

            "Quando nossos dedos quase se tocaram—"
            "O mundo perdeu o peso."

        "Ficar parado.":
            $ travessia_hesitacao = True

            "Eu congelei."
            "O chão parecia distante demais."
            "Meu corpo pesado demais."

            "O rosto de Cain escureceu por um instante."
            "Não de raiva."
            "De urgência."

    c "Por favor."

    "A palavra foi fraca."
    "Humana."
    "Errada demais para um sonho."

    "Acordei com o coração disparado."
    "Com o nome dele preso na garganta."
    "E a sensação terrível de que…"

    "Eu tinha acabado de perder algo."
    "De novo."

    jump a_travessia_detalhada

label a_travessia_detalhada:
    scene bg train_night with fade
    play music "audio/train_ambience.mp3" loop

    "Uma semana depois."
    "O mesmo trem."
    "O mesmo horário."

    "Era para ser reconfortante."
    "Não foi."

    "Eu abri o livro de latim."
    "O marcador ainda estava lá."
    "Página 112."
    "Onde eu parei no dia em que ele morreu."

    "Eu não lembrava de ter fechado o livro depois disso."

    "Minhas mãos tremiam levemente."
    "Não de frio."
    "De antecipação."

    "As palavras na página pareciam… inquietas."
    "Elas não ficavam no lugar."

    "{i}“Inter vivos et mortuos.”{/i}"

    "Entre os vivos e os mortos."

    "Eu não lembrava dessa frase estar ali."

    "O trem entrou no túnel."

    "A escuridão engoliu as janelas—"
    "Mas desta vez…"
    "Ela não passou."

    "As luzes do vagão começaram a piscar."
    "Não como uma falha elétrica."
    "Como um aviso."

    "O som constante do motor se quebrou."
    "Primeiro em estática."
    "Depois em nada."

    stop music

    "O silêncio foi tão absoluto que meus ouvidos doeram."
    "Vácuo puro."

    play music "audio/train_brake_screech.mp3"
    "O trem parou com um solavanco violento."
    "Meu corpo foi lançado para frente."
    play music "audio/impact.mp3"
    "O livro caiu no chão—"
    "Mas não fez barulho."

    scene bg black with fade

    "Quando abri os olhos…"

    "O vagão estava vazio."

    "Não havia passageiros."
    "Não havia anúncios."
    "Não havia reflexos."

    "As janelas mostravam apenas um brilho frio."
    "Azulado."
    "Imóvel."

    "Como se o mundo tivesse parado do outro lado do vidro."

    scene bg station_intervalla with fade
    play music "audio/ambient_mystery.mp3" loop

    "Eu desci do trem."

    "Meus pés tocaram a plataforma—"
    "E não houve som."

    "Nem eco."
    "Nem atrito."
    "Nada."

    "O ar não tinha cheiro."
    "Nem temperatura."
    "Ele apenas… existia."

    "O letreiro da estação estava acima de mim."

    "{b}INTERVALLA{/b}"

    "Eu senti um aperto no peito."
    "Não medo."
    "Reconhecimento."

    "Vi pessoas sentadas nos bancos."
    "Silhuetas humanas."
    "Feitas de fumaça e lembrança."

    "Algumas tinham rostos."
    "Outras… não."

    "Seus olhos eram buracos vazios."
    "Fixos em um horizonte que não existia."
    "Esperando algo que nunca chegava."

    "E então eu o vi."

    "No final da plataforma."
    "Sentado sozinho."

    show cain blurred at center with dissolve:
        alpha 0.6

    "Cain."

    "Ele parecia… incompleto."
    "Como se alguém tivesse abaixado a opacidade do mundo só para ele."

    a "Cain?"

    "A palavra saiu fraca."
    "Como se o lugar não gostasse de nomes."

    c "Você demorou, Haruto."
    c "Eu já estava começando a perder a cor das minhas próprias mãos."

    show cain maozinhas at center with dissolve:
        alpha 0.6

    "Ele levantou as palmas."
    "Elas tremulavam."
    "Quase transparentes."

    hide cain maozinhas with dissolve
    show cain blurred at center with dissolve:
        alpha 0.6

    a "O que é este lugar?"
    a "Eu morri também?"

    hide cain blurred with dissolve
    show cain calm_smile at center with dissolve:
        alpha 0.6

    "Cain sorriu."
    "Mas não havia humor ali."

    hide cain calm_smile with dissolve
    show cain blurred at center with dissolve:
        alpha 0.6
    
    c "Não."
    c "Você é um visitante."

    c "Eu sou um residente…"
    c "Por enquanto."

    "Essa última parte ficou suspensa no ar."
    "Como uma ameaça educada."

    hide cain blurred with dissolve
    show cain calm_smilee at center with dissolve:
        alpha 0.6

    c "Este é o Intervalla."
    c "O lugar onde as pessoas ficam quando o mundo começa a esquecê-las…"
    c "…mas elas ainda se recusam a soltar a vida."

    hide cain calm_smilee with dissolve

    "Uma das figuras nos bancos virou lentamente a cabeça."
    "Ela não tinha boca."
    "Mas parecia ouvir."

    show cain blurred at center with dissolve:
        alpha 0.6

    c "Cada vez que alguém para de falar de mim…"
    c "Eu fico mais transparente."

    c "Cada vez que uma foto minha é guardada em uma gaveta…"
    c "Eu perco um pedaço da minha voz."

    "Eu senti algo se fechar dentro do meu peito."

    a "Eu nunca vou te esquecer!"
    a "Eu estou aqui, não estou?"

    "Cain se levantou."
    "Quando seus pés tocaram o chão"

    c "Estar aqui não é o suficiente."

    "Ele deu um passo em minha direção."
    "O mundo pareceu se distorcer levemente."

    c "Você precisa enfrentar o que nos trouxe até aqui."
    c "As memórias que você trancou porque doíam demais."

    "Imagens passaram pela minha mente."
    "Mensagens não respondidas."
    "Silêncios ignorados."
    "Coisas que eu decidi não perguntar."

    c "Se você quer me manter real…"
    c "Precisa aceitar a realidade de quem fomos."

    c "Sem filtros."
    c "Sem desculpas."

    "O trem atrás de mim soltou um rangido baixo."
    "Como se estivesse pronto para partir."
    "Ou desaparecer."

    jump dungeons_memoria

label dungeons_memoria:
    scene bg station_intervalla with dissolve
    show cain calm_smilee at center with dissolve:
        alpha 0.6
        
    "O ar na estação é gelado. Cain aponta para três portais que se abriram na névoa."
    
    menu:
        "Entrar na Sala das Palavras Não Ditas (O Parque)" if not dungeon_1_feita:
            jump dungeon_palavras
        "Entrar no Túnel do Medo de Ser Esquecido (O Hospital)" if not dungeon_2_feita:
            jump dungeon_medo
        "Entrar no Corredor das Coisas Que Poderiam Ter Sido (A Itália)" if not dungeon_3_feita:
            jump dungeon_saudade

label dungeon_palavras:
    scene bg memory_park with dissolve

    "O cenário se reconstrói como uma lembrança mal acordada."
    "As cores surgem aos poucos, lavadas demais, como uma fotografia esquecida no sol."

    "O cheiro de grama recém-cortada invade meus sentidos."
    "Quente."
    "Doce."
    "Um verão que ainda não sabia que ia acabar."

    "Por um instante, eu esqueço tudo."
    "O trem."
    "O Intervalla."
    "O silêncio azul."

    "Lá estamos nós."
    "Anos atrás."

    "Eu estou sentado em um banco de madeira."
    "Cercado de livros abertos, anotações rabiscadas, planos empilhados."
    "Meu futuro inteiro organizado em páginas numeradas."

    "Cain está ao meu lado."
    "Balançando o pé na terra."
    "Arrancando pequenos pedaços de grama sem perceber."
    "Como se estivesse tentando se certificar de que o mundo ainda era real."

    show cain young_sad at left
    show ari young_distracted at right

    cy "Haruto…"
    cy "Você já parou pra pensar que talvez a gente esteja correndo rápido demais?"

    "Eu lembro de ter suspirado."
    "Não agora."
    "Naquele dia."

    cy "Todo mundo fala de futuro como se ele fosse garantido."
    cy "Como se fosse uma linha reta, sem falhas."

    cy "Mas e se não for?"

    "O vento passa entre as árvores."
    "As folhas fazem um som baixo."
    "Quase um aviso."

    "Eu me lembro do incômodo que senti."
    "Não pelas palavras dele."
    "Mas porque elas bagunçavam algo que eu acreditava controlar."

    cy "Às vezes eu sinto que você já decidiu tudo."
    cy "Que já escolheu quem vai ser."
    cy "Pra onde vai."
    cy "O que vale a pena."

    cy "E eu…"
    cy "Eu só tô aqui acompanhando."

    "Ele ri de leve."
    "Mas o riso não alcança os olhos."

    cy "Como se a minha função fosse não atrapalhar."

    a "(Eu devia ter fechado o livro.)"
    a "(Devia ter olhado pra ele.)"
    a "(Devia ter perguntado por quê.)"

    a "(Mas eu não fiz.)"

    menu:
        "Você está sendo dramático, Cain.":

            "A lembrança aperta."
            "A cena avança, obediente ao que eu escolhi naquela época."

            a "Eu lembro exatamente do tom da minha voz."
            a "Impaciente."
            a "Cansado."
            a "Convencido demais pra perceber."

            a "Cain, você pensa demais."
            a "A vida não é um poema trágico."

            a "Se você gastasse metade dessa energia estudando…"
            a "Não estaria tão perdido."

            "As palavras caem como pedras."

            cy "Perdido…"

            "Ele repete a palavra devagar."
            "Como se estivesse testando o peso dela."

            cy "Engraçado você dizer isso."

            cy "Porque naquele momento…"
            cy "Eu achei que você era o único que sabia exatamente pra onde estava indo."

            "Cain abaixa a cabeça."
            "A sombra dele se alonga no chão."
            "Estica demais."
            "Como se estivesse tentando fugir do corpo."

            cy "Eu não queria respostas, Haruto."
            cy "Eu não precisava de um plano."

            cy "Eu só queria que você me escutasse."

            "A saturação do mundo começa a cair."
            "O verde vira cinza."
            "O céu perde profundidade."

            "O som do parque desaparece."
            "Fica apenas o silêncio que eu deixei naquele dia."

            "Nada se fortalece."
            "Nada se reconstrói."

            "Agora eu entendo."
            "Não foi crueldade."

            "Foi indiferença."

        "Eu sinto muito por não ter te visto.":

            "A memória hesita."
            "Como se não tivesse certeza de que pode mudar."

            a "Eu fecho o livro."
            "Devagar."
            "Com cuidado demais."

            a "Como se esse gesto pudesse atravessar o tempo."
            a "Como se pudesse alcançar você."

            a "Eu estava tão ocupado tentando ser alguém…"
            a "Que não percebi que estava deixando você sozinho bem do meu lado."

            "Cain para de arrancar a grama."
            "O pé deixa de balançar."

            a "Você não era figurante, Cain."
            a "Eu é que transformei você em pano de fundo."

            cy "Você sabe o que mais doeu?"

            cy "Não foi você discordar."
            cy "Nem me chamar de dramático."

            cy "Foi você nem perceber…"
            cy "Que eu estava pedindo ajuda."

            "A palavra fica suspensa."
            "Ajuda."

            a "Eu sinto muito."
            a "De verdade."

            "Cain respira fundo."
            "O ar entra pesado."
            "Sai tremido."

            "Quando ele levanta o rosto…"
            "Ainda há dor."

            "Mas há algo novo."
            "Alívio."

            cy "Obrigado…"
            cy "Por finalmente olhar pra mim."

            "Uma luz suave envolve o corpo dele."
            "Não é brilho."
            "É presença."

            "As cores do parque voltam lentamente."
            "O vento fica mais quente."
            "O mundo parece… um pouco mais sólido."

            $ solidez += 1

    $ dungeon_1_feita = True

    "O parque começa a se desfazer."
    "Não em ruína."
    "Em papel."

    "As árvores viram páginas em branco."
    "O céu se dobra como uma folha antiga."

    "O vento espalha palavras não ditas."
    "Elas giram no ar como pétalas."
    "Como desculpas que chegaram tarde…"
    "Mas chegaram."

    jump check_dungeons

label dungeon_medo:
    scene bg memory_hospital with dissolve
    "O cheiro vem antes da imagem."
    "Álcool. Produtos de limpeza. Morte tentando ser escondida."

    "O som dos bipes é lento. Regular. Cruel."
    "Cada apito é um lembrete de que o tempo está ganhando."

    show cain weak at center

    cw "Você demorou."
    cw "Eu fiquei imaginando se você viria."

    a "(Ele parece menor.)"
    a "(Como se o mundo estivesse encolhendo ao redor dele.)"

    cw "Eu vi minha mãe chorando no corredor."
    cw "Ela tentou sorrir quando entrou."
    cw "Foi pior do que se ela tivesse chorado."

    cw "Ela vai sobreviver."
    cw "As pessoas sempre sobrevivem."

    cw "Mas e você, Haruto?"
    cw "Você vai me transformar em uma história bonita?"
    cw "Ou vai lembrar de mim como eu realmente fui?"

    menu:
        "Você foi perfeito para mim.":
            a "Eu me aproximo da cama."
            a "Seguro a mão dele com força demais."

            a "Você foi tudo de bom que eu tive."
            a "Você foi luz."
            a "Eu vou garantir que ninguém esqueça isso."

            cw "Isso soa… confortável."
            cw "Mas não é verdade."

            cw "Eu menti."
            cw "Eu tive medo."
            cw "Eu me afastei quando mais precisava de você."

            cw "Se você me transformar em um santo…"
            cw "Você não vai estar me lembrando."
            cw "Vai estar se protegendo."

            "O monitor cardíaco apita mais alto."
            "O quarto parece mais distante."

        "Eu estou com raiva de você por ter escondido isso.":
            a "Minha voz treme."
            a "Não de tristeza."
            a "De raiva acumulada."

            a "Você não confiou em mim!"
            a "Você decidiu sozinho!"
            a "E agora eu tenho que lidar com tudo isso sem nem ter tido escolha!"

            cw "Isso…"
            cw "Isso é real."

            cw "Eu fui egoísta."
            cw "Eu tive medo de ser fraco aos seus olhos."

            cw "Não me perdoa agora."
            cw "Mas não me apaga."

            "Os dedos dele apertam os meus."
            "Fraco — mas presente."

            $ solidez += 1

    $ dungeon_2_feita = True
    "O som do monitor se dissolve."
    "O quarto perde as paredes."
    "Resta apenas o eco."

    jump check_dungeons

label dungeon_saudade:
    scene bg memory_future with dissolve
    "O sol é quente."
    "O céu é absurdamente azul."
    "Tudo é bonito demais para ser real."

    show cain adult_happy at center

    ca "Olha isso, Haruto!"
    ca "A gente conseguiu."
    ca "Sem hospitais. Sem despedidas."

    ca "Aqui ninguém morre."
    ca "Aqui ninguém esquece."

    ca "Fica."
    ca "Só dessa vez."

    "Meu peito aperta."
    "Porque por um segundo…"
    "Eu quase acredito."

    menu:
        "Sim, eu fico. Eu não aguento mais a realidade.":
            a "Eu estou cansado."
            a "Cansado de enterros."
            a "Cansado de memórias que doem."

            a "Se isso for mentira…"
            a "Então deixa eu viver nela."

            ca "Você sempre escolheu o caminho mais difícil."
            ca "Mas dessa vez… escolheu fugir."

            ca "Se você ficar…"
            ca "Eu desapareço de verdade."

            "O sorvete derrete."
            "Vira algo escuro."
            "O céu racha."

        "Isso não é Roma. É um necrotério pintado de dourado.":
            a "Minha voz falha."
            a "Mas não recua."

            a "Isso não é vida."
            a "É uma vitrine."

            a "Você merece ser lembrado como foi."
            a "Não como eu gostaria que tivesse sido."

            ca "Então dói assim mesmo…"
            ca "Ser amado do jeito certo."

            "Ele sorri."
            "Sem máscaras."
            "Sem ilusões."

            $ solidez += 1

    $ dungeon_3_feita = True
    "Roma se desfaz."
    "Sobra apenas o vazio honesto do Intervalla."

    jump check_dungeons

label check_dungeons:
    if dungeon_1_feita and dungeon_2_feita and dungeon_3_feita:
        jump coracao_intervalo
    else:
        scene bg station_intervalla with fade
        "Volto para a plataforma central. O ar parece um pouco menos denso, mas o peso no meu coração continua o mesmo."
        "Cain está me esperando, sentado no mesmo banco."
        jump dungeons_memoria

label coracao_intervalo:
    scene bg white_room with fade
    play music "audio/final_theme.mp3"
    
    "A estação Intervalla começa a tremer. As paredes de névoa estão se dissipando, revelando um vazio branco infinito."
    "Cain se levanta. Ele não está mais desfocado. Ele parece... ele mesmo."
    
    if solidez >= 2:
        jump final_bom
    else:
        jump final_ruim

label final_bom:
    show cain solid at center with dissolve
    c "Haruto. Você conseguiu. Você atravessou o lodo das nossas falhas e não soltou a minha mão."
    a "Eu entendi agora, Cain. O marcador... {i}Memoria te servat{/i}. A memória me salva porque ela me obriga a ser honesto."
    a "Eu não vou te esquecer. Mas eu também não vou ficar preso no que poderia ter sido."

    c "Obrigado. Por me deixar ser humano uma última vez."
    c "Agora, volte para o trem. Há uma vida inteira esperando por você."

    "Ele me abraça. O toque é quente, real."

    scene bg train_interior with fade
    "Memoria te servat."

    play music "audio/credits_theme.mp3" fadein 2.0
    call screen rolling_credits

    return

label final_ruim:
    "O mundo ao redor se torna estático. O tempo para."
    "Cain me olha com uma tristeza infinita."
    c "Haruto... você não deveria ter escolhido isso."
    "Mas agora, somos apenas dois vultos sentados num banco, esperando o esquecimento chegar."

    play music "audio/credits_theme.mp3" fadein 2.0
    call screen rolling_credits

    return

transform credits_scroll:
    xalign 0.5
    ypos 1200
    linear 150 ypos -4200

screen rolling_credits():

    tag credits

    add Solid("#000")

    vbox:
        xalign 0.5
        spacing 50
        at credits_scroll

        text "CRÉDITOS" size 80 xalign 0.5

        null height 120

        text "Roteiro & Direção" size 50 xalign 0.5

        vbox:
            xalign 0.5
            spacing 8
        
            text "Gabriel Mendes" size 40 xalign 0.5
            text "github.com/GabrielMendes2009" size 30 xalign 0.5 color "#aaaaaa"
        
            null height 10

            text "Manuel Miranda" size 40 xalign 0.5
            text "github.com/manuelm11-bit" size 30 xalign 0.5 color "#aaaaaa"

        null height 100

        text "Arte" size 50 xalign 0.5
        vbox:
            xalign 0.5
            spacing 8

            text "Milkology8" size 40 xalign 0.5
            text "@g.ngyu" size 30 xalign 0.5 color "#aaaaaa"

            null height 10

            text "Brett Carlsen" size 40 xalign 0.5
            text "bcarlsen.artstation.com" size 30 xalign 0.5 color "#aaaaaa"

            null height 10

            text "Craiyon" size 40 xalign 0.5
            text "www.craiyon.com" size 30 xalign 0.5 color "#aaaaaa"

            null height 10

            text "Makoto Shinkai" size 40 xalign 0.5
            text "@makoto.shinkai" size 30 xalign 0.5 color "#aaaaaa"

            null height 10
            
            text "Foxeleos" size 40 xalign 0.5
            text "deviantart.com/foxeleos" size 30 xalign 0.5 color "#aaaaaa"
        
            null height 10

            text "Hachio" size 40 xalign 0.5
            text "@hachio81" size 30 xalign 0.5 color "#aaaaaa"

            null height 10

            text "goliatgashi" size 40 xalign 0.5
            text "deviantart.com/goliatgashi/" size 30 xalign 0.5 color "#aaaaaa"

            null height 10

            text "Nano Banana" size 40 xalign 0.5

            null height 10

            text "Pixabay" size 40 xalign 0.5

        null height 100

        text "Música & Áudio" size 50 xalign 0.5
        vbox:
            xalign 0.5
            spacing 8
        
            text "DELOSound" size 40 xalign 0.5
            text "pixabay.com/users/delosound-46524562" size 30 xalign 0.5 color "#aaaaaa"
        
            null height 10

            text "Cracious" size 40 xalign 0.5
            text "pixabay.com/users/cracious-49787968" size 30 xalign 0.5 color "#aaaaaa"
        
            null height 10

            text "Universfield" size 40 xalign 0.5
            text "pixabay.com/users/universfield-28281460" size 30 xalign 0.5 color "#aaaaaa"

            null height 10

            text "freesound_community" size 40 xalign 0.5
            text "pixabay.com/users/freesound_community-46691455" size 30 xalign 0.5 color "#aaaaaa"
        
            null height 10

            text "Kenji Kawai" size 40 xalign 0.5
            
            null height 10

            text "Lorien Testard" size 40 xalign 0.5
            text "@lorien_testard" size 30 xalign 0.5 color "#aaaaaa"

        null height 100

        text "Programação" size 50 xalign 0.5
        vbox:
            xalign 0.5
            spacing 8
            text "Gabriel Mendes" size 40 xalign 0.5
            text "github.com/GabrielMendes2009" size 30 xalign 0.5 color "#aaaaaa"

        null height 100

        text "Engine" size 50 xalign 0.5
        vbox:
            xalign 0.5
            spacing 8
            text "Ren'Py" size 40 xalign 0.5
            text "renpy.org" size 30 xalign 0.5 color "#aaaaaa"

        null height 140

        text "Obrigado por jogar" size 60 xalign 0.5

        null height 80

        vbox:
            xalign 0.5
            spacing 5
            text "Enquanto alguém se lembra…" size 36 xalign 0.5 color "#aaaaaa"
            text "ninguém desaparece de verdade." size 36 xalign 0.5 color "#aaaaaa"

        null height 200

        add "images/bg/ending_image.png":
            xalign 0.5
            alpha 0.95

        null height 600

    timer 130 action Stop("music", fadeout=7.0)
    timer 160 action Quit(confirm=False)
