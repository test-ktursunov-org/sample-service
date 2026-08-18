# Decision record

**Status:** Proposed

We will implement item filtering as an incremental extension to the current
service. This keeps the patch reviewable, makes the contract easy to test, and
avoids coupling the work to a future database migration.

Alternatives considered were a separate service and a framework-level plugin.
Both add operational or dependency overhead that is not justified at the
current scale.
