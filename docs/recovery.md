# Recover or resume BUILD

[BUILD home](https://stunspot.github.io/build/) · [Install and start](start.md) · [Workflow guide](use.md)

Start from the observed state. Preserve the existing record, artifact and collaborator identities before retrying; a retry should not multiply chats or schedules.

## BUILD is not found

Ask Codex to locate the installed skill and read `build/SKILL.md`. If no installation exists, follow [Install and start](start.md). If the folder exists but discovery is unavailable, use the host's documented refresh or new-chat route and check again. If a resource link fails, compare the installation with the complete extracted release; copying only `SKILL.md` omits required files.

You can point the current chat to the complete extracted folder for supported session use. Report that as session use, not durable discovery. If a direct CONCEIVE or BRAID request fails, ask BUILD to read the corresponding bundled entrypoint under `build/references/workflows/` before proceeding.

## Only briefs exist, or the expected chats are missing

Ask for the actual collaborator identifiers and observed communication state. **PREPARED** means briefs; **CREATED** means identities exist without verified coordination; **ACTIVE** means actual access and exchanges have been observed.

If creation returned an uncertain result, look for the requested objective in the host's chat inventory before retrying. Recover surviving collaborators and create only the missing ones when authorized. If the host cannot provide enough separate contexts, preserve the briefs and identify that capacity limit. One chat performing several voices is not evidence of independent contexts.

## A handoff has stalled

Ask which design or artifact revision was sent, who should receive it, whether receipt was acknowledged, and what should happen next. A file saved on disk does not prove another context received it. Restore the actual communication or shared-file route, then send the handoff to the existing recipient. Continue work that does not depend on the missing response.

## The supervisor is not checking in

Ask for the real schedule identifier, target chat, cadence and enabled state. An ACTIVE collaboration does not prove unattended supervision. If scheduling is unavailable or excluded by your instructions, decide whether to continue with manual check-ins or explicitly request a supported schedule. Do not create a second heartbeat before inspecting the existing one.

## Work changed direction or lost a constraint

Point to the original objective, correction or settled design choice. Ask for the current handoff revision and a narrow comparison. Implementation may improve the means; a material change to purpose or commitments needs the corresponding design question reopened. Preserve unaffected work, then recheck only the behavior whose assumptions changed.

## Resume after interruption

Return to the existing BUILD chat or make the work record and relevant artifacts available to your host. Use:

```text
Resume BUILD [name] from its existing record. Recover the current phase, design and artifact revisions, real collaborators and supervision schedule before creating anything new. State what is complete, the next actor and action, and any condition that prevents continuation.
```

If the record is missing, gather the last delivered artifact, known chat references, latest design and last independent verdict. Ask the host to reconstruct only what those sources establish; keep unknown state explicit. Stop safely with the current artifact and next action if a necessary context or permission cannot be recovered.

## Pause or cancel

Say whether you mean the current action, the whole BUILD or unattended supervision. For example: `Pause this BUILD and its supervisor schedule. Preserve the record and artifacts, and tell me how to resume.` Ask the host to confirm the observed schedule state. Pausing does not undo an action already completed; inspect the actual result before retrying or reversing it.

## Get help

[Open a GitHub issue](https://github.com/Stunspot/build/issues) for a reproducible defect. Include BUILD version, host, chosen workflow, the smallest non-private request that reproduces the problem, expected behavior, observed state and relevant error text. Omit credentials, private files and confidential chat contents.

For direct help, ask stunspot in [Collaborative Dynamics Discord](https://discord.gg/stunspot) or email [contact@collaborative-dynamics.com](mailto:contact@collaborative-dynamics.com). No response-time guarantee is implied.

Maintained by stunspot / Collaborative Dynamics for BUILD 0.1.0. Revisit this guide after a workflow, scheduling or host-discovery change, or a recurring support failure.