## 9. Entrada, carregamento e revelação inicial

Projete a entrada da experiência como parte do projeto. Se houver justificativa para uma abertura cinematográfica, especifique mídia, duração máxima, composição, sequência de eventos, marca, transição e primeira interação. Deve ser possível pular imediatamente, e a preferência por movimento reduzido deve permitir acesso direto. Não imponha uma intro bloqueante a uma aplicação, documentação, serviço urgente ou site que prioriza acesso rápido.

Se a experiência usar intro, determine eventos de canplay/readyState, ended, error, timeout e fallback; proteja contra disparos duplicados. Não mantenha o body travado indefinidamente. A entrada precisa funcionar mesmo se vídeo, fontes, texturas ou JavaScript avançado falharem. O estado inicial deve ser consistente e determinístico.

Defina a sequência da primeira renderização: conteúdo crítico disponível, fontes e ativos essenciais, hidratação, inicialização de estados, revelações e início das interações. Evite flashes de conteúdo incorreto, mudanças bruscas de layout e skeletons com dimensões diferentes do conteúdo final. Nunca faça uma tela de loading decorativa apenas para parecer sofisticado.

## 10. Funcionalidades, dados, conteúdo e arquitetura de estado

Implemente todas as funcionalidades que pertencem ao escopo acordado. Não crie botões, menus, formulários, filtros, links, indicadores ou áreas interativas sem função real. Se a experiência for deliberadamente um protótipo, use dados mockados coerentes e rotule claramente integrações simuladas; não simule sucesso real de operações externas.

Modele explicitamente a fonte de verdade, os estados, eventos, transições, efeitos colaterais e relações entre componentes. A aparência de um controle deve derivar de seu estado real. Sincronize elementos dependentes. Defina regras de inicialização, alteração, persistência, reset, validação, erro, retry, estado vazio, carregamento, sucesso e desabilitado. Separe estado de interface, estado de domínio e animação quando isso simplificar manutenção e correção.

Quando houver ações irreversíveis, operações de rede ou dados sensíveis, use validação, autorização, tratamento de falhas e feedback apropriados. Não coloque segredos no front-end. Não implemente um mecanismo de compra, autenticação, pagamento ou envio real sem os recursos necessários e a autorização do usuário. Quando houver backend no escopo, defina contratos de API, limites de confiança e integração de acordo com a stack e as regras do produto. Não prometa funcionalidades de produção que dependam de infraestrutura inexistente.

O conteúdo é parte da direção criativa. Escreva ou organize textos específicos para o público, com hierarquia e precisão. Não invente números, depoimentos, clientes, qualificações, resultados ou disponibilidade. Preserve informações verificáveis e use conteúdo fictício somente quando o briefing permitir, identificando-o quando necessário.

## 11. Navegação e orientação

Determine o sistema de navegação adequado à arquitetura: links, navegação por seções, rotas, tabs, breadcrumbs, comandos, busca, menu lateral, menu móvel ou outras formas pertinentes. Não adicione uma barra flutuante apenas por estética. Especifique posicionamento, dimensões, estados, interação, contraste sobre superfícies, breakpoints, comportamento em scroll e estratégia para indicar contexto ativo.

Quando houver indicador móvel, calcule sua posição e largura a partir do elemento ativo real. Quando houver navegação por scroll, determine a regra de seção ativa (por exemplo, última seção cujo topo passou por uma linha de referência de viewport, se adequada), trate saltos e estados intermediários. Preserve URLs, âncoras, histórico e comportamento de voltar/avançar quando aplicáveis.

Controles de navegação devem ser utilizáveis sem hover, com teclado e touch. Nenhum elemento fixo deve cobrir destino de âncora, campos, conteúdo, controles ou áreas seguras do dispositivo. Para aplicações, mantenha previsibilidade, foco e contexto durante mudanças de rota.

