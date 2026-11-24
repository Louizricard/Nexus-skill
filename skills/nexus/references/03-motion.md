## 7. Engenharia de interação e motion design

Trate movimento como um sistema temporal e espacial, não como uma coleção de efeitos CSS. Para cada interação expressiva, determine o estado de origem, destino, condições de disparo, comportamento intermediário e estado final. Use a técnica mais adequada (CSS, Web Animations API, SVG, Canvas, WebGL ou biblioteca compatível com a stack). Não instale uma biblioteca apenas para reproduzir algo nativo de forma mais pesada.

Crie uma tabela de coreografia para as interações relevantes com estes campos: identificador, gatilho, elementos afetados, propriedades, valores iniciais e finais, duração em ms, atraso, stagger, easing, dependências, cancelamento, repetição, direção inversa, fallback e comportamento sob reduced motion. Declare valores concretos na especificação do projeto, não apenas intenções.

Considere os seguintes mecanismos quando contribuírem com a tese criativa:

### 7.1. Continuidade entre estados e espaços

Para um objeto ou representação que viaja entre partes da interface, prefira preservar uma única entidade visual e seu estado. Evite recriar um objeto em cada seção e esconder a descontinuidade com fades. Defina âncoras com retângulos reais medidos no DOM ou coordenadas equivalentes. Um estado pode ser representado como `{x, y, h, w, rx, ry, rz, z, sx, sy, opacity, shadow, ...}`; inclua apenas campos pertinentes à representação.

Se a entidade atravessa A, B e C, calcule a progressão a partir da posição real da página ou do fluxo. Por exemplo, em uma transição entre seções, p = clamp(1 − sectionTop/vh, 0, 1). Use interpolação entre âncoras (`lerp(a,b,t) = a + (b−a)·t`) e easing explícito para cada campo. Defina as janelas de transição, quando objetos secundários desaparecem, quando a navegação muda e quando o estado final passa a responder às interações do destino.

Faça o objeto coincidir precisamente com a âncora de destino, inclusive após resize, mudança de orientação, alteração de conteúdo, carregamento de fontes e transformações interativas. Se existir uma representação estática equivalente, oculte-a somente quando a entidade dinâmica estiver pronta e presente; nunca mostre dois objetos indevidamente.

Em interfaces com shared-element transitions, a mesma regra se aplica à passagem de lista para detalhe, edição, visualização ou seleção. Preserve identidade, posição, contexto e foco. Trate interrupções e navegação inversa.

### 7.2. Scroll e narrativa temporal

Quando houver uma sequência conduzida pelo scroll, defina o comprimento de cada trecho, posição de sticky, proporção da viewport, entradas, saídas, janelas de movimento e progressão normalizada. Por exemplo, para uma seção fixada com altura H > vh: p = clamp(−sectionTop/(H−vh), 0, 1). Mapeie cada intervalo de p para uma ação ou informação concreta, e diferencie animações diretamente controladas pelo scroll de tweens disparados por mudança de etapa.

Ao atravessar um limite em ambas as direções, o estado deve ser determinístico. Saltos de scroll, âncoras, teclas, restauração de posição e navegação devem alcançar o estado correto sem depender de assistir à sequência inteira.

Se houver suavização de scroll, preserve por padrão o comportamento nativo. Uma suavização personalizada só é aceitável quando acrescentar valor e não comprometer teclado, tecnologia assistiva, zoom, touch, histórico, âncoras, conteúdo interno e preferências de movimento. Caso seja necessária, determine a constante de tempo; uma forma independente da taxa de quadros é `current += (target − current)·(1 − exp(−dt/τ))`. Defina tolerância de término, clamp, cancelamento e devolução imediata ao controle nativo. Nunca capture scroll por toda a aplicação indiscriminadamente.

Use seções pinned apenas se a leitura e a navegação continuarem naturais. Não prenda o visitante para assistir a uma animação. Dimensione a distância de scroll em função da quantidade de informação e não de uma altura arbitrária.

### 7.3. Gestos, seleção e manipulação direta

Quando houver carrossel, comparação, timeline arrastável, navegação espacial, reorganização ou outra interação de manipulação, especifique hit areas, mapeamento de coordenadas, limiar de intenção (por exemplo, 6 CSS px quando apropriado), pointer capture, axis lock, regras de touch-action, estados de drag, limites, snap, velocidade, aceleração, inércia e cancelamento.

Calcule velocidade com amostras de tempo reais e suavização, não com deslocamento bruto por frame. Se houver snap inercial, determine explicitamente a projeção (`target = round(pos + clamp(v·T, −L, L))` para um seletor discreto compatível), o limite de deslocamento L e a janela T. Ajuste parâmetros conforme a natureza da interação. Garanta que clique, toque, teclado e controles alternativos atinjam os mesmos estados. Use raycasting apenas quando houver objetos 3D reais que precisem disso.

Não force autoplay. Quando fizer sentido, especifique intervalo, pausa, retomada, visibilidade mínima, visibilidade da aba, condição de interação ativa e respeito a reduced motion. Disponibilize controle de pausa acessível e não altere conteúdo enquanto o usuário estiver lendo ou manipulando um controle dependente dele.

### 7.4. Transições de conteúdo, cor e composição

Projete trocas de estado como uma sequência sincronizada. Determine o momento em que a cor, conteúdo, ícone, número, imagem, geometria e estado lógico mudam. Use delay e stagger com intenção. O estado acessível precisa representar o conteúdo correto independentemente dos frames visuais.

Se uma revelação radial fizer sentido, determine centro c, raio máximo R = margem × distância ao canto mais distante, progresso r = R·ease(t), faixa de feather f e composição de máscara. Se uma transformação linear, máscara geométrica, recorte tipográfico ou transformação de material for mais adequada, use-a. Não reproduza revelações circulares em todos os projetos.

Para transições tipográficas, defina máscaras, agrupamento em palavras, deslocamento percentual, opacidade, ordem, direção, stagger e duração. Preserve leitura e semântica, evite duplicar anúncios em leitores de tela e garanta que nomes extensos e traduções não estourem o layout.

Como ponto de partida técnico, não como padrão visual obrigatório, microinterações podem usar 120–240 ms, feedback expressivo 250–450 ms, mudanças de contexto 400–750 ms e coreografias complexas 700–1600 ms. Calibre os valores em função da distância, significado e frequência da interação. Para movimentos de glide, considere curvas com aceleração rápida e desaceleração longa; para rotações contínuas, considere seno ou curvas de velocidade adequadas; para movimentos com massa aparente, use spring com parâmetros declarados. Evite usar o mesmo easing para tudo.

### 7.5. Feedback visual e consequências funcionais

Toda ação deve comunicar que foi recebida e qual consequência produziu. Projete feedback imediato, progresso e resultado. Uma transição de origem a destino pode conectar visualmente uma ação ao seu efeito (por exemplo, um item adicionado, um projeto aberto, uma seleção aplicada ou um dado atualizado), mas não invente uma ação comercial onde ela não existe.

Para uma trajetória entre origem S e destino D, calcule d = D − S em coordenadas da viewport, defina os keyframes intermediários, desvios, escala, rotação, opacidade e timing. Não use trajetórias fixas que quebrem quando a tela ou o layout mudar. Atualize o estado lógico no momento apropriado e de forma idempotente. Uma animação nunca deve causar dupla submissão ou perda de dados.

Trate cliques rápidos, interrupções, pointercancel, mudanças de tamanho, imagens tardias, navegação durante a animação e mudanças de estado concorrentes. Defina explicitamente se cada transição é cancelada, retomada, substituída ou enfileirada. Limpe listeners, timers, observers, animações e recursos ao desmontar a interface.

