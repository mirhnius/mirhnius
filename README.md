# Hi, I'm Niusha 👋

I'm an **ML/AI engineer at McGill University**, working at the intersection of **neuroimaging, reproducible research, and LLM-based agents**. I like building systems that are grounded, testable, and safe to rely on, whether that's a quality-control tool for brain MRI, a RAG pipeline that cites its sources, or an agent that can't make up a number.

- 🔬 **Research:** numerical stability of neuroimaging pipelines. First author of [*Numerical Uncertainty in Linear Registration: An Experimental Study*](https://arxiv.org/abs/2508.00781) (arXiv, 2025)
- 🧠 **Google Summer of Code 2026** with [INCF](https://www.incf.org/), contributing to [QC-Studio](https://github.com/nipoppy/qc-studio). [Read my final report →](https://github.com/mirhnius/gsoc-qc-studio-report)
- 🤖 **Currently exploring:** production RAG, agentic workflows, and how to test and secure coding agents
- 🏛️ Member of [NeuroDataScience](https://github.com/neurodatascience)

---

## Featured projects

| Project | What it is |
|---|---|
| [**practice_rag_production**](https://github.com/mirhnius/practice_rag_production) | A production-style agentic RAG system over arXiv papers: Docling PDF parsing, PostgreSQL, OpenSearch hybrid search (BM25 + vectors with Reciprocal Rank Fusion), a local LLM via Ollama, a LangGraph retrieval workflow, Redis caching and Langfuse tracing. |
| [**mca_linear_registration**](https://github.com/mirhnius/mca_linear_registration) | Code for my paper on how floating-point noise affects linear MRI registration. Uses Monte-Carlo Arithmetic across SPM, FSL and ANTs. Being refactored from research scripts into a Python package. |
| [**budget-buddy**](https://github.com/mirhnius/budget-buddy) | An AI budgeting agent built with Google ADK, Gemini and a custom MCP server. *Math in code, judgment in the LLM*: every number traces back to a deterministic tool call. Kaggle agents capstone. |
| [**agentic_coding**](https://github.com/mirhnius/agentic_coding) | A 12-week course on building web software safely with a coding agent (Claude Code + GitHub): guardrails, CI, security review, testing, and shipping. |
| [**gsoc-qc-studio-report**](https://github.com/mirhnius/gsoc-qc-studio-report) | My Google Summer of Code 2026 write-up: what I built, what I learned, and what's next for QC-Studio. |

## Open-source contributions

- **[nipoppy/qc-studio](https://github.com/nipoppy/qc-studio)** (GSoC 2026): a web app for quality control of neuroimaging data. I worked on the IQM (image quality metrics) viewer, a spec-driven Playwright end-to-end test suite, a fix for ratings being silently dropped, SVG montage caching, the project's first CI checks, and documentation.
- **[masoomeshafiee/DB_management_agent](https://github.com/masoomeshafiee/DB_management_agent)**: a safe, agent-based LLM system for managing a SQLite lab database with natural language. Refactors and a roadmap doc.
- **Reproducibility and annotation projects:** [LivingPark-MRI/zeighami-etal-2015](https://github.com/LivingPark-MRI/zeighami-etal-2015) and [litmining/labelbuddy-annotations](https://github.com/litmining/labelbuddy-annotations).

## Most-starred repos

Earlier engineering projects from 2021, built in MATLAB/Simulink:

| Project | Stars |
|---|---|
| [Control-Magnetic-Levitation-System](https://github.com/mirhnius/Control-Magnetic-Levitation-System): stabilization and tracking of a magnetic levitation ball with PID controllers | ![stars](https://img.shields.io/github/stars/mirhnius/Control-Magnetic-Levitation-System?style=social) |
| [Control-Position-Velocity-DC-Motor](https://github.com/mirhnius/Control-Position-Velocity-DC-Motor): DC motor position and velocity control with PID | ![stars](https://img.shields.io/github/stars/mirhnius/Control-Position-Velocity-DC-Motor?style=social) |
| [OpenmanipulatorX-Robot](https://github.com/mirhnius/OpenmanipulatorX-Robot): tracking control analysis of the OpenManipulator-X arm | ![stars](https://img.shields.io/github/stars/mirhnius/OpenmanipulatorX-Robot?style=social) |
| [Robotic-Arm-Simulation](https://github.com/mirhnius/Robotic-Arm-Simulation): position control of a two-degree-of-freedom arm in Simulink | ![stars](https://img.shields.io/github/stars/mirhnius/Robotic-Arm-Simulation?style=social) |

<details>
<summary><b>More from my earlier projects</b></summary>

<br>

**Signal processing:** [My-Shazam](https://github.com/mirhnius/My-Shazam) (music search engine), [DTMF-Signals-Processing](https://github.com/mirhnius/DTMF-Signals-Processing), [Communication-Modulations](https://github.com/mirhnius/Communication-Modulations), [Extraction-Components-Electroencephalography-Signal](https://github.com/mirhnius/Extraction-Components-Electroencephalography-Signal)

**Machine learning and statistics:** [Classification-Gender-Voice-Recognition](https://github.com/mirhnius/Classification-Gender-Voice-Recognition), [Facial-Landmarks-Detection](https://github.com/mirhnius/Facial-Landmarks-Detection), [Fit-Comparison-Behavioral-Models](https://github.com/mirhnius/Fit-Comparison-Behavioral-Models), [Statistical-Analysis](https://github.com/mirhnius/Statistical-Analysis), [Basic-Statistics](https://github.com/mirhnius/Basic-Statistics), [Optimization-Electricity-Dispatching](https://github.com/mirhnius/Optimization-Electricity-Dispatching)

**Control and robotics:** [Control-Ball-and-Beam-System](https://github.com/mirhnius/Control-Ball-and-Beam-System), [Robotic-Finger-Gesture-Emulation](https://github.com/mirhnius/Robotic-Finger-Gesture-Emulation)

**Software and embedded:** [Local-Messenger](https://github.com/mirhnius/Local-Messenger), [Pacman-Game](https://github.com/mirhnius/Pacman-Game), [Restaurant-Orders-Management-App](https://github.com/mirhnius/Restaurant-Orders-Management-App), [ARM-Frequency-Meter](https://github.com/mirhnius/ARM-Frequency-Meter), [Piplined-ARM](https://github.com/mirhnius/Piplined-ARM)

</details>

## Toolbox

**Languages:** Python · MATLAB · C / C++ · R · Shell
**AI and data:** RAG · LangGraph · Google ADK · MCP · Ollama · PostgreSQL · OpenSearch · Redis · Jupyter
**Engineering:** Docker · GitHub Actions / CI · Playwright · Langfuse
**Domain:** neuroimaging (BIDS, MRI registration, quality control) · numerical reproducibility
