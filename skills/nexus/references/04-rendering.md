## 8. Renderização avançada, 3D, composição e materialidade — quando o tema exigir

Determine se a experiência precisa de 3D real, 2.5D, SVG, Canvas 2D, imagens compostas, animação tipográfica ou DOM/CSS. Escolha pela qualidade percebida, pelas possibilidades interativas e pela função no projeto. Não imponha Three.js nem elimine 3D só porque sua implementação é trabalhosa. Se a ideia depende de perspectiva, geometria, iluminação, rotação livre ou materialidade, considere uma implementação 3D genuína.

Quando houver 3D, produza uma especificação de engenharia completa, não apenas a instrução “adicione um modelo 3D”. Inclua:

**Geometria e coordenadas:** escolha malha procedural, modelo importado ou geometria híbrida; declare unidades, dimensões, proporções, subdivisões, orientação, pivot, eixo, UVs, índices, winding, normais, limites e transformações. Se houver deformação, especifique funções matemáticas, coeficientes, intervalos e condições de contorno. Se a forma precisar ser fechada, verifique sua topologia em vez de confiar somente na aparência frontal. Se houver vários objetos semelhantes, considere geometria compartilhada, instancing ou pooling.

**Texturas:** determine resolução, mipmaps, espaço de cor, anisotropy, recorte, canais, transparência e mapeamento UV. Se usar texturas geradas por canvas, defina as áreas, camadas, tipografia, gradientes, gráficos, proporções e composição do desenho com valores normalizados ou pixels. Aguarde fontes e ativos necessários. Nunca reutilize um rótulo ou arte que não pertença ao tema.

**Materiais:** defina propriedades físicas coerentes com a superfície: base color, roughness, metalness, transmissão, clearcoat, opacity, alpha test, normal map, emissive, intensidade de ambiente e variantes. Não use os mesmos parâmetros para papel, metal, vidro, pele, tecido, plástico e elementos digitais. Declare valores numéricos e ajuste em relação ao ambiente e à identidade do projeto.

**Luz e sombra:** determine posições, intensidades, cores, ambiente, reflexos, tom, exposição e técnica de sombra. Se usar sombras procedurais de contato, especifique suas dimensões, gradiente, opacidade e relação com escala, posição, inclinação e orientação do objeto. Separe o que é efeito visual do que é fisicamente calculado.

**Câmera:** defina perspectiva ou ortográfica, posição, alvo, near/far, fov e projeção. Quando precisar alinhar uma cena de perspectiva ao DOM em z=0, uma solução possível é colocar a câmera a distância D, ajustar `fov = 2·atan((vh/2)/D)` em graus e usar x = screenX − vw/2 e y = vh/2 − screenY. A escala deve converter a dimensão do modelo à dimensão desejada em CSS pixels. Se o objeto estiver deslocado em profundidade, considere a alteração aparente da perspectiva. Declare ordem das rotações e conversão de unidades.

**Cena e camadas:** determine se uma cena persistente é necessária para manter continuidade entre seções. Um canvas único, transparente e fixo pode ser apropriado para objetos compartilhados; outras arquiteturas são válidas. Defina o mapa de z-index e stacking contexts, quais elementos são renderizados acima e abaixo da cena, quais recebem eventos, como ocorre picking/raycast e como placeholders DOM alinham a cena. Evite overlays que interceptem cliques ou escondam texto importante.

**Comportamento:** descreva estados de posição, escala, rotação, profundidade, opacidade e sombra. Para trajetórias com múltiplos slots, declare uma tabela com coordenadas, escala, ângulos, profundidade e fade; para posições fracionárias, interpole os slots de forma contínua. Para efeitos de partículas, defina quantidade, origem, seed, fases, distribuição, vida útil, velocidade, trajetória, escala, rotação e opacidade. Não use partículas que não tenham relação com o tema. Projete reversão e sincronização com o estado da interface.

**Render loop:** use um loop consistente baseado em timestamp/delta quando necessário, não múltiplos loops independentes desnecessários. Diferencie atualização de estado, medição de layout e renderização. Evite alocações excessivas por frame, leituras e escritas DOM alternadas, compilação de shaders durante interação e carregamento repetido. Limite device pixel ratio conforme o orçamento de desempenho, pause ou reduza renderização fora da viewport e em abas ocultas, libere texturas, geometrias, materiais e render targets. Trate perda e restauração de contexto WebGL.

**Fallback:** implemente representação visual e controles funcionalmente equivalentes sem WebGL, quando indisponível, lento ou incompatível. O site não deve se tornar inutilizável porque a cena não carregou. Para projetos sem 3D, aplique rigor equivalente à composição, geometria, pipeline de ativos, estados e renderização das técnicas escolhidas.

