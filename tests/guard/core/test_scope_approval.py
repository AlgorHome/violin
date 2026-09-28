"""An explicit, one-time operator decision controls engagement approval."""

from __future__ import annotations

import yaml

from plugins.violin_guard.core import bootstrap
from plugins.violin_guard.gates.scope_gate import validate_scope


def test_yes_approves_displayed_scope_and_no_revokes_it(tmp_path, capsys) -> None:
    eng = tmp_path / "owned-lab"
    assert bootstrap.init_engagement(eng, host="127.0.0.1", ctf=True) == 0
    scope_path = eng / "scope" / "scope.yaml"
    assert any("authorisation.confirmed" in error for error in validate_scope(scope_path).errors)

    assert bootstrap.approve_engagement(eng, input_fn=lambda _: "Yes", require_tty=False) == 0
    scope = yaml.safe_load(scope_path.read_text(encoding="utf-8"))
    assert scope["authorisation"]["confirmed"] is True
    assert scope["authorisation"]["confirmed_by"] == "lab owner (user)"
    assert scope["authorisation"]["confirmed_at"]
    assert "127.0.0.1" in capsys.readouterr().out

    assert bootstrap.approve_engagement(eng, input_fn=lambda _: "No", require_tty=False) == 2
    scope = yaml.safe_load(scope_path.read_text(encoding="utf-8"))
    assert scope["authorisation"]["confirmed"] is False


def test_ambiguous_answer_does_not_approve(tmp_path) -> None:
    eng = tmp_path / "exercise"
    assert bootstrap.init_engagement(eng, host="127.0.0.1") == 0
    scope_path = eng / "scope" / "scope.yaml"
    before = scope_path.read_text(encoding="utf-8")

    assert bootstrap.approve_engagement(eng, input_fn=lambda _: "maybe", require_tty=False) == 1
    assert scope_path.read_text(encoding="utf-8") == before


def test_noninteractive_call_cannot_approve(tmp_path, monkeypatch) -> None:
    eng = tmp_path / "exercise"
    assert bootstrap.init_engagement(eng, host="127.0.0.1") == 0
    monkeypatch.setattr("sys.stdin.isatty", lambda: False)

    assert bootstrap.approve_engagement(eng, input_fn=lambda _: "Yes") == 1
    assert (
        yaml.safe_load((eng / "scope" / "scope.yaml").read_text(encoding="utf-8"))["authorisation"][
            "confirmed"
        ]
        is False
    )


def test_changed_scope_requires_a_new_decision(tmp_path) -> None:
    eng = tmp_path / "exercise"
    assert bootstrap.init_engagement(eng, host="127.0.0.1") == 0
    scope_path = eng / "scope" / "scope.yaml"

    def change_scope_during_prompt(_prompt: str) -> str:
        scope_path.write_text(
            scope_path.read_text(encoding="utf-8") + "\n# changed during prompt\n",
            encoding="utf-8",
        )
        return "Yes"

    assert (
        bootstrap.approve_engagement(eng, input_fn=change_scope_during_prompt, require_tty=False)
        == 1
    )
    assert (
        yaml.safe_load(scope_path.read_text(encoding="utf-8"))["authorisation"]["confirmed"]
        is False
    )
