# Definições de Personagens
define a = Character("Ari", color="#3498db")
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
image bg school_corridor = "images/bg/school_corridor.jpg"
image bg dream = "images/bg/dream.png"
image bg train_night = "images/bg/train_night.jpg"
image bg station_intervalla = "images/bg/station_intervalla.jpg"
image bg white_room = "images/bg/dream.png"
image bg memory_park = "images/bg/memory_park.png"
image bg memory_hospital = "images/bg/memory_hospital.png"
image bg memory_future = "images/bg/memory_future.png"

# Imagens de Personagens
image cain calm_smile = "images/cain/calm_smile.png"
image cain laugh = "images/cain/cain_laugh.png"
image cain blurred = "images/cain/cain_blurred.png"
image cain hand_out = "images/cain/cain_hand_out.png"
image cain young_sad = "images/cain/cain_young_sad.png"
image cain adult_happy = "images/cain/cain_adult_happy.png"
image cain weak = "images/cain/cain_weak.png"
image cain solid = "images/cain/cain_solid.png"
image ari young_distracted = "images/ari/ari_young_distracted.png"
image staff serious = "images/cain/staff_serious.png"

# Variáveis de Estado
default solidez = 0
default dungeon_1_feita = False
default dungeon_2_feita = False
default dungeon_3_feita = False
default conversou_trem = False

# Início do Jogo
label start:
    scene bg train_interior with fade
    play music "audio/train_ambience.mp3" loop
    
    "O som rítmico das rodas do trem contra os trilhos sempre foi o metrônomo da minha vida. Mas hoje, o ritmo parece... fora de compasso."
    "As aulas recomeçam. O ar dentro do vagão está pesado com o cheiro de café barato e o hálito de gente que ainda não acordou para o mundo."
    "Eu seguro meu livro de latim como se fosse um escudo. {i}Grammatica Latina{/i}. Palavras mortas para um mundo que insiste em seguir em frente."
    
    "Procuro um lugar vazio, mas meus olhos travam em um ponto específico."
    "Lá está ele."
    
    show cain calm_smile at center with dissolve
    
    "Cain. Meu melhor amigo. Ou o que restou dele depois de um verão de silêncio absoluto."
    "Ele não parece o garoto que ignorou minhas mensagens por três meses. Ele parece... em paz. Uma paz que me incomoda."
    
    c "Ari. Eu sabia que você estaria nesse vagão. Você é uma criatura de hábitos, não é?"
    
    menu:
        "Por que você sumiu?":
            $ conversou_trem = True
            a "Hábitos? Você fala de hábitos depois de desaparecer da face da terra? Eu quase fui até a sua casa, Cain. Eu achei que você tinha se cansado de mim."
            c "Eu nunca me cansaria de você, Ari. É que... às vezes o ruído do mundo fica alto demais. Eu precisei de silêncio para conseguir ouvir o que realmente importava."
            a "E o que importava não incluía me responder?"
            c "Pelo contrário. Incluía me preparar para falar com você hoje."
        "Você parece diferente.":
            a "Você está... estranho, Cain. Não é o seu jeito de sempre. Onde está o sarcasmo? Onde está a reclamação sobre o sono?"
            c "Eu deixei essas coisas no verão, Ari. Elas pesavam demais. Você não acha que a gente gasta muito tempo sendo infeliz por hábito?"
            a "Eu acho que a gente gasta tempo sendo humano. E humanos reclamam."
            c "Talvez. Mas hoje, eu só quero observar. Olhe para essas pessoas... cada uma carregando um universo que vai desaparecer um dia."

    "Ele estende a mão e me entrega um pequeno objeto. Um marcador de página feito de papel grosso, com bordas cuidadosamente cortadas."
    "No centro, uma caligrafia elegante, mas com um erro que me faz sorrir involuntariamente."
    
    "{i}“Memoria te servat.”{/i}"
    
    a "Cain... você sabe que isso está errado, né? {i}Servat{/i} é salvar ou preservar. Se você queria dizer que a memória me mantém, deveria ser {i}tenet{/i}."
    
    show cain laugh with dissolve
    c "Hahaha! Eu sabia. Eu apostei comigo mesmo que você corrigiria a gramática antes de agradecer pelo presente."
    c "Mas e se eu não estiver errado, Ari? E se a memória for a única coisa que realmente pode salvar alguém?"
    
    a "Salvar de quê?"
    
    c "Do nada. Do vazio que fica quando a gente para de ocupar espaço no mundo."
    
    "O trem freia. A estação dele chegou."
    c "A gente se vê por aí, Ari. Não esqueça de marcar a página. É importante saber onde você parou."
    
    scene bg black with fade
    stop music fadeout 2.0
    
    "Eu não sabia, mas aquela foi a última vez que o vi respirar o mesmo ar que eu."

label dia_seguinte:
    scene bg school_rain with fade
    play music "audio/sad_piano.mp3" loop
    
    "O dia seguinte veio com uma chuva fina, daquelas que não molham a terra, mas esfriam a alma."
    "A escola parecia um funeral antes mesmo do anúncio. O silêncio nos corredores era denso, quase sólido."
    
    scene bg classroom with dissolve
    "Eu estava sentado na minha mesa, olhando para o lugar vazio ao meu lado. O lugar de Cain."
    "A porta da sala se abriu com um rangido que pareceu um grito."
    
    show staff serious at center
    f "Alunos... por favor, prestem atenção."
    "A voz dela tremia. Ela não olhava para ninguém."
    f "Recebemos uma notícia muito triste esta manhã. O aluno Cain... ele faleceu ontem à noite, em sua casa."
    
    "O mundo não parou. Ele simplesmente se quebrou."
    "Ouvi soluços. Ouvi alguém deixar uma caneta cair. Mas para mim, o som foi de vidro estilhaçando dentro dos meus ouvidos."
    
    a "(Não... ontem ele estava no trem. Ele sorriu. Ele me deu o marcador...)"
    a "(Ele estava se despedindo. Ele sabia. Ele sabia e eu estava corrigindo o latim dele!)"
    
    "A culpa é uma substância ácida. Ela corrói a memória até que tudo o que sobra é o arrependimento."

    jump rupturas_expandidas

label rupturas_expandidas:
    scene bg school_corridor with fade
    "Os dias que se seguiram foram um borrão de cinza. Eu via o rosto dele em cada sombra."
    "Na biblioteca, eu jurava ouvir o som da risada dele entre as estantes de história."
    "No reflexo da janela do ônibus, por um milésimo de segundo, ele estava lá, sentado no banco de trás, olhando para a rua."
    
    "Mas quando eu piscava, o assento estava vazio."
    "Eu estava ficando louco? Ou o mundo estava se recusando a aceitar que ele tinha ido?"
    
    scene bg dream with dissolve
    "E então, os sonhos começaram. Sonhos que pareciam mais reais que a própria vida."
    "Eu estava em um lugar sem cor, e Cain estava lá, estendendo a mão."
    
    show cain hand_out at center:
        alpha 0.8
    c "Não demora, Ari. O intervalo é curto, e o esquecimento é rápido."
    c "Se você não vier agora, não sobrará nada de mim para você salvar."
    
    jump a_travessia_detalhada

label a_travessia_detalhada:
    scene bg train_night with fade
    "Uma semana depois. O mesmo trem. O mesmo horário."
    "Eu abri o livro de latim. O marcador estava na página 112. Onde eu parei no dia em que ele morreu."
    
    "As palavras na página pareciam se mover. Elas se rearranjavam diante dos meus olhos."
    "{i}“Inter vivos et mortuos.”{/i}"
    
    "O trem entrou no túnel. Mas desta vez, a escuridão não passou."
    "As luzes do vagão começaram a piscar violentamente. O som do motor foi substituído por um silêncio absoluto, vácuo puro."
    
    stop music
    "O trem parou com um solavanco que me jogou para frente."
    
    scene bg black with flash
    "Quando abri os olhos, o vagão estava vazio. Não havia passageiros. Não havia anúncios."
    "Apenas uma luz fria, azulada, vindo de fora."
    
    scene bg station_intervalla with fade
    play music "audio/ambient_mystery.mp3" loop
    
    "Eu saí do trem. Meus pés não faziam barulho no chão da plataforma."
    "O letreiro da estação, em letras de neon que zumbiam baixo, dizia apenas uma palavra:"
    "{b}INTERVALLA{/b}"
    
    "Vi pessoas sentadas nos bancos. Elas pareciam feitas de fumaça. Seus olhos eram buracos vazios, olhando para um horizonte que não existia."
    "E no final da plataforma, sentado sozinho..."
    
    show cain blurred at center with dissolve:
        alpha 0.6

    a "Cain?"
    
    c "Você demorou, Ari. Eu já estava começando a perder a cor das minhas próprias mãos."
    
    a "O que é este lugar? Eu morri também?"
    
    c "Não. Você é um visitante. Eu sou um residente... por enquanto."
    c "Este é o Intervalla. O lugar onde as pessoas ficam quando o mundo começa a esquecê-las, mas elas ainda se recusam a soltar a vida."
    c "Cada vez que alguém para de falar de mim, eu fico mais transparente. Cada vez que uma foto minha é guardada em uma gaveta, eu perco um pedaço da minha voz."
    
    a "Eu nunca vou te esquecer! Eu estou aqui, não estou?"
    
    c "Estar aqui não é o suficiente. Você precisa enfrentar o que nos trouxe até aqui. As memórias que você trancou porque doíam demais."
    c "Se você quer me manter real, precisa aceitar a realidade de quem fomos. Sem filtros. Sem desculpas."

    jump dungeons_memoria

label dungeons_memoria:
    scene bg station_intervalla with dissolve
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
    "O cenário se reconstrói lentamente."
    "O cheiro de grama cortada se mistura ao calor abafado de um verão antigo."
    "Por um instante, eu esqueço onde estou. Esqueço o trem. Esqueço o Intervalla."
    "Lá estamos nós, dois anos atrás."

    "Eu estou sentado num banco, cercado de livros e anotações."
    "Cain está ao meu lado, balançando o pé na terra, arrancando pequenos pedaços de grama sem perceber."

    show cain young_sad at left
    show ari young_distracted at right

    cy "Ari… você já parou pra pensar que talvez a gente esteja correndo demais?"
    cy "Todo mundo fala de futuro como se ele fosse garantido."
    cy "Mas e se não for?"

    "Eu me lembro do incômodo que senti."
    "Não pelas palavras dele — mas porque elas me tiravam do controle."

    cy "Às vezes eu sinto que você já decidiu tudo."
    cy "Que eu só tô aqui… acompanhando."
    cy "Como se a minha função fosse não atrapalhar."

    a "(Eu devia ter fechado o livro.)"
    a "(Devia ter olhado pra ele.)"
    a "(Mas eu não fiz.)"

    menu:
        "Você está sendo dramático, Cain.":
            a "Eu lembro exatamente do tom da minha voz."
            a "Impaciente. Superior."
            a "Cain, você pensa demais. A vida não é um poema trágico."
            a "Se você gastasse metade dessa energia estudando, não estaria tão perdido."

            cy "Perdido…"
            cy "Engraçado você dizer isso."
            cy "Porque naquele momento, eu achei que você era o único que sabia exatamente pra onde estava indo."

            "Cain abaixa a cabeça."
            "A sombra dele se alonga no chão, como se estivesse sendo engolida."

            cy "Eu não queria respostas, Ari."
            cy "Eu só queria que você me escutasse."

            "A imagem dele perde saturação."
            "O mundo fica mais silencioso."

            "A solidez não aumenta."
            "Eu entendo agora: não foi crueldade."
            "Foi indiferença."

        "Eu sinto muito por não ter te visto.":
            a "Eu fecho o livro. Devagar."
            a "Como se esse gesto pudesse atravessar o tempo."

            a "Eu estava tão ocupado tentando ser alguém…"
            a "Que não percebi que estava deixando você sozinho bem do meu lado."

            a "Você não era figurante, Cain."
            a "Eu é que transformei você em pano de fundo."

            cy "Você sabe o que mais doeu?"
            cy "Não foi você discordar."
            cy "Foi você nem perceber que eu estava pedindo ajuda."

            a "Eu sinto muito."
            a "De verdade."

            "Cain respira fundo."
            "Quando ele levanta o rosto, há dor — mas também alívio."

            cy "Obrigado por finalmente olhar pra mim."

            "Uma luz suave envolve o corpo dele."
            "As cores voltam. O peso no ar diminui."

            $ solidez += 1

    $ dungeon_1_feita = True
    "O parque começa a se desfazer."
    "As árvores viram páginas em branco."
    "O vento espalha palavras não ditas como pétalas."

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

    cw "Mas e você, Ari?"
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

    ca "Olha isso, Ari!"
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
    c "Ari. Você conseguiu. Você atravessou o lodo das nossas falhas e não soltou a minha mão."
    a "Eu entendi agora, Cain. O marcador... {i}Memoria te servat{/i}. A memória me salva porque ela me obriga a ser honesto."
    a "Eu não vou te esquecer. Mas eu também não vou ficar preso no que poderia ter sido."

    c "Obrigado. Por me deixar ser humano uma última vez."
    c "Agora, volte para o trem. Há uma vida inteira esperando por você."

    "Ele me abraça. O toque é quente, real."

    scene bg train_interior with fade
    "Memoria te servat."

    return

label final_ruim:
    "O mundo ao redor se torna estático. O tempo para."
    "Cain me olha com uma tristeza infinita."
    c "Ari... você não deveria ter escolhido isso."
    "Mas agora, somos apenas dois vultos sentados num banco, esperando o esquecimento chegar."
    return