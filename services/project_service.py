from typing import List, Dict


def project_count() -> int:
    return 20


def major_projects(limit: int = 2) -> list[dict[str, str | int]]:
    return [
        {
            "budget": "20M",
            "type": "Rubbish",
            "name": "Railway Reclaimation Project",
            "id": 1,
        },
        {"budget": "40M", "type": "Useless", "name": "Stanley Banks Head Scheme", "id": 2},
        {
            "budget": "50M",
            "type": "Trumpets",
            "name": "Rocking Robots Closure Meak",
            "id": 3,
        },
        {"budget": "200M", "type": "Rollocks", "name": "Bomba Clifton Hedges", "id": 4},
    ][:limit]
