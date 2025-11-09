def print_models(unprinted, completed):
    """Print and move into the list of completd designs"""

    while unprinted:
        current_design = unprinted.pop(0)
        print(f"\nPrinting: {current_design}")
        completed.append(current_design)


def show_completed_models(completed):
    """Show completed models"""

    print("\nThe following models have been printed")
    for complete in completed:
        print(complete)
