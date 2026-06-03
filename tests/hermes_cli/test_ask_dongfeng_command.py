from argparse import Namespace


def test_dongfeng_command_preloads_ask_dongfeng_without_duplicates(monkeypatch):
    import hermes_cli.main as main_mod

    captured = {}
    monkeypatch.setattr(
        main_mod,
        "cmd_chat",
        lambda args: captured.update(vars(args)),
    )

    main_mod.cmd_dongfeng(
        Namespace(
            query="Guard this implementation plan.",
            skills=["ask-dongfeng", "github-auth,plan"],
            mode="plan-guard",
            artifact_only=False,
        )
    )

    assert captured["skills"] == ["ask-dongfeng", "github-auth", "plan"]
    assert captured["query"].startswith("Use Ask DongFeng in plan-guard mode.")
    assert captured["query"].endswith("Guard this implementation plan.")


def test_dongfeng_command_supports_prompt_positional_and_artifact_only(monkeypatch):
    import hermes_cli.main as main_mod

    captured = {}
    monkeypatch.setattr(
        main_mod,
        "cmd_chat",
        lambda args: captured.update(vars(args)),
    )

    main_mod.cmd_dongfeng(
        Namespace(
            prompt="Create a release feedback loop.",
            query=None,
            skills=None,
            mode=None,
            artifact_only=True,
        )
    )

    assert captured["skills"] == ["ask-dongfeng"]
    assert "machine-readable control-artifact YAML" in captured["query"]
    assert captured["query"].endswith("Create a release feedback loop.")


def test_parser_accepts_dongfeng_shortcut(monkeypatch):
    import sys
    import hermes_cli.main as main_mod

    captured = {}
    monkeypatch.setattr(main_mod, "_has_any_provider_configured", lambda: True)
    monkeypatch.setattr(
        main_mod,
        "cmd_chat",
        lambda args: captured.update(vars(args)),
    )
    monkeypatch.setattr(
        sys,
        "argv",
        [
            "hermes",
            "dongfeng",
            "--mode",
            "intent-to-spec",
            "-q",
            "Build a reviewable MVP spec.",
        ],
    )

    main_mod.main()

    assert captured["command"] == "dongfeng"
    assert captured["skills"] == ["ask-dongfeng"]
    assert captured["query"].startswith("Use Ask DongFeng in intent-to-spec mode.")


def test_dongfeng_preserves_top_level_tui_flag(monkeypatch):
    import sys
    import hermes_cli.main as main_mod

    captured = {}
    monkeypatch.setattr(main_mod, "_has_any_provider_configured", lambda: True)
    monkeypatch.setattr(
        main_mod,
        "cmd_chat",
        lambda args: captured.update(vars(args)),
    )
    monkeypatch.setattr(
        sys,
        "argv",
        ["hermes", "--tui", "dongfeng", "-q", "Build a controlled MVP loop."],
    )

    main_mod.main()

    assert captured["tui"] is True
    assert captured["skills"] == ["ask-dongfeng"]
