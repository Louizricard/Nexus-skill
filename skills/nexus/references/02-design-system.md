## 4. Especificação de ativos e pipeline visual

Planeje cada ativo antes de implementar as seções que dependem dele. Para cada imagem, vídeo, ilustração, ícone, fonte, textura, modelo, áudio ou elemento procedural relevante, registre:

- Identificador, função narrativa/funcional, origem, licença ou autorização conhecida, caminho ou URL real e formato.
- Dimensões, proporção, resolução, transparência, enquadramento, recorte, foco, densidade de pixels, tratamento de cor e variantes responsivas.
- Se é ativo fornecido, criado por ferramenta disponível, gerado por código ou obtido de fonte autorizada. Não invente links ou declare que gerou ativos inexistentes.
- Modo de exibição, object-fit/object-position, máscaras, composição, carregamento, pré-carregamento, cache, fallback e texto alternativo quando necessário.
- Dependências entre ativos e elementos de UI, animações, geometria, texturas ou estados.

Quando o projeto exigir ativos gerados, use ferramentas realmente disponíveis ou crie alternativas procedurais fiéis à direção. Se a geração externa não estiver disponível, produza um briefing específico para o ativo e use apenas substitutos honestos e visualmente coerentes, identificando a limitação na entrega. Não baseie a experiência em imagens quebradas nem em promessas de produção futura.

Se usar uma folha de sprites/atlas, declare dimensões de origem SW × SH, caixas de recorte (x, y, w, h), padding e escala de redimensionamento. Para CSS, após aplicar padding à caixa, use background-size = (SW/w × 100%, SH/h × 100%) e background-position = (x/(SW−w) × 100%, y/(SH−h) × 100%), tratando eixos de denominador zero. Para texturas, converta coordenadas para a resolução realmente carregada, respeitando escala e orientação UV. Reutilize os mesmos ativos quando houver ganho de consistência ou desempenho. Não imponha atlas a projetos que não precisem dele.

Se houver vídeo, defina poster, duração, enquadramento, ponto de início e término, estratégia de reprodução, controles, mute quando necessário, eventos de erro, fallback e impacto no carregamento. Se houver fontes, confirme os arquivos, pesos e licenças; prefira WOFF2 quando apropriado, escolha font-display conscientemente, preveja fallback com métricas compatíveis e aguarde as fontes antes de desenhar textos dependentes de suas métricas em canvas.

Declare a estratégia de hospedagem dos ativos e todas as origens externas necessárias. Não introduza serviços externos sem função. Fixe versões de dependências e verifique compatibilidade, CORS e disponibilidade de recursos quando o ambiente permitir.

## 5. Sistema visual, tipografia, tokens e geometria de layout

Crie um sistema visual próprio, derivado da tese criativa. Defina cores por função, e não por tendência: superfícies, texto, contraste, ênfase, estados, fundos, bordas e contexto. Se o tema exigir variações dinâmicas, modele a transição entre elas sem comprometer contraste ou legibilidade.

Defina famílias tipográficas e papéis: display, leitura, interface, dados ou código apenas quando necessário. Especifique pesos, escalas, tracking, leading, larguras máximas, quebras de linha, alinhamentos, composição e regras para textos extensos e traduções. Não reduza o texto até ficar ilegível para preservar uma composição.

Especifique tokens de espaçamento, grid, gutters, raio, borda, sombra, profundidade, escala, tamanhos interativos, durations, curvas de easing e estados visuais. Centralize tokens em variáveis ou estrutura equivalente. Defina elementos com valores concretos, não adjetivos como “espaçamento elegante”.

Escolha um sistema de coordenadas adequado: grid fluido, container queries, frames proporcionais, layout intrínseco ou combinação. Se usar frames de referência, declare largura e altura Wref/Href e sua escala k = min(vw/Wref, vh/Href), ou outra fórmula justificada. Use unidades de largura para composições que acompanham a página e unidades baseadas em viewport apenas onde fizer sentido. Use clamp e limites de leitura, interação e tamanho para impedir extremos.

Estabeleça a hierarquia visual de cada página ou estado. Especifique o posicionamento em relação ao grid, a escala de elementos, respiros, áreas negativas, alinhamentos, relações de sobreposição e o papel de cada camada. Crie um mapa de stacking contexts quando houver overlays, sticky, fixed, WebGL, máscaras ou transformações. Não use z-index arbitrariamente nem permita que uma superfície decorativa cubra controles.

Projete metadata, títulos, descrição, ícone e demais elementos de compartilhamento conforme a natureza pública ou privada do projeto. Defina semântica HTML, idioma e estrutura de headings. Não fabrique marca, prova social ou resultados para preencher lacunas de conteúdo.

## 6. Arquitetura da interface e especificação de cada seção, página ou fluxo

Defina a arquitetura somente depois de compreender a jornada. O número de páginas/seções, seus nomes, sua ordem, a presença de hero, navegação, CTA, rodapé, catálogo, filtros, formulários, login ou dashboard devem decorrer do projeto. Não crie áreas inúteis para atender a um modelo.

Para **cada seção, página ou tela relevante**, produza uma especificação suficientemente detalhada para que outro engenheiro consiga reconstruí-la com fidelidade:

- Identificador, propósito, conteúdo real e relação com o restante da experiência.
- Estrutura DOM/componente, semântica, ordem de leitura e ordem de pintura.
- Layout de referência: tamanho, posições, grid, padding, gaps, alinhamentos e proporções, com valores, intervalos ou fórmulas explícitas.
- Tipografia, cores, materiais, sombras, imagens, ícones e hierarquia.
- Estados de entrada, repouso, foco, hover, press, seleção, navegação, carregamento, vazio, sucesso, erro e desabilitado, quando relevantes.
- Eventos, gatilhos, lógica, dependências, duração, easing, origem e destino de animações, regra de reversão/interrupção e relação com outras seções.
- Comportamento em desktop, tablet, celular, telas estreitas, landscape e janelas baixas; tratamento de textos longos e conteúdo variável.
- Interações acessíveis, fallbacks e critérios verificáveis de conclusão.

Para páginas narrativas, trabalhe ritmo, escala, contraste, continuidade e transformação. Um primeiro quadro pode estabelecer o universo visual; as próximas seções devem desenvolver a tese em vez de repetir o mesmo componente. Para ferramentas funcionais, projete estados e transições centrados nas tarefas; garanta que uma pessoa consiga operar rapidamente mesmo sem apreciar ou perceber a camada expressiva.

Construa a interface integralmente. Não deixe a qualidade concentrada apenas no hero enquanto o restante parece um template. Componentes secundários, navegação, formulários, telas vazias e erros devem compartilhar o mesmo rigor e identidade.

