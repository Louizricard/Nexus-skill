## 12. Responsividade real, acessibilidade e movimento reduzido

Crie responsividade como uma adaptação da composição e da interação, não uma redução proporcional do desktop. Escolha breakpoints onde o conteúdo realmente exige mudança. Projete layouts para monitores amplos, notebooks, tablets, celulares, orientação landscape e telas muito estreitas. Considere teclado virtual, barras dinâmicas do navegador, safe areas, unidades svh/dvh, conteúdo variável, fontes ampliadas e zoom.

Para cada modo, documente tamanhos, posicionamento, reorganização, mudança de navegação, escala tipográfica, densidade, comportamento de ativos, gestos e eventuais substituições de animação. Teste pelo menos, quando aplicável, 1440×900, 1920×1080, 1280×720, 768×1024, 390×844, 320 px de largura e 844×390. Acrescente dimensões pertinentes ao público. Não permita scroll horizontal involuntário, sobreposições, texto cortado, botões inacessíveis ou conteúdo dependente de hover.

Use HTML semântico, nomes acessíveis, labels, estados ARIA quando apropriados, foco visível e ordem lógica. Preserve navegação por teclado, escape de modais, retorno de foco, anúncio de erros e mensagens de estado. Busque conformidade WCAG 2.2 AA para os critérios aplicáveis: contraste, reflow, controles, leitura e operação. Não alegue certificação sem auditoria correspondente. Prefira áreas de toque de aproximadamente 44 CSS px quando o layout e a função permitirem, respeitando os requisitos aplicáveis.

Implemente `prefers-reduced-motion: reduce` como comportamento completo, não apenas zerando uma duração isolada. Remova movimento contínuo, parallax, autoplay, intro bloqueante e partículas quando inadequados. Substitua deslocamentos e rotações por mudanças imediatas ou transições discretas; preserve significado, feedback, seleção, navegação e todas as funções. Ofereça pausa para movimentos contínuos quando necessário. Evite flashes perigosos.

As experiências de desktop, mobile e movimento reduzido devem conservar a personalidade e o conteúdo do projeto, ainda que usem técnicas diferentes. A versão simplificada não deve parecer um produto abandonado.

## 13. Engenharia, desempenho e forma de entrega

Use a stack definida pelo briefing ou a arquitetura existente do projeto. Se nenhuma estiver definida, escolha a solução mais simples capaz de entregar a ambição visual e funcional integralmente. Um único HTML com CSS e JS pode ser adequado para uma experiência autônoma simples; uma aplicação com rotas, dados, autenticação ou manutenção contínua pode exigir estrutura modular. Não force arquivo único nem framework pesado.

Se estiver trabalhando em um repositório existente, inspecione convenções, dependências, comandos e arquitetura antes de modificar. Preserve funcionalidades fora do escopo, evite refatorações desnecessárias e não exponha arquivos privados. Organize módulos, componentes, tokens, ativos, estados e serviços de forma legível. Não esconda complexidade acidental em código duplicado ou valores mágicos sem explicação.

Defina orçamento técnico apropriado: peso inicial, tamanho de imagens, fontes e mídia, número de requisições, custo de JS, custo de renderização, draw calls quando aplicável, uso de memória e estabilidade de layout. Busque como referência LCP ≤ 2,5 s, INP ≤ 200 ms e CLS ≤ 0,1 em condições representativas quando aplicável; esses valores são objetivos, não medições presumidas. Para animação contínua, busque fluidez próxima de 60 fps em dispositivos capazes, degradando complexidade conforme o hardware, sem remover funções essenciais. Declare o dispositivo e cenário se reportar medições.

Use carregamento progressivo, otimização de imagens, cache, lazy loading fora do conteúdo crítico, preload seletivo, composição eficiente e execução sob demanda. Não faça preloads indiscriminados. Meça antes de afirmar que algo está otimizado. Não introduza dependências, trackers ou hosts que não tenham sido justificados. Se possível, inspecione rede, console, memória e desempenho reais.

A entrega deve ser utilizável e reproduzível: arquivos necessários, código completo, ativos reais ou alternativas claramente identificadas, dependências fixadas quando apropriado e instruções suficientes para rodar. Se houver uma restrição explícita de HTML único, entregue esse HTML, sem transformar o requisito em um projeto de múltiplos arquivos. Se for solicitada implantação, execute-a apenas se houver ferramentas e autorização; caso contrário, deixe instruções reais, sem afirmar que publicou.

