# Copilot Instructions for Advent of Code Workspace

## Project Overview
This is an **Advent of Code solutions workspace** (2019-2024) using **Jupyter notebooks** as the primary development environment. Solutions are organized by year in directories like `2024/`, `2023/`, etc., with a single `days.ipynb` notebook per year containing all daily challenges.

## Architecture & Workflow

### Notebook-Centric Development
- **Single notebook per year**: `2024/days.ipynb` contains all 25 days as sequential cells with markdown sections
- **Cell structure per day**:
  1. Markdown header with AoC link and problem description
  2. `get_in_file(day, year)` to fetch/cache input from AoC API
  3. Input parsing using utilities from `aoc_utils.py`
  4. Part 1 solution code
  5. `submit(result, part="a", day=N, year=YYYY)` to submit answer
  6. Part 2 solution code
  7. `submit(result, part="b", day=N, year=YYYY)`

### Shared Utilities (`aoc_utils.py`)
**Critical imports** (always available in notebooks via `from aoc_utils import *`):
- **Input parsing**: `parse(day, parser, sep)`, `Input(day, line_parser)`, `ints(text)`, `digits(text)`
- **Collections**: `Counter`, `defaultdict`, `deque`, `namedtuple`, `OrderedDict`, `ChainMap`
- **Itertools**: All standard library + `more_itertools` (e.g., `pairwise`, `chunked`, `unzip`, `collapse`)
- **Data structures**: `numpy` as `np`, `heappop/heappush`, `lru_cache`
- **Grid utilities**: `get_adj(i, j, M)`, `get_adj_cross(i, j, M)`, `isValid(np_shape, index)`
- **Tuple ops**: `add_tuple(t1, t2)`, `sub_tuple(t1, t2)`
- **AoC API**: `get_data(day, year)`, `submit(answer, part, day, year)` from `advent-of-code-data`

### Environment Setup

**Conda-based (preferred)**:
```bash
# Inside container - environment already active
conda activate aoc
```

**Key dependencies** (see `2024/aoc_env_2024.yml`):
- Python 3.13+, NumPy, Matplotlib, NetworkX, Pygraphviz
- JupyterLab + IPython kernel
- `advent-of-code-data` for API access (requires `~/.config/aocd/token`)
- `line_profiler`, `memory_profiler` for optimization
- `more-itertools`, `bigtree` for data structures

**Dev Container**: Workspace runs in Docker via `.devcontainer` or `docker-compose up`
- Volumes: workspace mounted at `/workspace`, conda env persisted, `~/.config/aocd` shared
- Jupyter runs on `localhost:8888` (no token required in container)

## Coding Conventions

### Problem-Solving Patterns
1. **Start with test data**: Comment out real input, test with example from problem description
2. **Leverage numpy for grids**: Convert input to `np.matrix` for 2D problems (Days 4, 6, 8, 14)
3. **Use regex for parsing**: `re.findall(r'mul\((\d+),(\d+)\)', text)` common pattern (Day 3)
4. **Direction vectors**: Store as tuples/dicts for grid navigation (e.g., `{'>': (0, 1), 'v': (1, 0)}`)
5. **Pathfinding**: A* implementation in `astar.py` (Day 16), use `dijkstra_search` or `a_star_search`

### Common Idioms
```python
# Parse lines as tuples of integers
in_data = Input(day, line_parser=ints)

# Unpack columns from tuples
left, right = unzip(in_data)

# Grid neighbors (cross or diagonal)
adj = get_adj(i, j, matrix, diag=True)

# Count occurrences
counter = Counter(items)

# Iterate with indices
with np.nditer(M, flags=['multi_index']) as it:
    for x in it:
        i, j = it.multi_index
```

### Performance Optimization
- **Profiling**: Use `%lprun -f func_name func()` for line-by-line timing (Days 11, 14)
- **Memoization**: `@lru_cache` for recursive functions (Day 11 stone splitting)
- **Avoid premature optimization**: Solve first, profile if slow (>5 seconds)

## File Organization
```
/workspace/
├── aoc_utils.py              # Shared utilities (ALWAYS import from here)
├── 2024/
│   ├── days.ipynb            # All 2024 solutions (primary work file)
│   ├── aoc_env_2024.yml      # Conda environment spec
│   ├── astar.py              # Pathfinding algorithms (Day 16)
│   ├── input/inputN.txt      # Cached inputs (auto-generated)
│   └── Makefile              # Conda env management (mk_env, up_env, rm_env)
├── Dockerfile                # Dev container definition
└── docker-compose.yml        # Local JupyterLab setup
```

## Development Commands

**Inside container**:
```bash
# Run notebook (already started in background)
jupyter lab --ip=0.0.0.0 --port=8888

# Manage conda environment
cd 2024
make mk_env    # Create from YAML
make up_env    # Update packages
make rm_env    # Remove environment

# Manual package install
conda run -n aoc pip install <package>
```

**Outside container** (rebuilding):
```bash
docker-compose up --build      # Rebuild after YAML changes
docker-compose down            # Stop container
```

## AI Assistant Guidelines

### When working on AoC problems:
1. **Read problem statement carefully** - extract constraints, examples, edge cases
2. **Start small** - test with example data before running on full input
3. **Reuse utilities** - check `aoc_utils.py` before reinventing (grid ops, parsing, etc.)
4. **Notebook flow** - maintain markdown structure, run cells sequentially
5. **Input caching** - `get_in_file()` downloads once, reuses cached file
6. **Submit once** - AoC penalizes wrong answers; test thoroughly first

### When adding new utilities:
- Add to `aoc_utils.py` if reusable across days
- Keep year-specific helpers in the notebook
- Document complex algorithms (e.g., A* in `astar.py` has detailed comments)

### When debugging:
- Use `%pprint` for readable output (enabled in first cell)
- Check input file paths: relative to `2024/` directory
- Verify conda environment: `sys.path` should include `/workspace`
