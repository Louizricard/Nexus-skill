# Production contract — project-specific working record

Complete the applicable fields with actual decisions, not a generic template delivered as the final product. Keep the record in the working context or an existing project documentation location. Mark fields not applicable with a reason; never use N/A to skip required behavior. A build must follow the specification; update it if implementation proves a decision wrong.

## Brief and decisions

- Theme, audience, primary task and measurable success criterion.
- Scope: pages/routes/flows, production vs prototype, data sources, integrations and deliverable format.
- Constraints, verified content, references, assumptions and unresolved questions.
- Creative thesis, signature mechanism, alternatives rejected and why.

## Visual and technical specification

- Asset manifest: purpose, source/rights, format, dimensions, crop, load strategy and failure fallback.
- Tokens: colors, type families/weights, type scale, spacing, radii, strokes, elevation, contrast and motion curves.
- Layout: reference viewport, grid, alignment, widths, min/max, media and container queries, mobile/landscape alternatives, safe areas and layers.
- For each section/route/flow: purpose, hierarchy, component geometry, content, semantics, state, input, events, dependencies, focus and accessibility.
- Motion contract per transition: trigger, source/target, timing in ms, easing, keyframes or equations, path coordinate system, cancellation/reversal, reduced-motion variant, cleanup and effect on logical state.
- For advanced rendering: technique and justification, geometry or visual primitives, coordinate space, pipeline, textures, material and lighting if relevant, camera, compositing, state mapping, render budget, event routing and fallback.
- Function contract: state source, transitions, validation, loading, error, retry, empty, success, concurrency and persistence. Specify API/auth boundaries only where appropriate.
- Performance budgets and tools; declare measurement conditions, not imagined metrics.

## Acceptance record

For every critical feature create an observable test: ID, requirement, initial state, action, expected result, viewport/input/environment, tolerance if relevant, status (PASS/FAIL/NOT RUN), evidence, corrective action. Examples of categories: first render, primary task, signature continuity, interrupt/reverse, keyboard and touch, reduced motion, long content, narrow screen, landscape, asset error, network failure, repeated action, state cleanup. Do not claim accessibility compliance without adequate evidence.

Suggested checks for browser environments: 1440x900, 390x844, 320px wide, 768x1024, 844x390; adapt to the project's real target devices. Inspect scroll bounds, focus, visibility, layout and actual behavior. For animation, check intermediate frames and final state rather than only screenshots at rest. If the theme requires a travelling entity, verify origin and destination geometry at each viewport, resizing during the journey, reverse scroll and interruption. For a utility app, instead prioritize task completion, state integrity and legibility.

## Completion report

Summarize what was built, the reason for the chosen signature, how to run it, actual verification results, limitations, and next actions only when warranted. An unverified result is not a pass. Do not deliver this contract instead of implementation when the user requested a build.
