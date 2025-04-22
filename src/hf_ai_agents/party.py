from smolagents import CodeAgent, OpenAIServerModel, tool, DuckDuckGoSearchTool


@tool
def suggest_menu(occasion: str) -> str:
    """
    Suggests a menu based on the occasion.
    Args:
        occasion (str): The type of occasion for the party. Allowed values are:
                        - "casual": Menu for a casual party.
                        - "formal": Menu for a formal party.
                        - "superhero": Menu for a superhero party.
                        - "custom": Custom menu.
    """
    match occasion:
        case "casual":
            return "Pizza, snacks, and drinks."
        case "formal":
            return "3-course dinner with wine and dessert."
        case "superhero":
            return "Buffet with high-energy and healthy food."
        case _:
            return "Custom menu for the butler."


def main():
    model = OpenAIServerModel(
        model_id="gpt-4.1-nano",
    )
    # model = LiteLLMModel(
    #     model_id="ollama_chat/qwen2.5-coder:0.5b"
    # )

    agent = CodeAgent(
        model=model,
        tools=[
            DuckDuckGoSearchTool(),
            suggest_menu,
        ],
        max_steps=10,
        verbosity_level=2,
    )

    agent.run(
        "Search for the best music recommendations for a party at the Wayne's mansion."
    )
    agent.run("Prepare a formal menu for the party.")
    agent.run(
        """
        Alfred needs to prepare for the party. Here are the tasks:
        1. Prepare the drinks - 30 minutes
        2. Decorate the mansion - 60 minutes
        3. Set up the menu - 45 minutes
        4. Prepare the music and playlist - 45 minutes

        If we start right now, at what time will the party be ready?
        """
    )


if __name__ == "__main__":
    main()
