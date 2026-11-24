# Nexus

**Adaptive creative direction & high-fidelity web engineering for AI agents.**

Nexus is an Agent Skills-format workflow for designing, implementing and auditing original web experiences. It turns a brief into a theme-specific creative thesis, precise technical specifications, functional software and evidence-based acceptance tests. It is not a website template or a mandatory animation stack.

> Generalize the process, not the visual result.

Created for Louizricard. Version 1.0.0.

## Installation

Install directly from the public repository using the Skills CLI:

```bash
npx skills add Louizricard/Nexus-skill --skill nexus
```

For a local checkout, open the repository directory and run:

```bash
npx skills add . --skill nexus
```

Alternatively, copy the entire `skills/nexus/` directory (not just `SKILL.md`) to the skills directory documented by your agent. The format follows the [Agent Skills specification](https://agentskills.io/specification); the installer is documented at [vercel-labs/skills](https://github.com/vercel-labs/skills). Actual skill discovery, tools and execution capabilities depend on the agent and its version. No framework or runtime is required by the skill itself. Building and verifying websites requires suitable coding and browser tools. Python 3 is optional for the package validator.

## Usage

Ask your agent to use Nexus for a new project, redesign, implementation or audit. Examples:

- “Use Nexus para criar meu portfólio a partir do meu GitHub.”
- “Use Nexus to redesign this SaaS without changing its existing features.”
- “Use Nexus para criar uma experiência editorial sobre arquitetura.”
- “Use Nexus to audit this dashboard for task completion, accessibility and visual consistency.”

If the briefing is incomplete, Nexus asks targeted questions. If it is sufficient, Nexus proceeds to creative direction, specifications, implementation and verification. It responds in the user's language; the detailed technical modules are in Portuguese. A specification-only request does not trigger implementation.

## What makes Nexus different

The workflow retains the complete 17-chapter source master prompt, organized into mandatory stage-specific references. It does not require a shop, landing page, carousel, 3D model, intro video, animation library or framework. It requires that the chosen technique be justified, numerically specified where relevant and validated.

- Original creative thesis and signature interaction appropriate to the project's purpose.
- Asset pipeline, visual tokens, layout, typographic hierarchy and layer maps.
- Motion contracts, continuous state interpolation, scroll, gesture handling and interruptions.
- Optional advanced rendering: procedural geometry, materials, texture pipelines, lighting, camera, WebGL and fallbacks.
- Real functionality, state integrity, responsive behavior, keyboard/touch, reduced motion and error handling.
- Performance budgets, observable acceptance tests and explicit verification status.

## Repository structure

```text
Nexus/
├── README.md
├── README.pt-BR.md
├── CHANGELOG.md
├── .gitignore
├── evals/
│   ├── scenarios.json
│   └── source-manifest.json
└── skills/
    └── nexus/
        ├── SKILL.md
        ├── references/
        │   ├── 01-discovery.md
        │   ├── 02-design-system.md
        │   ├── 03-motion.md
        │   ├── 04-rendering.md
        │   ├── 05-experience-and-state.md
        │   ├── 06-responsive-engineering.md
        │   ├── 07-production-and-audit.md
        │   └── 08-production-contract.md
        └── scripts/
            └── validate.py
```

## Validation

```bash
python3 skills/nexus/scripts/validate.py
```

The included offline validator checks packaging, metadata conventions, reference links and coverage of chapters 0–16. The source manifest records the SHA-256 of the complete source body. `evals/scenarios.json` supplies manual behavioral evaluation cases for different site types; these are not an automated agent benchmark and no agent runs or generated website tests are claimed for this release.

## License

No open-source license has been selected. Public visibility alone does not grant a license to redistribute or modify this project; the repository owner can choose a license separately.
