import yaml
from smolagents import CodeAgent, HfApiModel, FinalAnswerTool, GradioUI


def main() -> None:
    model = HfApiModel(
        model_id="Qwen/Qwen2.5-Coder-32B-Instruct",
        max_tokens=2096,
        temperature=0.5,
        custom_role_conversions=None,
    )

    final_answer = FinalAnswerTool()

    with open("prompts/first_agent.yaml", "r") as f:
        prompt_templates = yaml.safe_load(f)

    if prompt_templates is None:
        raise ValueError("No prompt templates found.")

    agent = CodeAgent(
        model=model,
        tools=[final_answer],
        max_steps=6,
        verbosity_level=1,
        grammar=None,
        planning_interval=None,
        name=None,
        description=None,
        prompt_templates=prompt_templates,
        add_base_tools=True,
    )

    GradioUI(agent).launch()


if __name__ == "__main__":
    main()
