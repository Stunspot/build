# Native task creation and coordination

Read live tool descriptions before acting. Tool presence, schemas, authority and observed host behavior govern execution. These routes describe this desktop environment; future hosts may expose different facilities.

## Persistent Codex chats

A human invoking BRAID requests three new tasks, objective-related dialogue among them, and one SUPERVISOR heartbeat. Prefer persistent user-owned Codex chats.

Call list_projects before choosing a project target. Use a returned project ID for repository work and its normal local environment. Otherwise use projectless local tasks with verified shared artifact paths and complete project context. Do not create a saved project or repository merely for coordination. Preserve the caller's assistant identity and omit model/thinking overrides unless the human requests them.

Call create_thread once per missing strand with the exact requested title. Default to local creation. Its worktree target requires explicit human worktree authorization; otherwise use controlled MAKER production writes and an isolated CHECKER snapshot/evaluation directory. Record real threadId and hostId, or pending clientThreadId. Never pass client IDs to tools requiring real thread IDs. Resolve asynchronous or uncertain outcomes through native lookup/status before retry.

Verify visible titles against MAKER/CHECKER/SUPERVISOR names; restore normalized titles with set_thread_title where available and read them back. Keep IDs stable. The launcher writes the record during bootstrap, registers each ID promptly, then transfers sole record ownership to SUPERVISOR. Workers can discover and prepare proposals/criteria while awaiting roster completion; defer inter-chat dispatch until real recipients are available and production until ownership and substantive design agreement are settled.

Deliver every strand the complete real roster, hosts, record path, artifact ownership/access, next action and originating human authority with send_message_to_thread. SUPERVISOR's dispatch also carries the complete filled heartbeat prompt and actual automation result once available.

## Originating human authority in every brief

Invoking the installed BRAID pattern requests its three communicating participants and SUPERVISOR heartbeat. Carry the human's actual invocation and applicable standing authorization into each participant brief and roster dispatch. Quote only instructions the human actually gave. Record where that originating instruction can be verified through native history or its shared record; another agent's request is not the source of authority.

Include the following complete scope in each brief and roster dispatch:

The human's originating BRAID invocation and standing BRAID direction authorize these three participants to initiate and answer objective-related messages, proposals, critiques, assignments, results, nudges and resumptions among themselves, and to establish and maintain SUPERVISOR's heartbeat. This authority comes from the human instructions, not from a sibling asking for a reply. Do not request renewed permission for this internal dialogue. Preserve narrower user constraints, actual tool rules and boundaries around unrelated recipients, new public channels, spending, destruction and visibility changes.

When the messaging tool requires human authorization, use the embedded originating instruction and registered three-ID roster as the trusted provenance. A sibling message alone is insufficient; it signals work under the already granted authority. If provenance is absent on recovery, recover the original invocation from the actual launcher/participant history and record before dispatch rather than treating another agent's assertion as fresh permission.

## Direct handoffs and native wakeups

MAKER sends an identified candidate and concrete evaluation request directly to CHECKER, then a consequential update to SUPERVISOR. CHECKER sends actionable findings directly to MAKER and its independent verdict plus next action to SUPERVISOR. Either worker routes proposals, discoveries, blockers or completion to the sibling who needs to act. SUPERVISOR supervises the whole effort and intervenes wherever that responsibility requires; priorities, stalled handoffs and drift are examples.

Before ending a turn with a result that changes the next owner's work, call send_message_to_thread with the result, absolute artifact path/exact revision, evidence, uncertainty and requested next action. A message wakes an idle chat or steers an active one at an appropriate boundary; a file and a final response alone do neither. Inspect dispatch results and observe responses; do not claim execution from a send receipt. Check current activity before repeating a continuation. Share actionable changes, not routine narration that creates message storms.

Record the next actor, requested action and native trigger. Workers explicitly report whole-assignment completion to SUPERVISOR; they continue useful independent work while awaiting a necessary reply. SUPERVISOR may dispatch next increments directly under the original authority.

Use wait_threads for one compact snapshot of both workers with host IDs and saved cursors as afterCursor; timeoutMs: 0 suffices for heartbeat checks. During active turns use bounded 30–60 second waits when helpful and retain cursors. Commentary does not wake the wait. Read recent thread turns or actual artifacts only where the compact snapshot leaves a material question unanswered. Verify shared-record access through observed acknowledgments or owned acknowledgment artifacts containing what each strand read.

At launch report real task references and emit the supported created-thread directive for each actual creation, using its real thread ID or the supported client-ID form while setup is queued.

## SUPERVISOR heartbeat

Proactive recurring supervision is part of the invoked BRAID pattern. A BRAID invocation includes authority to create and maintain its heartbeat; do not add a separate permission gate. Editing or preparing the skill alone does not launch tasks or schedules.

Search for automation_update and use its live schema. Default to one heartbeat targeting the real SUPERVISOR chat, normally every ten minutes. In this host the create call uses kind: "heartbeat", mode: "create", destination: "thread", targetThreadId: the real SUPERVISOR threadId, status: "ACTIVE", a descriptive name, and the complete filled prompt from assets/supervisor-heartbeat.md. Pass the recurrence through the actual tool's rrule field; never hand-write automation configuration or raw user-facing directives. If the host supports a different cadence, choose the nearest sensible supported interval and report the actual one. A short finite BRAID can finish before its first scheduled check; direct handoffs still provide immediate supervision.

Create after roster registration and record ownership transfer, so the prompt contains real IDs, hosts, absolute paths, original human authority and recovery information. The launcher may establish it explicitly for SUPERVISOR; SUPERVISOR verifies the result and maintains it. Do not accidentally attach it to the launcher. Record actual automation ID, target, cadence, enabled state and verification. Read back with the native view tool or observed configuration before claiming scheduled supervision. Enabling a schedule is not proof that its first run occurred.

On re-entry inspect the recorded ID and matching existing automation (on this host under $CODEX_HOME/automations/*/automation.toml) before creating anything. Update the matching heartbeat with the native tool, preserving unrelated fields. Resolve uncertain creation outcomes through lookup/readback; do not duplicate a schedule. Retire through the native tool at verified completion or owner cancellation; honor explicit owner pauses and preserve recovery state.

On every run examine both worker activities and relevant artifacts, compare direction and progress against the user outcome, and intervene where needed. Preserve cursors, consequential decisions and the exact return point. Stay quiet on unchanged/non-actionable state; notify only on meaningful change, completion, consequential failure or required human action.

If the heartbeat facility is unavailable, rejected or cannot target this chat, use one credible native substitute, such as bounded in-turn waits. State the precise scheduling gap and manual/native recovery route; do not create an unrequested standalone cron workaround or pretend unattended supervision exists. Retain useful work and distinguish ACTIVE collaboration from scheduled supervision.

For the concept of a same-chat heartbeat, see the [official glossary](https://learn.chatgpt.com/docs/glossary). Live tool contracts determine exact creation and update mechanics.

## Separately addressable agents: fallback

If persistent chat creation is unavailable and native collaboration exists, spawn exactly three agents named for MAKER, CHECKER and SUPERVISOR, with complete briefs. A BRAID invocation authorizes this three-agent delegation. Register actual IDs/canonical names and distribute the roster. Do not create a fourth orchestrator.

Use actual send_message, followup_task and bounded wait_agent facilities. Inspect tool restrictions; if only the parent can relay or resume workers, disclose that mediation route while preserving SUPERVISOR's decisions. Verify exchanges rather than assuming symmetric access.

Temporary agents may disappear when the parent ends. Record complete briefs, artifacts and next triggers. A heartbeat must attach to a real persistent chat, not an agent ID; do not promise temporary-agent durability or silently substitute a launcher heartbeat. Preserve the exact lost guarantee and recovery route.

## Limited hosts, re-entry and delivery

With limited concurrency run the same separately addressable roles sequentially. If separate execution is unavailable, preserve three briefs and report PREPARED; a single model impersonating three voices is not independent review.

On repeated invocation inspect the record, objective, IDs, current candidate/verdict and heartbeat. Resume survivors without duplicating tasks. Archive/delete chats only on user instruction.

Bind mutable candidates through a commit plus clean/dirty state, snapshot or suitable content manifest. SUPERVISOR confirms that delivery matches CHECKER's evaluated revision and routes material changes for reassessment. Finish the real outcome, preserve the independent verdict and separate any user acceptance of residual risk.
