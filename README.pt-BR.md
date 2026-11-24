# Nexus

Direção criativa adaptativa e engenharia web de alta fidelidade para agentes de IA.

A Nexus não é um template. É uma skill que transforma um briefing em uma experiência web autoral e funcional, mantendo rigor técnico desde a entrevista até a auditoria. Ela preserva todos os 17 capítulos do prompt mestre que a originou e carrega as referências por etapa. Não obriga o uso de 3D, carrosséis, introduções cinematográficas, lojas ou landing pages.

## Instalação

Instale diretamente pelo repositório público:

```bash
npx skills add Louizricard/Nexus-skill --skill nexus
```

Para instalar de uma cópia local, entre na pasta do repositório e execute:

```bash
npx skills add . --skill nexus
```

Ou copie toda a pasta `skills/nexus/` para o diretório de skills do agente. A compatibilidade depende do suporte ao padrão Agent Skills e às ferramentas do ambiente.

## Como usar

Exemplo: “Use Nexus para criar meu portfólio com base no meu GitHub.”

Se o tema ainda não estiver definido, a skill entrevista o usuário. Depois define a tese criativa, o mecanismo de assinatura, os ativos, o layout, a interação, o estado, a engenharia, os fallbacks e os critérios de aceitação. Quando a solicitação for construir, implementa e verifica conforme as ferramentas disponíveis. Não afirma ter testado aquilo que não executou.

## Validação

Execute `python3 skills/nexus/scripts/validate.py` para checar a estrutura. Os cenários em `evals/` são casos de avaliação manual ainda não executados com agentes. Consulte o [README principal](README.md) para a estrutura completa. Nenhuma licença de código aberto foi escolhida nesta versão.
