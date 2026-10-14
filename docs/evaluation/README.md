# Evaluation results

The measurements behind the ECTEL paper, kept unchanged for reference:

- `test_result_human_*.txt`, `test_results_human_*.txt` — exams held with people
- `test_results_AI_*` — exams held with the simulated student
- `answer_evaluation_*.txt` — how the answer evaluation scored at different similarity thresholds
- `prompt_*.txt` — outputs used to compare prompt variants
- `help_*.txt` — generated hints, from the answer and from the vector store

These files are results, not inputs: nothing reads them at runtime.
`tests/count_feedback_criteria.py` counts how often the generated feedback names
each performance criterion in `prompt_feedback_01.txt`.

Output produced by running the system today goes to `runs/` instead, which is
not versioned.
